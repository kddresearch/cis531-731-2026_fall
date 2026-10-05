# CIS 531/731 Term Project: Data Sourcing & Task Execution Guide

To ensure your team can successfully execute the OSEMN pipeline (Obtain, Scrub, Explore, Model, iNterpret) without getting trapped by broken APIs or hidden paywalls, you must select your data sources carefully.

Your project proposal (PS 4) will be evaluated on the **feasibility of your Obtain and Scrub phases**. Below is the KDD Lab tier list for data sourcing.

## 🟢 TIER 1: The "Golden Path" (Highly Recommended)
*These sources are natively integrated or highly accessible, allowing you to focus your energy on Spark analytics, embeddings, and Machine Learning rather than fighting broken web scrapers.*

*   **Databricks Native Samples (`samples.wanderbricks` or `samples.tpcds_sf1`):** 
    *   *Best for:* Structured/Relational projects (Recommender Systems, Association Rule Mining, Customer Segmentation).
    *   *How to Obtain:* Native Unity Catalog queries in your Databricks workspace.
*   **Hugging Face Datasets (`wikimedia/wikipedia` or `librispeech_asr`):**
    *   *Best for:* Text Corpora (RAG, LLM Classification) and Audio (Whisper ASR pipelines).
    *   *How to Obtain:* Use the `datasets` library to pull the raw data, then write directly to a local Parquet/Delta table for Spark processing.

## 🟡 TIER 2: Real-World APIs (Challenging but Valuable)
*These sources require you to handle pagination, rate-limiting, and complex JSON schemas. Recommended for teams with strong Python/API experience.*

*   **Public REST APIs (NOAA Climate Data, Open-Meteo, USGS Earthquake Feed):**
    *   *Best for:* Time-Series forecasting, Anomaly Detection, and Spatial density mapping.
    *   *How to Obtain:* Write a Python request script to poll the API, dump the raw JSON payloads into a Bronze storage folder, and use Spark `Auto Loader` or batch reads to ingest them.
*   **Kaggle Competitions (e.g., IEEE-CIS Fraud Detection):**
    *   *Best for:* Predictive structured data and classification.
    *   *How to Obtain:* Requires managing a `kaggle.json` API token securely within your DevContainer to automate the download.

## 🔴 TIER 3: The Tarpits (Not Recommended)
*Unless you have specific domain expertise (e.g., you are a GIS or Audio Engineering researcher), avoid these sources. They will consume all your project time in the "Scrub" phase.*

*   **Raw Satellite Imagery (STAC APIs, Sentinel-2):** Cloud masking and distributed raster tiling in PySpark are extremely difficult.
*   **Raw Audio Feature Extraction (MFCCs from scratch):** Parallelizing heavy audio libraries across Spark worker nodes often results in memory crashes. Stick to pre-extracted datasets or the specific Whisper pipeline taught in Module 3.

---

### 🛠️ Execution Strategy: "Automating the Boring Stuff"
Your team is not required to write every OSEMN stage from scratch. 
*   **Focus your labor:** Claim the 1-2 stages that align with your learning goals (e.g., "I want to master Spark Streaming (Obtain)" or "I want to master XGBoost (Model)").
*   **Automate the rest:** Use existing scripts, Hugging Face loaders, or simple Pandas macros to push the data through the stages you didn't claim, allowing your team to integrate smoothly via Delta tables or Parquet files.
