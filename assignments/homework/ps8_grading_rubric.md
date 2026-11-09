<!-- RUBRIC-META
id: PS 8 Rubric
title: PS 8: Term Project Interim Report — Grading Rubric & Evaluation Specification
course: CIS 531 / CIS 731 (Fall 2026)
points: 30 (Undroppable Process Milestone)
canvas_page: https://k-state.instructure.com/courses/201513/pages/term-project-interim-update
canvas_survey: https://k-state.instructure.com/courses/201513/quizzes/623057
released: Thu 29 Oct 2026
due: Fri 13 Nov 2026 (Extended from Sat 07 Nov 2026)
-->

# PS 8: Term Project Interim Report — Grading Rubric (30 Points)

**Course:** CIS 531 / CIS 731 — Introduction to Programming Techniques for Data Science and Analytics  
**Milestone Weight:** 30 Points (Mandatory, Undroppable Process Milestone; 1 of 3 alongside PS 4 [30 pts] and HW 12 [30 pts] within the 390-point Capstone Framework)  
**Submission Modality:** 8-Question Canvas Survey ([Quiz #623057](https://k-state.instructure.com/courses/201513/quizzes/623057)) + `GenAI.pdf` File Upload + GitHub Repository Tag `ps8-submission` (with figure sources in `interim/`)  
**Team Policy:** Submitted per registered Term-Project Team (1–3 students; solo permitted)

---

## 1. Executive Summary & Schema Reconciliation

Unlike PS 4 (which required individual 1–1.5 page PDF uploads), **PS 8** is evaluated via an **8-question Canvas Survey** backed by reproducible code and figure sources committed under the Git tag `ps8-submission`. To ensure seamless grading across both the Canvas Survey ([`ps8_interim_report.html`](https://k-state.instructure.com/courses/201513/pages/term-project-interim-update)) and repository PDF/Markdown exports (`ps8_interim_report.md`), the 30 points map across the two representations as follows:

| Canvas Survey Question (`quizzes/623057`) | Survey Points | Corresponding Report Section (`ps8_interim_report.md`) | PDF Section Points | Core Artifacts & Invariants Audited |
| :--- | :---: | :--- | :---: | :--- |
| **Q1:** Team, 3x5x5 Taxonomy & Track Metadata | **2 pts** | **Section 1:** Team & Taxonomy Metadata *(Part A)* | **2 pts** *(with Q6)* | Roster, 3x5x5 Coordinate, OSEMN ownership, Fixed Track (`INV-3`), Schema Authority (`INV-11`) |
| **Q2:** Scope Delta & Proposal Responses | **4 pts** | **Section 2:** Scope Delta & Proposal Responses | **4 pts** | Updated problem statement, justified scope diff vs. PS 4, responses to PS 4 feedback (or self-audit) |
| **Q3:** Data Provenance & Exploratory Baselines | **8 pts** | **Section 3:** Data Provenance & Exploratory Baselines | **10 pts** *(split: 8 pts Q3 + 2 pts Q6)* | Provenance table (`INV-1`, `INV-9`), $\ge 3$ Wilke-compliant figures (UMAP sweep + drift/uncertainty), advisory baseline (`INV-12`) |
| **Q4:** Architecture, Invariants & Pillar Alignment | **5 pts** | **Section 4:** Architecture, Invariants & Pillar Alignment | **5 pts** | End-to-end OSEMN pipeline diagram, pinned manifest version table (`INV-14`), `deal` contracts |
| **Q5:** Risk Register & Revised Annotation Plan | **5 pts** | **Section 5:** Risk Register & Revised Plan | **5 pts** | $\ge 5$ quantified risks + CPU fallback (`INV-15`, `INV-18`), 50–200 gold/silver IAA plan, $\le 1\%$ validation cap |
| **Q6:** Honor Code Attestation *(True/False)* | **2 pts** | **Section 1:** Integrity Attestation *(Part B)* | *(Included in Sec 1/3)* | Mandatory attestation of human foundational effort & GenAI Kit (v1–3.3) editor-only compliance |
| **Q7:** GenAI Audit Log & Certificate (`GenAI.pdf`) | **2 pts** | **Section 7:** GenAI Audit Log & Certificate | **2 pts** | Uploaded `GenAI.pdf` containing exact prompts, pre-AI human bullet points/specs ("Toll"), and raw AI output |
| **Q8:** GitHub Repository Link & `ps8-submission` Tag | **2 pts** | **Section 6:** GitHub Repository Link | **2 pts** | Reachable repo URL, active commit history, working baseline skeleton, tag `ps8-submission`, `interim/` figure sources |
| **Total Milestone Score** | **30 pts** | **Total Milestone Score** | **30 pts** | **Feeds MP 9 (Gold/Silver & RAG), MP 10 (Evaluation), PS 11 (Ethics/Dashboard), and HW 12 (Final)** |

> **🛡️ Proactive Resolution Policy for Pending Upstream Feedback or Skipped MPs (GenAI Kit v3.3 Rule 3):**
> 1. **Pending PS 4 Feedback:** If instructor grading/feedback on PS 4 was not yet returned when drafting Q2, teams are **never** penalized for missing instructor comments; instead, full credit is awarded for performing a structured self-audit of their submitted PS 4 proposal against the [Data Sourcing & OSEMN Execution Guide](https://k-state.instructure.com/courses/201513/pages/term-project-data-sourcing-guide) acceptance checklist.
> 2. **Skipped Upstream Homework/MP (MP 3, MP 5, PS 6, or MP 7):** Because PS 8 is an undroppable milestone, a student or team who dropped/skipped an intermediate non-milestone assignment may bridge the missing dependency using the course-default baseline (*"Satellite radio caller analytics using local Whisper ASR transcription and FAISS VDB ingestion"*) while keeping PS 8 anchored to their registered term-project scope.

---

## 2. Enrollment Track Differentiation: CIS 531 vs. CIS 731

| Requirement Dimension | CIS 531 (Undergraduate Track) | CIS 731 (Graduate Track) | Mixed 531/731 Teams |
| :--- | :--- | :--- | :--- |
| **Data Source Tier (Q3)** | **🟢 Tier 1 (Golden Path)** default (`samples.wanderbricks`, `samples.tpcds_sf1`, HF `wikimedia/wikipedia`, `librispeech_asr`, Open-Meteo/NOAA, USGS GeoJSON). | **🟡 Tier 2 (Real-World API / Benchmark)** expected (authenticated/parameterized REST APIs with Bronze JSON archival, Kaggle IEEE-CIS, or custom licensed corpora). | Permitted to use **Tier 2** sources, provided all schema/ontology inference tasks are claimed by **CIS 731** members. |
| **Ontology & Schema Authority (`INV-11`, Q1 & Q4)** | Must adopt the **instructor-provided ontology and chunk schema unmodified**. | Must derive a **custom ontology and JSON Schema (Draft 2020-12)** (class hierarchy, relation types, cardinalities, change log since PS 6, and competency questions). Reusing the unmodified instructor schema loses schema credit. | Custom ontology and JSON Schema (`Draft 2020-12`) must be authored and maintained by the **CIS 731** team members. |
| **Downstream Model & Container Extensions (Q4 & Q5)** | Standard CPU DevContainer and fixed smoothing `[0.25, 0.5, 0.25]` / difference `[-1, 1]` cohort kernels in MP 9. | Conditional GPU/CPU image pull, `faiss.write_index` / `read_index` disk persistence, and **learned 1-D PyTorch convolutional kernel** comparison in MP 9. | CIS 731 members must own the learned 1-D PyTorch kernel and disk-persisted index extensions. |

---

## 3. Question-by-Question Grading Rubric & Anchor Tiers (30 Points)

### Question 1 (Section 1): Team, 3x5x5 Taxonomy & Track Metadata (2.0 Points)

* **Sub-Criteria Breakdown:**
  * **1.1 Team Roster & Enrollment Track (0.5 pts):** Lists all team members (1–3 students or solo) and identifies section composition (`CIS 531`, `CIS 731`, or `Mixed`).
  * **1.2 3x5x5 Data Cube Coordinates & OSEMN Delegation (0.5 pts):** Explicitly states (a) Analytical Category (`Prescriptive`, `Descriptive`, or `Predictive`), (b) Media/Topic Row (`Time-Series`, `Spatial`, `Text`, `Multimedia`, or `Structured/Relational`), and (c) the 1–2 OSEMN stages claimed per member (`Obtain`, `Scrub`, `Explore`, `Model`, `iNterpret`) plus how unclaimed stages are automated via persistent `Bronze -> Silver -> Gold` tables.
  * **1.3 Track Immutability (`INV-3`) (0.5 pts):** Confirms the fixed primary track (`ASR` or `VDB`) locked at PS 4 without mid-semester switching.
  * **1.4 Ontology & Schema Authority (`INV-11`) (0.5 pts):** CIS 531 confirms unmodified instructor schema; CIS 731 states custom ontology/JSON Schema (`Draft 2020-12`) version and change log summary.

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary** | **2.0** | All 4 sub-criteria are explicitly stated with zero ambiguity; CIS 731 custom schema version/change log (or CIS 531 unmodified attestation) and per-member OSEMN stage ownership are complete. |
| **Proficient** | **1.5** | Roster, track (`ASR`/`VDB`), and 3x5x5 coordinates are present, but OSEMN stage delegation across teammates or the `INV-11` schema version note is slightly underspecified. |
| **Developing** | **1.0** | Missing one major taxonomy dimension, unclear OSEMN stage ownership, or CIS 731 team omits custom ontology version/change log. |
| **Unacceptable** | **0.0–0.5** | Fails to identify team/track, attempts an unauthorized track switch (`INV-3` violation), or CIS 731 team uses the unmodified instructor schema without customization. |

---

### Question 2 (Section 2): Scope Delta & Proposal Responses (4.0 Points)

* **Sub-Criteria Breakdown:**
  * **2.1 Updated Problem Statement & Analytical Goal (1.5 pts):** Presents a clear, technically rigorous problem statement anchored to the team's 3x5x5 coordinate and target decision/analytical outcome.
  * **2.2 Itemized Scope Delta & Technical Justification (1.5 pts):** Explicitly diffs the PS 4 proposal against the current PS 8 implementation (data source refinements, chunking/cleaning changes, baseline adjustments, or narrowed claims) and justifies *why* each change improves feasibility or rigor.
  * **2.3 Direct Responses to PS 4 Feedback (or Proactive Self-Audit) (1.0 pt):** Provides point-by-point responses to every instructor comment on PS 4. *(If PS 4 feedback was pending, provides a point-by-point self-audit against the Section 7 PS 4 Proposal Acceptance Checklist in the Data Sourcing Guide).*

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary** | **4.0** | Crisp, falsifiable problem statement; comprehensive before/after Scope Delta table with concrete engineering justifications; thorough point-by-point resolution of all PS 4 feedback (or complete self-audit). |
| **Proficient** | **3.0–3.5** | Problem statement and scope changes are described clearly, but justifications are mostly narrative rather than tied to specific data/schema constraints, or one minor feedback item is glossed over. |
| **Developing** | **2.0–2.5** | Vague statement that "nothing changed" despite visible differences in dataset/methods, or superficial responses to proposal feedback without actionable adjustments. |
| **Unacceptable** | **0.0–1.5** | Missing problem statement, unacknowledged abandonment of the PS 4 project scope, or zero engagement with PS 4 feedback/sourcing checklist. |

---

### Question 3 (Section 3): Data Provenance, Exploratory Figures & Preliminary Baselines (8.0 Points Survey / 10.0 Points PDF with Attestation)

* **Sub-Criteria Breakdown:**
  * **3.1 Data Provenance & Sourcing Compliance Table (`INV-1`, `INV-9`) (2.5 pts):**
    * Tabulates every corpus or stream with: (a) exact source identifier (Unity Catalog table, HF dataset slug, Kaggle slug, REST/GeoJSON endpoint, or whitelisted ASR stream), (b) `whitelist_id` and `license_class` (`public_domain` or `instructor_provided`), (c) dataset scale (row/file count, MB/GB, date range), (d) Source Tier (`Tier 1`, `Tier 2`, or approved `Tier 3`), and (e) repeatable `Obtain -> Bronze -> Silver` ingestion method.
    * Confirms environment stability, secret exclusion from Git (`.gitignore` for `kaggle.json`/tokens), and **zero prohibited Yelp or SEC-filing datasets**.
  * **3.2 Exploratory Figures ($\ge 3$ Figures + Wilke Parts I–II Compliance) (3.5 pts):**
    * Presents at least **3 exploratory figures** with full interpretation and source scripts in `interim/`:
      1. **UMAP Parameter Sensitivity Sweep (1.5 pts):** Evaluates embedding structure across a grid of `n_neighbors` and `min_dist` (and `metric`) with a fixed `random_state`; discusses local vs. global topology and trustworthiness.
      2. **Cohort / Distributional Drift Plot with Uncertainty (1.0 pt):** Plots temporal, generational, or cohort drift with explicit uncertainty representation (error bars, 95% bootstrap CIs, or quantile bands).
      3. **Third Track-Specific Diagnostic Figure (0.5 pts):** E.g., class balance/imbalance distribution, token/chunk length histogram, ASR latency/duration distribution, or spatial density map.
      4. **Wilke Visual Design Compliance (0.5 pts):** Adheres to Wilke Parts I–II (perceptually uniform/colorblind-safe palettes such as Okabe-Ito or Viridis, redundant coding via shape/linetype, direct labeling, informative axis units, and zero unreadably small text).
  * **3.3 Preliminary / Naive Baseline & Advisory Metric Separation (`INV-12`) (2.0 pts):**
    * Reports an initial quantitative result from a working naive or preliminary baseline (random/majority heuristic or MP 7 CPU fixed-demonstration baseline) using the appropriate track metric (`Macro-F1`, `P@k`/`Recall@k`/`MRR`/`nDCG@k`, or NIST `WER`).
    * Explicitly labels the reported number as a **development/advisory metric (`compute_dev_metric`, `grading_eligible=False`)** rather than a leaked gold-set metric.

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary** | **7.5–8.0** | Complete provenance table with verified `license_class`/whitelist IDs and Bronze-to-Silver handoffs; $\ge 3$ publication-grade, Wilke-compliant figures including a multi-parameter UMAP sweep (`n_neighbors` $\times$ `min_dist`, fixed seed) and a cohort drift plot with uncertainty bands; working baseline metric reported and explicitly marked advisory (`INV-12`). |
| **Proficient** | **6.0–7.0** | Provenance table and baseline metric are complete; includes 3 figures, but UMAP sweep tests only a single parameter pair, uncertainty bands on the drift plot are omitted, or minor Wilke formatting flaws (e.g., default rainbow colormap or tiny labels) occur. |
| **Developing** | **4.0–5.5** | Provenance table lacks exact identifiers/sizes or Bronze storage details; fewer than 3 figures or UMAP plot is a single unparameterized scatter plot; baseline is described verbally without an executed advisory metric. |
| **Unacceptable** | **0.0–3.5** | Uses prohibited Yelp/SEC data or unapproved scraping without Bronze archive; no UMAP or exploratory figures generated; no baseline code or metric exists. |

---

### Question 4 (Section 4): Architecture, Invariants & Pillar Alignment (5.0 Points)

* **Sub-Criteria Breakdown:**
  * **4.1 End-to-End OSEMN Pipeline Diagram & Stage Justification (2.0 pts):**
    * Provides a clear pipeline architecture diagram/flow covering `Ingest (Obtain) -> Clean/Chunk (Scrub) -> Embed/Transcribe & Index (Explore) -> Retrieve/Analyze (Model) -> Evaluate (iNterpret)`.
    * Explains *why* this architecture fits the claimed OSEMN stages and specifies versioned `Bronze -> Silver -> Gold` Delta/Parquet/FAISS handoffs (no manual CSVs or ephemeral notebook state).
  * **4.2 Fixed Project Manifest / Component-Version Table (`INV-14`) (1.5 pts):**
    * Tabulates exact pinned package versions and container digests matching the course DevContainer manifest (Python, PySpark/Delta, PyTorch/Transformers/Whisper, FAISS, scikit-learn/statsmodels, `umap-learn`, `deal`, MLflow) and cites the data source and objective so enforced requirements can be verified.
  * **4.3 Enforced `deal` Contracts & Qualitative Invariants (1.5 pts):**
    * Includes concrete `deal` contract excerpts (`@deal.pre`, `@deal.post`, `@deal.inv`) or verifiable invariant assertions enforcing pipeline constraints (e.g., chunk duration $\le 30\text{s}$ with `ts_start < ts_end`, non-null IDs, valid coordinate/probability bounds $\sum p_i = 1.0 \pm 10^{-6}$, `license_class` checks, and `source=gold` vs. `source=silver` separation).

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary** | **5.0** | Detailed end-to-end architecture diagram with explicit Bronze/Silver/Gold table names; complete component-version manifest table pinned to the course DevContainer (`INV-14`); concrete, syntactically valid `deal` contract excerpts tied to track invariants. |
| **Proficient** | **3.75–4.5** | Pipeline architecture and component-version table are solid, but inter-stage table names are generic or `deal` contracts are described only in high-level prose without specific pre/post-conditions. |
| **Developing** | **2.5–3.5** | Missing component-version manifest table, pipeline diagram omits critical stages (e.g., indexing or evaluation), or invariants are omitted. |
| **Unacceptable** | **0.0–2.0** | Relying on manual browser downloads/local unversioned CSVs with no coherent pipeline architecture or version manifest. |

---

### Question 5 (Section 5): Risk Register, Annotation Plan & Validation Strategy (5.0 Points)

* **Sub-Criteria Breakdown:**
  * **5.1 Quantified Risk Register ($\ge 5$ Risks + CPU Fallback `INV-15`/`INV-18`) (2.0 pts):**
    * Lists at least **5 distinct, track-specific risks**, each quantified with **Likelihood** (e.g., Low/Med/High or probability), **Impact**, **Trigger Condition**, and **Actionable Mitigation**.
    * **Mandatory Inclusion:** Explicitly includes API credit / GPU compute / rate-limit exhaustion with an automatic fallback to the **pinned CPU DevContainer baseline** (local CPU Whisper or free-tier CPU model).
  * **5.2 Work Breakdown & MP 9 / HW 12 Gold/Silver Annotation Plan (2.0 pts):**
    * Milestone schedule aligned with **MP 9 (Nov 16)**, **MP 10 (Nov 25)**, **PS 11 (Dec 4)**, and **HW 12 (Dec 14)**.
    * Specifies the **50–200 labeled gold-example target** for HW 12 (respecting MP 9's per-student $\le 50$-row / $\le 2$-hour CI cap), how automated labeling functions (`source=silver`, $\ge 1,000$-chunk silver pool) scale pre-labeling without polluting `source=gold`, and the **Inter-Annotator Agreement (IAA) protocol** (20-object partner overlap `overlap_ids.txt`, 2-way/3-way Cohen's $\kappa$ with 95% CIs, and adjudication rules, citing *Jurafsky & Martin SLP3*).
  * **5.3 Validation Fractional Cap ($\le 1\%$) & Leakage Defense (1.0 pt):**
    * Explains why enforcing a strict fractional cap on the validation split (such as keeping validation splits $\le 1\%$ on large scaled corpora or solo projects) and isolating the human gold test set prevents data leakage, validation overfitting, and evaluation noise (citing *ISLP Chapter 5*).

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary** | **5.0** | $\ge 5$ quantified risks (Likelihood, Impact, Trigger, Mitigation) including the mandatory CPU-baseline quota fallback (`INV-15`/`INV-18`); concrete 50–200 gold + $\ge 1,000$ silver annotation plan with Cohen's $\kappa$ IAA and adjudication rules; rigorous statistical explanation of the $\le 1\%$ validation cap and leakage prevention. |
| **Proficient** | **3.75–4.5** | Includes 5 risks and CPU fallback plus the 50–200 annotation target, but risk triggers/mitigations are slightly generic, or the explanation of the $\le 1\%$ validation cap / silver-vs.-gold boundary is brief. |
| **Developing** | **2.5–3.5** | Fewer than 5 risks, omits the mandatory CPU-baseline fallback, omits the IAA overlap/adjudication protocol, or fails to address the validation fractional cap. |
| **Unacceptable** | **0.0–2.0** | Unquantified 1–2 line risk list; no viable plan for human gold annotation or validation split separation. |

---

### Question 6 (Section 1B): Honor Code & GenAI Role Attestation (2.0 Points)

* **Requirement:** Student selects **True** on Canvas Survey Question 6 (and includes the verbatim attestation in any PDF/Markdown report):
  > *"I attest that the written responses provided in this survey originate from my own thoughts, code, and bullet points. Where Generative AI was used, it was restricted to the role of an editor/synthesizer in accordance with the course GenAI Kit (v1–3). I did not use prompts that delegated the entire cognitive load to an AI system."*

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary (Pass)** | **2.0** | Attestation is affirmed (`True` in Q6 / verbatim statement included) and consistent with the submitted `GenAI.pdf` audit log. |
| **Unacceptable (Fail)** | **0.0** | Attestation is left blank, answered `False`, or contradicted by unacknowledged zero-shot AI generation of core results/numbers. |

---

### Question 7 (Section 7): GenAI Audit Log & Certificate (`GenAI.pdf`) (2.0 Points)

* **Requirement:** Uploads a complete `GenAI.pdf` in Canvas Survey Question 7 (and commits it to the repository) documenting compliance with the **GenAI Kit v3.3 Two Procedural Tollbooths** (*Anti-Spooning Stick* & *Systems Thinking Carrot*):
  1. **Exact Prompts:** Every system prompt and user prompt submitted to any LLM (ChatGPT, Gemini, Claude, Perplexity, Copilot).
  2. **Pre-AI Human Foundational Effort ("The Toll"):** The student's own raw bullet points, PS 4 scope diff notes, UMAP parameter sweep configurations, baseline numbers, and initial risk items fed into the AI.
  3. **Raw AI Outputs:** The unedited LLM responses showing how the AI was used strictly for red-teaming and prose synthesis ("Grammarly on Steroids").
  * *(Note: If no Generative AI was used, uploading a `GenAI.pdf` explicitly stating `"No Generative AI was used for PS 8"` earns the full 2.0 points).*

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary** | **2.0** | Complete `GenAI.pdf` uploaded containing (1) exact prompts, (2) original pre-AI human bullet points/specifications ("Toll"), and (3) raw AI responses (or a signed zero-AI declaration PDF). |
| **Developing** | **1.0** | `GenAI.pdf` is uploaded but contains only final AI outputs or summary screenshots without the student's pre-AI raw bullet points/prompts. |
| **Unacceptable** | **0.0** | No `GenAI.pdf` uploaded, or audit log reveals the AI invented fake baseline metrics/figures ab initio. |

---

### Question 8 (Section 6): GitHub Repository Link & `ps8-submission` Tag (2.0 Points)

* **Requirement:** Provides a valid, accessible URL to the team's active GitHub repository demonstrating:
  1. Multi-commit history showing working code skeleton and preliminary baseline implementation,
  2. Git tag `ps8-submission` created on the milestone commit, and
  3. Reproducible figure-generation code and figure outputs stored in the `interim/` directory.

| Tier | Score | Anchor Description |
| :--- | :---: | :--- |
| **Exemplary** | **2.0** | Valid repository URL with instructor/TA access (`kddresearch` org or `@banazir` collaborator), clean commit history, verified `ps8-submission` Git tag, and reproducible figure sources in `interim/`. |
| **Developing** | **1.0** | Repository URL works and contains code/figures, but the `ps8-submission` Git tag is missing or figure sources are not organized in `interim/`. |
| **Unacceptable** | **0.0** | Broken/private inaccessible URL, empty repository with only a `README.md`, or zero commits corresponding to PS 8. |

---

## 4. Hard Compliance Gates & Automatic Deduction Summary

To protect downstream execution in MP 9, MP 10, PS 11, and HW 12, the following invariant checks are enforced during grading:

| Gate ID | Invariant / Policy Rule | Check Method | Scoring Consequence if Violated |
| :--- | :--- | :--- | :--- |
| **GATE-1** | **Prohibited Datasets (`INV-1`)** | Provenance table & repo scan | Using prohibited **Yelp review** or **SEC-filing** datasets zeroes out Question 3 provenance credit (**-2.5 pts**) and requires immediate dataset replacement before MP 9. |
| **GATE-2** | **Track Immutability (`INV-3`)** | Q1 vs. PS 4 roster record | Switching between `ASR` and `VDB` tracks without prior written instructor sign-off loses Q1 track credit (**-1.0 pt**) and blocks grading until reconciled. |
| **GATE-3** | **CIS 731 Schema Authority (`INV-11`)** | Q1 & Q4 schema audit | CIS 731 teams reusing the unmodified CIS 531 instructor schema without a custom `Draft 2020-12` JSON Schema and change log lose schema credit in Q1 (**-0.5 pts**) and Q4 (**-1.5 pts**). |
| **GATE-4** | **Advisory Metric Separation (`INV-12`)** | Q3 & Q5 evaluation check | Presenting dev-split or silver-pool numbers as final gold-standard evaluation metrics without marking them advisory loses baseline rigor credit (**-1.0 pt**). |
| **GATE-5** | **UMAP Fixed Seed & Sweep** | Q3 figures & `interim/` code | Submitting a single default UMAP plot without sweeping `n_neighbors` and `min_dist` at a fixed `random_state` caps Q3 figure credit at **2.0 / 3.5 pts**. |
| **GATE-6** | **Quota / CPU Fallback (`INV-15`, `INV-18`)** | Q5 risk register check | Omitting the mandatory API/GPU quota-exhaustion risk and pinned CPU DevContainer fallback deducts **-1.0 pt** from Q5. |
