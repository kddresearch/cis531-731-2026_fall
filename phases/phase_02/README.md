<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
phase_metadata:
  phase_number: 2
  phase_identifier: "obtain_and_ingest"
  color_scheme: "Green"
  hex_code: "#1b5e20"
  badge_pill: "🟢"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 🟢 Phase 2: Obtain & Ingest

**Status:** ACTIVE | **Maintainer:** Course Maintainers / KDD Lab

---

## 📖 Overview

This directory defines **Phase 2** of the course progression. For the complete canonical specification, detailed lecture objectives, and unified assigned readings partition, see [Phase 2 Specification (`phase_02.md`)](./phase_02.md).

Phases act as high-level chronological and thematic wrappers that group multiple weekly modules together based on major pedagogical milestones (e.g., OSEMN framework transitions). This phase specifically focuses on ASR stream capture, VDB corpus acquisition, and Structured Streaming ingest architecture.

> **⚠️ Phase Routing Notice**
> This directory acts primarily as an organizational wrapper. Ensure that granular lecture assets, code snippets, and weekly materials are placed within their respective `module_XX/` subdirectories, rather than loosely at the root of the phase directory.

---

## 🗂️ Phase Structure (Included Modules)

| Module Directory | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| [`module_03/`](../../modules/module_03/) | **[Module 03: Obtain: ASR Stream Capture & VDB Corpus Acquisition](../../modules/module_03/module_03.md):** ASR stream capture, VDB corpus acquisition, and OpenAI Whisper local transcription architecture. | Lectures 8–10 | Mon 14 Sep - Fri 18 Sep 2026[cite: 3] | Jurafsky & Martin, *SLP3* Ch. 16[cite: 3]; OpenAI Whisper[cite: 3]; FAISS & Whisper-Streaming[cite: 3] |
| [`module_04/`](../../modules/module_04/) | **[Module 04: Data Analytics Pipelines](../../modules/module_04/module_04.md):** Structured Streaming, data lake models, and ASR ingest architecture. | Lectures 11–13 | Mon 21 Sep - Fri 25 Sep 2026[cite: 1] | Akidau et al., *The Dataflow Model*[cite: 1]; Apache Spark Structured Streaming Guide[cite: 1] |

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this phase directory must adhere to the following protocols:

* **Protocol 1 (Phase Cohesion):** Ensure all modules contained within this phase cleanly map to the overarching phase objective defined in the syllabus taxonomy.
* **Protocol 2 (Navigation):** Maintain cross-links in the module READMEs pointing back to this Phase root to preserve GitOps navigability.
* **Protocol 3 (Milestone Anchoring):** Ensure the terminal module of this phase explicitly prepares the student for the associated major assignment/milestone.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
