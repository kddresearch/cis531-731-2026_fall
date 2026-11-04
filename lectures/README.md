<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-03"
document_monotonicity: "REQUIRED"
routing_clearance: "PUBLIC - STUDENT FACING"
---
-->

<br>

<div align="center">
 <strong>🏫 Active Course Repositories:</strong> &nbsp;
 🏗️ <a href="https://github.com/kddresearch/course-architecture-base">Architecture Base</a> &nbsp;|&nbsp;
 🤖 CIS 530/730 &nbsp;|&nbsp;
 📊 <a href="https://github.com/kddresearch/cis531-731-2026_fall">CIS 531/731</a> &nbsp;|&nbsp;
 📈 CIS 732 &nbsp;|&nbsp;
 🎨 <a href="https://github.com/kddresearch/cis536-736-2026_fall">CIS 536/736</a> &nbsp;|&nbsp;
 👁️ CIS 798 X &nbsp;|&nbsp;
 🧠 CIS 830
</div>

<div align="center">
 <h1>📊 CIS 531/731 - Programming Techniques for Data Science and Analytics</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu<br>
 <strong>Status:</strong> ACTIVE | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Closed SSO Portal</a>
 </p>
</div>

<hr>

<div align="center">
 <h2>📂 Directory: lectures</h2>
 <p>
 <strong>Status:</strong> ACTIVE | <strong>Maintainer:</strong> Course Maintainers / KDD Lab
 </p>
</div>

<hr>

## 📖 Overview

This directory houses the official lecture schedule, slide decks, module breakdowns, and assigned reading materials for CIS 531/731 (Data Science Systems) for the Fall 2026 semester. The curriculum spans 43 structured lectures across 12 foundational modules, covering PySpark architectures, containerized environments, data streaming, vector database indexing, generative AI applications, EDA visualization, model evaluation, and MLOps deployment.

> **⚠️ Sub-Directory Routing Notice**
> This directory serves a specific pedagogical function. Ensure that artifacts committed here belong in this directory, rather than a different course module or upstream folder.

<hr>

## 🗂️ Directory Structure & Module Links

| Module Index / Directory | Description & Subcomponents |
| :--- | :--- |
| [`../modules/module_00/module_00.md`](../modules/module_00/module_00.md) | Module 00: Welcome, Track Selection Briefing & Course Overview |
| [`../modules/module_01/module_01.md`](../modules/module_01/module_01.md) | Module 01: PySpark Intro & Experiment Design (Lectures 01–04) |
| [`../modules/module_02/module_02.md`](../modules/module_02/module_02.md) | Module 02: Cloud Tools, DevContainers & AI/LLM Tooling (Lectures 05–07) |
| [`../modules/module_03/module_03.md`](../modules/module_03/module_03.md) | Module 03: ASR Stream Capture & VDB Corpus Acquisition (Lectures 08–10) |
| [`../modules/module_04/module_04.md`](../modules/module_04/module_04.md) | Module 04: Data Analytics Pipelines & Structured Streaming (Lectures 11–13) |
| [`../modules/module_05/module_05.md`](../modules/module_05/module_05.md) | Module 05: Chunking, Embedding Generation & VDB Design (Lectures 14–16) |
| [`../modules/module_06/module_06.md`](../modules/module_06/module_06.md) | Module 06: GenAI & Few-Shot Trope/Genre Classification (Lectures 17–21) |
| [`../modules/module_07/module_07.md`](../modules/module_07/module_07.md) | Module 07: Data Visualization & UMAP Embeddings (Lectures 22–24) |
| [`../modules/module_08/module_08.md`](../modules/module_08/module_08.md) | Module 08: Retrieval-Augmented Classification & Feature Pipelines (Lectures 25–27) |
| [`../modules/module_09/module_09.md`](../modules/module_09/module_09.md) | Module 09: Inferential Statistics & ASR Evaluation (Lectures 28–30) |
| [`../modules/module_10/module_10.md`](../modules/module_10/module_10.md) | Module 10: Model Interpretation, Metrics & Scoring (Lectures 31–33) |
| [`../modules/module_11/module_11.md`](../modules/module_11/module_11.md) | Module 11: Data Storytelling & Documentation Standards (Lectures 34–36) |
| [`../modules/module_12/module_12.md`](../modules/module_12/module_12.md) | Module 12: PaaS/IaaS, MLOps & Tracking (Lectures 37–39) |
| [`../modules/module_13/module_13.md`](../modules/module_13/module_13.md) | Module 13: Special Topics & Course Synthesis (Lectures 40–42) |

<hr>

## 📅 Lecture Schedule — CIS 531/731, Fall 2026 (43 Lectures)

*Refer to the complete chronological schedule and open-access reading index via the [Readings by Lecture Ledger](../reading_materials/readings_by_lecture.md).*

| Week | [Date & Master Schedule](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/02_course_schedule.md#-part-2-chronological-lecture--open-access-reading-schedule-43-lectures) | Lecture # | Topic | [Assigned Reading (Open-Access / Free-to-Read)](../reading_materials/readings_by_lecture.md) |
| :---: | :--- | :---: | :--- | :--- |
| 1 | Mon 24 Aug 2026 | [0](lecture_00.md) | Module 0 – Welcome & Course Overview | Wilkinson et al., *The FAIR Guiding Principles*; Jupyter Notebook Documentation |
| 1 | Wed 26 Aug 2026 | [1](lecture_01.md) | Module 1 – PySpark Intro: RDDs & DataFrames | VanderPlas, *Python Data Science Handbook* |
| 1 | Fri 28 Aug 2026 | [2](lecture_02.md) | Module 1 – Experiment Design & Reproducible Projects | Irving et al., *Research Software Engineering with Python* (Chs. 1–2) |
| 2 | Mon 31 Aug 2026 | [3](lecture_03.md) | Module 1 – RDD Transformations & Actions Lab | McKinney, *Python for Data Analysis*; VanderPlas |
| 2 | Wed 02 Sep 2026 | [4](lecture_04.md) | Module 1 – Project Structure, Testing & Module 1 Wrap-Up | Irving et al., *Research Software Engineering with Python* |
| 2 | Fri 04 Sep 2026 | [5](lecture_05.md) | Module 2 – Data Scrubbing & Early Exploration (MP 2 released) | Miner & Shook, Chapter 5; Brett et al., *Research Software Engineering* |
| 3 | Mon 07 Sep 2026 | — | **NO CLASS — Labor Day** | — |
| 3 | Wed 09 Sep 2026 | [6](lecture_06.md) | Module 2 – DevContainers & Docker | Docker *Get Started*; PyTorch Docker Hub |
| 3 | Fri 11 Sep 2026 | [7](lecture_07.md) | Module 2 – AI/LLM Tooling Overview; Wrap-Up (HW 1 due) | LiteLLM Virtual Keys; Milvus Quickstart; OpenAI Whisper |
| 4 | Mon 14 Sep 2026 | [8](lecture_08.md) | Module 3 `[O]` – Obtain: ASR Stream Capture & VDB Corpus Acquisition (MP 3 released) | Jurafsky & Martin, *SLP3* Ch. 16 (ASR) |
| 4 | Wed 16 Sep 2026 | [9](lecture_09.md) | Module 3 `[O]` – Whisper Architecture & Local Transcription | OpenAI Whisper Repository & Model Card |
| 4 | Fri 18 Sep 2026 | [10](lecture_10.md) | Module 3 `[O]` – Corpus Acquisition Lab; Wrap-Up (MP 2 due prior day) | Meta AI FAISS Repo; UFAL Whisper-Streaming |
| 5 | Mon 21 Sep 2026 | [11](lecture_11.md) | Module 4 – Data Analytics Pipelines: Streaming & Data Lakes (HW 4 released) | Akidau et al., *The Dataflow Model* (VLDB) |
| 5 | Wed 23 Sep 2026 | [12](lecture_12.md) | Module 4 – Spark Structured Streaming (PySpark 3.5 LTS) | Apache Spark 3.5.7 Structured Streaming Guide |
| 5 | Fri 25 Sep 2026 | [13](lecture_13.md) | Module 4 – Streaming Lab; Wrap-Up (MP 3 due prior day) | Apache Spark Streaming Overview |
| 6 | Mon 28 Sep 2026 | [14](lecture_14.md) | Module 5 `[S]` – Scrub: Chunking & Embedding Generation (PS 4 Proposal released) | Jurafsky & Martin, *SLP3* Ch. 11 (RAG) |
| 6 | Wed 30 Sep 2026 | [15](lecture_15.md) | Module 5 `[S]` – Semantic Search & VDB Schema Design | Sentence Transformers Semantic Search |
| 6 | Fri 02 Oct 2026 | [16](lecture_16.md) | Module 5 `[S]` – Embedding Lab / VDB Indexing; Wrap-Up (HW 4 due prior day) | Meta FAISS Index Docs; Milvus Quickstart |
| 7 | Mon 05 Oct 2026 | [17](lecture_17.md) | Module 6 – GenAI & LLMs: Candidates, Code, Classification (MP 5 released) | Jurafsky & Martin, *SLP3* Chs. 6 & 8 |
| 7 | Wed 07 Oct 2026 | [18](lecture_18.md) | Module 6 – Few-Shot Trope/Genre Classification | Hugging Face Transformers Text Classification Guide |
| 7 | Fri 09 Oct 2026 | — | **NO CLASS — Wildcat Pause Day** | — |
| 8 | Mon 12 Oct 2026 | [19](lecture_19.md) | Module 6 – Model Selection & Embedding-Backed Classification Lab (MP 6 released) | scikit-learn Text Data Tutorial |
| 8 | Wed 14 Oct 2026 | [20](lecture_20.md) | Module 6 – Trope/Genre Classification Workshop | Jurafsky & Martin, *SLP3* Ch. 10 |
| 8 | Fri 16 Oct 2026 | [21](lecture_21.md) | Module 6 – Wrap-Up (MP 5 due prior day; 5-lecture module absorbs Pause Day) | Hugging Face Transformers Evaluation Guide |
| 9 | Mon 19 Oct 2026 | [22](lecture_22.md) | Module 7 `[E]` – Explore: Data Visualization & Dashboards (MP 7 released) | Wilke, *Fundamentals of Data Visualization* |
| 9 | Wed 21 Oct 2026 | [23](lecture_23.md) | Module 7 `[E]` – Embedding-Space Visualization (UMAP) | UMAP-learn Parameters Documentation |
| 9 | Fri 23 Oct 2026 | [24](lecture_24.md) | Module 7 `[E]` – Generational Drift Dashboards Lab; Wrap-Up (PS 6 due prior day) | scikit-learn Manifold Guide; Wilke |
| 10 | Mon 26 Oct 2026 | [25](lecture_25.md) | Module 8 `[M]` – Modeling: Retrieval-Augmented Classification (MP 8 released) | Lewis et al., *RAG Paper* (arXiv:2005.11401) |
| 10 | Wed 28 Oct 2026 | [26](lecture_26.md) | Module 8 `[M]` – Feature Extraction Pipelines (PS 8 Interim Report released) | scikit-learn Text Feature Example |
| 10 | Fri 30 Oct 2026 | [27](lecture_27.md) | Module 8 `[M]` – Generational Convolution Models Lab; Wrap-Up (MP 7 due prior day) | Lewis et al. (RAG); scikit-learn Pipeline Docs |
| 11 | Mon 02 Nov 2026 | [28](lecture_28.md) | Module 9 – Evaluating Models: Inferential Statistics & Bootstrap CIs (HW 9 released) | James et al., *ISLP* (2023), Chs. 1, 5, 12 |
| 11 | Wed 04 Nov 2026 | [29](lecture_29.md) | Module 9 – ASR Evaluation Methodology & Gold-Standard Design | NIST OpenASR 2020 Challenge Evaluation Plan |
| 11 | Fri 06 Nov 2026 | [30](lecture_30.md) | Module 9 – Gold-Standard Construction Lab; Wrap-Up (PS 8 due Sat 07 Nov; MP 9 released) | scikit-learn Precision-Recall Guide; ISLP Labs |
| 12 | Mon 09 Nov 2026 | [31](lecture_31.md) | Module 10 `[N]` – Interpret: Applying Models for Data Science (MP 10 released) | James et al., *ISLP* Ch. 13 |
| 12 | Wed 11 Nov 2026 | [32](lecture_32.md) | Module 10 `[N]` – Model Metrics & Scoring | scikit-learn Metrics and Scoring Guide |
| 12 | Fri 13 Nov 2026 | [33](lecture_33.md) | Module 10 `[N]` – Interpretation Lab; Wrap-Up (HW 9 due prior day) | scikit-learn Calibration Guide; Sentence Transformers |
| 13 | Mon 16 Nov 2026 | [34](lecture_34.md) | Module 11 – Presenting Results: Ethics & Data Storytelling (MP 11 released) | Last, *Technical Writing Essentials* |
| 13 | Wed 18 Nov 2026 | [35](lecture_35.md) | Module 11 – Documentation & Notebook Presentation Standards | Jupyter Notebook Documentation; Wilkinson et al. (FAIR) |
| 13 | Fri 20 Nov 2026 | [36](lecture_36.md) | Module 11 – Dashboard Design Workshop; Wrap-Up (MP 10 due prior day) | Wilke; Last, *Technical Writing Essentials* |
| 14 | Mon 23 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| 14 | Wed 25 Nov 2026 | — | **NO CLASS — Fall Break** *(MP 10 due; PS 11 released)* | — |
| 14 | Fri 27 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| 15 | Mon 30 Nov 2026 | [37](lecture_37.md) | Module 12 – PaaS/IaaS, MLOps/AIOps (HW 12 released) | ML-Ops.org MLOps Principles |
| 15 | Wed 02 Dec 2026 | [38](lecture_38.md) | Module 12 – MLflow Tracking & Deployment | MLflow Tracking Documentation |
| 15 | Fri 04 Dec 2026 | [39](lecture_39.md) | Module 12 – Wrap-Up (MP 11 due prior day; **Take-Home Final Exam due today**) | FastAPI Docker Guide; MLflow Tracking |
| 16 | Mon 07 Dec 2026 | [40](lecture_40.md) | Module 13 – Special Topics: Agentic AI Systems Overview *(Extra-Credit Presentations begin)* | Software Engineering at Google (Winters et al.); Docker *Get Started* |
| 16 | Wed 09 Dec 2026 | [41](lecture_41.md) | Module 13 – Special Topics: Frontier Directions in Responsive Analytics | LiteLLM Proxy Docs; Bifrost Gateway; scikit-learn Text Examples |
| 16 | Fri 11 Dec 2026 | [42](lecture_42.md) | Module 13 – Special Topics: Course Synthesis & Wrap-Up (Last day of classes; HW 12 due Mon 14 Dec) | Winters et al., *Software Engineering at Google*; ML-Ops.org |

<hr>

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Schedule Integrity):** Any changes to lecture dates, topics, or assigned readings must be synchronized across the master schedule table and corresponding module READMEs.
* **Protocol 3 (Resource Archival):** Past semester lecture archives must be moved to `archive/` following final grade submission and verification.

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>
