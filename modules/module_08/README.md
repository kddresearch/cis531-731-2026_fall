<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-08"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 8
  module_identifier: "model_retrieval_augmented_classification"
  parent_phase:
    phase_number: 4
    phase_identifier: "explore_and_model"
    color_scheme: "Purple"
    hex_code: "#800080"
    badge_pill: "🟣"
  module_color_tokens:
    tint_class: "[!IMPORTANT]"
    shade_hex: "#660066"
    light_tint_hex: "#f3e6f3"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 📦 Module 08: Model: Retrieval-Augmented Classification

**Parent Phase:** 🟣 [Phase 4: Explore & Model](../../phases/phase_04/README.md) (`#800080`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!IMPORTANT]
> **Phase 4 Color Palette: Purple Token (`#800080`)**  
> **Module Scope:** Retrieval-Augmented Generation (RAG) architectures, feature extraction pipelines, scikit-learn `Pipeline` and `FeatureUnion` mechanics, and generative convolution models lab (`lab08.ipynb`).

---

## 📖 Overview

This directory defines **Module 08**. For the complete canonical specification, detailed lecture objectives, and localized reading sections, see [Module 08 Specification (`module_08.md`)](./module_08.md#lecture-25-model-retrieval-augmented-classification-mon-26-oct).

This module spans 3 lectures (Lectures 25–27; Mon 26 Oct - Fri 30 Oct 2026) and establishes retrieval-augmented classification pipelines, text feature extraction combinations, and generational convolution modeling.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_08.md` | **[Module 08 Canonical Specification](./module_08.md#lecture-25-model-retrieval-augmented-classification-mon-26-oct):** RAG architectures, feature extraction pipelines, and feature union modeling. | Lectures 25–27 | Mon 26 Oct - Fri 30 Oct 2026 | [Module 08 Readings](./module_08.md#lecture-25-model-retrieval-augmented-classification-mon-26-oct) |
| `lab08.ipynb` | Lab 8: Generational convolution models and feature extraction lab notebook | — | — | — |
| `README.md` | This module overview and index. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 25: Retrieval-Augmented Classification](../../lectures/lecture_25.md) | [Lecture 26: Feature Extraction Pipelines](../../lectures/lecture_26.md) | [Lecture 27: Generational Convolution Models Lab; Wrap-Up](../../lectures/lecture_27.md)
* **Active Assignments:** [Lab 8 Notebook](../../assignments/homework/lab08.ipynb) | [MP7 Exploratory Dashboards Specification](../../assignments/machine_problems/mp7_exploratory_dashboards.md) *(PS8 Interim Report released, MP7 due)*
* **Assigned Readings (Anchored in Module Spec):**
  * [Lecture 25 Readings (Lewis et al., *Retrieval-Augmented Generation* arXiv:2005.11401)](./module_08.md#lecture-25-model-retrieval-augmented-classification-mon-26-oct)
  * [Lecture 26 Readings (scikit-learn Pipeline & Grid Search Example)](./module_08.md#lecture-26-feature-extraction-pipelines-wed-28-oct)
  * [Lecture 27 Readings (Lewis et al. & scikit-learn Pipeline & FeatureUnion Docs)](./module_08.md#lecture-27-generational-convolution-models-lab-wrap-up-fri-30-oct)

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*