# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **[Phase 1](../phases/phase_01/):** Foundations & Tooling | **[Module 01](../modules/module_01/):** PySpark Intro: RDDs, DataFrames | **Lecture 02:** PySpark DataFrames & Spark SQL | Friday, August 28, 2026 |

---

## Slide 1: PySpark DataFrames & Structured Abstractions
### Moving Beyond Unstructured RDDs to Relational Schema Enforcement
* **Course Context:** CIS 531/731 - Lecture 02 (Module 01)
* **Core Topic:** Transitioning from low-level RDDs to high-level Spark DataFrames and Catalyst optimization
* **Assigned Reading:** Irving et al., *Research Software Engineering with Python* (Chs. 1–2)[cite: 4]
* **Tech Stack:** PySpark 4, Catalyst Optimizer, Tungsten Execution Engine
* **Objective:** Understand schema enforcement, relational operations, and reproducible experiment design principles.

**Speaker Notes:**
Welcome to Lecture 2. On Wednesday, we introduced distributed computing fundamentals and low-level Resilient Distributed Datasets (RDDs). Today, we transition to Spark DataFrames. While RDDs give you raw control over data partitions and transformations, they are black boxes to Spark's execution engine. DataFrames introduce relational schemas and metadata, enabling automated optimization through the Catalyst engine. We will also examine core research software engineering principles from Irving et al. to ensure our data pipelines remain reproducible and robust.

---

## Slide 2: The Limitations of RDDs & The Need for Structure
### Why Catalyst and Tungsten Replaced Raw Lambda Functions
* **The Black-Box Problem:** RDD transformations accept arbitrary Python lambdas, blinding Spark to the underlying data semantics.
* **Serialization Overhead:** Constant translation between JVM memory and Python worker interpreters.
* **Optimization Blindness:** Inability of the cluster to push down filters or reorder operations automatically.
* **The Relational Advantage:** DataFrames provide named columns and explicit data types, unlocking powerful automated query planning.

**Speaker Notes:**
When you write an RDD transformation using a custom Python function, Spark treats that function as an opaque block of code. It cannot inspect what your code is doing, so it cannot optimize it. This forces expensive data shuffling and JVM-to-Python serialization penalties. By structuring our data into DataFrames with named columns and defined types, we give Spark the semantic information it needs to mathematically optimize our queries before a single byte of data is processed.

---

## Slide 3: Spark DataFrames API & Schema Enforcement
### Strongly Typed DataFrames via `StructType` and `StructField`
* **Schema Definition:** Explicitly defining column names, data types, and nullability prior to ingestion.
* **`StructType` & `StructField`:** The fundamental building blocks for Spark schema architecture.
* **Avoiding Schema Inference:** Why relying on automatic type guessing fails on large or dirty datasets.
* **Fail-Fast Mechanics:** Forcing ingestion pipelines to reject malformed records immediately.

**Speaker Notes:**
One of the cardinal sins of data engineering is allowing Spark to infer your schema automatically. When Spark infers a schema, it scans your data twice, guessing types based on initial samples. If a null appears later or a string contains unexpected characters, your types shift silently. In this course, we enforce strict schemas using PySpark's `StructType` and `StructField`. If incoming data violates your schema contract, the pipeline fails fast, preventing corrupt data from poisoning downstream models.

---

## Slide 4: The Catalyst Optimizer Architecture
### Logical Planning, Optimization Phases, and Physical Plans
* **Unresolved Logical Plan:** Abstract representation of your DataFrame operations without schema bindings.
* **Resolved Logical Plan:** Validated against the catalog, confirming columns and tables exist.
* **Optimized Logical Plan:** Applying rule-based optimizations (constant folding, predicate pushdown, projection pruning).
* **Physical Planning:** Generating multiple execution strategies and selecting the lowest-cost physical plan.

**Speaker Notes:**
Catalyst is Spark's internal query optimization framework. When you chain DataFrame operations like `.filter()` and `.select()`, you aren't executing code immediately; you are building a logical plan. Catalyst takes that plan through multiple transformation phases. It uses rule-based optimizations—such as predicate pushdown, which moves filters as close to the data source as possible—to slash network traffic and disk I/O before execution begins.

---

## Slide 5: The Tungsten Execution Engine
### Off-Heap Memory Management & Whole-Stage Code Generation
* **Memory Management:** Bypassing Java Virtual Machine (JVM) garbage collection overhead via custom off-heap memory allocators.
* **Binary Processing Formats:** Encoding data in compact, cache-aware binary layouts to maximize CPU cache hit rates.
* **Whole-Stage Code Generation:** Collapsing multiple physical operators into a single, compact Java bytecode loop on the fly.
* **Hardware Consciousness:** Designing software execution specifically around modern CPU architecture and memory hierarchies.

**Speaker Notes:**
While Catalyst handles the query plan, the Tungsten engine handles execution. Standard Java objects suffer from heavy memory overhead and garbage collection pauses that can stall big data pipelines. Tungsten bypasses the JVM garbage collector by managing memory off-heap in raw binary formats. It also uses whole-stage code generation, compiling entire operator pipelines into flat, highly optimized machine code loops that fit entirely within CPU L1/L2 caches.

---

## Slide 6: Reproducible Research Software Engineering
### Core Principles from Irving et al. (Chapters 1–2)
* **Code as a Scientific Instrument:** Treating data science code with the same rigor as physical laboratory equipment.
* **Environment Control:** Eliminating system drift through version-controlled dependencies and containerization.
* **Deterministic Execution:** Managing random seeds, floating-point precision, and parallel execution non-determinism.
* **Modular Design:** Writing testable, single-responsibility functions rather than monolithic Jupyter notebooks.

**Speaker Notes:**
To ground our technical work, we look to Chapters 1 and 2 of Irving et al., *Research Software Engineering with Python*[cite: 4]. In data science, writing code that "works on your machine" is insufficient. Your data pipelines must be fully reproducible. That means managing dependencies explicitly, controlling random number generation, and structuring your code so that another researcher—or an automated grading harness—can run your pipeline and get identical numerical results.

---

## Slide 7: Experiment Design & Hypothesis Formulation
### Structuring Rigorous Analytical Workflows
* **The Scientific Method in Data Science:** Moving from exploratory scripting to formal experiment design.
* **Hypothesis Formulation:** Explicitly stating what your pipeline intends to prove or disprove.
* **Baseline Establishment:** Building simple heuristic baselines before deploying complex machine learning models.
* **Validation Split Strategy:** Partitioning data into training, validation, and held-out test sets to prevent data leakage.

**Speaker Notes:**
As we prepare for Milestone 1 and our experiment design deliverables, you must shift your mindset from casual scripting to formal experiment design. You cannot evaluate a complex model without a baseline. You must define your target metrics, establish rigorous validation splits, and formulate a clear hypothesis. If your advanced embedding pipeline performs identically to a simple keyword frequency baseline, your architecture needs re-evaluation.

---

## Slide 8: Structured Querying & Relational Expressions
### Common DataFrame Operations in Practice
* **Projections & Filters:** Using `select()`, `filter()`, and `where()` to isolate relevant feature spaces.
* **Aggregations:** Grouping data with `groupBy()` and applying statistical reductions (`mean`, `sum`, `agg`).
* **Joins & Relational Merging:** Combining distributed datasets using inner, outer, and broadcast joins.
* **Column Expressions:** Manipulating data using built-in SQL functions (`F.col`, `F.lit`, `F.when`).

**Speaker Notes:**
In the accompanying notebooks and labs, you will apply these DataFrame expressions directly. You will write code that projects specific feature columns, filters out anomalies, and aggregates data across millions of rows. Pay close attention to how joins are executed. When joining a large DataFrame with a small lookup table, utilizing Spark's broadcast join hint (`broadcast()`) can prevent catastrophic network shuffles.

---

## Slide 9: Handling Corrupt Records & Fail-Fast Workflows
### Robust Ingestion Under Hostile Data Conditions
* **Ingestion Modes:** Examining `PERMISSIVE`, `DROPMALFORMED`, and `FAILFAST` behaviors during data loading.
* **Dead Letter Queues:** Architecting secondary storage paths to capture malformed records for forensic auditing.
* **Schema Evolution:** Managing schema drift when upstream data sources change unexpectedly.
* **Logging & Auditing:** Tracking pipeline exceptions without crashing production workloads.

**Speaker Notes:**
When working with real-world data feeds, malformed records are guaranteed. If a JSON file is missing a closing bracket or a numeric field contains text, how your pipeline reacts is critical. While setting ingestion to permissive mode drops or nullifies bad rows silently, professional RSE practice often dictates a fail-fast approach or routing bad records to a Dead Letter Queue so you can audit data quality issues without halting execution.

---

## Slide 10: Summary & Lab Preparation
### Bridging DataFrames to Lab 1 and Module 1 Deliverables
* **Key Takeaway 1:** DataFrames provide relational structure and enable Catalyst query optimization.
* **Key Takeaway 2:** Explicit `StructType` schemas prevent silent data corruption and enforce pipeline integrity.
* **Key Takeaway 3:** Irving et al. principles ensure our code remains reproducible and scientifically valid[cite: 4].
* **Next Steps:** Review McKinney and VanderPlas chapters for upcoming lab sessions[cite: 4]; begin scoping your project matrix tracks.

**Speaker Notes:**
That covers the architecture of Spark DataFrames and our foundational experiment design principles. For our upcoming lab sessions, ensure your development environments are active and you are familiar with the pandas-to-Spark DataFrame syntax translations. Start discussing your term project track selections with your teams, as track locking occurs in Module 3. See you in lab.
