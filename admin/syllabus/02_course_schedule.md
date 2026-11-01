<!--
---
yaml_schema_version: "2.2"
document_version: "1.0"
document_last_updated_date: "2026-11-01"
document_monotonicity: "REQUIRED"
routing_clearance: "PUBLIC - STUDENT FACING"
canvas_target_slug: "/courses/201513/pages/lectures"
---
-->

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
 <h1>📅 CIS 531 / CIS 731 — Master Course Schedule & Deliverables Ledger</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu<br>
 <strong>Document:</strong> <code>admin/syllabus/02_course_schedule.md</code> | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513/pages/lectures">Lectures &amp; Schedule Page</a>
 </p>
</div>

<hr>

## 📖 Overview & Mutability Governance

This document is the master chronological ledger synchronizing all **5 Course Phases**, **14 Modules (`Module 00`–`Module 13`)**, **43 Lectures (`Lecture 00`–`Lecture 42`)**, **Open-Access Assigned Readings**, and **12 Graded Assignments (`HW 1`–`HW 12`)** for Fall 2026.

> **ℹ️ Mutability Notice ("Subject to Change Until Release Date"):**
> * **Locked Contract Items:** Grading weights, the 30-point assignment normalization, the "drop lowest 2 of 9 regular assignments" policy, and the undroppable milestone status of **PS 4**, **PS 8**, and **HW 12** are permanently fixed.
> * **Release-Gated Adjustments:** Specific dataset fixtures or instructions for **not-yet-released assignments** (and readings for upcoming modules) remain subject to refinement prior to their official release date to accommodate infrastructure availability or class pacing. Deadlines are never moved earlier than listed below.

<hr>

## 📝 Part 1: Master Assignment & Milestone Schedule (12 Deliverables)

* **Legend:** `HW` = Homework (Setup / Mixed) | `MP` = Machine Problem (Programming) | `PS` = Problem Set (Design / Written / Report)
* **Normalized Weight:** Every assignment is graded on a **30.0-point scale** in Canvas.

| # | Type & ID | Assignment Title & Core Technical Scope | Associated Lab(s) | Release Date | Due Date (11:59 PM CT) | Drop Eligibility |
| :-: | :---: | :--- | :---: | :--- | :--- | :---: |
| 1 | **`HW 1`** | **DevContainer Bring-Up & Term Project Architecture:** PySpark 4 verification, `StructType` schema enforcement, Spark UI (`:4040`), and initial matrix selection. | [`lab01.ipynb`](../../assignments/homework/lab01.ipynb) | Wed 26 Aug 2026 | **Fri 11 Sep 2026** | Regular (1 of 9) |
| 2 | **`MP 2`** | **DevContainer Deployment & Manifest Verification:** Pinned `Dockerfile` build, SHA-256 runtime digest check (`verify_env.py`), and CPU/GPU compute probe (`probe_compute.py`). | — | Fri 04 Sep 2026 | **Tue 22 Sep 2026** | Regular (2 of 9) |
| 3 | **`MP 3`** | **Real-Time ASR & Vector Database Ingestion:** PySpark regex hyphenation preservation (`lab02`), local Whisper transcription of public-domain WWI audio (`lab03a`), and FAISS semantic indexing (`lab03b`). | [`lab02.ipynb`](../../assignments/homework/lab02.ipynb), [`lab03a.ipynb`](../../assignments/homework/lab03a.ipynb), [`lab03b.ipynb`](../../assignments/homework/lab03b.ipynb) | Mon 14 Sep 2026 | **Sun 04 Oct 2026** | Regular (3 of 9) |
| 4 | **`PS 4`** | **Term Project Proposal *(Mandatory Milestone 1)*:** 3x5x5 Data Cube coordinate lock, Tier 1/2 data sourcing plan, source-to-Bronze Obtain test, Scrub schema, and individual OSEMN stage allocation. | — | Mon 28 Sep 2026 | **Sun 11 Oct 2026** | **UNDROPPABLE MILESTONE** |
| 5 | **`MP 5`** | **Spark Structured Streaming & Live Ingest Architecture:** Event-time watermarking, tumbling/sliding window aggregations, state-store bounds, and `StreamingQueryProgress` liveness logging (`metrics.jsonl`). | [`lab04.ipynb`](../../assignments/homework/lab04.ipynb) | Fri 09 Oct 2026 | **Mon 19 Oct 2026** | Regular (4 of 9) |
| 6 | **`PS 6`** | **Semantic Search, Chunking, & VDB Schema:** Chunking cost model, FAISS (`IndexFlatIP`, `IVF`, `HNSW`) trade-offs, retrieval evaluation design, and Draft 2020-12 JSON Schema (`ps6-submission` tag). | [`lab03b.ipynb`](../../assignments/homework/lab03b.ipynb), [`lab5.ipynb`](../../assignments/homework/lab5.ipynb) | Fri 16 Oct 2026 | **Sun 25 Oct 2026** | Regular (5 of 9) |
| 7 | **`MP 7`** | **Few-Shot Trope/Genre Classification & Model Selection:** Unified `Classifier` interface across embedding prototypes, FAISS kNN, and fixed-demo few-shot LLMs (`k in {0,1,3,5,8}`, $\ge 5$ seeds, 95% bootstrap CIs). | [`lab5.ipynb`](../../assignments/homework/lab5.ipynb), [`lab6.ipynb`](../../assignments/homework/lab6.ipynb) | Wed 21 Oct 2026 | **Tue 03 Nov 2026** *(Extended)* | Regular (6 of 9) |
| 8 | **`PS 8`** | **Term Project Interim Report *(Mandatory Milestone 2)*:** Scope delta vs. PS 4, provenance audit, $\ge 3$ Wilke-compliant EDA/UMAP sensitivity figures, MP 7 baseline table, 5-item risk register, and gold annotation plan. | [`lab7.ipynb`](../../assignments/homework/lab7.ipynb), `lab08.ipynb` | Thu 29 Oct 2026 | **Sat 07 Nov 2026** | **UNDROPPABLE MILESTONE** |
| 9 | **`MP 9`** | **RAG Classification, Generational Convolutions, & Gold-Standard Construction:** Top-$k$ RAG conditioning, fixed (`[0.25,0.5,0.25]`, `[-1,1]`) and learned (`CIS 731`) cohort convolutions, and human gold-standard set ($\le 50$ rows / 2 hrs). | `lab08.ipynb` | Fri 06 Nov 2026 | **Mon 16 Nov 2026** | Regular (7 of 9) |
| 10 | **`MP 10`** | **Interpretability, Calibration, & Multiple-Testing Metrics:** Reliability diagrams, ECE/Brier calibration, slice-based error analysis, and Benjamini–Hochberg FDR control across cohort comparisons. | — | Fri 13 Nov 2026 | **Wed 25 Nov 2026** | Regular (8 of 9) |
| 11 | **`PS 11`** | **Ethics, Data Storytelling, & Dashboards:** Provenance/licensing audit, PII & ecological-fallacy guardrails, 5-view Wilke storyboard, and interactive dashboard with explicit limitations panel. | [`lab7.ipynb`](../../assignments/homework/lab7.ipynb) | Fri 20 Nov 2026 | **Fri 04 Dec 2026** | Regular (9 of 9) |
| 12 | **`HW 12`** | **Final Project Deliverables *(Mandatory Milestone 3)*:** 12-page technical report (`REPORT.pdf`), digest-pinned MLflow-tracked pipeline (`make verify`), 50–200 pooled gold evaluation set, serving endpoint, and PSI/KS drift runbook. | — | Sat 05 Dec 2026 | **Mon 14 Dec 2026** | **UNDROPPABLE MILESTONE** |

<hr>

## 📅 Part 2: Chronological Lecture & Open-Access Reading Schedule (43 Lectures)

| Week | Date | Lec # | Phase & Module Topic | Assigned Open-Access Reading ("Why" & "How") |
| :---: | :--- | :---: | :--- | :--- |
| **1** | Mon 24 Aug 2026 | **00** | **Phase 1 / Mod 0** – Welcome, Track Selection Briefing & Course Overview | [Wilkinson et al., *The FAIR Guiding Principles*](https://www.nature.com/articles/sdata201618); [Danchev, *Reproducible DS with Python*](https://valdanchev.github.io/reproducible-data-science-python/intro.html); [Jupyter Docs](https://jupyter-notebook.readthedocs.io/) |
| **1** | Wed 26 Aug 2026 | **01** | **Mod 1** – PySpark Intro: RDDs & DataFrames *(HW 1 released)* | [VanderPlas, *Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/) |
| **1** | Fri 28 Aug 2026 | **02** | **Mod 1** – Experiment Design & Reproducible Projects | [Irving et al., *Research Software Engineering with Python* (Chs. 1–2)](https://third-bit.com/py-rse/) |
| **2** | Mon 31 Aug 2026 | **03** | **Mod 1** – RDD Transformations & Actions Lab (`lab01.ipynb`) | [McKinney, *Python for Data Analysis, 3rd ed.: Getting Started with pandas*](https://wesmckinney.com/book/pandas-basics) |
| **2** | Wed 02 Sep 2026 | **04** | **Mod 1** – Project Structure, Testing & Module 1 Wrap-Up | [Irving et al., *RSE with Python* (Testing & Project Organization)](https://third-bit.com/py-rse/) |
| **2** | Fri 04 Sep 2026 | **05** | **Mod 2** – Tools: Cloud, HPC & Hosted Services *(MP 2 released)* | [Brett et al., *Research Software Engineering* (Chs. 1–2: Environments & Reproducibility)](https://rse-book.github.io/) |
| **3** | Mon 07 Sep 2026 | — | **NO CLASS — Labor Day** | — |
| **3** | Wed 09 Sep 2026 | **06** | **Mod 2** – DevContainers, Docker & Digest Pinning | [Docker *Get Started*](https://docs.docker.com/get-started/); [Official `pytorch/pytorch` Docker Hub](https://hub.docker.com/r/pytorch/pytorch); [NVIDIA Container Toolkit Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) |
| **3** | Fri 11 Sep 2026 | **07** | **Mod 2** – AI/LLM Tooling, VDB/ASR Layers & Quota Gateways; Wrap-Up *(HW 1 due)* | [LiteLLM *Virtual Keys*](https://docs.litellm.ai/docs/proxy/virtual_keys) & [*Team Budgets*](https://docs.litellm.ai/docs/proxy/users); [Milvus *Quickstart*](https://milvus.io/docs/quickstart.md); [OpenAI *Whisper*](https://github.com/openai/whisper) |
| **4** | Mon 14 Sep 2026 | **08** | **Phase 2 / Mod 3 `[O]`** – Obtain: ASR Stream Capture & VDB Corpus Acquisition *(MP 3 released)* | [Jurafsky & Martin, *SLP3* (Aug 19, 2026 draft), Ch. 16: *Automatic Speech Recognition*](https://web.stanford.edu/~jurafsky/slp3/) |
| **4** | Wed 16 Sep 2026 | **09** | **Mod 3 `[O]`** – Whisper Architecture & Local Transcription (`lab03a.ipynb`) | [Radford et al. / OpenAI *Whisper* Repository & Model Card](https://github.com/openai/whisper) |
| **4** | Fri 18 Sep 2026 | **10** | **Mod 3 `[O]`** – Corpus Acquisition & FAISS Indexing Lab (`lab03b.ipynb`); Wrap-Up | [Meta AI *FAISS* Repository](https://github.com/facebookresearch/faiss); [UFAL *Whisper-Streaming* Repository](https://github.com/ufal/whisper_streaming) |
| **5** | Mon 21 Sep 2026 | **11** | **Mod 4** – Data Analytics Pipelines: Streaming & Data Lakes *(MP 2 due Tue 22 Sep)* | [Akidau et al., *“The Dataflow Model: Balancing Correctness, Latency, and Cost”* (VLDB 2015 PDF)](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf) |
| **5** | Wed 23 Sep 2026 | **12** | **Mod 4** – Spark Structured Streaming (PySpark 3.5 LTS) | [Apache Spark 3.5.7 *Structured Streaming Programming Guide*](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html) |
| **5** | Fri 25 Sep 2026 | **13** | **Mod 4** – Structured Streaming Lab (`lab04.ipynb`); Wrap-Up | [Spark *Structured Streaming Overview*](https://spark.apache.org/docs/latest/streaming/index.html); [Spark 3.5.7 *Watermarking & State Guide*](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html) |
| **6** | Mon 28 Sep 2026 | **14** | **Phase 3 / Mod 5 `[S]`** – Scrub: Chunking & Embedding Generation *(PS 4 released)* | [Jurafsky & Martin, *SLP3* (Aug 19, 2026 draft), Ch. 11: *“Information Retrieval and RAG”* (PDF)](https://web.stanford.edu/~jurafsky/slp3/11.pdf) |
| **6** | Wed 30 Sep 2026 | **15** | **Mod 5 `[S]`** – Semantic Search & VDB Schema Design | [Sentence Transformers Documentation: *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) |
| **6** | Fri 02 Oct 2026 | **16** | **Mod 5 `[S]`** – Embedding & VDB Indexing Lab; Wrap-Up *(MP 3 due Sun 04 Oct)* | [Meta AI *FAISS* Docs](https://github.com/facebookresearch/faiss); [Milvus *Quickstart* (CIS 731 VDB Schema Guide)](https://milvus.io/docs/quickstart.md) |
| **7** | Mon 05 Oct 2026 | **17** | **Mod 6** – GenAI & LLMs: Candidates, Code, Classification | [Jurafsky & Martin, *SLP3* (Aug 19, 2026 draft), Ch. 6 (*Neural Nets* PDF)](https://web.stanford.edu/~jurafsky/slp3/6.pdf) & [Ch. 8 (*Post-Training* PDF)](https://web.stanford.edu/~jurafsky/slp3/8.pdf) |
| **7** | Wed 07 Oct 2026 | **18** | **Mod 6** – Few-Shot Trope/Genre Classification (`lab5.ipynb`) | [Hugging Face Transformers Task Guide: *“Text Classification”*](https://huggingface.co/docs/transformers/en/tasks/sequence_classification) |
| **7** | Fri 09 Oct 2026 | — | **NO CLASS — Wildcat Pause Day** *(MP 5 released; PS 4 due Sun 11 Oct)* | — |
| **8** | Mon 12 Oct 2026 | **19** | **Mod 6** – Model Selection & Embedding-Backed Classification Lab (`lab6.ipynb`) | [scikit-learn Tutorial: *“Working With Text Data”*](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) |
| **8** | Wed 14 Oct 2026 | **20** | **Mod 6** – Trope/Genre Classification & Prompt Controls Workshop | [Jurafsky & Martin, *SLP3* (Aug 19, 2026 draft), Ch. 10: *“Large Language Models”*](https://web.stanford.edu/~jurafsky/slp3/) |
| **8** | Fri 16 Oct 2026 | **21** | **Mod 6** – Wrap-Up *(PS 6 released; MP 5 due Mon 19 Oct; 5-lecture module absorbs Pause Day)* | [Hugging Face Transformers: *Sequence Classification & Evaluation*](https://huggingface.co/docs/transformers/en/tasks/sequence_classification) |
| **9** | Mon 19 Oct 2026 | **22** | **Phase 4 / Mod 7 `[E]`** – Explore: Data Visualization & Dashboards | [Wilke, *Fundamentals of Data Visualization* (Chs. 19–20 & Parts I–II)](https://clauswilke.com/dataviz/) |
| **9** | Wed 21 Oct 2026 | **23** | **Mod 7 `[E]`** – Embedding-Space Visualization (UMAP) *(MP 7 released)* | [UMAP-learn Documentation: *“Basic UMAP Parameters”*](https://umap-learn.readthedocs.io/en/latest/parameters.html) |
| **9** | Fri 23 Oct 2026 | **24** | **Mod 7 `[E]`** – Generational Drift Dashboards Lab (`lab7.ipynb`); Wrap-Up *(PS 6 due Sun 25 Oct)* | [scikit-learn User Guide: *“Manifold Learning and t-SNE”*](https://scikit-learn.org/stable/modules/manifold.html); [Wilke, *Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/) |
| **10** | Mon 26 Oct 2026 | **25** | **Mod 8 `[M]`** – Modeling: Retrieval-Augmented Classification | [Lewis et al., *“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”* (arXiv:2005.11401)](https://arxiv.org/abs/2005.11401) |
| **10** | Wed 28 Oct 2026 | **26** | **Mod 8 `[M]`** – Feature Extraction Pipelines *(PS 8 Interim Report released Thu 29 Oct)* | [scikit-learn Example: *“Sample Pipeline for Text Feature Extraction and Evaluation”*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html) |
| **10** | Fri 30 Oct 2026 | **27** | **Mod 8 `[M]`** – Generational Convolution Models Lab (`lab08.ipynb`); Wrap-Up *(MP 7 due Tue 03 Nov)* | [Lewis et al. (RAG)](https://arxiv.org/abs/2005.11401); [scikit-learn *Pipeline & FeatureUnion Documentation*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html) |
| **11** | Mon 02 Nov 2026 | **28** | **Phase 5 / Mod 9** – Evaluating Models: Inferential Statistics & Bootstrap CIs | [James et al., *An Introduction to Statistical Learning with Applications in Python* (ISLP, 2023), Chs. 1, 5, & 12](https://www.statlearning.com/resources-python) |
| **11** | Wed 04 Nov 2026 | **29** | **Mod 9** – ASR Evaluation Methodology & Gold-Standard Design | [NIST *OpenASR 2020 Challenge Evaluation Plan* (PDF)](https://www.nist.gov/document/openasr20-challenge-evaluation-plan) |
| **11** | Fri 06 Nov 2026 | **30** | **Mod 9** – Gold-Standard Construction Lab ($\le 50$-row / 2-hr homework cap); Wrap-Up *(PS 8 due Sat 07 Nov; MP 9 released)* | [scikit-learn Guide: *“Precision-Recall”*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html); [ISLP *Python-Edition Errata & Labs*](https://www.statlearning.com/errata-python-edition) |
| **12** | Mon 09 Nov 2026 | **31** | **Mod 10 `[N]`** – Interpret: Applying Models, Calibration & Multiple Testing | [James et al., *ISLP* (2023), Chs. 1–2, 4, 5, & 13 (*Resampling & Multiple Testing / Benjamini–Hochberg*)](https://www.statlearning.com/resources-python) |
| **12** | Wed 11 Nov 2026 | **32** | **Mod 10 `[N]`** – Model Metrics, Calibration & Scoring | [scikit-learn Documentation: *“Metrics and Scoring: Quantifying the Quality of Predictions”*](https://scikit-learn.org/stable/modules/model_evaluation.html) |
| **12** | Fri 13 Nov 2026 | **33** | **Mod 10 `[N]`** – Interpretation & Error Analysis Lab; Wrap-Up *(MP 9 due Mon 16 Nov; MP 10 released)* | [scikit-learn *Metrics & Probability Calibration Guide*](https://scikit-learn.org/stable/modules/model_evaluation.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) |
| **13** | Mon 16 Nov 2026 | **34** | **Mod 11** – Presenting Results: Ethics & Data Storytelling | [Last, *Technical Writing Essentials* (Chs. 1–3)](https://pressbooks.bccampus.ca/technicalwriting/) |
| **13** | Wed 18 Nov 2026 | **35** | **Mod 11** – Documentation, Provenance & Notebook Presentation Standards | [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/); [Wilkinson et al., *The FAIR Guiding Principles*](https://www.nature.com/articles/sdata201618) |
| **13** | Fri 20 Nov 2026 | **36** | **Mod 11** – Dashboard Design & Limitations Panel Workshop; Wrap-Up *(MP 10 due Wed 25 Nov; PS 11 released)* | [Wilke, *Fundamentals of Data Visualization* (Parts I–II)](https://clauswilke.com/dataviz/); [Last, *Technical Writing Essentials*](https://pressbooks.bccampus.ca/technicalwriting/) |
| **14** | Mon 23 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| **14** | Wed 25 Nov 2026 | — | **NO CLASS — Fall Break** *(MP 10 due; PS 11 released)* | — |
| **14** | Fri 27 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| **15** | Mon 30 Nov 2026 | **37** | **Mod 12** – PaaS/IaaS, MLOps/AIOps & Drift Monitoring | [ML-Ops.org, *“MLOps Principles”*](https://ml-ops.org/content/mlops-principles) |
| **15** | Wed 02 Dec 2026 | **38** | **Mod 12** – MLflow Tracking, Lineage & Model Registry | [MLflow Documentation: *MLflow Tracking*](https://mlflow.org/docs/latest/ml/tracking/) |
| **15** | Fri 04 Dec 2026 | **39** | **Mod 12** – Service Containerization & Wrap-Up *(PS 11 due today; Take-Home Final Exam due today; HW 12 released Sat 05 Dec)* | [FastAPI Documentation: *“FastAPI in Containers — Docker”*](https://fastapi.tiangolo.com/deployment/docker/); [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/) |
| **16** | Mon 07 Dec 2026 | **40** | **Mod 13** – Special Topics: Agentic AI Systems & Testing *(Extra-Credit Presentations begin after lecture)* | [Winters, Manshreck, & Wright, *Software Engineering at Google* (Chs. 11–12 & CI)](https://abseil.io/resources/swe-book/html/toc.html); [Docker *Get Started*](https://docs.docker.com/get-started/) |
| **16** | Wed 09 Dec 2026 | **41** | **Mod 13** – Special Topics: Frontier Directions in Responsive Analytics | [LiteLLM Proxy Governance Docs](https://docs.litellm.ai/docs/proxy/virtual_keys); [Bifrost AI Gateway Overview](https://docs.getbifrost.ai/overview); [scikit-learn *Text Examples Gallery*](https://scikit-learn.org/stable/auto_examples/index.html) |
| **16** | Fri 11 Dec 2026 | **42** | **Mod 13** – Special Topics: Course Synthesis & Wrap-Up *(Last day of classes; HW 12 due Mon 14 Dec)* | [Winters et al., *Software Engineering at Google*](https://abseil.io/resources/swe-book/html/toc.html); [ML-Ops.org, *“MLOps Principles”*](https://ml-ops.org/content/mlops-principles) |