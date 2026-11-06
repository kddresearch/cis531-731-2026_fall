<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 3
  module_identifier: "obtain_asr_stream_capture_vdb_corpus_acquisition"
  parent_phase:
    phase_number: 2
    phase_identifier: "obtain_and_ingest"
    color_scheme: "Green"
    hex_code: "#1b5e20"
    badge_pill: "🟢"
  module_color_tokens:
    tint_class: "[!TIP]"
    shade_hex: "#0e3812"
    light_tint_hex: "#e8f5e9"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 📦 Module 03: Obtain: ASR Stream Capture & VDB Corpus Acquisition

**Parent Phase:** 🟢 [Phase 2: Obtain & Ingest](../../phases/phase_02/README.md) (`#1b5e20`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!TIP]
> **Phase 2 Color Palette: Green Token (`#1b5e20`)**  
> **Module Scope:** ASR Stream Capture, VDB Corpus Acquisition, OpenAI Whisper Local Transcription Architecture, and Corpus Acquisition Labs.

---

## 📖 Overview

This directory defines **Module 03**. For the complete canonical specification, detailed lecture objectives, and localized reading sections, see [Module 03 Specification (`module_03.md`)](./module_03.md#lecture-08-obtain-asr-stream-capture--vdb-corpus-acquisition).

This module spans 3 lectures (Lectures 08–10; Mon 14 Sep - Fri 18 Sep 2026) and establishes automatic speech recognition stream capture, vector database corpus acquisition, and local Whisper transcription workflows.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_03.md` | **[Module 03 Canonical Specification](./module_03.md#lecture-08-obtain-asr-stream-capture--vdb-corpus-acquisition):** ASR stream capture, Whisper transcription, and FAISS indexing. | Lectures 08–10 | Mon 14 Sep - Fri 18 Sep 2026 | [Module 03 Readings](./module_03.md#lecture-08-obtain-asr-stream-capture--vdb-corpus-acquisition) |
| `lab03a.ipynb` | Lab 3a: ASR stream capture and corpus ingestion | — | — | — |
| `lab03b.ipynb` | Lab 3b: Local Whisper transcription pipeline | — | — | — |
| `README.md` | This module overview and index. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 08: Obtain: ASR Stream Capture & VDB Corpus Acquisition](../../lectures/lecture-08.md) | [Lecture 09: Whisper Architecture & Local Transcription](../../lectures/lecture-09.md) | [Lecture 10: Corpus Acquisition Lab & Wrap-Up](../../lectures/lecture-10.md)
* **Active Assignments:** [Lab 03a Notebook](../../assignments/homework/lab03a.ipynb) | [Lab 03b Notebook](../../assignments/homework/lab03b.ipynb) | MP 3 (Released)
* **Assigned Readings (Anchored in Module Spec):**
  * [Lecture 08 Readings (Jurafsky & Martin, *SLP3* Ch. 16)](./module_03.md#lecture-08-obtain-asr-stream-capture--vdb-corpus-acquisition)
  * [Lecture 09 Readings (Radford et al. / OpenAI Whisper Model Card)](./module_03.md#lecture-09-whisper-architecture--local-transcription)
  * [Lecture 10 Readings (Meta AI FAISS & Whisper-Streaming Repositories)](./module_03.md#lecture-10-corpus-acquisition-lab--wrap-up)

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
