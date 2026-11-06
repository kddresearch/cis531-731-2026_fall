<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
phase_metadata:
  phase_number: 1
  phase_identifier: "foundations_and_tooling"
  color_scheme: "Blue"
  hex_code: "#0056b3"
  badge_pill: "🔵"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 🔵 Phase 1: Foundations & Tooling

**Status:** ACTIVE | **Maintainer:** Course Maintainers / KDD Lab

---

## 📖 Overview

This directory defines **Phase 1** of the course progression. For the complete canonical specification, detailed lecture objectives, and unified assigned readings partition, see [Phase 1 Specification (`phase_01.md`)](./phase_01.md).

Phases act as high-level chronological and thematic wrappers that group multiple weekly modules together based on major pedagogical milestones (e.g., OSEMN framework transitions). This phase specifically focuses on course orientation, PySpark foundations (RDDs & DataFrames), experiment design, containerization (Docker/DevContainers), and the AI/LLM tooling baseline.

> **⚠️ Phase Routing Notice**
> This directory acts primarily as an organizational wrapper. Ensure that granular lecture assets, code snippets, and weekly materials are placed within their respective `module_XX/` subdirectories, rather than loosely at the root of the phase directory.

---

## 🗂️ Phase Structure (Included Modules)

| Module Directory | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| [`module_00/`](../../modules/module_00/) | **[Module 00: Welcome & Course Overview](../../modules/module_00/module_00.md):** Course orientation, FAIR guiding principles, reproducible workflows, and Jupyter setup. | Lecture 00 | Mon 24 Aug 2026 | Wilkinson et al., *FAIR Principles*; Danchev, *Reproducible Data Science* |
| [`module_01/`](../../modules/module_01/) | **[Module 01: PySpark Intro](../../modules/module_01/module_01.md):** RDDs, DataFrames, transformations, actions, experiment design, and RSE practices. | Lectures 01–04 | Wed 26 Aug - Wed 02 Sep 2026 | VanderPlas, *Python Data Science Handbook*; Irving et al., *RSE Python* |
| [`module_02/`](../../modules/module_02/) | **[Module 02: Tools](../../modules/module_02/module_02.md):** Cloud & hosted services, DevContainers, Docker, and AI/LLM tooling baseline *(Note: Labor Day Break Mon 07 Sep)*. | Lectures 05–07 | Fri 04 Sep - Fri 11 Sep 2026 | Brett et al., *RSE Guide*; Docker Docs; LiteLLM & Milvus Docs |

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this phase directory must adhere to the following protocols:

* **Protocol 1 (Phase Cohesion):** Ensure all modules contained within this phase cleanly map to the overarching phase objective defined in the syllabus taxonomy.
* **Protocol 2 (Navigation):** Maintain cross-links in the module READMEs pointing back to this Phase root to preserve GitOps navigability.
* **Protocol 3 (Milestone Anchoring):** Ensure the terminal module of this phase explicitly prepares the student for the associated major assignment/milestone.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
