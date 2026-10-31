---
yaml_schema_version: "2.11"
document_version: "1.0"
document_last_updated_date: "2026-10-31"
document_last_updated_time: "15:40:00 CDT"
document_monotonicity: "REQUIRED - Ensure document_version and timestamps strictly increment on every update of the target document. Reject regressions."
anti_cwa_cardinal_rule: "ALWAYS ASK, NEVER INFER. Do not hallucinate physical world state, task completion, or implicit preferences."
routing_clearance: "GENERAL - COURSE INFRASTRUCTURE & HYDRATION SSOT (CIS 531/731)"
base_architecture_repo: "https://github.com/kddresearch/course-architecture-base"
target_course_repo: "https://github.com/kddresearch/cis531-731-2026_fall"
target_lms_base_url: "https://k-state.instructure.com/courses/201513"
---

# CIS 531/731 (Fall 2026) — Canvas LMS Hydration & Synchronization Specification

**Course:** CIS 531 / CIS 731 — Programming Techniques for Data Science and Analytics (Fall 2026)  
**Base Class Repository:** [`kddresearch/course-architecture-base`](https://github.com/kddresearch/course-architecture-base)  
**Derived Course Repository (Point of Origin):** [`kddresearch/cis531-731-2026_fall`](https://github.com/kddresearch/cis531-731-2026_fall)  
**Target LMS Instance (Point of Delivery):** [`https://k-state.instructure.com/courses/201513`](https://k-state.instructure.com/courses/201513)

---

## 1. Architectural Purpose & The Dual-SSOT Encapsulation Principle

### 1.1 The Point-of-Origin vs. Point-of-Delivery Contract
A foundational source of cognitive friction in university courses is the collision between **version-control engineering** and **student LMS expectations**:
1. **Point of Origin (Instructor / TA / Grader SSOT — GitHub):** The Git repository (`kddresearch/cis531-731-2026_fall`) is the authoritative authoring, versioning, and CI/CD source for all dehydrated Markdown (`.md`) specifications, Jupyter notebooks (`.ipynb`), Docker manifests, and grading rubrics.
2. **Point of Delivery (Student & Institutional SLA SSOT — Canvas LMS):** Students are conditioned by institutional policy and cross-course convention to treat **Instructure Canvas (`courses/201513`)** as the sole binding contract for deadlines, instructions, and navigation. Exposing internal GitOps mechanics—or allowing hydration sync latency to create visible discrepancies between GitHub `.md` files and Canvas HTML pages—is experienced by students as shifting assignment definitions ("the boundary moved over me").

### 1.2 Information Hiding & Encapsulation Rules (Representation Hiding)
Every dehydrated source document (`.md` by default) is compiled ("hydrated") into a target presentation document (`.html` by default) subject to four strict encapsulation rules:
* **Rule E-1 (Strip Authoring Metadata):** All YAML frontmatter blocks, `<!-- ASSIGNMENT-META ... -->` blocks, `REVIEW R-X` maintainer notes, and internal specification keys (`INV-1` through `INV-21`, `deal` decorator names) MUST be stripped during hydration and replaced with self-contained qualitative prose.
* **Rule E-2 (Never Route Navigation to Raw GitHub Markdown):** A hydrated Canvas HTML page MUST NEVER link a navigation button (e.g., *"Modules"*, *"Full Syllabus"*, *"Phase 1"*, *"Readings"*) to a raw `github.com/.../blob/main/.../*.md` file when a corresponding Canvas page or native Canvas endpoint exists.
* **Rule E-3 (Scope GitHub Links Strictly to Code Artifacts):** Links to `github.com/kddresearch/cis531-731-2026_fall` inside Canvas HTML are permitted **only** for downloadable code artifacts (`lab01.ipynb`–`lab08.ipynb`, `verify_env.py`, `Dockerfile`, or `git clone` instructions) or as a discreet footer provenance badge.
* **Rule E-4 (Atomic Publication Gate):** A change committed to a dehydrated `.md` file in GitHub is considered **unreleased** until its corresponding `.html` target is hydrated, passes the Static Link Validator (Section 3), and is pushed to Canvas LMS.

---

## 2. Golden Template Inheritance Hierarchy & Multi-LMS Skinning

All hydrated HTML files inherit from a single abstract visual base class (`golden_template.html`) and its six specialized structural subclasses located in `templates/html_layouts/`:

```text
templates/html_layouts/golden_template.html  [Abstract Base Class: Font, Max-Width, K-State Palette, Callout & Table Primitives]
 ├── 1. golden_template_universal_phase_page.html          --> phases/phase_01..05/index.html
 ├── 2. golden_template_universal_module_page.html         --> modules/module_00..13/index.html
 ├── 3. golden_template_universal_lecture_page.html        --> lectures/lecture-00..42.html
 ├── 4. golden_template_universal_assignment_index_page.html --> assignments/index.html & lectures/index.html
 ├── 5. golden_template_universal_assignment_page.html     --> assignments/homework/*.html & machine_problems/*.html
 └── 6. golden_template_universal_term_project_proposal_page.html --> admin/syllabus/04..08_*.html & policies/*.html
```

### 2.1 Theme Token Dictionary (Decoupled for Skin Retargeting)
To retarget the course skin (e.g., updating K-State brand colors or compiling to **Moodle**, **GitHub Pages**, or **Static HTML**), the hydrator binds the following semantic CSS tokens rather than hardcoding hex values inside content files:

| Semantic Token | Default CIS 531/731 Value | Usage Scope |
| :--- | :--- | :--- |
| `--brand-primary` | `#4b2e83` / `#512888` (K-State Purple) | Hero banners, `h2`/`h3` headers, primary action buttons, table headers |
| `--brand-secondary` | `#b7a57a` (K-State Gold/Tan) | Gradient stops (`135deg, #4b2e83 0%, #b7a57a 100%`), `h2` bottom borders |
| `--brand-accent` | `#d64309` (High-Contrast Orange) | Resource action links, critical warnings, due-date highlights |
| `--phase-1-palette` | `#0056b3` / `#e8f1fb` (Blue) | Phase 1 (Modules 00–02: Foundations & Tooling) |
| `--phase-2-palette` | `#1b5e20` / `#e8f5e9` (Green) | Phase 2 (Modules 03–04: Obtain & Ingest) |
| `--phase-3-palette` | `#d64309` / `#fdebe3` (Orange) | Phase 3 (Modules 05–06: Scrub & Embed) |
| `--phase-4-palette` | `#4b2e83` / `#efe9f7` (Purple) | Phase 4 (Modules 07–08: Explore & Model) |
| `--phase-5-palette` | `#856404` / `#fff3cd` (Gold/Amber) | Phase 5 (Modules 09–13: Evaluate & Deploy) |

* **Canvas RCE Target Adapter:** Inlines all CSS styles onto HTML elements (`style="..."`), strips `<script>`, `<style>`, and `<link>` tags (which Canvas Rich Content Editor strips on save), and adds `data-api-endpoint` / `data-api-returntype` attributes to internal Canvas links.
* **Moodle / Static Web Target Adapter:** Emits clean semantic HTML5 with a single scoped stylesheet class wrapper (`.kdd-course-shell`) for Moodle Book/Page activities or MkDocs/GitHub Pages.

---

## 3. Link Taxonomy & Static Pre-Commit Verification (Zero Dead Links)

The #1 operational goal of this specification is **zero dead or misrouted links** after Canvas hydration. Crucially, **sharing the prefix `https://k-state.instructure.com/courses/201513` does NOT make a link a local Wiki Page link.**

### 3.1 The Five Mutually Exclusive Link Classes

| Link Class | URL Pattern | Resolution Semantics & Failure Mode | Static Verification Method |
| :--- | :--- | :--- | :--- |
| **1. `LOCAL_WIKI_PAGE`** | `https://k-state.instructure.com/courses/201513/pages/<slug>` | Resolves to a hydrated Canvas Wiki Page inside the `/pages/` namespace. Fails if `<slug>` is misspelled, renamed, or unpublished. | **Offline Manifest Check:** `<slug>` MUST exist in Column 4 of the Master Hydration Manifest (Section 7) with `Pub = [x]`. |
| **2. `CANVAS_NATIVE_OBJECT`** *(External to Wiki Tree, Same Course Prefix)* | `https://k-state.instructure.com/courses/201513/{assignments,files,discussion_topics,quizzes,modules,grades}/<id>` | Resolves to a **Canvas database entity or native widget**, NOT a Wiki Page. Fails if `<id>` belongs to a previous semester's course shell (e.g., `courses/189131` leak) or if the object is unpublished in the Canvas Assignments/Files tab. | **Canvas ID Registry Check:** Course ID MUST equal `201513` and `<id>` MUST appear in `platforms/canvas/canvas_object_ids.json`. |
| **3. `CANVAS_LTI_TOOL`** *(External Tool Wrapper, Same Course Prefix)* | `https://k-state.instructure.com/courses/201513/external_tools/<tool_id>` | Launches a third-party LTI iframe (e.g., My Mediasite `18171`, Microsoft Education `26835`). Fails if disabled in Course Navigation or blocked by third-party cookies/VPN. | **Sidebar LTI Registry Check:** `<tool_id>` MUST match Section 5 Sidebar Registry and carry a fallback access note. |
| **4. `EXTERNAL_WEB_URI`** | `https://<domain>/...` (excluding `k-state.instructure.com`) | Points to open-access textbooks, VLDB/arXiv PDFs, official docs, or GitHub code artifacts. | **HTTP Head/Get Linter:** Must carry `target="_blank" rel="noopener"` and return HTTP `200 OK` without paywall redirect. |
| **5. `FORBIDDEN_REPO_LEAK`** *(Compile-Time Error)* | Relative paths (`../phases/phase_01/`, `lecture-01.html`, `#`) OR raw GitHub `.md` page links (`github.com/.../blob/main/.../*.md`) | **BROKEN IN CANVAS:** Relative `.html` and `../` paths resolve to `404 Not Found` inside Canvas `/pages/`, while raw GitHub `.md` links trap students outside the LMS. | **Regex AST Blocker:** Any `href` matching `^(\.\./|lecture-\d+\.html|#)` or `github\.com/.+\.md$` (outside a code-download block) **fails the build**. |

### 3.2 Live Audit of Current Link Defects Caught by This Specification
Applying the rules above to the currently deployed `programming-techniques-for-data-science-and-analytics-cis-531-slash-731-fall-2026.html` (Front Page) and `lectures/index.html` immediately surfaces **4 active link/sync defects** to fix on the next hydration pass:
1. **Front Page Callout Leak:** *"Start by navigating to the Modules section here"* currently points to `https://github.com/kddresearch/cis531-731-2026_fall/blob/main/modules/README.md` (`FORBIDDEN_REPO_LEAK`) instead of `https://k-state.instructure.com/courses/201513/pages/modules`.
2. **Front Page Week 10 Status Box Leak & Off-by-One Drift:** Points to `github.com/.../modules/module_06/README.md` labeled *"Module 7 (GenAI & LLMs)"*, whereas Week 10 (Oct 26–30) is **Module 08 (Retrieval-Augmented Classification & Convolutions)** (`https://k-state.instructure.com/courses/201513/pages/module-08`).
3. **Front Page Button & Table Phase Leaks:** The *"Full Syllabus"* button points to `github.com/.../admin/syllabus/README.md` instead of `https://k-state.instructure.com/courses/201513/pages/syllabus`, and the Phase 1–5 links in the 16-week table point to `github.com/.../tree/main/phases/phase_0X` instead of `/courses/201513/pages/phase-1`..`phase-5`.
4. **Lectures Index (`lectures/index.html`) Relative Path Leaks:** Contains relative links `href="../phases/phase_01/"`, `href="../modules/module_00/"`, and `href="lecture-00.html"` (`FORBIDDEN_REPO_LEAK`), which break inside Canvas unless rewritten to `/courses/201513/pages/phase-1`, `/courses/201513/pages/module-00`, and `/courses/201513/pages/lecture-00`.

---

## 4. "Renaming Apart" Protocol for Multi-File Generative Hydration

Because commercial LLM web UIs (Gemini, Claude, ChatGPT, M365 Copilot) flatten attached filenames by stripping directory paths—triggering a *"You already have a README.md / index.html attached"* collision—any human or script staging multiple repository files for hydration MUST use the **Reversible Path-Prefix ("Renaming Apart") Protocol**:

### 4.1 Deterministic Bijection Rule (`/` $\leftrightarrow$ `__`)
Before attaching files to an LLM prompt (either via a local pre-flight script or browser upload helper), copy the target files into a transient `.hydration_stage/` directory (listed in `.gitignore`) with their repository-relative path encoded using **double underscores (`__`)**:

* `README.md` $\Longleftrightarrow$ `ROOT__README.md`
* `lectures/README.md` $\Longleftrightarrow$ `lectures__README.md`
* `lectures/index.html` $\Longleftrightarrow$ `lectures__index.html`
* `modules/module_08/README.md` $\Longleftrightarrow$ `modules__module_08__README.md`
* `reading_materials/README.md` $\Longleftrightarrow$ `reading_materials__README.md`
* `reading_materials/index.html` $\Longleftrightarrow$ `reading_materials__index.html`

### 4.2 Pre-Prompt Staging & Post-Prompt Cleanup Script (`tools/stage_hydration_context.py`)
```python
#!/usr/bin/env python3
"""Stages colliding repo files (e.g., multiple README.md / index.html files)
into .hydration_stage/ with reversible path prefixes, and cleans up after hydration."""
import shutil, sys
from pathlib import Path

STAGE_DIR = Path(".hydration_stage")

def stage_files(repo_root: Path, rel_paths: list[str]) -> None:
    STAGE_DIR.mkdir(exist_ok=True)
    for rel in rel_paths:
        src = repo_root / rel
        encoded_name = ("ROOT__" + rel if "/" not in rel else rel.replace("/", "__"))
        shutil.copy2(src, STAGE_DIR / encoded_name)
        print(f"[STAGED] {rel} -> {STAGE_DIR / encoded_name}")

def unstage_and_clean() -> None:
    if STAGE_DIR.exists():
        shutil.rmtree(STAGE_DIR)
        print("[CLEANED] Removed transient .hydration_stage/ directory.")
```

---

## 5. Canvas Sidebar Widget Parity & Wrapper Dashboard (Double-Empathy Guard)

### 5.1 Why Wrapper-to-Widget Parity Is Mandatory
Students who encounter dead links on custom Wiki Pages retreat to the **native Canvas left-hand sidebar** (`Assignments`, `Modules`, `Files`, `Course Schedule`), whereas the course designer—working inside custom HTML wrappers—rarely clicks the native sidebar widgets and may not notice when a native widget is unpublished, empty, or out of sync. To break this mutual UI avoidance loop, every native Canvas sidebar endpoint is governed by the parity table below:

| Canvas Sidebar Item | Native Canvas Endpoint (`/courses/201513/...`) | Sidebar Visibility | Custom Wrapper Page (if any) | Synchronization & Parity Contract |
| :--- | :--- | :---: | :--- | :--- |
| **Home** | `/courses/201513` | **Visible** | `/pages/programming-techniques-...` (Front Page) | Front Page embeds the top-level **Canvas Quick-Nav Dashboard** so students have 1-click access to both custom hubs and native widgets. |
| **Announcements** | `/courses/201513/announcements` | **Visible** | Mirrored in Front Page "Current Status" box | All oral in-class policy clarifications (e.g., PS 6 ontology rule) must be posted here within 60s for `ZA` distance parity. |
| **Assignments** | `/courses/201513/assignments` | **Visible** | `/pages/assignments` (`assignments/index.html`) | **CRITICAL PARITY:** Every row in `/pages/assignments` MUST link to its corresponding native `/courses/201513/assignments/<id>` submission portal, with identical due dates and 30-pt normalized weights. |
| **Modules** | `/courses/201513/modules` | **Visible** | `/pages/modules` (`modules/index.html`) | Native Canvas Modules must contain published links to the hydrated `/pages/module-00`..`13` pages and `/assignments/<id>` portals. |
| **Pages** | `/courses/201513/wiki` | **Visible** | `/pages/phases` & `/pages/lectures` | All active pages in Section 7 must be toggled **Published** (`[x]`) and verified in **Student View** (`[x]`). |
| **Files** | `/courses/201513/files` | **Visible** | Wrapped by `/pages/course-references` & Lab links | Lab notebooks (`lab01.ipynb`–`lab08.ipynb`) and slide PDFs uploaded to Canvas Files must have their file permissions set to **Published** so preview links (`?wrap=1`) never throw `403 Unauthorized`. |
| **Course Schedule** | `/courses/201513/assignments/syllabus` | **Visible** | `/pages/syllabus` (`admin/syllabus/README.md`) | The native Canvas Syllabus page auto-generates a chronological assignment table at the bottom; its top HTML body should transclude `/pages/syllabus`. |
| **Discussions** | `/courses/201513/discussion_topics` | **Visible** | Linked from `PS 4` Step 1 | Used for Weeks 02–04 Project Proposal Class Participation (`Out of 5`). |
| **Grades** | `/courses/201513/grades` | **Visible** | *Native Only* | All homework/MP columns normalized to `Out of 30` (excluding class participation). |
| **My Mediasite** | `/courses/201513/external_tools/18171` | **Visible** | Linked per-lecture in `/pages/lecture-XX` | Must include fallback note if Mediasite SSO/VPN fails (fallback: local OBS recording on M365 SharePoint/Teams). |
| **Microsoft Education** | `/courses/201513/external_tools/26835` | **Visible** | Linked on Front Page (`📹 Microsoft Teams`) | Primary synchronous/asynchronous class channel and office-hours bridge. |

---

## 6. Dynamic Mutability Zones ("Subject to Change Until" Governance)

To support mid-semester adaptation (due to infrastructure outages, VPN/Mediasite failures, TA availability shifts, or diagnostic pretest gaps) without violating student SLA expectations, every hydrated element belongs to one of three mutability zones:

1. **Zone A — `IMMUTABLE_SEMESTER_CONTRACT` (Locked After Week 1):**
   * Grading scale, category weights, the 30-point homework normalization rule, the "drop lowest 2 of 9 regular assignments" rule, and the **undroppable milestone status** of `PS 4`, `PS 8`, and `HW 12`.
2. **Zone B — `RELEASE_GATED_MUTABLE` ("Subject to Change Until Release Date"):**
   * **Not-Yet-Released Assignments (`MP 9`, `MP 10`, `PS 11`, `HW 12` prior to their release dates):** Specific dataset fixtures, fallback models (e.g., local CPU Whisper fallback on API quota exhaustion), or due-date extensions (never contractions) may be adjusted *prior to the assignment release date*.
   * **Upcoming Module Readings:** Readings for Module $k$ are designated *"Subject to refinement until 1 week prior to Module $k$ Lecture 1"* (provided any replacement remains 100% open-access).
   * **HTML Rendering Rule:** Any unreleased assignment row on `/pages/assignments` or `/pages/lectures` must display a badge: `<span style="background:#fff3cd; color:#856404; padding:2px 6px; border-radius:3px; font-size:0.8em;">Provisional Until Release Date</span>`.
3. **Zone C — `STUDENT_CUSTOMIZABLE_SLOTS` (Per-Team / Per-Student):**
   * The 3x5x5 Data Cube project coordinate (`Category x Media Topic x OSEMN Stage`), dataset selection (Tier 1 Golden Path vs. Tier 2 API/Benchmark), and `CIS 731` custom JSON Schema / ontology definitions.

---

## 7. Complete Source-to-Destination Hydration Manifest (`CIS 531/731`)

Every dehydrated source document in `kddresearch/cis531-731-2026_fall` is mapped below from **Source (`.md` / `.ipynb` by default)** to **Repo HTML Mirror (`.html`)** and **Canvas Destination URL**, with explicit **Publication (`Pub`)** and **HITL Student-View (`SV`)** verification checkboxes.

### 7.1 Core Course Hubs, Indices & Policies

| Pub | SV | Dehydrated Source Path (`.md` Default) | Repo HTML Mirror Path (`.html` Default) | Canvas Destination URL (`/courses/201513/...`) | Inherited Golden Template | Mutability Zone |
| :-: | :-: | :--- | :--- | :--- | :--- | :---: |
| - [x] | - [ ] | `README.md` *(+ schedule metadata)* | `platforms/canvas/front_page.html` | `/pages/programming-techniques-for-data-science-and-analytics-cis-531-slash-731-fall-2026` *(Front Page)* | `golden_template.html` (Dashboard) | Zone B (Weekly Status) |
| - [x] | - [ ] | `admin/syllabus/README.md` | `admin/syllabus/index.html` | `/pages/syllabus` *(+ `/assignments/syllabus`)* | `golden_template.html` | Zone A |
| - [x] | - [x] | `reading_materials/README.md` | `reading_materials/index.html` | `/pages/course-references` | `golden_template.html` (Card Grid) | Zone B |
| - [x] | - [x] | `reading_materials/readings_by_lecture.md` + `lectures/README.md` | `lectures/index.html` | `/pages/lectures` | `..._assignment_index_page.html` | Zone B |
| - [x] | - [ ] | `phases/README.md` | `phases/index.html` | `/pages/phases` | `..._phase_page.html` | Zone A |
| - [x] | - [ ] | `modules/README.md` | `modules/index.html` | `/pages/modules` | `..._module_page.html` | Zone B |
| - [x] | - [ ] | `assignments/README.md` + `assignments/homework/README.md` | `assignments/index.html` | `/pages/assignments` | `..._assignment_index_page.html` | Zone B |
| - [x] | - [x] | `docs/setup/hw1_mp2_windows11_wsl2_docker_walkthrough.md` | `modules/module_02/hw1_mp2_windows11_wsl2_docker_walkthrough.html` | `/pages/hw-1-and-mp-2-setup-walkthrough-docker-desktop-windows-11-+-wsl-2` | `..._assignment_page.html` | Zone A |
| - [x] | - [x] | `admin/syllabus/04_term_project_guidelines.md` | `admin/syllabus/04_term_project_guidelines.html` | `/pages/term-project-guidelines` | `..._term_project_proposal_page.html` | Zone A |
| - [x] | - [ ] | `admin/syllabus/05_term_project_taxonomy.md` | `admin/syllabus/05_term_project_taxonomy.html` | `/pages/term-project-taxonomy` | `..._term_project_proposal_page.html` | Zone A |
| - [x] | - [x] | `admin/syllabus/06_term_project_sourcing_guide.md` | `admin/syllabus/06_term_project_sourcing_guide.html` | `/pages/term-project-deliverable-how-to` | `..._term_project_proposal_page.html` | Zone A |
| - [x] | - [x] | `admin/syllabus/07_term_project_evaluation.md` | `admin/syllabus/07_term_project_evaluation.html` | `/pages/term-project-evaluation` | `..._term_project_proposal_page.html` | Zone A |
| - [x] | - [x] | `admin/syllabus/08_term_project_grading_rubric.md` | `admin/syllabus/08_term_project_grading_rubric.html` | `/pages/term-project-grading-rubric` | `..._term_project_proposal_page.html` | Zone A |
| - [x] | - [x] | `admin/policies/generative_ai_kit_v3.md` + `generative_ai_kit_howto_v2.md` | `admin/policies/generative_ai_kit_v3.html` | `/pages/generative-ai-kit` | `..._term_project_proposal_page.html` | Zone B |
| - [x] | - [ ] | `admin/policies/generative_ai_kit.md` + `generative_ai_kit_howto.md` | `admin/policies/generative_ai_kit_v1.html` | `/pages/generative-ai-kit-v1` | `..._term_project_proposal_page.html` | Archived |
| - [ ] | - [ ] | `admin/policies/term_project_invariants.md` | *(Inline-substituted into student specs; never published raw)* | *(Internal Guard Only — Do Not Publish Raw `INV-XX` Table)* | — | Internal |
| - [ ] | - [ ] | `term_project/fixed_docker_manifest_requirement.md` | `term_project/fixed_docker_manifest_requirement.html` | `/pages/fixed-docker-manifest-requirement` | `golden_template.html` | Zone A |

### 7.2 Phase Wrapper Pages (`phases/phase_01` – `phases/phase_05`)

| Pub | SV | Dehydrated Source Path (`.md`) | Repo HTML Mirror Path (`.html`) | Canvas Destination URL (`/courses/201513/...`) | Inherited Golden Template |
| :-: | :-: | :--- | :--- | :--- | :--- |
| - [x] | - [ ] | `phases/phase_01/README.md` | `phases/phase_01/index.html` | `/pages/phase-1` | `golden_template_universal_phase_page.html` |
| - [x] | - [ ] | `phases/phase_02/README.md` | `phases/phase_02/index.html` | `/pages/phase-2` | `golden_template_universal_phase_page.html` |
| - [x] | - [ ] | `phases/phase_03/README.md` | `phases/phase_03/index.html` | `/pages/phase-3` | `golden_template_universal_phase_page.html` |
| - [x] | - [ ] | `phases/phase_04/README.md` | `phases/phase_04/index.html` | `/pages/phase-4` | `golden_template_universal_phase_page.html` |
| - [x] | - [ ] | `phases/phase_05/README.md` | `phases/phase_05/index.html` | `/pages/phase-5` | `golden_template_universal_phase_page.html` |

### 7.3 Module Pages (`modules/module_00` – `modules/module_13`)

| Pub | SV | Dehydrated Source Path (`.md`) | Repo HTML Mirror Path (`.html`) | Canvas Destination URL (`/courses/201513/...`) | Inherited Golden Template |
| :-: | :-: | :--- | :--- | :--- | :--- |
| - [ ] | - [ ] | `modules/module_00/README.md` | `modules/module_00/index.html` | `/pages/module-00` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_01/README.md` | `modules/module_01/index.html` | `/pages/module-01` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_02/README.md` | `modules/module_02/index.html` | `/pages/module-02` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_03/README.md` | `modules/module_03/index.html` | `/pages/module-03` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_04/README.md` | `modules/module_04/index.html` | `/pages/module-04` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_05/README.md` | `modules/module_05/index.html` | `/pages/module-05` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_06/README.md` | `modules/module_06/index.html` | `/pages/module-06` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_07/README.md` | `modules/module_07/index.html` | `/pages/module-07` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_08/README.md` | `modules/module_08/index.html` | `/pages/module-08` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_09/README.md` | `modules/module_09/index.html` | `/pages/module-09` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_10/README.md` *(Create)* | `modules/module_10/index.html` | `/pages/module-10` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_11/README.md` *(Create)* | `modules/module_11/index.html` | `/pages/module-11` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_12/README.md` *(Create)* | `modules/module_12/index.html` | `/pages/module-12` | `golden_template_universal_module_page.html` |
| - [ ] | - [ ] | `modules/module_13/README.md` *(Create)* | `modules/module_13/index.html` | `/pages/module-13` | `golden_template_universal_module_page.html` |

### 7.4 Assignments: Homeworks, Problem Sets & Machine Problems (`assignments/`)

| Pub | SV | Dehydrated Source Path (`.md`) | Repo HTML Mirror Path (`.html`) | Canvas Native Assignment Portal (`/courses/201513/assignments/...`) | Inherited Golden Template | Mutability Zone |
| :-: | :-: | :--- | :--- | :--- | :--- | :---: |
| - [x] | - [x] | `assignments/homework/hw1_devcontainer_bringup_architecture.md` | `assignments/homework/hw1_devcontainer_bringup_architecture.html` | `/courses/201513/assignments/2597889` | `..._assignment_page.html` | Locked (Closed) |
| - [x] | - [x] | `assignments/machine_problems/mp2_devcontainer_deployment_manifest_verification.md` | `assignments/machine_problems/mp2_devcontainer_deployment_manifest_verification.html` | `/courses/201513/assignments/2600010` | `..._assignment_page.html` | Locked (Closed) |
| - [x] | - [x] | `assignments/machine_problems/mp3_real_time_asr_vector_database_ingestion.md` | `assignments/machine_problems/mp3_real_time_asr_vector_database_ingestion.html` | `/courses/201513/assignments/{{MP3_ID}}` | `..._assignment_page.html` | Locked (Closed) |
| - [x] | - [x] | `assignments/homework/ps4_proposal.md` | `assignments/homework/ps4_proposal.html` | `/courses/201513/assignments/{{PS4_ID}}` | `..._term_project_proposal_page.html` | Locked (Milestone 1) |
| - [x] | - [x] | `assignments/machine_problems/mp5_structured_streaming.md` | `assignments/machine_problems/mp5_structured_streaming.html` | `/courses/201513/assignments/{{MP5_ID}}` | `..._assignment_page.html` | Locked (Closed) |
| - [x] | - [x] | `assignments/homework/ps6_semantic_search_vdb_schema.md` | `assignments/homework/ps6_semantic_search_vdb_schema.html` | `/courses/201513/assignments/{{PS6_ID}}` | `..._assignment_page.html` | Locked (Closed) |
| - [x] | - [ ] | `assignments/machine_problems/mp7_genre_classification.md` | `assignments/machine_problems/mp7_genre_classification.html` | `/courses/201513/assignments/{{MP7_ID}}` *(Due Tue 03 Nov)* | `..._assignment_page.html` | Active (Released) |
| - [ ] | - [ ] | `assignments/homework/ps8_interim_report.md` | `assignments/homework/ps8_interim_report.html` | `/courses/201513/assignments/{{PS8_ID}}` *(Due Sat 07 Nov)* | `..._assignment_page.html` | Active (Milestone 2) |
| - [ ] | - [ ] | `assignments/machine_problems/mp9_rag_classification_gold_standard.md` | `assignments/machine_problems/mp9_rag_classification_gold_standard.html` | `/courses/201513/assignments/{{MP9_ID}}` *(Rel Sat 07 Nov)* | `..._assignment_page.html` | Zone B (Until Nov 7) |
| - [ ] | - [ ] | `assignments/machine_problems/mp10_interpretability_metrics.md` | `assignments/machine_problems/mp10_interpretability_metrics.html` | `/courses/201513/assignments/{{MP10_ID}}` *(Rel Mon 16 Nov)* | `..._assignment_page.html` | Zone B (Until Nov 16) |
| - [ ] | - [ ] | `assignments/homework/ps11_ethics_storytelling_dashboards.md` | `assignments/homework/ps11_ethics_storytelling_dashboards.html` | `/courses/201513/assignments/{{PS11_ID}}` *(Rel Wed 25 Nov)* | `..._assignment_page.html` | Zone B (Until Nov 25) |
| - [ ] | - [ ] | `assignments/homework/hw12_final_deliverables.md` | `assignments/homework/hw12_final_deliverables.html` | `/courses/201513/assignments/{{HW12_ID}}` *(Rel Sat 05 Dec)* | `..._assignment_page.html` | Zone B (Milestone 3) |

### 7.5 Individual Lecture Pages (`lectures/lecture-00.md` – `lectures/lecture-42.md`)

| Pub | SV | Dehydrated Source Pattern (`.md`) | Repo HTML Mirror Pattern (`.html`) | Canvas Destination URL Pattern | Inherited Golden Template |
| :-: | :-: | :--- | :--- | :--- | :--- |
| - [ ] | - [ ] | `lectures/lecture-00.md` .. `lecture-10.md` *(Create)* | `lectures/lecture-00.html` .. `lecture-10.html` | `/pages/lecture-00` .. `/pages/lecture-10` | `golden_template_universal_lecture_page.html` |
| - [ ] | - [ ] | `lectures/lecture-11.md` .. `lecture-27.md` *(Extant; delete `lectture-26.md`)* | `lectures/lecture-11.html` .. `lecture-27.html` | `/pages/lecture-11` .. `/pages/lecture-27` | `golden_template_universal_lecture_page.html` |
| - [ ] | - [ ] | `lectures/lecture-28.md` .. `lecture-42.md` *(Create)* | `lectures/lecture-28.html` .. `lecture-42.html` | `/pages/lecture-28` .. `/pages/lecture-42` | `golden_template_universal_lecture_page.html` |

---

## 8. Automated CI/CD Hydration Pipeline for Self-Hosted Open-Weight Models

To enable rapid, quota-free batch hydration on your local open-weight stack (`vLLM` / `Ollama`) or via GitHub Actions:

1. **Stage 1 — Pre-Flight Sanitization (`tools/pre_hydrate_sanitize.py`):**
   * Strips YAML frontmatter and `<!-- ASSIGNMENT-META -->` comments.
   * Scans against `admin/policies/term_project_invariants.md` to ensure zero bare `INV-XX` codes or `deal` contract strings remain in the Markdown source.
2. **Stage 2 — Hybrid Template + Local LLM Hydration (`tools/hydrate_to_canvas.py`):**
   * **Deterministic Jinja2/AST Binding:** Injects all dates, point weights, breadcrumb links (`{{COURSE_HOME_URL}}`, `{{PHASE_URL}}`, `{{MODULE_URL}}`), and reading URLs directly from the schedule tables.
   * **Open-Weight LLM Slot Hydration:** Calls the local `vLLM` endpoint (`temperature=0.0`) exclusively to format prose sections into the Ask/Tell callout boxes of the assigned Golden Template.
3. **Stage 3 — Static Link & Accessibility Gate (`tools/validate_canvas_html.py`):**
   * Rejects the build if any `href` matches `FORBIDDEN_REPO_LEAK` (`#`, `../`, `*.md`, or `courses/189131`).
   * Verifies that every `/courses/201513/pages/<slug>` target exists in Section 7 of this manifest.
4. **Stage 4 — Deployment & Student-View Verification:**
   * Pushes validated HTML to Canvas via the Canvas REST API (`PUT /api/v1/courses/201513/pages/:url` or `/assignments/:id`) or emits a single copy-pasteable artifact for HITL deployment, followed by toggling `[x] SV` after a 10-second check in Canvas **Student View**.
