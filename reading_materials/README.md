<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-10-30"
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
 <h2>📚 Directory: reading_materials/</h2>
 <h3>Document: README.md (Module-Aligned Readings, Licensing & Runtime Compatibility Ledger)</h3>
 <p>
 <strong>Status:</strong> ACTIVE | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview & Three-Tier Open-Access Licensing Mandate

This document serves as the canonical **Module-Aligned Readings Index** for **CIS 531/731 (Fall 2026)**, paired with the chronological lecture breakdown in [`readings_by_lecture.md`](./readings_by_lecture.md). For every module (`0`–`13`), one or more **Theoretical Readings ("Why")** are paired with **Practical Systems & API Documents ("How")**.

All assigned readings strictly obey a **100% Open-Access / Free-to-Read Mandate** (zero paywalls or proprietary institutional logins required) and the **Stale Edition Rule** (legacy free editions of textbooks whose current editions are paywalled or mismatched with Python 3 / PySpark 3.5 LTS / PyTorch 2.x are suppressed):

1. **Tier 1 (Preferred — Fully Open Access):** Materials released under Creative Commons (e.g., `CC BY 4.0`, `CC BY-NC-SA 4.0`, `CC BY-NC-ND 4.0`), open-source documentation licenses, or official open-access venue/preprint distributions (`Scientific Data`, `VLDB`, `arXiv`).
2. **Tier 2 (Acceptable — Sanctioned Author / Project-Hosted Free-to-Read):** Books or manuscripts formally copyrighted by academic/commercial publishers (e.g., Springer, Stanford NLP, Chapman & Hall/CRC) where the authors host the current HTML/PDF edition free of charge on their official `.edu` or primary project domain. Assign by direct URL link rather than repackaging into local LMS storage.
3. **Tier 3 (Acceptable with Caveats — Publisher-Authorized Free Web Editions):** Commercial engineering texts (e.g., Google/Abseil web edition of *Software Engineering at Google*) where a complete, legal free-to-read web edition is officially maintained.

<hr>

## 🗂️ Module-Aligned Readings (Modules 0–13)

| Module | Topic | Theoretical “Why” (with License & Origin) | Practical “How” & Supplementary Systems References (with Origin) |
| :---: | :--- | :--- | :--- |
| **0** | Orientation; reproducibility; computational notebooks; research-data workflow | **1. “The FAIR Guiding Principles for Scientific Data Management and Stewardship” — Mark D. Wilkinson et al.** (*Scientific Data*, 2016). Establishes why datasets, metadata, notebooks, and project handoffs must be findable, accessible, interoperable, and reusable. [Read online](https://www.nature.com/articles/sdata201618)<br>*License:* Tier 1 — Open-access article.<br>*Origin:* New Discovery (Replaced due to age).<br><br>**2. “Introduction” & “A Workflow for Reproducible Data Analysis,” _Reproducible Data Science with Python_ — Valentin Danchev.** [Read online](https://valdanchev.github.io/reproducible-data-science-python/intro.html)<br>*License:* Tier 1 — Fully Open Access author-hosted open textbook.<br>*Origin:* Second Search (Theory Focus). | **1. Jupyter Notebook Documentation — Project Jupyter.** Operational model for executable notebooks, kernels, structure, and interactive computational analysis. [Read online](https://jupyter-notebook.readthedocs.io/)<br>*Origin:* Original Search (API Focus). |
| **1** | Python programming technique; project structure; experiment design | **_Python Data Science Handbook_ — Jake VanderPlas** (selected chapters on NumPy, pandas, visualization, and machine learning). Maintained, author-hosted online edition. [Read online](https://jakevdp.github.io/PythonDataScienceHandbook/)<br>*License:* Tier 1 — CC BY-NC-ND text; MIT-licensed code/notebooks.<br>*Origin:* Original Search (API Focus). | **1. Chs. 1–2, _Research Software Engineering with Python_ — Damien Irving, Kate Hertweck, Greg Wilson, et al.** ("The Basics of Organizing Research Software", testing, CLI design, and version control). [Read online](https://third-bit.com/py-rse/)<br>*License:* Tier 1 — CC BY 4.0 text; MIT code.<br>*Origin:* Second Search (Theory Focus).<br><br>**2. _Python for Data Analysis, 3rd ed.: Getting Started with pandas_ — Wes McKinney.** [Read online](https://wesmckinney.com/book/pandas-basics)<br>*Origin:* Original Search (API Focus). |
| **2** | DevContainers; CPU/GPU portability; data-science environments; self-hostable platform & quota layer | **Chs. 1–2, _Research Software Engineering_ — Catherine R. Brett et al.** Frames software environments, containers, automation, and reproducibility as controls on experimental validity. [Read online](https://rse-book.github.io/)<br>*License:* Tier 1 — CC BY-NC-SA 4.0 free-to-read online edition.<br>*Origin:* Second Search (Theory Focus). | **1. Docker “Get Started” — Docker Documentation.** Images, containers, Dockerfiles, volumes, and Compose. [Read online](https://docs.docker.com/get-started/)<br>*Origin:* Original Search (API Focus).<br><br>**2. GPU Overlay & Container Runtime References:** [Official `pytorch/pytorch` Docker Hub](https://hub.docker.com/r/pytorch/pytorch) & [NVIDIA Container Toolkit Install Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).<br><br>**3. Course AI Quota Gateway & Self-Hosted VDB/ASR References:** [LiteLLM Proxy Virtual Keys](https://docs.litellm.ai/docs/proxy/virtual_keys) & [Users/Teams Budgets](https://docs.litellm.ai/docs/proxy/users); [Bifrost AI Gateway](https://docs.getbifrost.ai/overview); [Milvus Quickstart](https://milvus.io/docs/quickstart.md); [OpenAI Whisper](https://github.com/openai/whisper). |
| **3 `[O]`** | Obtain: ASR stream capture, audio/corpus acquisition, speech transcription, provenance | **Ch. 16, “Automatic Speech Recognition and Spoken Language Understanding,” _Speech and Language Processing_, 3rd-ed. draft (Aug 19, 2026) — Dan Jurafsky & James H. Martin.** Modern neural encoder-decoder ASR, decoding, and evaluation. [Read online](https://web.stanford.edu/~jurafsky/slp3/)<br>*License:* Tier 2 — Copyrighted author manuscript hosted on Stanford domain; classroom use expressly permitted.<br>*Origin:* New Discovery (Replaced due to age). | **1. OpenAI Whisper — Repository and README.** Local installation, `ffmpeg` dependency, model sizes (`base.en`, `small.en`, `turbo`), and VRAM/speed trade-offs. [Read online](https://github.com/openai/whisper)<br>*Origin:* Original Search (API Focus).<br><br>**2. Supplementary Obtain Libraries:** [Meta AI FAISS Repository](https://github.com/facebookresearch/faiss) (in-process vector search) & [UFAL Whisper-Streaming](https://github.com/ufal/whisper_streaming) (real-time long-form ASR).<br>*Origin:* Original Search (API Focus). |
| **4** | Data engineering; event streams; windows; state; watermarks; fault-tolerant streaming | **“The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing” — Tyler Akidau et al.** (*VLDB*, 2015). Theoretical basis for event time vs. processing time, watermarks, windows, triggers, and late-data semantics. [Read PDF](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf)<br>*License:* Tier 1 — Official open-access VLDB paper.<br>*Origin:* Second Search (Theory Focus). | **1. Structured Streaming Programming Guide, Spark 3.5.7 — Apache Spark.** Normative reference aligned with **PySpark 3.5 LTS** (`SparkSession.readStream()`, watermarks, output modes, checkpointing, and fault tolerance). [Read online](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html)<br>*Origin:* New Discovery (Replaced due to age).<br><br>**2. Apache Spark Structured Streaming Overview.** [Read online](https://spark.apache.org/docs/latest/streaming/index.html)<br>*Origin:* Original Search (API Focus). |
| **5 `[S]`** | Scrub: chunking; embedding generation; VDB schema design; dense-vector retrieval | **Ch. 11, “Information Retrieval and Retrieval-Augmented Generation,” _Speech and Language Processing_, 3rd-ed. draft (Aug 19, 2026) — Dan Jurafsky & James H. Martin.** Replaces the 2008 Manning et al. IR text to cover modern dense retrieval, bi-encoders, vector indexing, and RAG directly. [Read chapter PDF](https://web.stanford.edu/~jurafsky/slp3/11.pdf)<br>*License:* Tier 2 — Copyrighted current author manuscript hosted by Stanford.<br>*Origin:* New Discovery (Replaced due to age). | **1. Sentence Transformers “Semantic Search” Documentation.** Query/document embeddings, symmetric vs. asymmetric search, bi-encoder retrieval with cross-encoder re-ranking, and ANN indexing. [Read online](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)<br>*Origin:* Original Search (API Focus).<br><br>**2. Vector Index & Schema References:** [Meta AI FAISS](https://github.com/facebookresearch/faiss) (mandatory course baseline) & [Milvus Quickstart](https://milvus.io/docs/quickstart.md) (optional CIS 731 service-based VDB upgrade).<br>*Origin:* Original Search (API Focus). |
| **6** | GenAI & LLMs: text representation; few-shot trope/genre classification; model selection | **Chs. 6–8 & Ch. 10, _Speech and Language Processing_, 3rd-ed. draft (Aug 19, 2026) — Dan Jurafsky & James H. Martin.** Covers neural networks ([Ch. 6 PDF](https://web.stanford.edu/~jurafsky/slp3/6.pdf)), transformers, post-training/SFT/preference alignment/RLVR ([Ch. 8 PDF](https://web.stanford.edu/~jurafsky/slp3/8.pdf)), and Large Language Models / in-context learning (Ch. 10). [Read online](https://web.stanford.edu/~jurafsky/slp3/)<br>*License:* Tier 2 — Copyrighted current author manuscript hosted by Stanford.<br>*Origin:* New Discovery (Replaced due to age). | **1. Hugging Face Transformers “Text Classification” Task Guide.** Tokenization, sequence-classification heads, `Trainer` workflow, and metric evaluation. [Read online](https://huggingface.co/docs/transformers/en/tasks/sequence_classification)<br>*Origin:* Original Search (API Focus).<br><br>**2. scikit-learn “Working With Text Data” Tutorial.** Baseline bag-of-words/TF-IDF pipelines and grid search. [Read online](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)<br>*Origin:* Original Search (API Focus). |
| **7 `[E]`** | Explore: high-dimensional embedding geometry; UMAP/t-SNE; generational drift dashboards | **Chs. 19–20 & Parts I–II, _Fundamentals of Data Visualization_ — Claus O. Wilke.** Dimensionality reduction, visualizing high-dimensional data and uncertainty, color scales, and avoiding misleading encodings. [Read online](https://clauswilke.com/dataviz/)<br>*License:* Tier 1 — CC BY-NC-ND 4.0 complete author-hosted manuscript.<br>*Origin:* Second Search (Theory Focus). | **1. UMAP-learn “Basic UMAP Parameters.”** Effects of `n_neighbors`, `min_dist`, `n_components`, and `metric` on local vs. global embedding structure. [Read online](https://umap-learn.readthedocs.io/en/latest/parameters.html)<br>*Origin:* Original Search (API Focus).<br><br>**2. scikit-learn “Manifold Learning and t-SNE” User Guide.** [Read online](https://scikit-learn.org/stable/modules/manifold.html)<br>*Origin:* Original Search (API Focus). |
| **8 `[M]`** | Model: retrieval-augmented classification; feature extraction pipelines; generational convolutions | **“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” — Patrick Lewis et al.** (*NeurIPS*, 2020). Combines parametric model memory with non-parametric FAISS retrieval; directly motivates retrieval-conditioned classification. [Read online/PDF](https://arxiv.org/abs/2005.11401)<br>*License:* Tier 1 — Open-access arXiv preprint.<br>*Origin:* Second Search (Theory Focus). | **1. scikit-learn “Sample Pipeline for Text Feature Extraction and Evaluation.”** Composable preprocessing/classifier `Pipeline` design, TF-IDF weighting, and cross-validated hyperparameter tuning without data leakage. [Read online](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)<br>*Origin:* Original Search (API Focus). |
| **9** | Evaluate: inferential statistics; retrieval P@k & Recall@k; ASR WER; gold-standard design | **Chs. 1, 5, & 12, _An Introduction to Statistical Learning: with Applications in Python_ (ISLP, 2023) — Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, & Jonathan Taylor.** Resampling, cross-validation, and the bootstrap for confidence intervals and significance testing. [ISLP Python Resources](https://www.statlearning.com/resources-python) · [Python Errata](https://www.statlearning.com/errata-python-edition)<br>*License:* Tier 2 — Copyright Springer; legally free-to-read/download from official author site.<br>*Origin:* New Discovery (Replaced due to age). | **1. NIST _OpenASR 2020 Challenge Evaluation Plan_.** Normative protocol for reference-transcript normalization, alignment, and Word Error Rate ($\text{WER} = (S+D+I)/N$). [Read PDF](https://www.nist.gov/document/openasr20-challenge-evaluation-plan)<br>*Origin:* Original Search (API Focus).<br><br>**2. scikit-learn “Precision-Recall” Guide.** [Read online](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)<br>*Origin:* Original Search (API Focus). |
| **10 `[N]`** | Interpret: applying models to streams; calibration; multiple testing; cohort drift limits | **Chs. 1–2, 4, 5, & 13, _An Introduction to Statistical Learning: with Applications in Python_ (ISLP, 2023) — James et al.** Prediction vs. inference, classification metrics, resampling uncertainty, and multiple hypothesis testing (Bonferroni and Benjamini–Hochberg FDR control). [Official Python Resources](https://www.statlearning.com/resources-python)<br>*License:* Tier 2 — Copyright Springer; sanctioned free official author-site distribution.<br>*Origin:* New Discovery (Replaced due to age). | **1. scikit-learn “Metrics and Scoring: Quantifying the Quality of Predictions.”** Averaging strategies (`macro`, `micro`, `weighted`), custom scorers, and probability calibration. [Read online](https://scikit-learn.org/stable/modules/model_evaluation.html)<br>*Origin:* Original Search (API Focus).<br><br>**2. Sentence Transformers “Semantic Search”** (nearest-neighbor error & threshold analysis). [Read online](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)<br>*Origin:* Original Search (API Focus). |
| **11** | Present: ethics, data storytelling, dashboards, and reproducible technical reporting | **Chs. 1–3, _Technical Writing Essentials_ — Suzan Last.** Audience analysis, document design, evidence-based technical arguments, and integrating visuals with prose. [Read online](https://pressbooks.bccampus.ca/technicalwriting/)<br>*License:* Tier 1 — CC BY 4.0 open textbook.<br>*Origin:* Second Search (Theory Focus). | **1. Jupyter Notebook Documentation — Project Jupyter.** Structuring narrative and code cells, clean restart-and-run-all execution, and HTML/PDF export. [Read online](https://jupyter-notebook.readthedocs.io/)<br>*Origin:* Original Search (API Focus).<br><br>**2. Wilkinson et al., “The FAIR Guiding Principles”** (provenance, licensing, and limitations panels). [Read online](https://www.nature.com/articles/sdata201618)<br>*Origin:* Original Search (API Focus). |
| **12** | PaaS/IaaS; MLOps/AIOps; model lifecycle; experiment lineage; deployment & drift monitoring | **“MLOps Principles” — ML-Ops.org.** Living architectural reference covering versioning of data/models/code/environments, continuous delivery, reproducibility, and drift monitoring. [Read online](https://ml-ops.org/content/mlops-principles)<br>*License:* Tier 2 — Public free-to-read project reference (assign by link; do not repackage).<br>*Origin:* New Discovery (Replaced due to age). | **1. MLflow Tracking Documentation — MLflow.** Logging parameters, metrics, artifacts, Git SHAs, and model registry versions. [Read online](https://mlflow.org/docs/latest/ml/tracking/)<br>*Origin:* Original Search (API Focus).<br><br>**2. FastAPI “FastAPI in Containers — Docker.”** Containerizing real-time retrieval/classification microservices. [Read online](https://fastapi.tiangolo.com/deployment/docker/)<br>*Origin:* Original Search (API Focus). |
| **13** | Term project wrap-up; agentic AI systems; testing; continuous integration; artifact delivery | **Chs. 11–12 (“Testing Overview” & “Unit Testing”) and “Continuous Integration,” _Software Engineering at Google_ — Titus Winters, Tom Manshreck, & Hyrum Wright.** Engineering theory of test-size taxonomy, deterministic verification (`make verify`), and maintainable software evolution. [Read online](https://abseil.io/resources/swe-book/html/toc.html)<br>*License:* Tier 2/3 — Free official online edition hosted by Google/Abseil (link-only).<br>*Origin:* Second Search (Theory Focus). | **1. Docker “Get Started” — Docker Documentation.** Packaging final reproducible project deliverables and digest-pinned container execution. [Read online](https://docs.docker.com/get-started/)<br>*Origin:* Original Search (API Focus).<br><br>**2. scikit-learn “Examples: Working With Text Documents.”** Reproducible baseline gallery. [Read online](https://scikit-learn.org/stable/auto_examples/index.html)<br>*Origin:* Original Search (API Focus). |

<hr>

## 🚫 Stale-Edition Suppression Ledger (Audit Record)

To prevent API/concept mismatches between older free textbooks and the Fall 2026 software stack (**Python 3.11+**, **PySpark 3.5 LTS**, **PyTorch 2.x**, **FAISS**, **Hugging Face Transformers**, **MLflow**), the following legacy editions are suppressed:

| Suppressed Reading | Reason for Suppression | Adopted Replacement |
| :--- | :--- | :--- |
| **_Introduction to Information Retrieval_ — Manning, Raghavan, & Schütze (2008)** | Although legally hosted on Stanford NLP's site, the 2008 text predates dense vector retrieval, neural bi-encoders, FAISS/Milvus vector databases, and RAG pipelines. | **Jurafsky & Martin, _SLP3_ (Aug 19, 2026 draft), Ch. 11 (“Information Retrieval and RAG”)** + Sentence Transformers documentation + *ISLP* (2023). |
| **_An Introduction to Statistical Learning with Applications in R_ (ISLR, 2013 / 2021)** | R-centric labs and syntax create friction in a Python/PySpark/PyTorch curriculum. | **_An Introduction to Statistical Learning: with Applications in Python_ (ISLP, 2023)** with maintained Python labs and errata. |
| **Unpinned Spark “latest” Guides or Legacy Spark 2.x Streaming Tutorials** | Unpinned `"latest"` URLs can drift to Spark 4.x, while 2.x tutorials reference deprecated DStream APIs rather than Structured Streaming DataFrames. | **Apache Spark 3.5.7 Structured Streaming Programming Guide** explicitly pinned to the course's PySpark 3.5 LTS baseline. |
| **Pre-2026 Editions of Jurafsky & Martin (_SLP2_ / Early _SLP3_ Snapshots)** | Older snapshots lack coverage of contemporary post-training (SFT, preference alignment, RLVR), modern instruction-tuned LLMs, and dense RAG architectures. | **Jurafsky & Martin, _SLP3_ (August 19, 2026 author manuscript)** on Stanford's primary domain. |

<hr>

## ⚙️ Course Runtime, DevContainer & Quota Gateway Compatibility Manifest

All practical readings above map to a two-tier reproducible container policy (a universal **CPU-pinned DevContainer baseline** required for all grading, plus an optional **digest-pinned `pytorch/pytorch` CUDA overlay** for validated Beocat/Bridges-2 GPU nodes) and a fail-closed **LiteLLM Proxy** virtual-key quota gateway:

```yaml
course_runtime:
  semester: "fall-2026"
  python: "3.11.x (pinned in requirements.lock)"
  pyspark: "3.5.x (LTS)"
  spark_docs_reference: "3.5.7"
  pytorch: "2.2.1 (CPU baseline pinned; GPU overlay pinned by SHA-256 digest)"
  transformers: "4.38.2"
  sentence_transformers: "pinned in requirements.lock (default model: all-MiniLM-L6-v2)"
  openai_whisper: "pinned in requirements.lock (+ system ffmpeg; CPU default: base / base.en; GPU: turbo)"
  mlflow: "2.11.1"
  faiss: "1.8.0 (faiss-cpu baseline; Milvus optional upgrade for CIS 731)"
  container_images:
    cpu_baseline: "Course CPU DevContainer pinned by immutable SHA-256 digest (100% of coursework solvable on CPU)"
    gpu_overlay: "pytorch/pytorch:<validated-torch>-cuda<validated-cuda>-cudnn<validated-cudnn>-devel@sha256:<digest>"
  quota_gateway:
    engine: "LiteLLM Proxy + PostgreSQL + Redis (fail_closed_budget_enforcement: true)"
    fallback: "Automatic fallback to local CPU Whisper / CPU baseline inference on team quota exhaustion"
```

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>
