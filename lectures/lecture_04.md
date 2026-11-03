# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 1:** Foundations & Tooling | **Module 01:** PySpark Intro & Experiment Design | **Lecture 04:** Lab 1 – PySpark 4 Bring-up & The "Obtain" Stage | Wednesday, September 02, 2026 |

---

## Slide 1: Lab 1 — PySpark 4, Project Architectures & The Rubric
### CIS 531/731 - Lecture 04 (Module 01)
* **Objective:** Move from local Python to distributed cluster execution.
* **The Tools:** PySpark 4, Docker DevContainers, or the Beocat Cluster.
* **The Goal:** Initialize a `SparkSession` and define your term project trajectory.
* **The Shift:** Retiring Databricks Accelerators in favor of the Multidimensional Matrix.
* **Session Format:** Instructor demonstration followed by team formation and matrix selection.

**Speaker Notes:**
Welcome to Lab 1. Today, we are putting our PySpark 4 theory into practice. You are going to spin up your Spark Sessions and begin the 'Obtain' phase of the OSEMN pipeline. But before you write a line of ingestion code, you need to know what you are building. In the past, this course relied heavily on pre-packaged Databricks Solution Accelerators. This semester, we are ripping off the training wheels. You are going to build custom pipelines using a multidimensional rubric, mapping your chosen data track to specific analytic tasks.

---

## Slide 2: The Two Data Tracks (The "What")
### Track Selection & Ingest Pipeline Scope
* **Track 1: ASR (Audio/Multimedia & Text)**
  * Live streaming radio, podcast, or call-in audio.
  * Bounding real-time buffers and executing speech-to-text.
* **Track 2: VDB (Text & Information Retrieval)**
  * Massive static text corpora (lyrics, YA-Lit, Xianxia/Wuxia).
  * Semantic chunking and vector embedding generation.
* **Track Immutability:** You must lock in your data source today.

**Speaker Notes:**
Your first decision is the "What". What data are you processing? You must choose between Track 1 (ASR) and Track 2 (VDB). ASR requires you to handle live, streaming multimedia and convert it to text on the fly. VDB requires you to ingest massive, static text corpora and convert them into dense vector embeddings. Choose carefully based on your team's systems engineering comfort level, because once you lock this track, your data ingestion pipeline is set for the semester.

---

## Slide 3: The Multidimensional Matrix (The "How")
### Categorizing Project Analytical Scope
* **Category 1:** Recommendation, Information Retrieval, Prescriptive Analytics, Automation.
* **Category 2:** Descriptive Analytics (Dashboards, Storytelling).
* **Category 3:** Predictive Analytics, Generative Text for Question Answering.
* **The Rule:** Each team must select at least one Category. Solo projects select exactly one.

**Speaker Notes:**
Once you know *what* your data is, you must decide *how* you will analyze it. We divide projects into three broad categories. Category 1 focuses on building engines—retrieval systems, automation, and prescriptive recommendations. Category 2 is entirely about making the invisible visible—building descriptive analytics and dashboards to find anomalies. Category 3 is about the future—predictive analytics and generative question-answering systems. Your team must plant its flag in at least one of these categories.

---

## Slide 4: Mapping Tasks to Team Members
### Accountability & Division of Labor
* **The Task Columns:** Prediction, Classification, Summarization, Collection Analysis, Retrieval.
* **The Accountability Rule:** Every team should identify at least one task for the team.
* **Individual Ownership:** *No more than one task per team member.*
* **Shared Tasks:** If a task is shared, the exact division of labor (e.g., baseline vs. alternative model) must be explicitly stated.

**Speaker Notes:**
This is where individual accountability comes in. Look at the task columns in the rubric: Classification, Summarization, Retrieval, and so on. If you are on a three-person team, I expect to see distinct task ownership. One team member might own "Classification" of the text, while another owns "Summarization," and the third owns "Retrieval." If two of you want to tackle "Classification," one of you is building the baseline model, and the other is building the alternative model. There is nowhere to hide in this architecture.

---

## Slide 5: Matrix Example — The ASR Track
### Audio & Speech Processing Pipeline Mapping
* **Data Variety:** Multimedia (Audio) / Text.
* **Category 3 (Predictive/QA) + Summarization:** "Automating Podcast Review Summarization with LLMs."
* **Category 2 (Descriptive) + Classification:** "Toxicity Detection in Live Gaming Streams."
* **Category 1 (Retrieval) + Structured Data:** "Automated Protected Health Information (PHI) Removal."

**Speaker Notes:**
Let’s look at how this maps out. If you choose the ASR track, your data variety is Multimedia and Text. If you pair that with Category 3 and the "Summarization" task, your project might be building a pipeline that listens to live podcasts and generates real-time summaries. If you pair it with Category 2 and "Classification," you are building a toxicity detection dashboard for live gaming streams. The matrix gives you the freedom to explore, but the structure to actually finish the project.

---

## Slide 6: Matrix Example — The VDB Track
### Text Corpora & Vector Embedding Pipeline Mapping
* **Data Variety:** Text / Structured Data.
* **Category 1 (Retrieval) + Text:** "Biomedical Literature Q&A with LLMs."
* **Category 2 (Descriptive) + Collection Analysis:** "Cohort Building with Knowledge Graphs from YA-Lit."
* **Category 3 (Generative) + Retrieval:** "LLMs for Knowledge-Based Q&A Agents."

**Speaker Notes:**
For the VDB track, your data variety is Text. Pairing this with Category 1 Retrieval yields a classic Vector Database architecture: a Q&A agent querying biomedical literature or Wuxia novels. Pairing it with Category 2 Collection Analysis means you might be extracting entities from literature to build knowledge graphs and trace how tropes evolve across generations.

---

## Slide 7: Initialization (The Spark Session)
### Cluster & DevContainer Entry Points
* **The Entry Point:** `SparkSession.builder.getOrCreate()`
* **Spark Connect:** Decoupling the client environment from the heavy JVM backend.
* **Local Mode:** Running `local[*]` to utilize all laptop CPU cores.
* **Cluster Mode:** Submitting the job to Beocat (YARN / Slurm).
* **The Web UI:** Accessing port `4040` to visually track your DAG execution.

**Speaker Notes:**
Now, let's get to the keyboards. Before we can process any of this data, we have to wake up the engine. If you are developing locally on your Docker DevContainers, you will initialize Spark with `local[*]`. If you are on Beocat, your session will negotiate with the cluster manager. Once your session is alive, open a tab to port `4040`—that is your Spark Web UI. You will need to watch this to see your Directed Acyclic Graphs compile.

---

## Slide 8: The "Obtain" Stage & Schema Enforcement
### Reading Data & Strict Typing
* **DataFrame Reader API:** `spark.read.format("...").load("...")`
* **The `StructType` Definition:** Explicitly defining your expected columns.
* **Fail-Fast Mechanics:** Forcing the pipeline to crash at the ingestion gate if data is malformed.
* **VDB Ingest:** Loading massive JSON lines with metadata intact.
* **ASR Ingest:** Structured Streaming (`spark.readStream`) to buffer 10-second audio chunks.

**Speaker Notes:**
The Obtain stage is the first step of the OSEMN pipeline. We use the DataFrame Reader API to ingest our data. The cardinal rule today is: do not use schema inference. You must define a strict PySpark `StructType`. If you define a column as an Integer, and a live stream hands you a string, the pipeline must reject the row immediately. This "fail-fast" mechanic is mandatory. It is infinitely better for your pipeline to crash today during the Obtain phase than to silently pass poisoned data into your models in Week 8.

---

## Slide 9: Handling Malformed Records
### Ingestion Modes & Dead Letter Queues
* **`mode="PERMISSIVE"`:** Spark sets corrupt fields to null (dangerous).
* **`mode="DROPMALFORMED"`:** Spark silently throws away the bad row.
* **`mode="FAILFAST"`:** Spark kills the job upon hitting a bad record.
* **The Dead Letter Queue:** Routing bad data to a separate folder for forensic analysis.

**Speaker Notes:**
You will hit malformed records today. Your JSON will be missing a bracket, or your audio stream will drop packets. By default, Spark is "Permissive"—it fills bad data with nulls and keeps running. Do not rely on this. The professional architecture is to use a "Dead Letter Queue"—routing the bad data to a separate storage bucket so your pipeline stays up, but you still have a forensic record of what failed.

---

## Slide 10: Lab Execution, Coursework Links & Cross-Platform Notes
### Homework & Machine Problem Integration
* **Lab Notebook Execution:** Work directly through [`lab01.ipynb`](../assignments/homework/lab01.ipynb) to bring up `SparkSession` and test schema modes.
* **Homework & MP Links:** Complete your matrix commitments in [`HW 1`](../assignments/homework/hw1_devcontainer_bringup_architecture.md) and prepare environment pinning for [`MP 2`](../assignments/machine_problems/mp2_devcontainer_deployment_manifest_verification.md).
* **Environment Verification:** Execute [`verify_env.py`](../assignments/machine_problems/verify_env.py) inside your DevContainer to check your SHA-256 manifest string (`6f0648c...`).
* **Platform-Specific Architecture Guides:**
  * **Windows 11 Users:** Follow the [Windows 11 + WSL 2 + Docker Desktop Walkthrough](../docs/setup/hw1_mp2_windows11_wsl2_docker_walkthrough.md).
  * **macOS (Intel/Apple Silicon) & Linux Users:** Refer to the parallel [macOS & Linux DevContainer Bring-Up Guide](../docs/setup/hw1_mp2_macos_linux_docker_walkthrough.md) for native Docker socket permissions (`/var/run/docker.sock`), arm64 Java 11 JRE setups, and host-to-container volume mount nuances.

**Speaker Notes:**
It is time to execute. Open `lab01.ipynb` in VS Code. If you are on Windows 11 with WSL 2, follow the step-by-step setup walkthrough in `docs/setup/`. If you are running on macOS (Intel or M1/M2/M3) or native Linux, use the companion macOS/Linux guide to ensure your Docker daemon socket and volume permissions are correctly configured. Once your Spark Web UI is live on port 4040 and `verify_env.py` returns the target digest string, present your screen to the instructor or TA to complete the verification gate.
