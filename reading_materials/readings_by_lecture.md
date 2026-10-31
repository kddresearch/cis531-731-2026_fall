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
 <h3>Document: readings_by_lecture.md (Chronological Schedule)</h3>
 <p>
 <strong>Status:</strong> ACTIVE | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This document provides the strict chronological breakdown of assigned readings by lecture date across all 43 lectures of **CIS 531/731 (Fall 2026)**. It is designed to be used alongside the [Module-Aligned Readings Index](./README.md), which categorizes these same texts by their Theoretical ("Why") and Practical ("How") contributions, open-access licensing tiers, and runtime version constraints.

All texts listed below are freely accessible online without requiring a proprietary institutional login or publisher subscription.

<hr>

## 📅 Assigned Readings by Lecture

| Week | Date | Lecture # | Topic | Assigned Reading (Open-Access / Free-to-Read) |
| :---: | :--- | :---: | :--- | :--- |
| 1 | Mon 24 Aug 2026 | 0 | Module 0 – Welcome, Track Selection Briefing & Course Overview | [Wilkinson et al., *The FAIR Guiding Principles*](https://www.nature.com/articles/sdata201618); [Danchev, *Reproducible Data Science with Python* (Intro & Workflow)](https://valdanchev.github.io/reproducible-data-science-python/intro.html); [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/) |
| 1 | Wed 26 Aug 2026 | 1 | Module 1 – PySpark Intro: RDDs & DataFrames (HW 1 released) | [VanderPlas, *Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/) |
| 1 | Fri 28 Aug 2026 | 2 | Module 1 – Experiment Design & Reproducible Projects | [Irving et al., *Research Software Engineering with Python* (Chs. 1–2)](https://third-bit.com/py-rse/) |
| 2 | Mon 31 Aug 2026 | 3 | Module 1 – RDD Transformations & Actions Lab (`lab01.ipynb`) | [McKinney, *Python for Data Analysis, 3rd ed.: Getting Started with pandas*](https://wesmckinney.com/book/pandas-basics); [VanderPlas, *Python Data Science Handbook* (pandas chapters)](https://jakevdp.github.io/PythonDataScienceHandbook/) |
| 2 | Wed 02 Sep 2026 | 4 | Module 1 – Project Structure, Testing & Module 1 Wrap-Up | [Irving et al., *Research Software Engineering with Python* (Testing & Project Organization)](https://third-bit.com/py-rse/) |
| 2 | Fri 04 Sep 2026 | 5 | Module 2 – Tools: Cloud, HPC & Hosted Services (MP 2 released) | [Brett et al., *Research Software Engineering* (Chs. 1–2: Environments & Reproducibility)](https://rse-book.github.io/) |
| 3 | Mon 07 Sep 2026 | — | **NO CLASS — Labor Day** | — |
| 3 | Wed 09 Sep 2026 | 6 | Module 2 – DevContainers, Docker & Digest Pinning | [Docker Documentation: *Get Started*](https://docs.docker.com/get-started/); [Official `pytorch/pytorch` Docker Hub](https://hub.docker.com/r/pytorch/pytorch); [NVIDIA Container Toolkit Install Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) |
| 3 | Fri 11 Sep 2026 | 7 | Module 2 – AI/LLM Tooling, VDB/ASR Layers & Quota Gateways; Wrap-Up (HW 1 due) | [LiteLLM Proxy: *Virtual Keys*](https://docs.litellm.ai/docs/proxy/virtual_keys) & [*Users/Teams Budgets*](https://docs.litellm.ai/docs/proxy/users); [Milvus *Quickstart*](https://milvus.io/docs/quickstart.md); [OpenAI *Whisper* README](https://github.com/openai/whisper) |
| 4 | Mon 14 Sep 2026 | 8 | Module 3 `[O]` – Obtain: ASR Stream Capture & VDB Corpus Acquisition (MP 3 released) | [Jurafsky & Martin, *Speech and Language Processing* (3rd ed. draft, Aug 19, 2026), Ch. 16: *Automatic Speech Recognition*](https://web.stanford.edu/~jurafsky/slp3/) |
| 4 | Wed 16 Sep 2026 | 9 | Module 3 `[O]` – Whisper Architecture & Local Transcription (`lab03a.ipynb`) | [Radford et al. / OpenAI *Whisper* Repository & Model Card](https://github.com/openai/whisper) |
| 4 | Fri 18 Sep 2026 | 10 | Module 3 `[O]` – Corpus Acquisition & FAISS Indexing Lab (`lab03b.ipynb`); Wrap-Up | [Meta AI Research, *FAISS Documentation & Repository*](https://github.com/facebookresearch/faiss); [UFAL, *Whisper-Streaming Repository*](https://github.com/ufal/whisper_streaming) |
| 5 | Mon 21 Sep 2026 | 11 | Module 4 – Data Analytics Pipelines: Streaming & Data Lakes (MP 2 due Tue 22 Sep) | [Akidau et al., *“The Dataflow Model: Balancing Correctness, Latency, and Cost”* (VLDB 2015 PDF)](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf) |
| 5 | Wed 23 Sep 2026 | 12 | Module 4 – Spark Structured Streaming (PySpark 3.5 LTS) | [Apache Spark 3.5.7 *Structured Streaming Programming Guide*](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html) |
| 5 | Fri 25 Sep 2026 | 13 | Module 4 – Structured Streaming Lab (`lab04.ipynb`); Wrap-Up | [Apache Spark *Structured Streaming Overview*](https://spark.apache.org/docs/latest/streaming/index.html); [Spark 3.5.7 *Watermarking & State Store Guide*](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html) |
| 6 | Mon 28 Sep 2026 | 14 | Module 5 `[S]` – Scrub: Chunking & Embedding Generation (PS 4 Proposal released) | [Jurafsky & Martin, *SLP3* (Aug 19, 2026 draft), Ch. 11: *“Information Retrieval and Retrieval-Augmented Generation”* (PDF)](https://web.stanford.edu/~jurafsky/slp3/11.pdf) |
| 6 | Wed 30 Sep 2026 | 15 | Module 5 `[S]` – Semantic Search & VDB Schema Design | [Sentence Transformers Documentation: *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) |
| 6 | Fri 02 Oct 2026 | 16 | Module 5 `[S]` – Embedding & VDB Indexing Lab; Wrap-Up (MP 3 due Sun 04 Oct) | [Meta AI *FAISS* Index Factory Docs](https://github.com/facebookresearch/faiss); [Milvus *Quickstart* (CIS 731 Schema & Index Guide)](https://milvus.io/docs/quickstart.md) |
| 7 | Mon 05 Oct 2026 | 17 | Module 6 – GenAI & LLMs: Candidates, Code, Classification | [Jurafsky & Martin, *SLP3* (Aug 19, 2026 draft), Ch. 6 (*Neural Networks* PDF)](https://web.stanford.edu/~jurafsky/slp3/6.pdf) & [Ch. 8 (*Post-Training / Alignment* PDF)](https://web.stanford.edu/~jurafsky/slp3/8.pdf) |
| 7 | Wed 07 Oct 2026 | 18 | Module 6 – Few-Shot Trope/Genre Classification (`lab5.ipynb`) | [Hugging Face Transformers Task Guide: *“Text Classification”*](https://huggingface.co/docs/transformers/en/tasks/sequence_classification) |
| 7 | Fri 09 Oct 2026 | — | **NO CLASS — Wildcat Pause Day** *(MP 5 released; PS 4 due Sun 11 Oct)* | — |
| 8 | Mon 12 Oct 2026 | 19 | Module 6 – Model Selection & Embedding-Backed Classification Lab (`lab6.ipynb`) | [scikit-learn Tutorial: *“Working With Text Data”*](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) |
| 8 | Wed 14 Oct 2026 | 20 | Module 6 – Trope/Genre Classification & Prompt Controls Workshop | [Jurafsky & Martin, *SLP3* (Aug 19, 2026 draft), Ch. 10: *“Large Language Models”*](https://web.stanford.edu/~jurafsky/slp3/) |
| 8 | Fri 16 Oct 2026 | 21 | Module 6 – Wrap-Up (PS 6 released; MP 5 due Mon 19 Oct; 5-lecture module absorbs Pause Day) | [Hugging Face Transformers: *Sequence Classification & Evaluation*](https://huggingface.co/docs/transformers/en/tasks/sequence_classification) |
| 9 | Mon 19 Oct 2026 | 22 | Module 7 `[E]` – Explore: Data Visualization & Dashboards | [Wilke, *Fundamentals of Data Visualization* (Chs. 19–20 & Parts I–II)](https://clauswilke.com/dataviz/) |
| 9 | Wed 21 Oct 2026 | 23 | Module 7 `[E]` – Embedding-Space Visualization (UMAP) (MP 7 released) | [UMAP-learn Documentation: *“Basic UMAP Parameters”*](https://umap-learn.readthedocs.io/en/latest/parameters.html) |
| 9 | Fri 23 Oct 2026 | 24 | Module 7 `[E]` – Generational Drift Dashboards Lab (`lab7.ipynb`); Wrap-Up (PS 6 due Sun 25 Oct) | [scikit-learn User Guide: *“Manifold Learning and t-SNE”*](https://scikit-learn.org/stable/modules/manifold.html); [Wilke, *Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/) |
| 10 | Mon 26 Oct 2026 | 25 | Module 8 `[M]` – Modeling: Retrieval-Augmented Classification | [Lewis et al., *“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”* (arXiv:2005.11401)](https://arxiv.org/abs/2005.11401) |
| 10 | Wed 28 Oct 2026 | 26 | Module 8 `[M]` – Feature Extraction Pipelines (PS 8 Interim Report released Thu 29 Oct) | [scikit-learn Example: *“Sample Pipeline for Text Feature Extraction and Evaluation”*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html) |
| 10 | Fri 30 Oct 2026 | 27 | Module 8 `[M]` – Generational Convolution Models Lab (`lab08.ipynb`); Wrap-Up (MP 7 due Tue 03 Nov) | [Lewis et al. (RAG)](https://arxiv.org/abs/2005.11401); [scikit-learn *Pipeline & FeatureUnion Documentation*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html) |
| 11 | Mon 02 Nov 2026 | 28 | Module 9 – Evaluating Models: Inferential Statistics & Bootstrap CIs | [James et al., *An Introduction to Statistical Learning with Applications in Python* (ISLP, 2023), Chs. 1, 5, & 12](https://www.statlearning.com/resources-python) |
| 11 | Wed 04 Nov 2026 | 29 | Module 9 – ASR Evaluation Methodology & Gold-Standard Design | [NIST *OpenASR 2020 Challenge Evaluation Plan* (PDF)](https://www.nist.gov/document/openasr20-challenge-evaluation-plan) |
| 11 | Fri 06 Nov 2026 | 30 | Module 9 – Gold-Standard Construction Lab ($\le 50$-row / 2-hr homework cap); Wrap-Up (PS 8 due Sat 07 Nov; MP 9 released) | [scikit-learn Guide: *“Precision-Recall”*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html); [ISLP *Python-Edition Errata & Labs*](https://www.statlearning.com/errata-python-edition) |
| 12 | Mon 09 Nov 2026 | 31 | Module 10 `[N]` – Interpret: Applying Models, Calibration & Multiple Testing | [James et al., *ISLP* (2023), Chs. 1–2, 4, 5, & 13 (*Resampling & Multiple Testing / Benjamini–Hochberg*)](https://www.statlearning.com/resources-python) |
| 12 | Wed 11 Nov 2026 | 32 | Module 10 `[N]` – Model Metrics, Calibration & Scoring | [scikit-learn Documentation: *“Metrics and Scoring: Quantifying the Quality of Predictions”*](https://scikit-learn.org/stable/modules/model_evaluation.html) |
| 12 | Fri 13 Nov 2026 | 33 | Module 10 `[N]` – Interpretation & Error Analysis Lab; Wrap-Up (MP 9 due Mon 16 Nov; MP 10 released) | [scikit-learn *Metrics & Probability Calibration Guide*](https://scikit-learn.org/stable/modules/model_evaluation.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) |
| 13 | Mon 16 Nov 2026 | 34 | Module 11 – Presenting Results: Ethics & Data Storytelling | [Last, *Technical Writing Essentials* (Chs. 1–3)](https://pressbooks.bccampus.ca/technicalwriting/) |
| 13 | Wed 18 Nov 2026 | 35 | Module 11 – Documentation, Provenance & Notebook Presentation Standards | [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/); [Wilkinson et al., *The FAIR Guiding Principles*](https://www.nature.com/articles/sdata201618) |
| 13 | Fri 20 Nov 2026 | 36 | Module 11 – Dashboard Design & Limitations Panel Workshop; Wrap-Up (MP 10 due Wed 25 Nov; PS 11 released) | [Wilke, *Fundamentals of Data Visualization* (Parts I–II)](https://clauswilke.com/dataviz/); [Last, *Technical Writing Essentials*](https://pressbooks.bccampus.ca/technicalwriting/) |
| 14 | Mon 23 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| 14 | Wed 25 Nov 2026 | — | **NO CLASS — Fall Break** *(MP 10 due; PS 11 released)* | — |
| 14 | Fri 27 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| 15 | Mon 30 Nov 2026 | 37 | Module 12 – PaaS/IaaS, MLOps/AIOps & Drift Monitoring | [ML-Ops.org, *“MLOps Principles”*](https://ml-ops.org/content/mlops-principles) |
| 15 | Wed 02 Dec 2026 | 38 | Module 12 – MLflow Tracking, Lineage & Model Registry | [MLflow Documentation: *MLflow Tracking*](https://mlflow.org/docs/latest/ml/tracking/) |
| 15 | Fri 04 Dec 2026 | 39 | Module 12 – Service Containerization & Wrap-Up (PS 11 due today; HW 12 released Sat 05 Dec) | [FastAPI Documentation: *“FastAPI in Containers — Docker”*](https://fastapi.tiangolo.com/deployment/docker/); [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/) |
| 16 | Mon 07 Dec 2026 | 40 | Module 13 – Special Topics: Agentic AI Systems & Testing *(Extra-Credit Presentations begin after lecture)* | [Winters, Manshreck, & Wright, *Software Engineering at Google* (Chs. 11–12: *Testing Overview* & *Unit Testing*, plus *CI*)](https://abseil.io/resources/swe-book/html/toc.html); [Docker *Get Started*](https://docs.docker.com/get-started/) |
| 16 | Wed 09 Dec 2026 | 41 | Module 13 – Special Topics: Frontier Directions in Responsive Analytics | [LiteLLM Proxy Governance Docs](https://docs.litellm.ai/docs/proxy/virtual_keys); [Bifrost AI Gateway Overview](https://docs.getbifrost.ai/overview); [scikit-learn *Text Examples Gallery*](https://scikit-learn.org/stable/auto_examples/index.html) |
| 16 | Fri 11 Dec 2026 | 42 | Module 13 – Special Topics: Course Synthesis & Wrap-Up (Last day of classes; HW 12 due Mon 14 Dec) | [Winters et al., *Software Engineering at Google*](https://abseil.io/resources/swe-book/html/toc.html); [ML-Ops.org, *“MLOps Principles”*](https://ml-ops.org/content/mlops-principles) |

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>
