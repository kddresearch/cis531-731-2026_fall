# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../phases/phase_05/):** Evaluate & Deploy | **[Module 11](../modules/module_11/):** Presenting Results: Ethics & Data Storytelling | **Lecture 35:** Documentation, Provenance & Notebook Presentation Standards | Wed 18 Nov 2026 | [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/); [Wilkinson et al., *The FAIR Guiding Principles*](https://www.nature.com/articles/sdata201618); *(Additional — aligned with course readings)*: [Rule et al., *Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks* (PLOS Comput Biol, 2019)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007007), [Apache Spark 3.5.7 *RDD Programming Guide*](https://spark.apache.org/docs/3.5.7/rdd-programming-guide.html), [pydash API Documentation](https://pydash.readthedocs.io/en/latest/) |

---

## Slide 1: Documentation, Provenance & Notebook Presentation Standards
### CIS 531/731 - Lecture 35
* **Core Focus:** Implementing reproducible notebooks, FAIR metadata manifests, and low-level PySpark provenance pipelines using `SparkContext`/RDD primitives and `pydash` functional chains.
* **Assigned Reading:** [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/); [Wilkinson et al., *The FAIR Guiding Principles*](https://www.nature.com/articles/sdata201618)
* **Additional Readings (Added for Low-Level Implementation):**
  * [Rule et al., *Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks* (PLOS Comput Biol, 2019)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007007) — operationalizes notebook hygiene alongside Module 0–1 texts (Danchev; Irving et al.).
  * [Apache Spark 3.5.7 *RDD Programming Guide*](https://spark.apache.org/docs/3.5.7/rdd-programming-guide.html) — matches the Spark 3.5.7 documentation baseline from Module 4.
  * [pydash Documentation](https://pydash.readthedocs.io/en/latest/) — functional Python utility toolkit (`from pydash import py_`) for deterministic nested JSON/dictionary lineage shaping.
* **Learning Goals:** Eliminate hidden notebook state, serialize low-level Spark DAG provenance, compute partition-level content digests, and package clean open-access computational narratives.

**Speaker Notes:**
Welcome to Lecture 35. On Monday we covered ethical storytelling and technical writing essentials. Today we drop down to the engineering substrate that makes analytical storytelling trustworthy: reproducible execution, machine-actionable FAIR provenance, and auditable notebooks. Rather than treating provenance as hand-written prose in a README, we will build it programmatically using low-level PySpark RDDs and `pydash`—a Lo-Dash-style functional Python library that excels at safely traversing, normalizing, and validating deeply nested JSON structures like `.ipynb` files, Spark schemas, and RO-Crate metadata records. Note the three additional open-access readings added to align today's implementation directly with our earlier RSE and Spark 3.5.7 course materials.

---

## Slide 2: Reproducible Notebooks & Hidden-State Hazards in Spark
### Why Out-of-Order Execution Breaks Distributed DAGs
* **The Hidden-State Failure Mode:** Interactive kernels retain deleted variable bindings, mutated globals, and stale `rdd.persist()` caches across non-sequential cell runs—causing a notebook that "worked on my machine" to fail under a clean *Restart & Run All*.
* **Spark Closure Serialization Trap:** When a notebook cell mutates a driver-side Python dictionary or list and passes a lambda into `rdd.map()`, `cloudpickle` captures the *current* runtime value at action time, silently coupling results to cell execution order.
* **Rule of Determinism:** Every production or submission notebook must execute cleanly from Cell 1 to Cell $N$ with fixed seeds (`randomSplit(..., seed=...)`), explicit `unpersist()`, and pure, side-effect-free record functions.
* **Functional Immutability with `pydash`:** Because `py_.set_()` mutates dictionaries in place, always pair it with `py_.clone_deep()` inside Spark worker functions so cached partition objects are never corrupted across retries.

**Speaker Notes:**
Jupyter notebooks are extraordinary exploratory tools, but they are notorious for hidden state—especially when paired with a long-lived `SparkContext`. Imagine running Cell 8, editing a threshold dictionary in Cell 3 without re-running Cell 4, and then triggering `.collect()` in Cell 9. Your RDD closure now reflects an undocumented state that no reader can reproduce from the saved source code. One subtle gotcha we must call out right away with `pydash`: functions like `py_.set_` and `py_.merge` mutate their first argument in place. Inside a PySpark `map` or `mapPartitions` function, in-place mutation of a broadcasted or cached dictionary creates nondeterministic bugs if Spark re-executes a failed task. Always clone before mutating or stick to pure chain operations.

---

## Slide 3: Low-Level PySpark Notebook Auditing with `pydash`
### Parsing `.ipynb` JSON Across a Repository via `wholeTextFiles`
* **Notebooks Are Just JSON:** Every `.ipynb` file adheres to the `nbformat` JSON schema containing `cells`, `execution_count`, `metadata`, and `outputs`.
* **Distributed Linting Pipeline:** Use `sc.wholeTextFiles()` to ingest a directory of notebooks into an RDD of `(path, raw_json)` pairs, then audit execution monotonicity with `py_.chain`:

```python
import json
from pydash import py_

def audit_notebook(item):
    path, raw = item
    nb = json.loads(raw)
    counts = (
        py_.chain(nb)
        .get("cells", [])
        .filter_(lambda c: py_.get(c, "cell_type") == "code")
        .map_(lambda c: py_.get(c, "execution_count"))
        .value()
    )
    non_null = py_.compact(counts)
    is_monotonic = non_null == sorted(non_null) and len(non_null) == len(counts)
    return (path, {"code_cells": len(counts), "monotonic_top_to_bottom": is_monotonic,
                   "unexecuted": counts.count(None),
                   "kernel": py_.get(nb, "metadata.kernelspec.name", "unknown")})

audit_report = sc.wholeTextFiles("notebooks/*.ipynb").map(audit_notebook).collectAsMap()
```

**Speaker Notes:**
Here is our first concrete low-level PySpark + `pydash` pattern. Because `sc.wholeTextFiles` gives us `(filename, content)` pairs directly as an RDD, we can audit an entire course or lab repository of notebooks in parallel. Look at how `py_.chain` reads cleanly from top to bottom: `get("cells", [])` safely avoids `KeyError` on malformed files, `filter_` isolates code cells, `map_` extracts `execution_count`, and `py_.compact` strips `None` values. If `non_null` does not match `sorted(non_null)` or if any cell has `None`, the notebook fails the top-to-bottom reproducibility gate. This same pattern can run inside CI before grading or publication.

---

## Slide 4: Operationalizing FAIR Principles (Wilkinson et al., 2016)
### From Conceptual Guidelines to Machine-Actionable JSON-LD
* **F — Findable:** Globally unique, persistent identifiers (DOIs, commit SHAs, content hashes) and rich structured metadata indexed in searchable repositories.
* **A — Accessible:** Retrievable via open, standardized protocols (HTTPS/Git/Zenodo); metadata persists even if raw restricted audio/text data cannot be redistributed.
* **I — Interoperable:** Formal, shared knowledge representation vocabularies (JSON-LD, Schema.org, RO-Crate, W3C PROV-O) and open binary formats (Parquet, Arrow).
* **R — Reusable:** Explicit machine-readable license (e.g., CC-BY-4.0 / MIT), complete processing provenance, and community-standard column schemas.
* **Enforcing FAIR Defaults with `pydash`:**

```python
FAIR_TEMPLATE = {
    "@context": "[https://schema.org/](https://schema.org/)",
    "@type": "Dataset",
    "license": "[https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)",
    "distribution": [],
    "provenance": {"spark_version": None, "git_commit": None},
}

def build_fair_manifest(partial_meta):
    manifest = py_.defaults_deep(py_.clone_deep(partial_meta), FAIR_TEMPLATE)
    return py_.pick(manifest, ["@context", "@type", "identifier", "name",
                               "license", "distribution", "provenance"])
```

**Speaker Notes:**
Wilkinson et al. emphasize a crucial point that people often miss: FAIR is not just about making data readable for humans; it is specifically about **machine-actionability**—enabling automated agents and pipelines to discover, verify, and reuse an asset without human guesswork. Notice also that Accessibility does not mean "everything must be public"; if you are working with restricted student or clinical transcripts, the *metadata* describing the dataset and access rules must still be openly accessible. In Python, `py_.defaults_deep` paired with `py_.clone_deep` guarantees that every generated manifest inherits required Schema.org and provenance keys without silently overwriting custom fields, while `py_.pick` enforces an allowlist schema so stray scratchpad keys never leak into published metadata.

---

## Slide 5: Extracting Low-Level Spark Lineage & Execution Provenance
### Inspecting RDD Dependencies, Schemas, and Catalyst Plans
* **RDD Lineage (`toDebugString()`):** Every RDD carries an immutable DAG of parent dependencies; `rdd.toDebugString().decode("utf-8")` captures the exact shuffle boundaries, partition counts, and storage levels.
* **Schema & Config Introspection:** `df.schema.jsonValue()` emits a standard nested Python dict of column types and nullability, while `sc.getConf().getAll()` returns key-value runtime tuples.
* **Normalizing Cluster Metadata with `pydash`:**

```python
SENSITIVE_KEYS = ("secret", "token", "password", "key")

def capture_spark_provenance(sc, df, target_rdd):
    raw_conf = py_.from_pairs(sc.getConf().getAll())
    safe_conf = py_.omit_by(
        raw_conf,
        lambda v, k: any(s in k.lower() for s in SENSITIVE_KEYS)
    )
    schema_fields = (
        py_.chain(df.schema.jsonValue())
        .get("fields", [])
        .map_(lambda f: py_.pick(f, ["name", "type", "nullable"]))
        .value()
    )
    return {
        "spark_version": sc.version,
        "conf": safe_conf,
        "schema": schema_fields,
        "rdd_lineage": target_rdd.toDebugString().decode("utf-8"),
        "physical_plan": df._jdf.queryExecution().simpleString(),
    }
```

**Speaker Notes:**
High-level notebooks rarely record *how* Spark actually executed a transformation. Did a join broadcast or shuffle? What was the exact partition count or memory fraction? By calling `sc.getConf().getAll()`, `df.schema.jsonValue()`, `target_rdd.toDebugString()`, and the underlying JVM `queryExecution().simpleString()`, we capture deterministic execution provenance directly from the engine. Notice the security guardrail powered by `py_.omit_by`: before serializing `SparkConf` into a repository artifact, we strip any key containing `secret`, `token`, `password`, or `key` so S3 credentials or API tokens never get committed to GitHub.

---

## Slide 6: Partition-Level Content Checksums & Record Telemetry
### Deterministic Hashing with `mapPartitionsWithIndex` and Accumulators
* **Why File-Level Hashes Are Not Enough:** Distributed Parquet outputs consist of many `part-*.parquet` files whose ordering across executors can vary unless keys and fields are canonicalized.
* **Order-Invariant Partition Hashing:** Use `mapPartitionsWithIndex` to sort record keys via `py_.sort_by` and canonicalize JSON before hashing, while counting schema anomalies via a Spark `Accumulator`:

```python
import hashlib, json
from pydash import py_

bad_records = sc.accumulator(0)

def hash_partition(idx, iterator):
    h = hashlib.sha256()
    count = 0
    for rec in iterator:
        if not py_.has(rec, "doc_id"):
            bad_records.add(1)
            continue
        canonical = py_.from_pairs(py_.sort_by(list(rec.items()), lambda kv: kv[0]))
        h.update(json.dumps(canonical, sort_keys=True).encode("utf-8"))
        count += 1
    yield (idx, {"rows": count, "sha256": h.hexdigest()})

part_digests = raw_rdd.mapPartitionsWithIndex(hash_partition).collect()
dataset_digest = hashlib.sha256(
    "".join(py_.chain(part_digests).sort_by(lambda x: x[0]).map_("1.sha256").value()).encode()
).hexdigest()
```

**Speaker Notes:**
If a colleague re-runs your pipeline on a different cluster, how do they prove their scrubbed corpus matches yours byte-for-byte? Using `mapPartitionsWithIndex`, each executor hashes its local records in streaming $O(1)$ memory without ever pulling the dataset to the driver. Notice two `pydash` idioms here: `py_.has(rec, "doc_id")` validates required nested paths while incrementing a Spark `Accumulator` for malformed rows, and on the driver `py_.chain(part_digests).sort_by(...).map_("1.sha256")` uses `pydash`'s path-string iteratee to pluck each partition's digest in deterministic index order before computing a Merkle-style root hash.

---

## Slide 7: Environment, Dependency & Hyperparameter Snapshotting
### Capturing the Full Computational Envelope
* **Rule 5 (Rule et al., 2019):** Code alone is insufficient without exact runtime versions (`python`, `pyspark`, `pydash`, `scikit-learn`, `torch`, JVM version, and container image digest).
* **Hyperparameter & Config Merging:** Combine global pipeline defaults, stage overrides, and CLI flags into a single frozen provenance object via `py_.merge` on deep-cloned dicts.
* **Structured Diffing Across Runs:** Use `py_.to_pairs` and `py_.difference` to detect which hyperparameters changed between Run $t-1$ and Run $t$ before writing a provenance sidecar:

```python
import platform, sys, pyspark, pydash
from pydash import py_

def snapshot_run_config(defaults, overrides, prev_config=None):
    merged = py_.merge(py_.clone_deep(defaults), py_.clone_deep(overrides))
    sanitized = py_.omit(merged, ["api_key", "hf_token", "aws_secret_access_key"])
    env = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "pyspark": pyspark.__version__,
        "pydash": pydash.__version__,
    }
    changed = (
        py_.difference(py_.to_pairs(sanitized), py_.to_pairs(prev_config))
        if prev_config else py_.to_pairs(sanitized)
    )
    return {"environment": env, "hyperparameters": sanitized, "delta_from_prev": changed}
```

**Speaker Notes:**
This slide directly bridges Module 2 (Docker digest pinning) and Module 12 (MLflow Tracking). Before you even launch an MLflow server, a 15-line pure-Python function using `py_.
