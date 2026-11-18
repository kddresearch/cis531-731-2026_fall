# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../phases/phase_05/):** Evaluate & Deploy | **[Module 11](../modules/module_11/):** Presenting Results: Ethics & Data Storytelling | **Lecture 36:** Dashboard Design & Limitations Panel Workshop; Wrap-Up | Fri 20 Nov 2026 | [Wilke, *Fundamentals of Data Visualization* (Parts I–II)](https://clauswilke.com/dataviz/); [Last, *Technical Writing Essentials*](https://pressbooks.bccampus.ca/technicalwriting/); *(Additional — aligned with course readings)*: [Mitchell et al., *Model Cards for Model Reporting* (FAT* 2019, arXiv:1810.03993)](https://arxiv.org/abs/1810.03993), [Apache Spark 3.5.7 *RDD Programming Guide*](https://spark.apache.org/docs/3.5.7/rdd-programming-guide.html), [pydash API Documentation](https://pydash.readthedocs.io/en/latest/) |

---

## Slide 1: Dashboard Design & Limitations Panel Workshop; Wrap-Up
### CIS 531/731 - Lecture 36
* **Core Focus:** Architecting low-latency model monitoring dashboards backed by low-level PySpark RDD aggregations and `pydash` view-model pipelines, followed by a structured Limitations Panel peer-review workshop.
* **Assigned Reading:** [Wilke, *Fundamentals of Data Visualization* (Parts I–II)](https://clauswilke.com/dataviz/); [Last, *Technical Writing Essentials*](https://pressbooks.bccampus.ca/technicalwriting/)
* **Additional Readings (Added for Low-Level Implementation & Workshop):**
  * [Mitchell et al., *Model Cards for Model Reporting* (FAT* 2019, arXiv:1810.03993)](https://arxiv.org/abs/1810.03993) — standard open-access framework for disaggregated subgroup reporting and limitation disclosures (aligning with Modules 9–10).
  * [Apache Spark 3.5.7 *RDD Programming Guide*](https://spark.apache.org/docs/3.5.7/rdd-programming-guide.html) — `combineByKey`, `Broadcast`, and bounded driver collection patterns.
  * [pydash Documentation](https://pydash.readthedocs.io/en/latest/) — driver-side payload shaping, clutter pruning, and Model Card schema validation.
* **Course Milestones:** `MP 10` due **Wed 25 Nov 2026**; `PS 11` released before Fall Break (due **Fri 04 Dec 2026**).

**Speaker Notes:**
Welcome to Lecture 36 and the wrap-up of Module 11 before Fall Break. Today combines two tightly linked engineering disciplines: building operational monitoring dashboards that communicate model health without overloading the viewer, and building transparent Limitations Panels that prevent stakeholders from misinterpreting those dashboards. Note our three additional open-access readings, especially Mitchell et al.'s Model Cards paper, which gives us a concrete checklist for today's Limitations Panel workshop. Keep an eye on the calendar: MP 10 is due next Wednesday, and PS 11 releases as we head into Fall Break.

---

## Slide 2: Dashboard Architecture for Distributed Model Monitoring
### Separating Cluster Compute from Presentation State
* **The Cardinal Anti-Pattern:** Never wire a web dashboard callback directly to a raw `rdd.collect()` or unaggregated full-table scan—doing so causes driver OOM crashes and multi-second UI freezes.
* **Three-Layer Monitoring Architecture:**
  1. **Executor Compute Layer (Low-Level PySpark):** Single-pass `combineByKey` / `aggregateByKey` reductions over partitioned telemetry logs (ASR WER/MER, classifier confidence, embedding drift, latency).
  2. **Driver View-Model Layer (`pydash`):** Pure functional transformation of compact collected aggregates into normalized, sorted, JSON-serializable chart payloads (`O(cohorts × bins)`).
  3. **Presentation Layer (Declarative UI):** Lightweight visual renderer (Plotly/Dash, Vega-Lite, or Jupyter dashboard panel) bound strictly to the pre-shaped view-model—zero business logic inside plotting code.

**Speaker Notes:**
When students first build dashboards on top of Spark, the most common failure is coupling the UI directly to raw data. Every time a user clicks a filter dropdown, the app fires a heavy Spark job or tries to pull millions of rows into pandas on the driver. Instead, we architect a strict three-layer boundary. Spark executors reduce millions of prediction events down to a few hundred cohort-level summary tuples. Then `pydash` on the driver reshapes those tuples into a crisp, schema-validated JSON payload. Finally, your dashboard renderer simply draws the payload. That keeps interactivity sub-second and makes the exact dashboard state testable with unit tests.

---

## Slide 3: Low-Level PySpark Pre-Aggregation (`combineByKey` + `Broadcast`)
### Single-Pass Cohort Telemetry Without Shuffle Explosion
* **Why `combineByKey` Beats `groupByKey`:** `groupByKey` shuffles every raw prediction record across the network; `combineByKey` performs map-side combining inside each partition first, minimizing network I/O.
* **Broadcasting Monitoring Thresholds:** Ship alert cutoffs via `sc.broadcast()` so workers evaluate SLA breaches locally without repeatedly serializing config dicts:

```python
thresholds_bc = sc.broadcast({"max_latency_ms": 250.0, "min_conf": 0.65})

def create_comb(rec):
    th = thresholds_bc.value
    err = int(rec["y_pred"] != rec["y_true"])
    slow = int(rec["latency_ms"] > th["max_latency_ms"])
    low_c = int(rec["conf"] < th["min_conf"])
    return (1, err, slow, low_c, float(rec["latency_ms"]))

def merge_val(acc, rec):
    c = create_comb(rec)
    return tuple(a + b for a, b in zip(acc, c))

def merge_comb(a, b):
    return tuple(x + y for x, y in zip(a, b))

cohort_stats = (
    preds_rdd
    .map(lambda r: (r["cohort"], r))
    .combineByKey(create_comb, merge_val, merge_comb)
    .collectAsMap()
)
```

**Speaker Notes:**
Look closely at why `combineByKey` is the workhorse of low-level PySpark monitoring. Each executor reduces every record for a given cohort into a fixed 5-tuple: `(n, errors, slow_requests, low_confidence, sum_latency)`. Only one 5-tuple per cohort per partition ever crosses the network shuffle. Because we broadcast the threshold dictionary with `sc.broadcast()`, executors read SLA cutoffs from local memory. By the time `.collectAsMap()` runs, the driver receives a tiny dictionary with one entry per cohort, even if `preds_rdd` scanned 50 million inference events.

---

## Slide 4: Shaping Dashboard View-Models with `pydash`
### Pure Driver-Side Transformation into Visual Payloads
* **Deterministic Payload Assembly:** Use `py_.chain`, `py_.map_values`, `py_.order_by`, and `py_.round_` to turn raw Spark reduction tuples into chart-ready records with explicit denominators (`n`) and severity flags:

```python
from pydash import py_

def build_dashboard_payload(cohort_stats, top_k=8):
    enriched = (
        py_.chain(cohort_stats)
        .map_values(lambda v, k: {
            "cohort": k,
            "n": v[0],
            "error_rate": py_.round_(v[1] / v[0], 4) if v[0] else None,
            "sla_breach_rate": py_.round_(v[2] / v[0], 4) if v[0] else None,
            "mean_latency_ms": py_.round_(v[4] / v[0], 1) if v[0] else None,
            "low_support_flag": v[0] < 30,
        })
        .values()
        .order_by(["error_rate", "n"], ["desc", "desc"])
        .value()
    )
    return {
        "primary_panel": py_.take(enriched, top_k),
        "overflow_count": max(0, len(enriched) - top_k),
        "flagged_cohorts": py_.filter_(enriched, "low_support_flag"),
    }
```

**Speaker Notes:**
Once `cohort_stats` lands on the driver, `pydash` turns a messy dictionary of positional tuples into a clean, self-describing dashboard payload. Notice how `py_.map_values` computes rates and flags small-sample cohorts (`n < 30`), `py_.order_by` ranks the highest-error cohorts first so attention goes straight to failure modes, and `py_.take(enriched, top_k)` caps the primary chart at 8 categories while explicitly reporting `overflow_count`. That one line directly implements clutter control in code rather than relying on manual chart editing.

---

## Slide 5: Cognitive Load & Data-Ink Ratio in Operational Displays
### Applying Wilke (*Fundamentals of Data Visualization*, Parts I–II)
* **Perceptual Encoding Hierarchy (Wilke, Ch. 2):** Encode primary quantitative metrics via **position along a common aligned scale** (dot plots, horizontal bar charts with zero baseline) rather than pie angles, area bubbles, or rainbow colormaps.
* **Proportional Ink & Clutter Elimination:** Every pixel should encode data or essential scale context—remove 3D effects, heavy gridlines, redundant legends, and dual y-axes.
* **Small Multiples Over Spaghetti Plots:** Partition high-cardinality cohorts into aligned facets with shared axes using `py_.chunk()` or `py_.group_by()` so operators compare shapes rather than tracing 20 overlapping lines:

```python
# Partition monitoring panels into balanced 2x2 small-multiple grid specs
facet_pages = (
    py_.chain(dashboard_payload["primary_panel"])
    .map_(lambda r: py_.pick(r, ["cohort", "error_rate", "n", "low_support_flag"]))
    .chunk(4)
    .value()
)
```

**Speaker Notes:**
Wilke's Parts I and II give us a rigorous visual grammar, and we can enforce much of it structurally in our data-shaping layer. First, avoid dual y-axes and pie charts on operational monitoring displays—aligned horizontal bars or Cleveland dot plots let an operator spot a 4-point error spike in milliseconds. Second, resist the temptation to plot 25 cohorts on one line chart; use `py_.chunk(4)` to split cohorts into clean 2x2 small-multiple grids with identical y-axis bounds. Finally, notice `py_.pick`: stripping unused metadata fields from the panel payload ensures your rendering component does not accidentally clutter tooltips or legends with irrelevant columns.

---

## Slide 6: Visualizing Disaggregated Uncertainty & Calibration
### Never Render a Point Estimate Without Support & Error Bounds
* **The Executive Summary Trap:** Displaying a single global accuracy or MER KPI hides subgroup regressions (Simpson's paradox) and overstates confidence on tiny cohorts ($n = 7$ vs. $n = 1{,}000$).
* **Distributed Bootstrap Bounds in Low-Level PySpark:** Resample predictions per partition (`sample(withReplacement=True, fraction=1.0, seed=b)`) to compute empirical $[q_{0.025}, q_{0.975}]$ confidence intervals on Spark, then join atomically onto the view-model via `py_.key_by` and `py_.merge`:

```python
def attach_uncertainty_bands(primary_rows, bootstrap_draws):
    # bootstrap_draws: list of {"cohort": str, "error_rate": float} across B resamples
    ci_by_cohort = (
        py_.chain(bootstrap_draws)
        .group_by("cohort")
        .map_values(lambda rows: (
            lambda vals: {
                "ci_low": py_.round_(vals[int(0.025 * len(vals))], 4),
                "ci_high": py_.round_(vals[int(0.975 * len(vals))], 4),
            }
        )(py_.sort_by(py_.map_(rows, "error_rate"))))
        .value()
    )
    return py_.map_(
        primary_rows,
        lambda row: py_.merge(py_.clone_deep(row), py_.get(ci_by_cohort, row["cohort"], {}))
    )
```

**Speaker Notes:**
Connecting directly back to Modules 9 and 10: a point estimate without its denominator `n` and uncertainty interval is an invitation to make a bad decision. Here we collect bootstrap replicates computed across our Spark cluster and use `py_.group_by("cohort")` plus `py_.map_values` to derive 95% percentile intervals for every cohort. By merging `ci_low` and `ci_high` directly into each chart record via `py_.merge(py_.clone_deep(row), ...)`, the error bars travel atomically with the point estimate—meaning a downstream plot cannot render the bar without seeing its uncertainty interval.

---

## Slide 7: Structured Limitations Panels & Model Cards
### Operationalizing Mitchell et al. (2019) & Last (*Technical Writing Essentials*)
* **Why Limitations Belong *Inside* the Dashboard:** Burying caveats in an appendix means stakeholders never see them at decision time; every operational dashboard needs a co-located **Limitations Panel**.
* **Required Model Card Disclosure Fields (Mitchell et al., 2019):**
  1. **Intended Use & Out-of-Scope Uses:** Explicit deployment boundaries.
  2. **Evaluation Data & Denominators:** Sample sizes, selection biases, and annotator provenance.
  3. **Disaggregated Subgroup Performance:** Where error rates diverge or support is sparse (`low_support_flag`).
  4. **Ethical, Privacy & Compliance Status:** Consent scope, PII handling, and unresolved redistribution constraints.
* **Machine-Checked Limitations Schema via `pydash`:**

```python
REQUIRED_DISCLOSURES = [
    "intended_use", "out_of_scope", "denominators_disclosed",
    "known_confounds", "ethical_and_data_status"
]

def audit_limitations_panel(card_dict):
    incomplete = py_.filter_(
        REQUIRED_DISCLOSURES,
        lambda field: py_.is_empty(py_.get(card_dict, field))
    )
    return {"ready_for_display": py_.is_empty(incomplete), "missing_sections": incomplete}
```

**Speaker Notes:**
In Last's *Technical Writing Essentials*, good technical documentation anticipates reader misinterpretation before it happens. Mitchell et al.'s Model Cards framework formalizes that principle for machine learning systems. Notice that our Limitations Panel is not an afterthought—it is a structured dictionary validated by `py_.is_empty` and `py_.get` before the dashboard even builds. If `out_of_scope` or `known_confounds` is blank, `audit_limitations_panel` flags the dashboard as incomplete. Transparently disclosing small samples, unseparated confounds, or single-annotator limits strengthens scientific credibility rather than weakening it.

---

## Slide 8: Limitations Panel Workshop (In-Class Peer Review)
### 20-Minute Structured Adversarial Audit
* **Setup (3 min):** Pair with another team/student; exchange your current dashboard mockup (or rendered figures) plus your 5-field Limitations Panel JSON/Markdown draft.
* **Peer Audit Checklist (12 min — 4 Failure Modes to Hunt):**
  1. **Unstated Denominators:** Does any percentage, rate, or chart bar appear without an explicit $n$ or uncertainty interval?
  2. **Visual Distortion (Wilke):** Are y-axes truncated without justification, encodings mismatched, or clutter obscuring the signal?
  3. **Hidden Aggregation Bias:** Are heterogeneous subgroups collapsed into one headline KPI that masks a failing slice?
  4. **Overclaimed Causality:** Does the Limitations Panel contradict the dashboard headline (e.g., claiming causal improvement on an observational or small-$n$ sample)?
* **Debrief & Action Log (5 min):** Record **at most 3** concrete, actionable repairs (distinguishing *wording fix*, *visual redesign*, and *re-aggregation required*) for PS 11.

**Speaker Notes:**
For the workshop portion of today's session, pair up and treat your peer's dashboard and Limitations Panel like an adversarial conference reviewer—constructive, specific, and evidence-grounded. Look specifically for mismatches between what the visual implies at a glance and what the fine print admits. If a bar chart shows a dramatic difference between two cohorts where one cohort has $n = 6$ and huge overlapping bootstrap intervals, that is a visual distortion even if the caveat appears in a footnote. Write down three concrete repairs that you will fold directly into PS 11.

---

## Slide 9: Module 11 Synthesis — End-to-End FAIR Storytelling Pipeline
### Unifying Lectures 34, 35, and 36
* **The Complete Phase 5 Communication Stack:**
  * **Lecture 34 (Story & Ethics):** Audience-calibrated technical narrative, honest uncertainty, zero cherry-picking (Last).
  * **Lecture 35 (Reproducibility & Provenance):** Top-to-bottom executable `.ipynb` audits (`sc.wholeTextFiles`), FAIR Schema.org manifests (`py_.defaults_deep`), low-level Spark lineage (`toDebugString()`), and partition SHA-256 digests (`mapPartitionsWithIndex`).
  * **Lecture 36 (Operational Visibility & Limits):** Bounded `combineByKey` + `Broadcast` monitoring reductions, `pydash`-shaped low-clutter dashboard payloads (Wilke), disaggregated bootstrap error bars, and co-located Model Card Limitations Panels (Mitchell et al.).
* **Design Invariant:** Every visual claim on a dashboard must trace backward through a deterministic `pydash` view-model and a Spark lineage digest to an immutable, documented data slice.

**Speaker Notes:**
Stepping back across all three lectures of Module 11, notice how every piece interlocks into a single engineering discipline. Storytelling without provenance is marketing; provenance without clear visualization is an unreadable log dump; visualization without an explicit Limitations Panel is an overconfidence trap. Using low-level PySpark for scalable reduction and `pydash` for clean, deterministic dictionary and metadata pipelines lets you enforce all three standards in code.

---

## Slide 10: Phase Transition — Fall Break, MP 10, PS 11 & Module 12 Preview
### Next Steps and Upcoming Deadlines
* **Immediate Deadlines:**
  * **Fall Break:** Mon 23 Nov – Fri 27 Nov 2026 (**No Class**).
  * **MP 10 Due:** Wed 25 Nov 2026 (Interpretation, Calibration & Error Analysis).
  * **PS 11 Released:** Wed 25 Nov 2026 (Due **Fri 04 Dec 2026**) — requires:
    1. A top-to-bottom verified `.ipynb` passing the Lecture 35 monotonicity audit;
    2. A FAIR JSON provenance manifest including Spark `toDebugString()` lineage and partition digests;
    3. A low-clutter monitoring dashboard view-model + peer-reviewed Limitations Panel.
* **Module 12 Preview (Resumes Mon 30 Nov 2026):**
  * **Lecture 37:** PaaS/IaaS, MLOps/AIOps & Production Drift Monitoring (`ML-Ops.org`).
  * **Lecture 38:** Automating today's provenance sidecars with **MLflow Tracking & Model Registry**.
  * **Lecture 39:** Containerizing model inference & dashboard services with **FastAPI + Docker**.

**Speaker Notes:**
Have a restorative Fall Break next week. Remember that MP 10 is due Wednesday, November 25, and PS 11 releases on the same day—giving you a full week after break until Friday, December 4 to integrate today's workshop revisions into your provenance manifest, clean notebook narrative, and monitoring dashboard. When we return on Monday, November 30 for Module 12, we will take the manual JSON provenance snapshots and monitoring reductions we wrote by hand in PySpark and `pydash` this week and operationalize them with MLflow Tracking, Model Registries, and containerized FastAPI services. Safe travels, and see you after break.
