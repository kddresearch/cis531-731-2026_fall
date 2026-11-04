# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 1:** Foundations & Tooling | **Module 01:** PySpark Intro: RDDs & DataFrames; Projects, Experiment Design | **Lectures 01-04** | Wed 26 Aug - Wed 02 Sep 2026 |

---

## Lecture 01: PySpark Basics & Resilient Distributed Datasets (RDDs) (Wed 26 Aug)

1. **Distributed Computing Fundamentals:** Understanding cluster computing, driver nodes, and executor processes in Apache Spark.
2. **Resilient Distributed Datasets (RDDs):** Core immutability, lineage graphs, lazy evaluation, and fault-tolerance guarantees.
3. **Transformations vs. Actions:** Distinguishing narrow/wide transformations (`map`, `filter`, `flatMap` vs. `groupByKey`, `reduceByKey`) from terminal action operations (`collect`, `count`, `take`).
4. **PySpark Context & Session:** Initializing and configuring `SparkContext` and `SparkSession` within Python execution environments.
5. **Memory Management & Partitioning:** Controlling data partitioning, shuffling overhead, and caching strategies (`persist`, `cache`).

---

## Lecture 02: PySpark DataFrames & Spark SQL (Fri 28 Aug)

1. **Spark DataFrames API:** Transitioning from unstructured RDDs to structured DataFrame abstractions with defined schemas.
2. **Catalyst Optimizer:** Query optimization lifecycle covering logical planning, physical planning, and code generation.
3. **Structured Querying & Expressions:** Executing SQL queries and relational operations (`select`, `filter`, `groupBy`, `agg`, `join`).
4. **Tungsten Execution Engine:** Off-heap memory management, binary processing formats, and cache-aware memory layout.
5. **Schema Definition & Enforcement:** Utilizing `StructType` and `StructField` for explicit schema enforcement on heterogeneous data sources.

---

## Lecture 03: RDD Transformations & Actions Lab / PySpark 4 Architecture (Mon 31 Aug)

1. **PySpark 4 & Distributed Architecture:** Moving from single-node pandas bottlenecks to horizontal cluster scaling with driver/executor topology and Spark Connect.
2. **Lazy Evaluation & DAGs:** Understanding transformations, actions, and Directed Acyclic Graph optimization before execution.
3. **Data Exploration & Profiling:** Initial data inspection, schema validation (`printSchema`), and statistical summarization (`describe`) following Miner & Shook Chapter 5.
4. **The OSEMN Pipeline:** Establishing the 5-stage methodological framework (Obtain, Scrub, Explore, Model, Interpret) governing course projects.
5. **Term Project Track Selection:** Committing immutably to parallel operational architectures: Track 1 (ASR Live Stream Ingest) vs. Track 2 (VDB Text Corpora).

---

## Lecture 04: Lab 1 – PySpark 4 Bring-up & The "Obtain" Stage (Wed 02 Sep)

1. **Environment Bring-Up & Verification:** Instantiating `SparkSession`, monitoring execution via the Spark Web UI (port 4040), and verifying environment manifests.
2. **Multidimensional Matrix Scoping:** Mapping project data tracks across analytical categories (Recommendation/Retrieval, Descriptive, Predictive/Generative) and distinct team member task allocations.
3. **Schema Enforcement & Fail-Fast Mechanics:** Using explicit PySpark `StructType` definitions to reject malformed records at the ingestion gate.
4. **Malformed Record Handling:** Managing corrupt records across permissive, drop-malformed, and fail-fast modes, alongside Dead Letter Queue design.
5. **Streaming vs. Batch Ingestion:** Setting up Structured Streaming (`readStream`) for ASR audio chunk buffers versus batch JSON reads for VDB corpora.
