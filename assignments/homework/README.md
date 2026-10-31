<!--
yaml_schema_version: "2.2"
document_version: "1.0"
document_last_updated_date: "2026-10-30"
document_monotonicity: "REQUIRED - Ensure document_version and timestamps strictly increment on every update. Reject regressions."
routing_clearance: "PUBLIC - STUDENT FACING (CIS 531/731 INFRASTRUCTURE)"
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
 <strong>Directory:</strong> <code>assignments/homework/</code> | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Closed SSO Portal</a>
 </p>
</div>

<hr>

## 📖 Overview

This directory contains the specifications for **Homeworks (`HW`)**, **Problem Sets (`PS`)**, and the hands-on **Laboratory Notebooks (`lab01.ipynb` – `lab7.ipynb`)** that scaffold the OSEMN (Obtain, Scrub, Explore, Model, iNterpret) data science pipeline across the semester.

*(Note: Standalone Machine Problem specifications live in the sibling [`../machine_problems/`](../machine_problems/) directory.)*

<hr>

## 📝 Homework & Problem Set Specifications

| Assignment | Title & Core Scope | Module / Phase | Milestone Type |
| :--- | :--- | :--- | :--- |
| [**`HW 1`**](./hw1_devcontainer_bringup_architecture.md) | **DevContainer Bring-Up & Term Project Architecture:** PySpark 4 verification, `StructType` schema enforcement, Spark Web UI (`:4040`), and initial project matrix selection. | Module 1 (Phase 1) | Diagnostic Gate |
| [**`PS 4`**](./ps4_proposal.md) | **Term Project Proposal:** 3x5x5 Data Cube coordinate selection, Tier 1/2 data sourcing plan, Obtain/Scrub feasibility evidence, and individual OSEMN stage allocation. | Module 4 (Phase 2) | **Milestone 1 (Undroppable)** |
| [**`PS 6`**](./ps6_semantic_search_vdb_schema.md) | **Semantic Search, Chunking, & VDB Schema:** Chunking cost model, FAISS (`IndexFlatIP`, `IVF`, `HNSW`) trade-offs, retrieval evaluation protocol, and provenance-bearing JSON Schema (Draft 2020-12). | Module 5 (Phase 3) | Problem Set |
| [**`PS 8`**](./ps8_interim_report.md) | **Interim Report:** Scope delta from PS 4, data provenance table, UMAP sensitivity sweep (`n_neighbors`, `min_dist`), MP 7 baseline metrics, 5-item quantified risk register, and 50–200 gold annotation plan. | Modules 7–8 (Phase 4) | **Milestone 2 (Undroppable)** |
| [**`PS 11`**](./ps11_ethics_storytelling_dashboards.md) | **Ethics, Data Storytelling, & Dashboards:** Provenance, privacy/PII redaction, ecological-fallacy and ASR-disparity audit, 5-view Wilke storyboard, and reproducible dashboard prototype with limitations panel. | Module 11 (Phase 5) | Problem Set |
| [**`HW 12`**](./hw12_final_deliverables.md) | **Final Project Deliverables:** 12-page technical report (`REPORT.pdf`) and digest-pinned, MLflow-tracked reproducible pipeline (`make verify`, 50–200 gold-standard range gate, serving path, and PSI/KS drift runbook). | Module 12 (Phase 5) | **Milestone 3 (Undroppable)** |

<hr>

## 🧪 Laboratory Notebooks (`Labs` Table of Contents)

The following interactive Jupyter notebooks provide the executable building blocks for both the Machine Problems and the default course pipeline (**satellite radio caller ASR streams + song lyric/media trope vector databases**):

### 📑 Quick Navigation
1. [Lab 1a (`lab01.ipynb`): PySpark Bring-Up, The "Obtain" Stage & Matrix Selection](#1-lab-1a-lab01ipynb--pyspark-bring-up-the-obtain-stage--matrix-selection)
2. [Lab 2 (`lab02.ipynb`): The "Scrub" Stage – Data Cleaning, Text Tokenization & Feature Extraction](#2-lab-2-lab02ipynb--the-scrub-stage--data-cleaning-text-tokenization--feature-extraction)
3. [Lab 3a (`lab03a.ipynb`): Local ASR with OpenAI Whisper](#3-lab-3a-lab03aipynb--local-asr-with-openai-whisper)
4. [Lab 3b (`lab03b.ipynb`): VDB Corpus Acquisition with FAISS](#4-lab-3b-lab03bipynb--vdb-corpus-acquisition-with-faiss)
5. [Lab 4 (`lab04.ipynb`): Spark Structured Streaming](#5-lab-4-lab04ipynb--spark-structured-streaming)
6. [Lab 5 (`lab5.ipynb`): Few-Shot Trope & Genre Classification](#6-lab-5-lab5ipynb--few-shot-trope--genre-classification)
7. [Lab 6 (`lab6.ipynb`): Model Selection & Embedding-Backed Classification](#7-lab-6-lab6ipynb--model-selection--embedding-backed-classification)
8. [Lab 7 (`lab7.ipynb`): Generational Drift Dashboards & UMAP](#8-lab-7-lab7ipynb--generational-drift-dashboards--umap)

---

### 1. [Lab 1a (`lab01.ipynb`)](./lab01.ipynb) — PySpark Bring-Up, The "Obtain" Stage & Matrix Selection
* **Module & Phase:** Module 1 (Phase 1: Infrastructure & Foundations)
* **Associated Assignments:** [`HW 1`](./hw1_devcontainer_bringup_architecture.md)
* **Definition & Technical Scope:** Initializes a local `SparkSession` and demonstrates schema enforcement (`StructType`) across both course tracks: (1) **VDB Track** batch JSON ingestion comparing `PERMISSIVE` vs. `FAILFAST` malformed-record handling, and (2) **ASR Track** `readStream` micro-batch ingestion into an in-memory sink. Concludes with the editable Markdown template for locking in team rosters and project matrix coordinates.

### 2. [Lab 2 (`lab02.ipynb`)](./lab02.ipynb) — The "Scrub" Stage – Data Cleaning, Text Tokenization & Feature Extraction
* **Module & Phase:** Module 3 (Phase 2: Pipeline Construction)
* **Associated Assignments:** [`MP 3`](../machine_problems/mp3_real_time_asr_vector_database_ingestion.md) (Part 1)
* **Definition & Technical Scope:** Implements an end-to-end PySpark SQL and `pyspark.ml.feature` cleaning pipeline over dirty/duplicate document records: null filtering (`dropna`), primary-key deduplication (`dropDuplicates`), metadata imputation (`fillna`), regex text normalization (`F.regexp_replace`, modified in MP 3 to preserve hyphenated compound words such as `large-scale`), `Tokenizer`, `StopWordsRemover`, and sparse TF-IDF vectorization (`HashingTF` + `IDF`).

### 3. [Lab 3a (`lab03a.ipynb`)](./lab03a.ipynb) — Local ASR with OpenAI Whisper
* **Module & Phase:** Module 3 (Phase 2: Pipeline Construction)
* **Associated Assignments:** [`MP 3`](../machine_problems/mp3_real_time_asr_vector_database_ingestion.md) (Part 2)
* **Definition & Technical Scope:** Initializes a local, offline `openai-whisper` (`base`) model inside the DevContainer (without relying on paid cloud APIs), downloads the public-domain LibriVox WWI Poetry archive (`wwi_poetry.zip`), extracts Wilfred Owen's *"Anthem for Doomed Youth"* (`wwipoem_51_owen_am_64kb.mp3`), and produces the raw speech-to-text transcription `result["text"]` for downstream vector indexing.

### 4. [Lab 3b (`lab03b.ipynb`)](./lab03b.ipynb) — VDB Corpus Acquisition with FAISS
* **Module & Phase:** Module 3 (Phase 2: Pipeline Construction)
* **Associated Assignments:** [`MP 3`](../machine_problems/mp3_real_time_asr_vector_database_ingestion.md) (Part 2), [`PS 6`](./ps6_semantic_search_vdb_schema.md)
* **Definition & Technical Scope:** Encodes simulated radio caller ASR snippets (breakup distress, summer music nostalgia, generational angst) alongside the transcribed LibriVox poem from Lab 3a into 384-dimensional dense vectors using Hugging Face `SentenceTransformer('all-MiniLM-L6-v2')`. Indexes the embeddings in a local `faiss.IndexFlatL2` vector database and executes nearest-neighbor semantic search (`k=1`) for the trope concept `"doomed youth"`.

### 5. [Lab 4 (`lab04.ipynb`)](./lab04.ipynb) — Spark Structured Streaming
* **Module & Phase:** Module 4 (Phase 2: Obtain & Ingest)
* **Associated Assignments:** [`MP 5`](../machine_problems/mp5_structured_streaming.md)
* **Definition & Technical Scope:** Operationalizes *The Dataflow Model* (Akidau et al.) in PySpark Structured Streaming. Connects to a continuous simulated `rate` stream, enriches records with event categories, applies a 15-second event-time watermark (`.withWatermark("timestamp", "15 seconds")`) to bound state growth on late-arriving data, computes 10-second tumbling-window counts, and polls the live micro-batch sink via Spark SQL.

### 6. [Lab 5 (`lab5.ipynb`)](./lab5.ipynb) — Few-Shot Trope & Genre Classification
* **Module & Phase:** Module 6 (Phase 3: Scrub & Embed / GenAI & LLMs)
* **Associated Assignments:** [`PS 6`](./ps6_semantic_search_vdb_schema.md), [`MP 7`](../machine_problems/mp7_genre_classification.md)
* **Definition & Technical Scope:** Transitions from vector retrieval to zero-shot/few-shot classification using Hugging Face `pipeline("zero-shot-classification", model="facebook/bart-large-mnli")`. Evaluates ASR and literary transcript chunks against the baseline 4-class trope ontology (`"Chosen One Fantasy"`, `"Doomed Youth / Tragedy"`, `"Summer Romance"`, `"Sci-Fi Cyberpunk"`) and outputs top-2 trope probability distributions.

### 7. [Lab 6 (`lab6.ipynb`)](./lab6.ipynb) — Model Selection & Embedding-Backed Classification
* **Module & Phase:** Module 6 (Phase 3: Scrub & Embed / GenAI & LLMs)
* **Associated Assignments:** [`PS 6`](./ps6_semantic_search_vdb_schema.md), [`MP 7`](../machine_problems/mp7_genre_classification.md), [`MP 9`](../machine_problems/mp9_rag_classification_gold_standard.md)
* **Definition & Technical Scope:** Constructs an embedding-prototype classifier using `SentenceTransformer('all-MiniLM-L6-v2')` by encoding explicit natural-language definitions of the reference tropes (`reference_tropes` dictionary). Classifies incoming chunks via cosine similarity (`1 - cosine(u, v)`) and enforces an out-of-distribution confidence threshold (`CONFIDENCE_THRESHOLD = 0.35`) to reject off-domain inputs (e.g., an unrelated pizza order) as `UNKNOWN / OUT OF DISTRIBUTION`.

### 8. [Lab 7 (`lab7.ipynb`)](./lab7.ipynb) — Generational Drift Dashboards & UMAP
* **Module & Phase:** Module 7 (Phase 4: Explore & Model)
* **Associated Assignments:** [`PS 8`](./ps8_interim_report.md), [`MP 9`](../machine_problems/mp9_rag_classification_gold_standard.md), [`PS 11`](./ps11_ethics_storytelling_dashboards.md)
* **Definition & Technical Scope:** Fits a global 2D topological projection (`umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2, random_state=42)`) across chronologically tagged embeddings (`1990s`, `2000s`, `2010s`, `2020s`) without per-era coordinate warping, computes high-dimensional centroid cosine distance (`calculate_centroid_drift`) between eras, and provides a modular Streamlit + Plotly interactive dashboard skeleton (`app.py`).

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>
