<!--
yaml_schema_version: "2.2"
document_version: "1.2"
document_last_updated_date: "2026-10-02"
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
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu, Ph.D.<br>
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
| `.github/` | CI/CD workflows and sync configurations (e.g., `sync_architecture_template.yml`). |
| `admin/` | Course policies and syllabus resources. |
| `assignments/` | Problem sets (PSs), machine problems (MPs), project milestones, and labs. |
| `exams_quizzes/` | Quizzes, exams, and other assessments  **that are *taken*, not submitted***. |
| `lectures/` | Core lecture materials and related assets. |
| `modules/` | Weekly/topic-based module directories (`module_00` to `module_13`). |
| `phases/` | High-level course progression phase wrappers (`phase_01` to `phase_05`). |
| `platforms/` | Platform-specific configurations and assets (Canvas, Gemini, Piazza). |
| `reading_materials/` | Assigned papers, texts, and supplementary reading. |
| `slides/` | Slide decks and archived presentations. |
| `term_project/` | Rubrics, sprint specs, and `docker` compute configs for the term project. |
| `README.md` | This file. |

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
| **Instructor** | William H. Hsu | [@banazir](https://www.google.com/search?q=https://github.com/banazir) |
| **Head TA** | [TBD] | [@GITHUB_HANDLE] |
