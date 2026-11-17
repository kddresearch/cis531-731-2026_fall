<!--
yaml_schema_version: "2.2"
document_version: "3.4"
document_last_updated_date: "2026-11-16"
-->

<br>

<div align="center">
 <strong>🏫 Active Course Repositories:</strong> &nbsp;
 🏗️ <a href="https://github.com/kddresearch/course-architecture-base">Architecture Base</a> &nbsp;|&nbsp;
 🤖 CIS 530/730 &nbsp;|&nbsp;
 📊 <a href="https://github.com/kddresearch/cis531-731-2026_fall">CIS 531/731</a> &nbsp;|&nbsp;
 📈 CIS 732 &nbsp;|&nbsp;
 🎨 <a href="https://github.com/kddresearch/cis536-736-2026_fall">CIS 536/736</a> &nbsp;|&nbsp;
 👁️ CIS 798 X &nbsp;|&nbsp;
 🧠 CIS 830
</div>

<div align="center">
 <h1>📊 CIS 531/731 - Programming Techniques for Data Science and Analytics</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu<br>
 <strong>Status:</strong> ACTIVE | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Closed SSO Portal</a>
 </p>
</div>

<hr>

## 📖 Overview

Central repository for CIS 531/731 (Fall 2026) academic execution. This repository manages the DevContainer environments, Machine Problems (MPs), and primary codebase for students learning modern data science programming techniques. 

> **⚠️ Single Source of Truth (SSOT) Notice**
> This repository is the designated SSOT for all public-facing course materials, assignments, and infrastructure. While grades and closed discussions occur in the Canvas SSO environment, all operational state, Machine Problems (MPs), codebases, and structural rubrics MUST be committed here before being mirrored. A non-paywalled HTML mirror of Canvas content is derived from this repository.

<hr>

## 🗂️ Repository Structure

| Directory / File | Description |
| :--- | :--- |
| [`.github/`](.github/) | CI/CD workflows and sync configurations (e.g., `sync_architecture_template.yml`). |
| [`admin/`](admin/) | Course policies and syllabus resources. |
| [`assignments/`](assignments/) | Problem sets (PSs), machine problems (MPs), project milestones, and labs. |
| [`docs/`](docs/) | Supplemental documentation including architecture references, setup instructions, and implementation guides. |
| [`exams_quizzes/`](exams_quizzes/) | Quizzes, exams, and other assessments **that are *taken*, not submitted* **. |
| [`lectures/`](lectures/) | Core lecture materials and related assets. |
| [`modules/`](modules/) | Weekly/topic-based module directories (`module_00` to `module_13`). |
| [`phases/`](phases/) | High-level course progression phase wrappers (`phase_01` to `phase_05`). |
| [`platforms/`](platforms/) | Platform-specific configurations and assets (Canvas, Gemini, Piazza). |
| [`reading_materials/`](reading_materials/) | Assigned papers, texts, and supplementary reading. |
| [`slides/`](slides/) | Slide decks and archived presentations. |
| [`templates/`](templates/) | HTML and Markdown templates for Canvas and other learning management systems. |
| [`term_project/`](term_project/) | Rubrics, sprint specs, and `docker` compute configs for the term project. |
| [`README.md`](README.md) | This file. |

<hr>

## 🚀 Quick Start & Execution

**1. Prerequisites**
* Git client
* Docker Desktop & VS Code (for DevContainer deployment)

**2. Initialization**
```bash
git clone [https://github.com/kddresearch/cis531-731-2026_fall.git](https://github.com/kddresearch/cis531-731-2026_fall.git)
cd cis531-731-2026_fall
# Open in VS Code to initialize the DevContainer
```

## 🦅 Lab Execution Protocols

All Teaching Assistants and GRAs operating in this repository fall under the KDD Lab **Keep Flying Directive v2.1**.

* **Observable State:** Progress is measured by commits, drafts, logs, and reproducible outputs—not intentions.
* **The Triad:** When opening an issue or Pull Request, provide explicit goals, current blockers, and proposed next actions.
* **Artifact-Gated Routing:** Do not request synchronous meetings for routine status updates. Push your grading state or syllabus updates to this repository first.

## 👥 Instructional Staff

| Role | Name | GitHub Handle |
| --- | --- | --- |
| **Instructor** | William H. Hsu | [@banazir](https://github.com/banazir) |
| **Teaching Asssistant** | Joshua Garcia | |

## 📂 Repository Structure (Full Tree)

<details>
<summary><b>Click to expand: Course Repository Template Directory Tree</b></summary>

```
Folder PATH listing for volume Windows
Volume serial number is 60E2-4FEF
C:.
|   propagation_log.txt
|   README.md
|   structure_dump.txt
|   
+---.github
|       .gitkeep
|       
+---admin
|   |   .gitkeep
|   |   
|   +---policies
|   |   |   .gitkeep
|   |   |   generative_ai_kit.html
|   |   |   generative_ai_kit.md
|   |   |   generative_ai_kit_howto.md
|   |   |   generative_ai_kit_howto_v2.md
|   |   |   generative_ai_kit_v2.md
|   |   |   generative_ai_kit_v3.html
|   |   |   generative_ai_kit_v3.md
|   |   |   office_hours_scheduling.md
|   |   |   ps4_self_service_feedback_guide.md
|   |   |   README.md
|   |   |   term_project_invariants.md
|   |   |   
|   |   \---prompts
|   |           claude_critical_review_coordinator.md
|   |           perplexity_instructor_trope_ontology_sourcing.md
|   |           perplexity_project_lifecycle_coordinator.md
|   |           perplexity_systems_engineering_auditor.md
|   |           
|   \---syllabus
|           .gitkeep
|           01_course_syllabus.html
|           01_course_syllabus.md
|           02_course_schedule.html
|           02_course_schedule.md
|           03_environment_runbook.html
|           03_environment_runbook.md
|           04_term_project_guidelines.html
|           04_term_project_guidelines.md
|           05_term_project_taxonomy.html
|           05_term_project_taxonomy.md
|           06_term_project_sourcing_guide.html
|           06_term_project_sourcing_guide.md
|           07_term_project_evaluation.html
|           07_term_project_evaluation.md
|           08_term_project_grading_rubric.html
|           08_term_project_grading_rubric.md
|           README.md
|           
+---assignments
|   |   assignment_template.md
|   |   README.md
|   |   
|   +---homework
|   |       hw12_final_deliverables.html
|   |       hw12_final_deliverables.md
|   |       hw1_devcontainer_bringup_architecture.html
|   |       hw1_devcontainer_bringup_architecture.md
|   |       hw1_grading_rubric.md
|   |       hw1_model_solution.html
|   |       hw1_model_solution.ipynb
|   |       lab01.ipynb
|   |       lab02.ipynb
|   |       lab03a.ipynb
|   |       lab03b.ipynb
|   |       lab04.ipynb
|   |       lab08.ipynb
|   |       lab10.ipynb
|   |       lab11.ipynb
|   |       lab5.ipynb
|   |       lab6.ipynb
|   |       lab7.ipynb
|   |       ps11_ethics_storytelling_dashboards.html
|   |       ps11_ethics_storytelling_dashboards.md
|   |       ps4_grading_rubric.md
|   |       ps4_proposal.html
|   |       ps4_proposal.md
|   |       ps6_grading_rubric.md
|   |       ps6_semantic_search_vdb_schema.html
|   |       ps6_semantic_search_vdb_schema.md
|   |       ps8_grading_rubric.html
|   |       ps8_grading_rubric.md
|   |       ps8_interim_report.html
|   |       ps8_interim_report.md
|   |       README.md
|   |       
|   +---machine_problems
|   |       .gitkeep
|   |       mp10_interpretability_metrics.html
|   |       mp10_interpretability_metrics.md
|   |       mp2_devcontainer_deployment_manifest_verification.html
|   |       mp2_devcontainer_deployment_manifest_verification.md
|   |       mp2_grading_rubric.md
|   |       mp3_grading_rubric.md
|   |       mp3_real_time_asr_vector_database_ingestion.html
|   |       mp3_real_time_asr_vector_database_ingestion.md
|   |       mp5_grading_rubric.md
|   |       mp5_structured_streaming.html
|   |       mp5_structured_streaming.md
|   |       mp7_genre_classification.html
|   |       mp7_genre_classification.md
|   |       mp9_rag_classification_gold_standard.html
|   |       mp9_rag_classification_gold_standard.md
|   |       verify_env.py
|   |       
|   \---project_sprints
|           .gitkeep
|           guidelines.md
|           
+---docs
|   |   .gitkeep
|   |   
|   +---architecture
|   |       .gitkeep
|   |       
|   +---guides
|   |       .gitkeep
|   |       databricks_to_docker.md
|   |       evaluate_models.ipynb
|   |       evaluate_models.py
|   |       lab03_poem_list.md
|   |       ps6-walkthrough-ieee_fraud.ipynb
|   |       
|   \---setup
|           .gitkeep
|           hw1_mp2_windows11_wsl2_docker_walkthrough.html
|           hw1_mp2_windows11_wsl2_docker_walkthrough.md
|           
+---exams_quizzes
|       .gitkeep
|       
+---lectures
|       index.html
|       lectture-26.md
|       lecture_00.md
|       lecture_01.md
|       lecture_02.md
|       lecture_03.html
|       lecture_03.md
|       lecture_04.html
|       lecture_04.md
|       lecture_05.md
|       lecture_06.md
|       lecture_07.md
|       lecture_08.md
|       lecture_09.md
|       lecture_10.md
|       lecture_10_slide_template.md
|       lecture_11.md
|       lecture_12.md
|       lecture_13.md
|       lecture_14.md
|       lecture_15.md
|       lecture_16.md
|       lecture_17.md
|       lecture_18.md
|       lecture_19.md
|       lecture_20.md
|       lecture_21.md
|       lecture_22.md
|       lecture_23.md
|       lecture_24.md
|       lecture_25.md
|       lecture_26.md
|       lecture_27.md
|       lecture_28.md
|       lecture_29.md
|       lecture_30.md
|       lecture_31.md
|       lecture_32.md
|       lecture_33.md
|       lecture_34.md
|       lecture_template.md
|       README.md
|       
+---modules
|   |   index.html
|   |   module_template.md
|   |   README.md
|   |   
|   +---module_00
|   |       module_00.md
|   |       README.md
|   |       
|   +---module_01
|   |       module_01.html
|   |       module_01.md
|   |       README.md
|   |       
|   +---module_02
|   |       module_02.html
|   |       module_02.md
|   |       README.md
|   |       
|   +---module_03
|   |       module_03.md
|   |       README.md
|   |       
|   +---module_04
|   |       .gitkeep
|   |       module_04.md
|   |       README.md
|   |       
|   +---module_05
|   |       .gitkeep
|   |       module_05.md
|   |       README.md
|   |       
|   +---module_06
|   |       .gitkeep
|   |       module_06.md
|   |       README.md
|   |       
|   +---module_07
|   |       .gitkeep
|   |       module_07.md
|   |       README.md
|   |       
|   +---module_08
|   |       .gitkeep
|   |       module_08.md
|   |       README.md
|   |       
|   +---module_09
|   |       module_09.md
|   |       README.md
|   |       
|   +---module_10
|   |       .gitkeep
|   |       module_10.md
|   |       
|   +---module_11
|   |       .gitkeep
|   |       module_11.md
|   |       
|   +---module_12
|   |       .gitkeep
|   |       module_12.md
|   |       
|   \---module_13
|           .gitkeep
|           module_13.md
|           
+---phases
|   |   index.html
|   |   phase_template.md
|   |   README.md
|   |   
|   +---phase_01
|   |       index.html
|   |       phase_01.md
|   |       README.md
|   |       
|   +---phase_02
|   |       index.html
|   |       phase_02.md
|   |       README.md
|   |       
|   +---phase_03
|   |       index.html
|   |       phase_03.md
|   |       README.md
|   |       
|   +---phase_04
|   |       index.html
|   |       README.md
|   |       
|   \---phase_05
|           index.html
|           README.md
|           
+---platforms
|   +---canvas
|   |       .gitkeep
|   |       hydration_specification.md
|   |       
|   +---gemini
|   |       .gitkeep
|   |       
|   +---github
|   |       github_intro.md
|   |       
|   +---moodle
|   |       .gitkeep
|   |       
|   \---piazza
|           .gitkeep
|           
+---reading_materials
|       .gitkeep
|       index.html
|       readings_by_lecture.md
|       README.md
|       
+---slides
|   |   .gitkeep
|   |   
|   \---archive
|           .gitkeep
|           
+---templates
|   +---html_layouts
|   |       golden_template.html
|   |       golden_template_universal_assignment_index_page.html
|   |       golden_template_universal_assignment_page.html
|   |       golden_template_universal_lecture_index_page.html
|   |       golden_template_universal_lecture_page.html
|   |       golden_template_universal_module_index_page.html
|   |       golden_template_universal_module_page.html
|   |       golden_template_universal_phase_index_page.html
|   |       golden_template_universal_phase_page.html
|   |       golden_template_universal_syllabus.html
|   |       golden_template_universal_term_project_proposal_page.html
|   |       README.md
|   |       
|   \---repo_structures
|           directory_README_academic_template.md
|           module_README_template.md
|           phase_README_template.md
|           
\---term_project
    |   fixed_docker_manifest_requirement.md
    |   
    +---docker
    |       Dockerfile
    |       
    +---obtain
    |   |   fetch_term_project_corpus.py
    |   |   README.md
    |   |   
    |   \---data
    |       \---raw_corpus
    |           \---texts
    \---rubrics
            ps4_proposal_feedback_rubric.md            
```
</details>
