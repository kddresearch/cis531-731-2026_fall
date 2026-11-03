# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 1:** Foundations & Tooling | **Module 01:** PySpark Intro: RDDs, DataFrames; Projects, Experiment Design | **Lectures 01-04** | Wed 26 Aug - Wed 02 Sep 2026 |

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

## Lecture 03: Data Science Project Lifecycle & Experimentation (Mon 31 Aug)

1. **Data Science Lifecycles:** Mapping business objectives to iterative data acquisition, scrubbing, modeling, and deployment phases.
2. **Experimental Design Principles:** Formulating testable hypotheses, defining baseline metrics, and establishing validation strategies.
3. **Reproducibility & Environment Control:** Managing random seeds, dataset versioning, and environment dependencies across distributed runs.
4. **Metric Selection:** Aligning evaluation metrics (RMSE, MAE, Precision, Recall, F1, ROC-AUC) with analytical goals.
5. **A/B Testing & Controlled Evaluation:** Structuring split testing frameworks and statistical significance evaluation in analytical pipelines.

---

## Lecture 04: Advanced PySpark DataFrames & Project Scoping (Wed 02 Sep)

1. **User-Defined Functions (UDFs):** Implementing scalar and vector (Pandas UDFs via PyArrow) custom transformation functions.
2. **Complex Data Types:** Handling nested structures, arrays (`explode`), and map columns in PySpark DataFrames.
3. **Window Functions:** Computing rolling aggregations, lead/lag operations, and analytical rankings over partitioned windows.
4. **Data Ingestion & Serialization:** Reading/writing optimized columnar formats (Parquet, ORC) and JSON/CSV streams.
5. **Term Project Scoping & Problem Formulation:** Structuring project proposals, defining data intake requirements, and establishing milestone deliverables.
