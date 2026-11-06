<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 1
  module_identifier: "pyspark_intro_rdds_dataframes"
  parent_phase:
    phase_number: 1
    phase_identifier: "foundations_and_tooling"
    color_scheme: "Blue"
    hex_code: "#0056b3"
    badge_pill: "🔵"
  module_color_tokens:
    tint_class: "[!NOTE]"
    shade_hex: "#004085"
    light_tint_hex: "#e7f1ff"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 📦 Module 01: PySpark Intro: RDDs & DataFrames

**Parent Phase:** 🔵 [Phase 1: Foundations & Tooling](../../phases/phase_01/README.md) (`#0056b3`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!NOTE]
> **Phase 1 Color Palette: Blue Token (`#0056b3`)**  
> **Module Scope:** PySpark Fundamentals, RDDs & DataFrames, Transformations & Actions, Experiment Design, and RSE Practices.

---

## 📖 Overview

This directory defines **Module 01**. For the complete canonical specification, detailed lecture objectives, and localized reading sections, see [Module 01 Specification (`module_01.md`)](./module_01.md#lecture-01-pyspark-basics--resilient-distributed-datasets-rdds).

This module spans 4 lectures (Lectures 01–04; Wed 26 Aug - Wed 02 Sep 2026) and establishes distributed computing fundamentals, PySpark DataFrames, experiment design, and RSE practices.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_01.md` | **[Module 01 Canonical Specification](./module_01.md#lecture-01-pyspark-basics--resilient-distributed-datasets-rdds):** PySpark intro, RDDs, DataFrames, and experiment design. | Lectures 01–04 | Wed 26 Aug - Wed 02 Sep 2026 | [Module 01 Readings](./module_01.md#lecture-01-pyspark-basics--resilient-distributed-datasets-rdds) |
| `lab01.ipynb` | Lab 1: PySpark RDDs and DataFrames introductory exercises | — | — | — |
| `lab02.ipynb` | Lab 2: Experiment design and reproducible research software engineering | — | — | — |
| `README.md` | This module overview and index. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 01: PySpark Basics & RDDs](../../lectures/lecture_01.md) | [Lecture 02: PySpark DataFrames & Spark SQL](../../lectures/lecture-02.md) | [Lecture 03: RDD Transformations & Actions Lab](../../lectures/lecture-03.md) | [Lecture 04: Lab 1 & Obtain Stage](../../lectures/lecture-04.md)
* **Active Assignments:** [Lab 01 Notebook](../../assignments/homework/lab01.ipynb) | [Lab 02 Notebook](../../assignments/homework/lab02.ipynb)
* **Assigned Readings (Anchored in Module Spec):**
  * [Lecture 01 Readings (VanderPlas, *Python Data Science Handbook*)](./module_01.md#lecture-01-pyspark-basics--resilient-distributed-datasets-rdds)
  * [Lecture 02 Readings (Irving et al., *Research Software Engineering*)](./module_01.md#lecture-02-pyspark-dataframes--spark-sql)
  * [Lecture 03 Readings (McKinney & VanderPlas pandas chapters)](./module_01.md#lecture-03-rdd-transformations--actions-lab--pyspark-4-architecture)
  * [Lecture 04 Readings (Irving et al., *RSE Testing*)](./module_01.md#lecture-04-lab-1--pyspark-4-bring-up--the-obtain-stage)

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
