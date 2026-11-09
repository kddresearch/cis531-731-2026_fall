<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-08"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 7
  module_identifier: "explore_data_visualization_dashboards"
  parent_phase:
    phase_number: 4
    phase_identifier: "explore_and_model"
    color_scheme: "Purple"
    hex_code: "#800080"
    badge_pill: "🟣"
  module_color_tokens:
    tint_class: "[!WARNING]"
    shade_hex: "#660066"
    light_tint_hex: "#f3e6f3"
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 CIS 531/731 - Programming Techniques for Data Science and Analytics

**Semester:** Fall 2026 | **Instructor:** William H. Hsu  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/201513)

---

## 📦 Module 07: Explore: Data Visualization & Dashboards

**Parent Phase:** 🟣 [Phase 4: Explore & Model](../../phases/phase_04/README.md) (`#800080`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!WARNING]
> **Phase 4 Color Palette: Purple Token (`#800080`)**  
> **Module Scope:** Exploratory Data Analysis (EDA) principles, visual encoding constraints, dashboard architecture (Dash/Streamlit), UMAP dimensionality reduction, hyperparameter tuning (`n_neighbors` & `min_dist`), and time-series embedding drift analysis.

---

## 📖 Overview

This directory defines **Module 07**. For the complete canonical specification, detailed lecture objectives, and localized reading sections, see [Module 07 Specification (`module_07.md`)](./module_07.md#lecture-22-explore-data-visualization--dashboards-mon-19-oct).

This module spans 3 lectures (Lectures 22–24; Mon 19 Oct - Fri 23 Oct 2026) and establishes interactive dashboard design, topological dimensionality reduction via UMAP, and generational drift visualization for embeddings.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_07.md` | **[Module 07 Canonical Specification](./module_07.md#lecture-22-explore-data-visualization--dashboards-mon-19-oct):** EDA principles, UMAP projection mechanics, and exploratory dashboard construction. | Lectures 22–24 | Mon 19 Oct - Fri 23 Oct 2026 | [Module 07 Readings](./module_07.md#lecture-22-explore-data-visualization--dashboards-mon-19-oct) |
| `lab7.ipynb` | Lab 7: Generational drift dashboards and UMAP visualization lab notebook | — | — | — |
| `README.md` | This module overview and index. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 22: Explore: Data Visualization & Dashboards](../../lectures/lecture_22.md) | [Lecture 23: Embedding-Space Visualization (UMAP)](../../lectures/lecture_23.md) | [Lecture 24: Generational Drift Dashboards Lab; Wrap-Up](../../lectures/lecture_24.md)
* **Active Assignments:** [Lab 7 Notebook](../../assignments/homework/lab7.ipynb) | [MP7 Exploratory Dashboards Specification](../../assignments/machine_problems/mp7_exploratory_dashboards.md) *(PS6 due)*
* **Assigned Readings (Anchored in Module Spec):**
  * [Lecture 22 Readings (Wilke, *Fundamentals of Data Visualization* Chs. 19–20 & Parts I–II)](./module_07.md#lecture-22-explore-data-visualization--dashboards-mon-19-oct)
  * [Lecture 23 Readings (UMAP-learn Documentation)](./module_07.md#lecture-23-embedding-space-visualization-umap-wed-21-oct)
  * [Lecture 24 Readings (scikit-learn User Guide & Wilke)](./module_07.md#lecture-24-generational-drift-dashboards-lab-wrap-up-fri-23-oct)

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*