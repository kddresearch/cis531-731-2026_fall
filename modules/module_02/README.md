<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
module_metadata:
  module_number: 2
  module_identifier: "tools_cloud_devcontainers_ai_llms"
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

## 📦 Module 02: Tools: Cloud, DevContainers & AI/LLMs

**Parent Phase:** 🔵 [Phase 1: Foundations & Tooling](../../phases/phase_01/README.md) (`#0056b3`) | **Maintainer:** Course Maintainers / KDD Lab

---

> [!NOTE]
> **Phase 1 Color Palette: Blue Token (`#0056b3`)**  
> **Module Scope:** Cloud & Hosted Services, DevContainers, Docker Containerization, and AI/LLM Tooling Baselines.  
> *(Note: Labor Day Break Mon 07 Sep)*

---

## 📖 Overview

This directory defines **Module 02**. For the complete canonical specification, detailed lecture objectives, and the unified chronological reading schedule, see [Module 02 Specification (`module_02.md`)](./module_02.md) and [Assigned Reading(s)](../../reading_materials/readings_by_lecture.md).

This module spans 3 lectures (Lectures 05–07; Fri 04 Sep - Fri 11 Sep 2026) and establishes containerized reproducible environments and AI Gateway/Vector DB baselines.

> **⚠️ Module Routing Notice**  
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

---

## 🗂️ Module Structure & Artifacts

| Subdirectory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| `module_02.md` | **[Module 02 Canonical Specification](./module_02.md):** Cloud tools, DevContainers, Docker, and AI/LLM tooling baselines. | Lectures 05–07 | Fri 04 Sep - Fri 11 Sep 2026 | [Assigned Reading(s)](../../reading_materials/readings_by_lecture.md) |
| `README.md` | This module overview and index. | — | — | — |

---

## 🔗 Associated Course Materials

* **Lectures:** [Lecture 05: Data Scrubbing & Early Exploration](../../lectures/lecture-05.md) | [Lecture 06: DevContainers & Docker](../../lectures/lecture-06.md) | [Lecture 07: AI/LLM Tooling Overview](../../lectures/lecture-07.md)
* **Active Assignments:** HW 1 (Due Fri 11 Sep 2026) | MP 2 (Released Fri 04 Sep 2026)
* **Assigned Readings (Inherited from Phase 1 & Detailed in Specification):**
  * [Brett et al., *Research Software Engineering* (Chs. 1–2: Environments & Reproducibility)](https://rse-book.github.io/)
  * [Docker Documentation: *Get Started*](https://docs.docker.com/get-started/)
  * [Official `pytorch/pytorch` Docker Hub](https://hub.docker.com/r/pytorch/pytorch) & [NVIDIA Container Toolkit Install Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
  * [LiteLLM Proxy: *Virtual Keys*](https://docs.litellm.ai/docs/proxy/virtual_keys) & [*Users/Teams Budgets*](https://docs.litellm.ai/docs/proxy/users)
  * [Milvus *Quickstart*](https://milvus.io/docs/quickstart.md) & [OpenAI *Whisper* README](https://github.com/openai/whisper)
  * *See full chronological schedule in [readings_by_lecture.md](../../reading_materials/readings_by_lecture.md).*

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
