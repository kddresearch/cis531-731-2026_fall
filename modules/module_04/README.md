<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 4
  module_identifier: "data_analytics_pipelines_structured_streaming"
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

## 📦 Module 04: Data Analytics Pipelines

**Parent Phase:** 🟢 [Phase 2: Obtain & Ingest](../../phases/phase_02/README.md) (`#1b5e20`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!TIP]
> **Phase 2 Color Palette: Green Token (`#1b5e20`)**  
> **Module Scope:** Structured Streaming, Data Lake Models, ASR Ingest Architecture, and Spark Streaming Pipelines.

---

## 📖 Overview

This directory defines **Module 04**. For the complete canonical specification, detailed lecture objectives, and localized reading sections, see [Module 04 Specification (`module_04.md`)](./module_04.md#lecture-11-data-analytics-pipelines-streaming--data-lakes).

This module spans 3 lectures (Lectures 11–13; Mon 21 Sep - Fri 25 Sep 2026) and establishes stream processing foundations, Akidau's dataflow model, and Spark Structured Streaming pipelines.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_04.md` | **[Module 04 Canonical Specification](./module_04.md#lecture-11-data-analytics-pipelines-streaming--data-lakes):** Dataflow models, Structured Streaming, and data lake sinks. | Lectures 11–13 | Mon 21 Sep - Fri 25 Sep 2026 | [Module 04 Readings](./module_04.md#lecture-11-data-analytics-pipelines-streaming--data-lakes) |
| `lab04.ipynb` | Lab 4: Structured streaming and data analytics pipelines | — | — | — |
| `README.md` | This module overview and index. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 11: Data Analytics Pipelines: Streaming & Data Lakes](../../lectures/lecture-11.md) | [Lecture 12: Spark Structured Streaming (PySpark 3.5 LTS)](../../lectures/lecture-12.md) | [Lecture 13: Structured Streaming Lab & Wrap-Up](../../lectures/lecture-13.md)
* **Active Assignments:** [Lab 04 Notebook](../../assignments/homework/lab04.ipynb) | MP 2 (Due Tue 22 Sep 2026)
* **Assigned Readings (Anchored in Module Spec):**
  * [Lecture 11 Readings (Akidau et al., *The Dataflow Model*)](./module_04.md#lecture-11-data-analytics-pipelines-streaming--data-lakes)
  * [Lecture 12 Readings (Apache Spark Structured Streaming Programming Guide)](./module_04.md#lecture-12-spark-structured-streaming-pyspark-35-lts)
  * [Lecture 13 Readings (Spark Structured Streaming Overview & Watermarking Guide)](./module_04.md#lecture-13-structured-streaming-lab--wrap-up)

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
