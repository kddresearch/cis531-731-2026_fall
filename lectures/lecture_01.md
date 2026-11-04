# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 1: Foundations & Tooling** | **Module 01: PySpark Intro: RDDs & DataFrames** | **Lecture 01: PySpark Basics & Resilient Distributed Datasets (RDDs)** | Wednesday, August 26, 2026 |

---

## Slide 1: Course Introduction & Distributed Computing Foundations
### CIS 531/731 - Lecture 01 (Module 01)
* **Course Context:** Launching Phase 1 and Module 1 of the Fall 2026 semester.
* **Core Topic:** Distributed computing fundamentals, Spark cluster architecture, and Resilient Distributed Datasets (RDDs).
* **Assigned Reading:** VanderPlas, *Python Data Science Handbook* (referenced in the [Readings Master Index](../reading_materials/readings_by_lecture.md)).
* **Administrative Roadmap:** Reviewing the [Course Syllabus](../admin/syllabus/01_course_syllabus.md) and the [Master Course Schedule](../admin/syllabus/02_course_schedule.md).
* **Deliverable Release:** Official release of [HW 1: DevContainer Bring-Up & Term Project Architecture](../assignments/homework/hw1_devcontainer_bringup_architecture.md).

**Speaker Notes:**
Welcome to Lecture 1 of CIS 531/731. Building upon our foundational orientation in [Module 00: Welcome & Course Overview](../modules/module_00/module_00.md), today we transition into core distributed computing techniques using Apache Spark. As outlined in our [Course Syllabus](../admin/syllabus/01_course_syllabus.md), this course focuses on scalable data engineering and responsive analytics. Today we also officially release [HW 1: DevContainer Bring-Up & Term Project Architecture](../assignments/homework/hw1_devcontainer_bringup_architecture.md), which establishes your computational environment and term project track selections.

---

## Slide 2: Spark Cluster Architecture
### Driver Nodes, Executor Processes, and Parallelism
* **The Distributed Paradigm:** Moving from single-node local memory limitations to horizontal cluster scaling.
* **Driver Program:** The central coordinator that initializes the `SparkContext` / `SparkSession`, creates RDDs, and defines logical execution plans.
* **Cluster Manager:** Allocates physical resources across nodes (Standalone, YARN, Kubernetes, or Mesos).
* **Executor Processes:** Worker nodes launched across the cluster that execute assigned tasks and store cached data in memory or disk.

**SpeakerNotes:**
In standard single-node programming (like Pandas on a laptop), your data must fit entirely within local RAM. Spark shatters this limitation by adopting a master-worker topology. The Driver node acts as the brain, translating your Python script into a directed acyclic graph (DAG) of tasks. These tasks are sent out to Executor processes running across worker nodes, enabling massive parallel processing across distributed datasets without requiring manual thread management.

---

## Slide 3: Resilient Distributed Datasets (RDDs)
### Immutability, Lineage Graphs, and Fault Tolerance
* **Definition:** RDDs are fault-tolerant collections of operational elements that can be processed in parallel.
* **Immutability:** RDDs cannot be changed in place once created; transformations always produce new RDDs.
* **Lineage Graphs:** Spark records the deterministic sequence of operations (transformations) used to build an RDD, enabling instant reconstruction if a partition is lost.
* **Lazy Evaluation:** Operations are not computed when declared; execution is deferred until a terminal action is invoked.

**Speaker Notes:**
The foundational abstraction in Spark is the Resilient Distributed Dataset, or RDD. RDDs are immutable collections partitioned across your cluster. Instead of copying data across the network to recover from hardware failures, Spark uses lineage graphs. Because every RDD remembers exactly how it was constructed from raw storage, a lost partition can be recomputed on the fly. This guarantees fault tolerance without the massive overhead of synchronous checkpointing.

---

## Slide 4: Transformations vs. Actions
### Narrow Transformations, Wide Transformations, and Terminal Actions
* **Narrow Transformations (`map`, `filter`, `flatMap`):** Each partition of the parent RDD is used by at most one partition of the child RDD. No network shuffling required.
* **Wide Transformations (`groupByKey`, `reduceByKey`, `join`):** Child partitions depend on data from multiple parent partitions, triggering a costly network shuffle.
* **Actions (`collect`, `count`, `take`, `save`):** Trigger physical computation by evaluating the DAG and returning results to the driver or writing to storage.

**Speaker Notes:**
Understanding the boundary between transformations and actions is critical for writing efficient Spark code. Transformations are lazy—they only build the execution plan. Narrow transformations happen entirely within local executor nodes. Wide transformations, however, require data to be reorganized across the network—a process called a shuffle. Actions are the only operations that force Spark to execute the accumulated DAG. Never call `.collect()` on a massive dataset unless you want to crash the driver with an Out-Of-Memory error.

---

## Slide 5: Memory Management, Partitioning, and Caching
### Optimizing Cluster Resource Utilization
* **Partition Tuning:** Aligning partition counts with available CPU cores to maximize parallelism (avoiding excessive task overhead or partition starvation).
* **Caching & Persistence (`cache()` / `persist()`):** Storing intermediate RDD results in memory or disk across iterative algorithms.
* **Environment Alignment:** Ensuring all execution nodes match the pinned environment specifications detailed in the [Environment Runbook 1.0](../admin/syllabus/03_environment_runbook.md).
* **Integration with Schedule:** Tracking operational checkpoints against the [Master Course Schedule](../admin/syllabus/02_course_schedule.md).

**Speaker Notes:**
Performance in Spark is heavily governed by how you manage memory and partitions. If your partitions are too large, executors run out of memory; if they are too small, scheduling overhead dominates. When you reuse an RDD across multiple steps, you should explicitly cache it using `.persist()`. Furthermore, to guarantee that memory and Java dependencies behave identically across workstations, all local execution must run inside our containerized environment as specified in the [Environment Runbook 1.0](../admin/syllabus/03_environment_runbook.md).

---

## Slide 6: HW 1 Overview: DevContainer Bring-Up & Setup
### Verifying Your Local Infrastructure for Distributed Execution
* **Assignment Purpose:** Proving your local Docker DevContainer or Beocat access is correctly configured for PySpark 4.
* **Core Requirements:** Initializing `SparkSession`, verifying execution via the Spark Web UI (port 4040), and locking in term project matrix selections.
* **Governing Specification:** Read the complete requirements in [HW 1: DevContainer Bring-Up & Term Project Architecture](../assignments/homework/hw1_devcontainer_bringup_architecture.md).
* **Execution Standard:** Follow container build and runtime checks outlined in the [Environment Runbook 1.0](../admin/syllabus/03_environment_runbook.md).

**Speaker Notes:**
This brings us to our first major assignment release: [HW 1: DevContainer Bring-Up & Term Project Architecture](../assignments/homework/hw1_devcontainer_bringup_architecture.md). You are required to spin up your pinned DevContainer environment, verify that PySpark executes successfully, and confirm that your Spark Web UI is active on port 4040. Review the [Environment Runbook 1.0](../admin/syllabus/03_environment_runbook.md) carefully to ensure your local Docker daemon and WSL 2 integration are fully operational before attempting the bring-up.

---

## Slide 7: HW 1 Part 1 — PySpark 4 & Spark Web UI Proof
### Schema Enforcement and Port 4040 Verification
* **Task Scope:** Initialize a local `SparkSession` bound to port `4040` (`http://localhost:4040`).
* **Schema Enforcement:** Define an explicit `StructType` schema containing `StringType` and `IntegerType` fields (alongside metadata columns).
* **Data Verification:** Populate a 3-row test DataFrame and execute `.show(truncate=False)` to prove type safety.
* **Web UI Capture:** Capture a verification screenshot showing both your DataFrame output and the active Spark Web UI jobs page.
* **Scoring Criteria:** Graded strictly against the metrics in the [HW 1 Grading Rubric](../assignments/homework/hw1_grading_rubric.md).

**Speaker Notes:**
For Part 1 of HW 1, you must write a Python script or notebook that initializes Spark, builds an explicit `StructType` schema, and displays a 3-row DataFrame. You must also verify that the Spark Web UI is active on port 4040. The grader will evaluate your submission directly against the standards published in the [HW 1 Grading Rubric](../assignments/homework/hw1_grading_rubric.md). Make sure your screenshot clearly captures both the console output and the web interface.

---

## Slide 8: HW 1 Part 2 — Term Project Architecture & Matrix Selection
### Team Roster, Immutable Track Selection, and Task Allocation
* **Team Roster:** Form teams of 1–3 students and declare members.
* **Immutable Data Track Selection:** Choose either **Track 1 (ASR Live Stream Ingestion)** or **Track 2 (VDB Text Corpora)**.
* **Analytical Category Mapping:** Select your overarching goal (Prescriptive, Descriptive, or Predictive) using the [Term Project Taxonomy](../admin/syllabus/05_term_project_taxonomy.md).
* **Task Matrix Allocation:** Assign unique task ownership per team member across OSEMN stages, adhering to the [Term Project Sourcing Guide](../admin/syllabus/06_term_project_sourcing_guide.md).
* **Problem Statement:** Write a concise 3–4 sentence summary integrating your track, category, and task assignments.

**Speaker Notes:**
Part 2 of HW 1 locks in your architectural foundation for the semester. Every team must commit to an immutable data track: either Track 1 (ASR Live Stream) or Track 2 (VDB Text Corpora). You must consult the [Term Project Taxonomy](../admin/syllabus/05_term_project_taxonomy.md) to select your analytical category and the [Term Project Sourcing Guide](../admin/syllabus/06_term_project_sourcing_guide.md) to verify that your chosen dataset meets course standards. Ensure your team distributes OSEMN task ownership cleanly with zero overlapping duplicate tasks.

---

## Slide 9: Generative AI Policy & Audit Compliance
### Responsible AI Integration in CIS 531/731
* **Permitted Assistance:** Using LLMs for architectural debugging, schema review, and Python syntax explanation.
* **Mandatory Audit Log:** Every submission must include your exported `GenAI.pdf` interaction log (or an explicit `"No GenAI Used"` statement).
* **Core Governance:** Adhering strictly to the rules, prompts, and tollbooths defined in the [Generative AI Kit](../admin/policies/generative_ai_kit.md).
* **Platform Setup:** Follow the step-by-step configuration workflows detailed in the [Generative AI Kit How-To](../admin/policies/generative_ai_kit_howto.md).

**Speaker Notes:**
We encourage the responsible use of generative AI tools as epistemic co-pilots throughout this course. However, all AI interactions must be fully transparent. As detailed in the [Generative AI Kit](../admin/policies/generative_ai_kit.md) and [Generative AI Kit How-To](../admin/policies/generative_ai_kit_howto.md), you are required to include your `GenAI.pdf` audit log with your HW 1 submission. Never submit unverified boilerplate or fabricated citations; you remain fully responsible for the correctness of your code.

---

## Slide 10: Summary & Transition to Lecture 2
### Consolidating Foundations and Previewing DataFrames
* **Key Takeaway 1:** Distributed computing relies on RDD immutability, lazy evaluation, and lineage graph recovery.
* **Key Takeaway 2:** HW 1 is officially released—verify your DevContainer environment and establish your project matrix teams immediately ([HW 1 Assignment Guide](../assignments/homework/hw1_devcontainer_bringup_architecture.md)).
* **Key Takeaway 3:** Ground all project ideas in the [Term Project Taxonomy](../admin/syllabus/05_term_project_taxonomy.md) and [Term Project Sourcing Guide](../admin/syllabus/06_term_project_sourcing_guide.md).
* **Next Lecture:** In [Lecture 02: PySpark DataFrames & Spark SQL](lecture_02.md), we transition from raw RDDs to structured DataFrames and the Catalyst Optimizer.

**Speaker Notes:**
Today we laid down the foundational theory of distributed computing and RDD mechanics, while initiating our HW 1 bring-up. Be sure to review [HW 1: DevContainer Bring-Up & Term Project Architecture](../assignments/homework/hw1_devcontainer_bringup_architecture.md) and set up your project workspace using the [Environment Runbook 1.0](../admin/syllabus/03_environment_runbook.md). In our next session, [Lecture 02: PySpark DataFrames & Spark SQL](lecture_02.md), we will advance to structured DataFrames and query optimization. See you in class and in lab.
