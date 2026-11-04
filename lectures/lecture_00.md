# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **[Phase 1](../phases/phase_01/):** Foundations & Tooling | **[Module 00](../modules/module_00/):** Welcome & Course Overview | **Lecture 00:** Welcome, Track Selection Briefing & Course Overview | Monday, August 24, 2026 |

---

## Slide 1: Course Orientation & Administrative Overview
### Launching CIS 531/731 Fall 2026
* **Course Context:** Launching Phase 1 and [`Module 00`](../modules/module_00/module_00.md) of the Fall 2026 semester.
* **Core Topic:** Comprehensive course orientation, logistics, and Canvas LMS portal navigation.
* **Governing Policies:** Detailed review of the [`Course Syllabus`](../admin/syllabus/01_course_syllabus.md) and [`Master Course Schedule`](../admin/syllabus/02_course_schedule.md).
* **Instructor Contact:** Office hours, Canvas announcements, and Microsoft Teams collaboration channel.
* **Objective:** Establish clear academic expectations, grading standards, and computational workflows.

**Speaker Notes:**
Welcome to CIS 531/731 (Programming Techniques for Data Science and Analytics) for Fall 2026. Today in Lecture 0, we establish our course orientation, review administrative logistics, and introduce the core architectural philosophy of the semester. Please ensure you are familiar with the [`Course Syllabus`](../admin/syllabus/01_course_syllabus.md) and bookmark our [`Master Course Schedule`](../admin/syllabus/02_course_schedule.md) on Canvas. Everything we do this semester is geared toward practical, scalable data engineering and responsive analytics.

---

## Slide 2: Syllabus Walkthrough & Grading Distribution
### Navigating the 1000-Point Scale and Course Policies
* **Grading Scale:** 1000-point scale partitioned across regular assignments, milestones, term project execution, and exams.
* **Assignment Policy:** 9 regular assignments (HWs and MPs) graded on a 30-point scale, with the **highest 7 of 9 counting** (lowest 2 dropped automatically).
* **Mandatory Milestones:** Three undroppable milestones ([`PS 4 Proposal`](../../assignments/homework/ps4_proposal.md), [`PS 8 Interim Report`](../../assignments/homework/ps8_interim_report.md), and [`HW 12 Final Deliverables`](../../assignments/homework/hw12_final_deliverables.md)).
* **Late Work Policy:** Zero late work allowed without pre-approved OSSA documentation, absorbed by the automatic assignment drops.
* **Detailed Breakdown:** Consult the [`Course Syllabus`](../admin/syllabus/01_course_syllabus.md) for full letter grade thresholds.

**Speaker Notes:**
Let's review our grading structure as detailed in the [`Course Syllabus`](../admin/syllabus/01_course_syllabus.md). Regular assignments are worth 21% of your grade, structured so your two lowest scores are automatically dropped. However, note that the three term project milestones are mandatory and cannot be dropped. We maintain a strict zero late work policy to keep grading consistent across all enrolled sections, relying on the built-in drop policy to accommodate personal or technical hiccups.

---

## Slide 3: The Fall 2026 Responsive Analytics Mandate
### Eliminating Legacy Stale Grinds in Favor of Modern Multimodal Pipelines
* **The Problem:** Traditional sentiment grinds (Yelp reviews, SEC filings) lack modern systems complexity and architectural depth.
* **The Mandate:** Complete prohibition of legacy sentiment datasets across all homeworks, machine problems, and term projects.
* **The Solution:** Transitioning to high-throughput streaming and dense vector retrieval architectures.
* **Alignment:** Governed by the [`Term Project Taxonomy`](../admin/syllabus/05_term_project_taxonomy.md) and [`Term Project Sourcing Guide`](../admin/syllabus/06_term_project_sourcing_guide.md).

**Speaker Notes:**
A major update for Fall 2026 is our Responsive Analytics Mandate, outlined in the [`Course Syllabus`](../admin/syllabus/01_course_syllabus.md). In past years, data science courses relied heavily on stale Yelp review datasets or SEC financial filings. We are strictly prohibiting those legacy grinds this semester. Modern data science requires streaming ingestion, real-time speech transcription, and dense vector database indexing. Every project must adhere to the high standards defined in our [`Term Project Taxonomy`](../admin/syllabus/05_term_project_taxonomy.md).

---

## Slide 4: Immutable Term Project Tracks: ASR vs. VDB Corpora
### Choosing Your Team's Operational Architecture at Proposal Stage
* **Track 1 (ASR Live Stream Ingestion):** Live or simulated radio call-in audio capture, local OpenAI Whisper transcription, and PySpark Structured Streaming windowed aggregation.
* **Track 2 (VDB & Trope Ontologies):** Public-domain and instructor-provided lyric or literary corpus ingestion, structure-aware chunking, and FAISS/Milvus dense vector indexing.
* **Immutability:** Teams commit immutably to their selected track during [`HW 1`](../assignments/homework/hw1_devcontainer_bringup_architecture.md) and [`PS 4`](../../assignments/homework/ps4_proposal.md).
* **Reference Material:** Consult the [`Term Project Sourcing Guide`](../admin/syllabus/06_term_project_sourcing_guide.md) for approved data sources.

**Speaker Notes:**
For your term projects, every team must commit immutably to one of two parallel operational tracks, as specified in [`Module 00`](../modules/module_00/module_00.md). Track 1 focuses on Automatic Speech Recognition (ASR) streaming ingest, dealing with real-time audio buffers and temporal watermarking. Track 2 focuses on Vector Databases (VDB) and literary trope ontologies, processing text corpora into dense vector spaces. You will lock in your track selection starting with [`HW 1`](../assignments/homework/hw1_devcontainer_bringup_architecture.md).

---

## Slide 5: Undergraduate vs. Graduate Differentiation
### Calibrating Expectations Between CIS 531 and CIS 731
* **Shared Foundations:** Both sections share core OSEMN lectures, PySpark notebooks, and the CPU DevContainer baseline.
* **CIS 531 (Undergraduate / Tier 1):** Focuses on core pipeline mastery, standard Golden Path datasets, and unmodified instructor ontologies.
* **CIS 731 (Graduate / Tier 2):** Requires custom ontology derivation (Draft 2020-12 JSON Schemas), self-hosted Milvus schema deployment, and advanced modeling comparisons.
* **Team Composition:** Mixed undergraduate/graduate teams must clearly delineate graduate-level contributions in project milestones.

**Speaker Notes:**
As noted in the [`Course Syllabus`](../admin/syllabus/01_course_syllabus.md), CIS 531 (Undergraduate) and CIS 731 (Graduate) share the same lectures and foundational lab environments. However, graduate students face higher expectations in schema design, ontology derivation, and advanced modeling. For example, CIS 731 students must derive custom Draft 2020-12 JSON schemas and implement advanced vector persistence rather than relying solely on default local FAISS indices.

---

## Slide 6: FAIR Guiding Principles for Scientific Data Management
### Ensuring Findability, Accessibility, Interoperability, and Reusability
* **Findable (F):** Metadata and data identifiers must be globally unique and persistent (Wilkinson et al.).
* **Accessible (A):** Protocols must be open, free, and universally implementable.
* **Interoperable (I):** Data must integrate seamlessly with other applications using standard vocabularies.
* **Reusable (R):** Datasets must be richly described with clear provenance and licensing.
* **Primary Reading:** [Wilkinson et al., *The FAIR Guiding Principles*](https://www.nature.com/articles/sdata201618) (indexed in [`Readings Master Index`](../reading_materials/readings_by_lecture.md)).

**Speaker Notes:**
Data management in this course is governed by Wilkinson et al.'s FAIR Guiding Principles, as assigned in our [`Readings Master Index`](../reading_materials/readings_by_lecture.md). We expect your pipelines to produce findable, accessible, interoperable, and reusable artifacts. In practice, this means strict version control, clean JSON metadata schemas, and reproducible notebook outputs that any peer or automated grader can inspect without friction.

---

## Slide 7: Reproducible Data Science Workflows
### Eliminating Environment Drift and Ad-Hoc Scripting
* **Reproducible Foundations:** Danchev’s framework for version-controlled, modular data science notebooks and scripts.
* **Jupyter Ecosystem:** Best practices for notebook structuring, execution order, and documentation ([`Jupyter Documentation`](https://jupyter-notebook.readthedocs.io/)).
* **Version Control Standards:** Maintaining clean Git repositories and standardized directory layouts across all assignments.
* **Reading Integration:** Review [Danchev, *Reproducible Data Science with Python*](https://valdanchev.github.io/reproducible-data-science-python/intro.html) alongside [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/).

**Speaker Notes:**
Following Danchev’s principles on reproducible data science and our [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/), we enforce strict workflow standards. Ad-hoc scripts and notebooks that fail to run sequentially from top to bottom will lose points on grading. Your project structure must be clean, modular, and fully reproducible across different machines.

---

## Slide 8: Environment Runbook & Containerized Baseline
### The Pinned CPU DevContainer Mandate
* **Containerized Execution:** 100% of coursework runs inside the course's pinned CPU DevContainer (Docker Desktop + VS Code).
* **Hardware Independence:** Dedicated GPUs are never required; all assignments are 100% solvable on the CPU baseline.
* **Environment Verification:** Running [`verify_env.py`](../../assignments/machine_problems/verify_env.py) and verifying the exact SHA-256 digest (`6f0648c69f69b1faeb96cfecaa7e2a904ed9210c8c07e0b5dd13d2f9df25ff75`).
* **Primary Runbook:** Consult the [`Environment Runbook 1.0`](../admin/syllabus/03_environment_runbook.md) and [`HW 1 & MP 2 Setup Walkthrough`](../docs/setup/hw1_mp2_windows11_wsl2_docker_walkthrough.md).

**Speaker Notes:**
To eliminate the "it works on my machine" dilemma, we enforce a strict containerized baseline detailed in the [`Environment Runbook 1.0`](../admin/syllabus/03_environment_runbook.md) and our [`HW 1 & MP 2 Setup Walkthrough`](../docs/setup/hw1_mp2_windows11_wsl2_docker_walkthrough.md). You are required to build our pinned CPU DevContainer. You never need a GPU to succeed in this course; our container environment guarantees exact dependency pinning and reproducible execution.

---

## Slide 9: Master Schedule, Deadlines, and Deliverables Ledger
### Tracking 5 Phases, 43 Lectures, and 12 Assignments
* **Master Ledger:** The complete chronological roadmap is maintained in the [`Master Course Schedule`](../admin/syllabus/02_course_schedule.md).
* **Lead-Time Guarantee:** Every assignment receives at least a 9-calendar-day lead time and a 6-calendar-day gap between due dates.
* **Phase 1 Roadmap:** Spanning [`Module 00`](../modules/module_00/module_00.md) through [`Module 02`](../modules/module_02/module_02.md), covering course orientation, PySpark foundations, DevContainers, and AI tooling.
* **Immediate Action:** Review [`HW 1`](../assignments/homework/hw1_devcontainer_bringup_architecture.md) release details and prepare your environment.

**Speaker Notes:**
Be sure to bookmark the [`Master Course Schedule`](../admin/syllabus/02_course_schedule.md). It outlines all 5 phases, 43 lectures, and 12 deliverables for the semester. We guarantee a minimum 9-day lead time on all assignments so you can plan your research sprints effectively. Phase 1 kicks off right now with [`Module 00`](../modules/module_00/module_00.md) and [`HW 1`](../assignments/homework/hw1_devcontainer_bringup_architecture.md).

---

## Slide 10: Summary, Course Expectations, and HW 1 Preparation
### Setting the Stage for Distributed Spark Computing and Project Initiation
* **Key Takeaway 1:** CIS 531/731 demands rigorous software engineering, reproducible containers, and adherence to the FAIR principles.
* **Key Takeaway 2:** The Fall 2026 Responsive Analytics Mandate requires streaming or vector database tracks—legacy sentiment grinds are prohibited.
* **Key Takeaway 3:** Complete your DevContainer bring-up using the [`Environment Runbook 1.0`](../admin/syllabus/03_environment_runbook.md) and [`HW 1 & MP 2 Setup Walkthrough`](../docs/setup/hw1_mp2_windows11_wsl2_docker_walkthrough.md).
* **Next Steps:** Review [`HW 1: DevContainer Bring-Up & Term Project Architecture`](../assignments/homework/hw1_devcontainer_bringup_architecture.md) and prepare for [Lecture 01: PySpark Basics & Resilient Distributed Datasets (RDDs)](lecture_01.md).

**Speaker Notes:**
That concludes Lecture 0. Today we established our course orientation, reviewed our syllabus policies, introduced the responsive analytics mandate, and set up our container expectations. Your immediate task is to review [`HW 1: DevContainer Bring-Up & Term Project Architecture`](../assignments/homework/hw1_devcontainer_bringup_architecture.md) and verify your Docker DevContainer environment. In our next session, we dive into [Lecture 01](lecture_01.md) and Apache Spark RDD fundamentals. See you in class!
