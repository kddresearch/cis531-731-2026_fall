<!--
---
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "YYYY-MM-DD"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
template_metadata:
  template_id: "directory_README_academic_template"
  description: "Genericized academic directory README template with cross-platform LMS skinning support"
  target_filename: "README.md"
  platform_compatibility:
    - "github"
    - "canvas"
    - "moodle"
    - "piazza"
  hydration_instructions:
    step_1: "Replace all template parameters marked with double curly braces {{ PARAMETER_NAME }} with target instance metadata."
    step_2: "Configure phase_metadata block attributes (color_scheme, hex_code, badge_pill) to match designated phase design tokens."
    step_3: "Update active course repository list to reflect current course cluster / department offerings."
    step_4: "Ensure relative GFM navigation links map correctly to local subdirectories (e.g., modules/module_XX/)."
  parameters:
    - name: "COURSE_CODE"
      description: "Primary course designation code (e.g., DEPT 101/501)"
      required: true
    - name: "COURSE_TITLE"
      description: "Official title of the course offering"
      required: true
    - name: "COURSE_EMOJI"
      description: "Generic emoji symbol representing the course focus"
      default: "📚"
    - name: "SEMESTER_TERM"
      description: "Term and year of current active instance (e.g., Fall 2026)"
      required: true
    - name: "INSTRUCTOR_NAME"
      description: "Primary instructor or course lead name"
      required: true
    - name: "LMS_NAME"
      description: "Target Learning Management System platform name (e.g., Canvas, Moodle)"
      default: "Course LMS Portal"
    - name: "LMS_PORTAL_URL"
      description: "Direct URL link to LMS course entry portal"
      required: true
    - name: "PHASE_NUMBER"
      description: "Numerical index of current academic phase"
      required: true
    - name: "PHASE_TITLE"
      description: "Descriptive title of phase milestone (e.g., Foundations & Setup)"
      required: true
    - name: "PHASE_SUMMARY"
      description: "Concise summary of phase pedagogical focus"
      required: true
phase_metadata:
  phase_number: {{ PHASE_NUMBER }}
  phase_identifier: "{{ PHASE_IDENTIFIER }}"
  color_scheme: "{{ COLOR_SCHEME }}"
  hex_code: "{{ HEX_CODE }}"
  badge_pill: "{{ BADGE_PILL }}"
---
-->

**🏫 Active Course Cluster / Department Repositories:** 🏗️ [Architecture Base]({{ ARCHITECTURE_BASE_URL }}) &nbsp;|&nbsp; {{ COURSE_EMOJI }} [{{ COURSE_CODE }}]({{ COURSE_REPO_URL }}) &nbsp;|&nbsp; 📖 [Course Sequence A]({{ COURSE_SEQ_A_URL }}) &nbsp;|&nbsp; 🔬 [Course Sequence B]({{ COURSE_SEQ_B_URL }}) &nbsp;|&nbsp; 🎓 [Course Sequence C]({{ COURSE_SEQ_C_URL }})

# {{ COURSE_EMOJI }} {{ COURSE_CODE }} - {{ COURSE_TITLE }}

**Semester:** {{ SEMESTER_TERM }} | **Instructor:** {{ INSTRUCTOR_NAME }}  
**Status:** ACTIVE | **LMS Portal:** [{{ LMS_NAME }}]({{ LMS_PORTAL_URL }})

---

## {{ BADGE_PILL }} Phase {{ PHASE_NUMBER }}: {{ PHASE_TITLE }}

**Status:** ACTIVE | **Maintainer:** {{ MAINTAINER_GROUP }}

---

## 📖 Overview

This directory defines **Phase {{ PHASE_NUMBER }}** of the course progression. For the complete canonical specification, detailed lecture objectives, and unified chronological reading schedule, see [Phase {{ PHASE_NUMBER }} Specification (`phase_{{ PHASE_NUMBER_PADDED }}.md`)](./phase_{{ PHASE_NUMBER_PADDED }}.md) and [Assigned Reading(s)]({{ READINGS_SCHEDULE_PATH }}).

Phases act as high-level chronological and thematic wrappers that group multiple weekly modules together based on major pedagogical milestones (e.g., taxonomy transition points). This phase specifically focuses on {{ PHASE_SUMMARY }}.

> **⚠️ Phase Routing Notice**
> This directory acts primarily as an organizational wrapper. Ensure that granular lecture assets, code snippets, and weekly materials are placed within their respective `module_XX/` subdirectories, rather than loosely at the root of the phase directory.

---

## 🗂️ Phase Structure (Included Modules)

| Module Directory | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| [`module_01/`](../../modules/module_01/) | **[Module 01: {{ MODULE_01_TITLE }}](../../modules/module_01/module_01.md):** {{ MODULE_01_DESCRIPTION }} | Lectures {{ MODULE_01_LECTURES }} | {{ MODULE_01_DATES }} | [Assigned Reading(s)]({{ READINGS_SCHEDULE_PATH }}) |
| [`module_02/`](../../modules/module_02/) | **[Module 02: {{ MODULE_02_TITLE }}](../../modules/module_02/module_02.md):** {{ MODULE_02_DESCRIPTION }} | Lectures {{ MODULE_02_LECTURES }} | {{ MODULE_02_DATES }} | [Assigned Reading(s)]({{ READINGS_SCHEDULE_PATH }}) |

---

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this phase directory must adhere to the following protocols:

* **Protocol 1 (Phase Cohesion):** Ensure all modules contained within this phase cleanly map to the overarching phase objective defined in the syllabus taxonomy.
* **Protocol 2 (Navigation):** Maintain cross-links in the module READMEs pointing back to this Phase root to preserve GitOps navigability across target platforms (GitHub, Canvas, Moodle, Piazza).
* **Protocol 3 (Milestone Anchoring):** Ensure the terminal module of this phase explicitly prepares the student for the associated major assignment/milestone.

---

*Maintained by {{ MAINTAINER_ORGANIZATION }} at {{ INSTITUTION_NAME }}.*
