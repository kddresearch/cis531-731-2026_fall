---
yaml_schema_version: "2.1"
document_version: "2.0"
document_version: "2.1"
document_last_updated_date: "2026-11-07"
document_monotonicity: "REQUIRED"
---

# Term Project Guidelines
**Design, Implementation, and Evaluation of an End-to-End OSEMN Data Science System**

## 🎯 Architecture & Grading Structure
The Term Project is the capstone of **CIS 531 / 731**. It is evaluated via a dual-grading structure worth a total of **390 points** across the semester:

* **Process Milestones (90 pts):** You earn assignment points for completing the three mandatory project milestones on time: **PS 4 (Proposal — 30 pts)**, **PS 8 (Interim Report — 30 pts, due Sat 07 Nov 2026)**, and **HW 12 (Final Submission Milestone — 30 pts, due Mon 14 Dec 2026)**.
* **Substance Evaluation (300 pts / 200-pt HW 12 Rubric Scale):** Your final deliverables (the technical report, the digest-pinned MLflow codebase/pipeline, and the oral presentation/dashboard defense) are evaluated holistically against the [Term Project Grading Rubric](./08_term_project_grading_rubric.md) at the end of the semester.

> **The Canonical 3x5x5 Data Cube Taxonomy:** Every project must be explicitly anchored across three orthogonal dimensions: **(1) Analytical Category** (`Prescriptive`, `Descriptive`, `Predictive`), **(2) Media/Topic Row** (`Time-Series`, `Spatial`, `Text`, `Multimedia`, `Structured/Relational`), and **(3) OSEMN Execution Stages** (`Obtain`, `Scrub`, `Explore`, `Model`, `iNterpret`), operating on either the **ASR Track** or the **VDB Track** locked at PS 4. Review [`05_term_project_taxonomy.md`](./05_term_project_taxonomy.md) and [`06_term_project_sourcing_guide.md`](./06_term_project_sourcing_guide.md).

---

## 👥 Teaming, Enrollment Track & Annotation Protocols

### 1. CIS 531 vs. CIS 731 Track & Schema Rules
* **CIS 531 Teams (Undergraduate Only):** Must use a verified Tier 1 "Golden Path" data source and **adopt the instructor-provided ontology and chunk schema unmodified**.
* **CIS 731 Teams (Graduate Only):** Expected to use a Tier 2 Real-World API/Benchmark source and **derive a custom ontology and JSON Schema (Draft 2020-12)** (class hierarchy, relation types, cardinalities, change log, and competency questions), plus fit a learned 1-D PyTorch convolutional kernel in MP 9.
* **Mixed 531/731 Teams:** Permitted to use Tier 2 sources, provided all schema/ontology inference tasks in Obtain, Scrub, and Explore are explicitly claimed and executed by the **CIS 731 members**.

### 2. Individual vs. Team Milestones & Annotation Bounds
* **Individual Homework Gates (`MP 5`, `PS 6`, `MP 7`, `MP 9`, `MP 10`, `PS 11`):** Submitted individually via Git tags (`mp5-submission`, `ps6-submission`, `mp7-submission`, `mp9-submission`, `mp10-submission`, `ps11-submission`). In **MP 9**, each student labels **at most 50 gold objects or 2 hours** (enforced by a deterministic CI row-count gate; $>50$ rows returns a 0) with a 20-object partner overlap (`overlap_ids.txt`) for Cohen's $\kappa$ IAA.
* **Pooled Team Milestones (`PS 8` Interim Report & `HW 12` Final Deliverables):** Submitted by the registered term-project team (or solo). In **HW 12**, teammates pool their adjudicated gold files to satisfy the **50–200 labeled-example range gate** with 2-way/3-way IAA and adjudication rules (solo projects keep labeled validation data at $\le 1\%$).

### 3. Corpus Scale Guideline & Ground-Truth Sourcing Policy (No Manual Hand-Gathering)
* **Automated Ingestion & Normative Scale ($5 \times 10^3$ to $5 \times 10^6$ Records/Chunks):** Per [`06_term_project_sourcing_guide.md`](./06_term_project_sourcing_guide.md), the **Obtain** stage must be executed via a repeatable script, dataset loader, or API consumer—never by manually gathering, copy-pasting, or hand-editing CSVs. Consistent with the $\le 1\%$ validation-split cap on a 50–200 item gold set ($50 / 0.01 = 5{,}000$) and the $\ge 1{,}000$-chunk silver pool required in MP 9 and MP 10, project datasets should span **$10^4$ to $10^6$ rows or chunks, give or take half an order of magnitude ($5 \times 10^3$ to $5 \times 10^6$)** (with $\ge 1{,}000$ chunks as the absolute floor for bounded audio or specialized API corpora).
* **Ground-Truth Label Sourcing (Manual Annotation Is Not Required by Default):** Students are **not** required to annotate data by hand. You should perform manual scratch annotation **only if explicitly authorized to do so in your project approval**. Instead, use one of the two default strategies below (and use the $\le 50$-object / $\le 2$-hour MP 9 gate to human-audit and verify your held-out evaluation slice):
  1. **Third-Party-Annotated or Historical Data (Default Recommended):** Source datasets in the **Obtain** step that already carry third-party human annotations, benchmark labels, reference transcripts, or historical outcome variables.
  2. **Deterministic Join / Rule-Based Alignment (Generally Acceptable):** Derive labels by deterministically joining alignable data sources, provided the alignment itself is verifiable (e.g., via an explicit join key, timestamp window, or deterministic string/regexp matching, for which generative programming is permitted).
  3. **Authorized Manual Annotation (By Project Approval Only):** Hand-label a bounded sample ($\le 50$ objects / $\le 2$ hours per student in MP 9; 50–200 pooled in HW 12) only when explicitly approved by the instructor. In all cases, unverified LLM/ASR outputs may only serve as weak-supervision `source=silver` labels, never as `source=gold` evaluation truth.

---

## Phase 1: Project Proposal (PS 4 — Completed)
*The PS 4 Proposal milestone is complete. Your data track (ASR or VDB) was fixed at PS 4 and may not change. Any refinements to your scope must be documented in Section 2 (Scope Delta) of your PS 8 Interim Report.*

---

## Phase 2: Interim Report (PS 8 — Due Sat 07 Nov 2026)
**PS 8 (30 Points)** evaluates your provenance, architecture, exploratory embedding analysis, preliminary baselines, and quantified risk and annotation plan. Submit a **single PDF (at most 10 pages) delivered with figure sources in `interim/` under Git tag `ps8-submission`** containing the seven required sections defined in [`ps8_interim_report.md`](../../assignments/homework/ps8_interim_report.md):

1. **Section 1: Team & Taxonomy Metadata (2 pts):** Roster, Analytical Category, Media Type, claimed OSEMN stages, and the mandatory GenAI Integrity Attestation.
2. **Section 2: Scope Delta and Proposal Responses (4 pts):** Updated problem statement, justified changes since PS 4, and direct responses to every instructor proposal comment.
3. **Section 3: Data Provenance & Exploratory Baselines (10 pts):** Provenance table (`source`, `whitelist_id` / `license_class`, `size`, `ingest_method`), $\ge 3$ Wilke-compliant figures (including a **UMAP sensitivity sweep** over `n_neighbors` and `min_dist` with fixed `random_state` and a cohort/drift plot with uncertainty), and advisory baseline performance.
4. **Section 4: Architecture, Invariants, & Pillar Alignment (5 pts):** End-to-end pipeline diagram, component-version table keyed to the course manifest, and enforced `deal` contract excerpts.
5. **Section 5: Risk Register and Revised Plan (5 pts):** At least 5 quantified risks (likelihood, impact, trigger, mitigation, including CPU/quota fallback) and your 50–200 annotation & IAA plan aligned with MP 9 and HW 12 due dates.
6. **Section 6: GitHub Repository Link (2 pts):** Active commit history under tag `ps8-submission`.
7. **Section 7: GenAI Audit Log & Certificate (2 pts):** Complete `GenAI.pdf` audit log under the "Grammarly on Steroids" policy (see [`generative_ai_kit_v3.md`](../policies/generative_ai_kit_v3.md)).

---

## Phase 3: Gold-Standard Construction, RAG & Statistical Evaluation (MP 7, MP 9, MP 10)
Your Phase 3 machine problems build the exact codebase and evaluation harness required for HW 12:

* **MP 7: Few-Shot Trope/Genre Classification (Due Tue 03 Nov 2026):** Locks `protocol.md`, builds the FAISS `IndexFlatIP` index, and compares prototype, kNN, and fixed-demonstration few-shot LLM classifiers behind a unified `Classifier` interface (`mp7-submission`).
* **MP 9: Retrieval-Augmented Classification & Convolutions (Due Mon 16 Nov 2026):** Constructs your human-labeled gold set ($\le 50$ objects / $\le 2$ hours, 20-object partner overlap for Cohen's $\kappa$), expands $\ge 1,000$ chunks via weak supervision (`source=silver`), evaluates top-$k$ ($k \in \{3, 5, 10\}$) RAG classification against MP 7, and runs cohort convolution analysis (`[0.25, 0.5, 0.25]` smoothing and `[-1, 1]` first-difference kernels; **CIS 731:** learned 1-D PyTorch conv kernel) (`mp9-submission`).
* **MP 10: Data Science Interpretability & Metrics Scoring (Due Wed 25 Nov 2026):** Implements `evaluate(model, X, y)` with `deal` contracts on your adjudicated MP 9 gold set, hand-derives metrics (including an imbalance counterexample and NIST OpenASR WER), runs permutation importance ($\ge 30$ repeats) and local retrieval explanations ($\ge 10$ misclassifications), computes 10/15-bin ECE calibration, executes paired bootstrap ($B \ge 10,000$) / McNemar's test with Benjamini–Hochberg FDR control across $\ge 6$ comparisons, and charts CI width vs. $n$ on silver subsamples (`mp10-submission`).

See [`07_term_project_evaluation.md`](./07_term_project_evaluation.md) for the complete statistical evaluation specification.

---

## Phase 4: Ethics, Storytelling, Dashboards (PS 11) & Final Presentations
* **PS 11: Ethics, Data Storytelling, & Dashboards (Due Fri 04 Dec 2026, before Dead Week):** Submit a 4-page ethics memo PDF (provenance/PII redaction, ecological fallacy, survivorship/selection bias, ASR disparity, and prompt-injection/hallucination mitigations respecting no-lyric-reproduction), a 5-view Wilke storyboard, and a restart-and-run-all prototype dashboard with a limitations panel (`ps11-submission`).
* **Standard Reflection Questions (Required in Presentation Slides):** Each team member must individually answer:
  1. What aspect of data science/machine learning did you find most technically challenging in completing this term project?
  2. What aspect of data science/machine learning do you think you learned the most about over the course of the project?
  3. What is your top priority for future work, if you were to continue this project as a research project or in independent study?
* **Scheduling Protocols:** Optional extra-credit presentations run during **Dead Week (Mon 07 – Fri 11 Dec 2026)** after Lecture 40 and do not substitute for any part of the HW 12 written/code deliverable. No live presentations will be scheduled during Finals Week without prior written OSSA accommodation approval before the end of Week 16.

---

## Phase 5: Final Report & Reproducible MLOps Package (HW 12 — Due Mon 14 Dec 2026)
Your unified final deliverables are submitted under Git tag `hw12-final` (see [`hw12_final_deliverables.md`](../../assignments/homework/hw12_final_deliverables.md)) and shared with **@banazir** on GitHub:

* **The Final Technical Report (`REPORT.pdf`, at most 12 pages):** Contains (1) Problem, Data, and Provenance (`license_class` / whitelist ID; no Yelp/SEC data), (2) Methods, Architecture, `deal` Contracts, and Manifest Versions, (3) Evaluation on the 50–200 Gold Standard (IAA with CIs or $\le 1\%$ solo validation fraction, 95% CIs, ablations, BH-controlled significance tests, cohort-stratified results, error analysis), (4) Ethics, Limitations, and Implemented Mitigations from PS 11, (5) Reproducibility, MLOps, and Serving, and (6) `GenAI.pdf` Audit.
* **The Reproducible MLOps Package (`hw12-final`):** Digest-pinned `Dockerfile` or DevContainer, lockfile, `Makefile` (where `make verify` runs lockfile/digest checks, contract tests, the 50–200 gold-standard range gate, and headline-metric reproduction on the CPU baseline), `reproduce.md`, MLflow run export and registered model entry, working serving code (checkpointed Structured Streaming job with restart for ASR; CLI/HTTP service with smoke test for VDB), and a PSI/KS drift-monitoring runbook.
