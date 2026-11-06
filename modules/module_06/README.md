<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 6
  module_identifier: "genai_llms_candidates_code_classification"
  parent_phase:
    phase_number: 3
    phase_identifier: "scrub_and_embed"
    color_scheme: "Orange"
    hex_code: "#d64309"
    badge_pill: "🟠"
  module_color_tokens:
    tint_class: "[!WARNING]"
    shade_hex: "#b33507"
    light_tint_hex: "#fff3cd"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 📦 Module 06: GenAI & LLMs: Candidates, Code, Classification

**Parent Phase:** 🟠 [Phase 3: Scrub & Embed](../../phases/phase_03/README.md) (`#d64309`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!WARNING]
> **Phase 3 Color Palette: Orange Token (`#d64309`)**  
> **Module Scope:** Generative AI & LLMs, Candidate Generation, Model Selection, Few-Shot Trope/Genre Classification, and Embedding-Backed Classification Labs *(Note: Wildcat Pause Day Fri 09 Oct)*.

---

## 📖 Overview

This directory defines **Module 06**. For the complete canonical specification, detailed lecture objectives, and localized reading sections, see [Module 06 Specification (`module_06.md`)](./module_06.md#lecture-17-genai--llms-candidates-code-classification-mon-05-oct).

This module spans 5 lectures (Lectures 17–21; Mon 05 Oct - Fri 16 Oct 2026) and establishes neural language modeling, transformer architectures, few-shot trope/genre classification, and Hugging Face pipeline integration.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_06.md` | **[Module 06 Canonical Specification](./module_06.md#lecture-17-genai--llms-candidates-code-classification-mon-05-oct):** GenAI, LLM candidate generation, few-shot classification, and model selection. | Lectures 17–21 | Mon 05 Oct - Fri 16 Oct 2026 | [Module 06 Readings](./module_06.md#lecture-17-genai--llms-candidates-code-classification-mon-05-oct) |
| `lab6.ipynb` | Lab 6: Model selection and embedding-backed classification lab notebook | — | — | — |
| `README.md` | This module overview and index. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 17: GenAI & LLMs: Candidates, Code, Classification](../../lectures/lecture-17.md) | [Lecture 18: Few-Shot Trope/Genre Classification](../../lectures/lecture-18.md) | [Lecture 19: Model Selection & Embedding-Backed Classification Lab](../../lectures/lecture-19.md) | [Lecture 20: Trope/Genre Classification Workshop](../../lectures/lecture-20.md) | [Lecture 21: Wrap-Up](../../lectures/lecture-21.md)
* **Active Assignments:** [Lab 6 Notebook](../../assignments/homework/lab6.ipynb) | [MP7 Genre Classification Specification](../../assignments/machine_problems/mp7_genre_classification.md) *(MP5 released, MP6 released, MP5 due)*
* **Assigned Readings (Anchored in Module Spec):**
  * [Lecture 17 Readings (Jurafsky & Martin, *SLP3* Chs. 6 & 8)](./module_06.md#lecture-17-genai--llms-candidates-code-classification-mon-05-oct)
  * [Lecture 18 Readings (Hugging Face Transformers Task Guide)](./module_06.md#lecture-18-few-shot-tropegenre-classification-wed-07-oct)
  * [Lecture 19 Readings (scikit-learn Tutorial & Sentence Transformers Semantic Search)](./module_06.md#lecture-19-model-selection--embedding-backed-classification-lab-mon-12-oct)
  * [Lecture 20 Readings (Jurafsky & Martin, *SLP3* Ch. 10)](./module_06.md#lecture-20-tropegenre-classification-workshop-wed-14-oct)
  * [Lecture 21 Readings (Hugging Face Sequence Classification & Evaluation)](./module_06.md#lecture-21-wrap-up-fri-16-oct)

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
