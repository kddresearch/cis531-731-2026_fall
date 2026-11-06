<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
phase_metadata:
  phase_number: 3
  phase_identifier: "scrub_and_embed"
  color_scheme: "Orange"
  hex_code: "#d64309"
  badge_pill: "🟠"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 🟠 Phase 3: Scrub & Embed

**Status:** ACTIVE | **Maintainer:** Course Maintainers / KDD Lab

---

## 📖 Overview

This directory defines **Phase 3** of the course progression. For the complete canonical specification, detailed lecture objectives, and the unified chronological reading schedule, see [Phase 3 Specification (`phase_03.md`)](./phase_03.md).

Phases act as high-level chronological and thematic wrappers that group multiple weekly modules together based on major pedagogical milestones (e.g., OSEMN framework transitions). This phase specifically focuses on data scrubbing, chunking, dense vector embeddings, VDB schema design, and GenAI few-shot classification pipelines.

> **⚠️ Phase Routing Notice**
> This directory acts primarily as an organizational wrapper. Ensure that granular lecture assets, code snippets, and weekly materials are placed within their respective `module_XX/` subdirectories, rather than loosely at the root of the phase directory.

---

## 🗂️ Phase Structure (Included Modules)

| Module Directory | Topic / Description | Lectures | Date Range | [Assigned Reading(s)](../../reading_materials/readings_by_lecture.md) |
| :--- | :--- | :--- | :--- | :--- |
| [`module_05/`](../../modules/module_05/) | **[Module 05: Scrub: Chunking, Embedding Generation & VDB Schema Design](../../modules/module_05/module_05.md):** Recursive character chunking, boundary problem mitigation, vector space models, Sentence Transformers, and FAISS/Milvus vector database schema design. | Lectures 14–16 | Mon 28 Sep - Fri 02 Oct 2026 | [Assigned Reading(s)](../../reading_materials/readings_by_lecture.md) |
| [`module_06/`](../../modules/module_06/) | **[Module 06: GenAI & LLMs: Candidates, Code, Classification](../../modules/module_06/module_06.md):** Neural language modeling, transformer architecture, prompt engineering, few-shot trope/genre classification, and Hugging Face pipeline integration *(Note: Wildcat Pause Day Fri 09 Oct)*. | Lectures 17–21 | Mon 05 Oct - Fri 16 Oct 2026 | [Assigned Reading(s)](../../reading_materials/readings_by_lecture.md) |

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this phase directory must adhere to the following protocols:

* **Protocol 1 (Phase Cohesion):** Ensure all modules contained within this phase cleanly map to the overarching phase objective defined in the syllabus taxonomy.
* **Protocol 2 (Navigation):** Maintain cross-links in the module READMEs pointing back to this Phase root to preserve GitOps navigability.
* **Protocol 3 (Milestone Anchoring):** Ensure the terminal module of this phase explicitly prepares the student for the associated major assignment/milestone.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
