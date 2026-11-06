<!--
  Template Note: This file serves as the canonical template for module pages.
  When instantiated as `modules/module_YY/module_YY.md`, use relative paths 
  (`../../phases/phase_0X/` and `../../lectures/lecture_j.md`) to maintain correct routing.
  Note that the module name itself does not self-link, but lectures link directly to their markdown files.
  Module readings may be contiguous or separate per lecture; the module readings for the modules within a parent phase form a partition of that phase’s readings.
-->

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 2](../../phases/phase_02/):** Obtain & Ingest | **Module 04:** Data Analytics Pipelines: Streaming & Data Lakes | **Lectures 11-13** | Mon 21 Sep - Fri 25 Sep 2026 | [Akidau et al., *The Dataflow Model*](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf); [Apache Spark Structured Streaming Guide](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html) |

---

## [Lecture 11: Data Analytics Pipelines — Streaming & Data Lakes](../../lectures/lecture_11.md) (Mon 21 Sep 2026)

1. **The Dataflow Model:** Principles of handling massive, unbounded, out-of-order datasets based on the Akidau et al. framework.
2. **Streaming vs. Batch Processing:** Identifying the computational and latency trade-offs between continuous event streams and static batch pipelines.
3. **Data Lakes Architecture:** Decoupling storage from compute to support scalable, heterogeneous data ingestion and schema-on-read paradigms.
4. **Event Time vs. Processing Time:** Defining windowing functions, watermarks, and late data handling in continuous analytics.
5. **HW4 Release:** Introduction to the data stream monitoring assignment constraints and pipeline deliverables.
* **Assigned Reading:** [Akidau et al., *“The Dataflow Model: Balancing Correctness, Latency, and Cost”* (VLDB 2015 PDF)](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf)

---

## [Lecture 12: Spark Structured Streaming](../../lectures/lecture_12.md) (Wed 23 Sep 2026)

1. **Structured Streaming Model:** Translating DataFrame and Dataset operations onto unbounded streaming tables in Spark 3.5.7.
2. **Triggers and Output Modes:** Configuring micro-batch execution frequencies and Complete, Append, or Update output logic.
3. **Fault Tolerance & Checkpointing:** Ensuring exactly-once fault-tolerance semantics using write-ahead logs and state stores.
4. **Stateful Operations:** Managing arbitrary state across micro-batches for complex event processing and sessionization.
5. **Source & Sink Integration:** Connecting Spark Structured Streaming to distributed message brokers (Kafka) and Data Lake sinks.
* **Assigned Reading:** [Apache Spark 3.5.7 *Structured Streaming Programming Guide*](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html)

---

## [Lecture 13: Streaming Lab & Wrap-Up](../../lectures/lecture_13.md) (Fri 25 Sep 2026)

1. **Lab Setup:** Initializing the PySpark streaming context and connecting to a simulated live continuous data feed.
2. **Continuous Query Execution:** Authoring and deploying a windowed aggregation query to compute rolling metrics on the stream.
3. **Watermark Configuration:** Applying late-data thresholds to bound memory usage during stateful aggregations.
4. **Storage Sink Routing:** Ensuring the processed micro-batches are correctly persisted to the designated Data Lake storage path.
5. **MP 3 Debrief & Wrap-Up:** Reviewing the MP 3 (submitted prior day) solutions and verifying readiness for the Module 5 Scrub phase.
* **Assigned Reading:** [Apache Spark *Structured Streaming Overview*](https://spark.apache.org/docs/latest/streaming/index.html); [Spark 3.5.7 *Watermarking & State Store Guide*](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html)
