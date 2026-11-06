<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-11-05"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
template_metadata:
  template_id: "directory_README_academic_template"
  target_filename: "README.md"
  description: "Generic clean GFM directory README template for phase, module, and structural hubs."
hydration_instructions:
  - step_1: "Replace {{COURSE_NUMBER}}, {{COURSE_TITLE}}, {{SEMESTER}}, {{INSTRUCTOR_NAME}}, and {{CANVAS_COURSE_ID}} with active course parameters."
  - step_2: "Configure phase_metadata block (or omit if non-phase directory): set phase_number, phase_identifier, color_scheme, hex_code, and badge_pill."
  - step_3: "Set directory_type to one of ['phase', 'module', 'root', 'support']."
  - step_4: "Replace all {{SECTION_*}} and {{TABLE_*}} placeholders with specific directory context, cross-links, and module/lecture matrices."
  - step_5: "Ensure relative links follow GitOps hierarchy rules (e.g., ../../modules/module_XX/)."
phase_metadata:
  phase_number: "{{PHASE_NUMBER}}"
  phase_identifier: "{{PHASE_IDENTIFIER}}"
  color_scheme: "{{COLOR_SCHEME_NAME}}"           # e.g., Blue, Green, Orange, Purple, Brown
  hex_code: "{{COLOR_HEX_CODE}}"                 # e.g., #0056b3, #1b5e20, #d64309, #4b2e83, #856404
  badge_pill: "{{COLOR_BADGE_PILL}}"             # e.g., 🔵, 🟢, 🟠, 🟣, 🟤
---
-->

**🏫 Active Course Repositories:** 🏗️ [Architecture Base](https://github.com/kddresearch/course-architecture-base) &nbsp;|&nbsp; 🤖 CIS 530/730 &nbsp;|&nbsp; 📊 [CIS 531/731](https://github.com/kddresearch/cis531-731-2026_fall) &nbsp;|&nbsp; 📈 CIS 732 &nbsp;|&nbsp; 🎨 [CIS 536/736](https://github.com/kddresearch/cis536-736-2026_fall) &nbsp;|&nbsp; 👁️ CIS 798 X &nbsp;|&nbsp; 🧠 CIS 830

# 📊 {{COURSE_NUMBER}} - {{COURSE_TITLE}}

**Semester:** {{SEMESTER}} | **Instructor:** {{INSTRUCTOR_NAME}}  
**Status:** ACTIVE | **Canvas LMS:** [Closed SSO Portal](https://k-state.instructure.com/courses/{{CANVAS_COURSE_ID}})

---

## {{COLOR_BADGE_PILL}} {{DIRECTORY_TITLE}}

**Status:** ACTIVE | **Maintainer:** {{MAINTAINER_NAME}}

---

## 📖 Overview

{{DIRECTORY_OVERVIEW_PARAGRAPH}}

> **⚠️ Phase Routing Notice**  
> {{DIRECTORY_ROUTING_NOTICE}}

---

## 🗂️ Directory Structure / Included Assets

| Directory / File | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| [`{{ITEM_01_PATH}}`]({{ITEM_01_LINK}}) | **[{{ITEM_01_TITLE}}]({{ITEM_01_SPEC_LINK}}):** {{ITEM_01_SUMMARY}} | {{ITEM_01_LECTURES}} | {{ITEM_01_DATES}} | [{{ITEM_01_READING_LABEL}}]({{ITEM_01_READING_LINK}}) |
| [`{{ITEM_02_PATH}}`]({{ITEM_02_LINK}}) | **[{{ITEM_02_TITLE}}]({{ITEM_02_SPEC_LINK}}):** {{ITEM_02_SUMMARY}} | {{ITEM_02_LECTURES}} | {{ITEM_02_DATES}} | [{{ITEM_02_READING_LABEL}}]({{ITEM_02_READING_LINK}}) |

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this directory must adhere to the following protocols:

* **Protocol 1 (Scope & Cohesion):** {{PROTOCOL_1_TEXT}}
* **Protocol 2 (GitOps Navigation):** {{PROTOCOL_2_TEXT}}
* **Protocol 3 (Milestone Anchoring):** {{PROTOCOL_3_TEXT}}

---

*Maintained by the [Knowledge Discovery in Databases (KDD) Lab](https://github.com/kddresearch) at Kansas State University.*
