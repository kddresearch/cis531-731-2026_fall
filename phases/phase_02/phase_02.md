<!--
  Template Note: This file serves as the canonical instantiation for phase_02/README.md.
  Generic Templatized Link Formats (Relative GFM):
   - Module directory/file link: `../../modules/module_03/` or `../../modules/module_03/module_03.md`
   - Lecture markdown link: `../../lectures/lecture_08.md`
   - Sibling phase link: `../../phases/phase_01/`
  
  Note: The assigned readings for Phase 2 are the exact union of readings from Module 03 and Module 04.
-->

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Description | Modules | Date Range | [Assigned Reading(s)](../../reading_materials/readings_by_lecture.md) |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 2:** Obtain & Ingest | ASR stream capture, Whisper local transcription architecture, vector database corpus acquisition, data analytics pipelines, and Spark Structured Streaming. | [`Module 03`](../../modules/module_03/) - [`Module 04`](../../modules/module_04/) | Mon 14 Sep - Fri 25 Sep 2026 | [Jurafsky & Martin, *SLP3* Ch. 16](https://web.stanford.edu/~jurafsky/slp3/); [OpenAI Whisper](https://github.com/openai/whisper); [FAISS & Whisper-Streaming](https://github.com/facebookresearch/faiss); [Akidau et al., *The Dataflow Model*](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf); [Apache Spark Structured Streaming Guide](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html) |

---

## 📖 Phase Overview & Objectives

* **Core Pedagogical Theme:** Transitioning from raw environment setup and tooling into high-throughput data acquisition (Obtain) and distributed streaming architectures (Ingest) within the OSEMN framework.
* **Included Modules:** 
  * [`Module 03`](../../modules/module_03/): Obtain: ASR Stream Capture & VDB Corpus Acquisition (Lectures 08–10)
  * [`Module 04`](../../modules/module_04/): Data Analytics Pipelines: Streaming & Data Lakes (Lectures 11–13)
* **Phase Deliverables / Milestones:** Machine Problem 3 (`MP 3`), Machine Problem 2 due (`MP 2`), and Homework 4 (`HW 4`).

---

## 🗂️ Phase Structure (Included Modules)

| Module Directory | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| [`module_03/`](../../modules/module_03/) | **Obtain: ASR Stream Capture & VDB Corpus Acquisition:** Continuous socket capture, FFmpeg subprocesses, OpenAI Whisper ASR architecture, local VRAM/FP16 optimization, and FAISS vector indexing. | Lectures 08–10 | Mon 14 Sep - Fri 18 Sep 2026 | [Jurafsky & Martin, *SLP3* Ch. 16](https://web.stanford.edu/~jurafsky/slp3/); [OpenAI Whisper](https://github.com/openai/whisper); [Meta AI FAISS & Whisper-Streaming](https://github.com/facebookresearch/faiss) |
| [`module_04/`](../../modules/module_04/) | **Data Analytics Pipelines: Streaming & Data Lakes:** Akidau dataflow model, Spark Structured Streaming (PySpark 3.5 LTS), micro-batch triggers, state management, watermarking, and data lake sink integration. | Lectures 11–13 | Mon 21 Sep - Fri 25 Sep 2026 | [Akidau et al., *The Dataflow Model*](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf); [Apache Spark Structured Streaming Guide](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html) |
