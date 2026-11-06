<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 5
  module_identifier: "scrub_chunking_embedding_generation_vdb_schema"
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

## 📦 Module 05: Scrub: Chunking, Embedding Generation & VDB Schema Design

**Parent Phase:** 🟠 [Phase 3: Scrub & Embed](../../phases/phase_03/README.md) (`#d64309`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!WARNING]
> **Phase 3 Color Palette: Orange Token (`#d64309`)**  
> **Module Scope:** Data Scrubbing, Document Chunking, Embedding Generation, Semantic Search, and Vector Database Schema Design[cite: 14, 15].

---

## 📖 Overview

This directory defines **Module 05**. For the complete canonical specification, detailed lecture objectives, and localized reading sections, see [Module 05 Specification (`module_05.md`)](./module_05.md#lecture-14-scrub--chunking--embedding-generation).

This module spans 3 lectures (Lectures 14–16; Mon 28 Sep - Fri 02 Oct 2026)[cite: 14, 15] and establishes document chunking, dense vector embeddings, semantic search, and VDB indexing workflows.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content[cite: 15].

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_05.md` | **[Module 05 Canonical Specification](./module_05.md#lecture-14-scrub--chunking--embedding-generation):** Text chunking, embedding generation, vector space models, and VDB schema design[cite: 14]. | Lectures 14–16[cite: 14, 15] | Mon 28 Sep - Fri 02 Oct 2026[cite: 14, 15] | [Module 05 Readings](./module_05.md#lecture-14-scrub--chunking--embedding-generation) |
| `lab5.ipynb` | Lab 5: Chunking, embedding generation, and vector indexing lab notebook[cite: 15] | — | — | — |
| `README.md` | This module overview and index[cite: 15]. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 14: Scrub — Chunking & Embedding Generation](../../lectures/lecture-14.md)[cite: 14, 15] | [Lecture 15: Semantic Search & VDB Schema Design](../../lectures/lecture-15.md)[cite: 14, 15] | [Lecture 16: Embedding Lab & VDB Indexing](../../lectures/lecture-16.md)[cite: 14, 15]
* **Active Assignments:** [Lab 5 Notebook](../../assignments/homework/lab5.ipynb)[cite: 15] | [PS6 Semantic Search & VDB Schema](../../assignments/homework/ps6_semantic_search_vdb_schema.md) *(HW4 due prior day)*[cite: 15]
* **Assigned Readings (Anchored in Module Spec):**
  * [Lecture 14 Readings (Jurafsky & Martin, *SLP3* Ch. 11)](./module_05.md#lecture-14-scrub--chunking--embedding-generation)[cite: 14]
  * [Lecture 15 Readings (Sentence Transformers Semantic Search)](./module_05.md#lecture-15-semantic-search--vdb-schema-design)[cite: 14]
  * [Lecture 16 Readings (Meta AI FAISS & Milvus Quickstart)](./module_05.md#lecture-16-embedding-lab--vdb-indexing)[cite: 14]

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University[cite: 15].*
