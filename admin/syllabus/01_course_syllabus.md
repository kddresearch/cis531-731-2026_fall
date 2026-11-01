<!--
---
yaml_schema_version: "2.2"
document_version: "1.0"
document_last_updated_date: "2026-11-01"
document_monotonicity: "REQUIRED"
routing_clearance: "PUBLIC - STUDENT FACING"
canvas_target_slug: "/courses/201513/pages/syllabus"
---
-->

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
 <h1>📊 CIS 531 / CIS 731 — Programming Techniques for Data Science and Analytics</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Institution:</strong> Kansas State University<br>
 <strong>Document:</strong> <code>admin/syllabus/01_course_syllabus.md</code> | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Course Portal</a>
 </p>
</div>

<hr>

## 🔗 Quick Navigation

* 📦 **[Modules Overview](https://k-state.instructure.com/courses/201513/pages/modules)** | 📚 **[Lectures & Readings](https://k-state.instructure.com/courses/201513/pages/lectures)** | 📝 **[Assignments Index](https://k-state.instructure.com/courses/201513/pages/assignments)** | 📖 **[Course References](https://k-state.instructure.com/courses/201513/pages/course-references)**
* 📹 **[Microsoft Teams Channel](https://teams.microsoft.com/l/team/19%3AlzcSt1tN4vyJEgDRCku2ZzsVpL4NK7jd703mrb99i_s1%40thread.tacv2/conversations?groupId=bfc54c12-7e41-4f56-88bb-04ee9f99b1db&tenantId=d9a2fa71-d67d-4cb6-b541-06ccaa8013fb)** | 🐙 **[Course GitHub Repository](https://github.com/kddresearch/cis531-731-2026_fall)** | 🌐 **[Instructor Site](http://www.cs.ksu.edu/~bhsu)**

---

## 📍 Course Logistics & Office Hours

| Logistics Field | Details |
| :--- | :--- |
| **📍 Classroom Venue** | {{CLASSROOM_ROOM_E_G_1116_DUE}} Engineering Hall (DUE) & Global Campus (`ZA`) Asynchronous/Hybrid |
| **⏰ Class Meeting Time** | MWF {{CLASS_TIME_E_G_0930_1020_OR_1030_1120}} (U.S. Central Time) |
| **👨🏻‍🏫 Instructor** | **William H. Hsu, Ph.D.** ([`bhsu@ksu.edu`](mailto:bhsu@ksu.edu)) |
| **🏢 Instructor Office** | 2178 Engineering Hall (DUE) |
| **📞 Instructor Phone** | [+1 785 236 8247](tel:+17852368247) |
| **🕒 Instructor Office Hours** | Hybrid (In-Person DUE 2178 + Microsoft Teams):<br>• **Mon / Wed:** {{MON_WED_OFFICE_HOURS}}<br>• **By Appointment:** [**Book via Calendly (`calendly.com/banazir`)**](https://calendly.com/banazir/) or [**Outlook Booking**](http://bit.ly/hsu-calendar-2026-fall) |
| **🧑🏽‍💻 Graduate Teaching Assistant** | **Joshua Garcia** ([`{{GTA_EMAIL}}@ksu.edu`](mailto:{{GTA_EMAIL}}@ksu.edu))<br>• *GTA Office Hours:* {{GTA_HOURS_AND_ROOM}} |

---

## 📖 Course Overview & Fall 2026 Architectural Pivot

This course provides a rigorous, hands-on introduction to modern programming techniques and software architectures for scalable data science and responsive analytics. Structured around the five-stage **OSEMN** data-science lifecycle (**O**btain $\rightarrow$ **S**crub $\rightarrow$ **E**xplore $\rightarrow$ **M**odel $\rightarrow$ **iN**terpret), the curriculum progresses from distributed tabular and stream processing in **PySpark 3.5 LTS** and reproducible **Docker DevContainers** to dense vector indexing (**FAISS / Milvus**), local speech transcription (**OpenAI Whisper**), retrieval-augmented classification (**RAG**), generational drift convolutions, inferential evaluation, and **MLflow** deployment.

### ⚠️ Fall 2026 Responsive Analytics Mandate
To reflect contemporary agentic and multimodal data engineering, **legacy sentiment-analysis grinds (specifically Yelp review corpora and SEC filings) are strictly prohibited** across all homeworks, machine problems, and term projects. Every team commits at the proposal stage ([**PS 4**](../../assignments/homework/ps4_proposal.md)) to one of two immutable analytics tracks that converge at Module 7 for embedding-space exploration and generational drift modeling:

1. **🎙️ Track 1 — Automatic Speech Recognition (`ASR`) Stream Ingestion:** Live or simulated radio call-in / broadcast audio capture, local OpenAI Whisper / streaming transcription, and PySpark Structured Streaming windowed aggregation with event-time watermarking.
2. **📚 Track 2 — Vector Database (`VDB`) & Trope Ontologies:** Public-domain and instructor-provided lyric, poetry, or literary corpus ingestion, structure-aware chunking, dense bi-encoder embedding generation (`all-MiniLM-L6-v2`), FAISS/Milvus indexing, and few-shot/RAG trope classification.

### Prerequisites
* **Programming & Data Structures:** Proficiency in Python 3 (functions, classes, basic `numpy`/`pandas`) and undergraduate data structures (**CIS 300 / CIS 501** or equivalent).
* **Mathematics & Statistics:** Introductory probability and statistics (**STAT 510 / STAT 703** or equivalent) and linear algebra fundamentals.
* **System Requirements:** Ability to run the course's pinned **CPU DevContainer** (via Docker Desktop + VS Code on Windows 11 WSL 2, macOS, or Linux). **100% of coursework is solvable on the CPU baseline; a dedicated GPU is never required.**

---

## 📚 Open-Access Textbooks & Reference Materials

This course adheres strictly to a **100% Open-Access / Free-to-Read Mandate**. You do not need to purchase any textbooks or paid API subscriptions. All required theoretical texts ("Why") and practical systems manuals ("How") are indexed in [**Course References (`reading_materials/README.md`)**](../../reading_materials/README.md):

* **Primary NLP, ASR & RAG Text:** Jurafsky, D., & Martin, J. H. (Aug 19, 2026 Draft). [*Speech and Language Processing (3rd ed. draft)*](https://web.stanford.edu/~jurafsky/slp3/). Stanford University (Chs. 6, 8, 10, 11, & 16).
* **Primary Statistical Evaluation Text:** James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). [*An Introduction to Statistical Learning: with Applications in Python (ISLP)*](https://www.statlearning.com/resources-python). Springer (Chs. 1, 2, 4, 5, 12, & 13).
* **Python & Research Software Engineering:**
  * VanderPlas, J. [*Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/).
  * Irving, D., et al. (2021). [*Research Software Engineering with Python*](https://third-bit.com/py-rse/).
  * Brett, C. R., et al. [*Research Software Engineering*](https://rse-book.github.io/).
* **Visualization, Communication & Software Testing:**
  * Wilke, C. O. [*Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/) (Parts I–II & Chs. 19–20).
  * Last, S. [*Technical Writing Essentials*](https://pressbooks.bccampus.ca/technicalwriting/) (Chs. 1–3).
  * Winters, T., Manshreck, T., & Wright, H. (2020). [*Software Engineering at Google*](https://abseil.io/resources/swe-book/html/toc.html) (Chs. 11–12 & CI).

---

## 💯 Course Grading Breakdown (`CIS 531` vs. `CIS 731`)

All individual Homeworks (`HW`), Problem Sets (`PS`), and Machine Problems (`MP`) are normalized to **30.0 points each** in the Canvas gradebook. Please review the grading distribution and section-specific technical expectations corresponding to your enrollment (**CIS 531 Undergraduate** vs. **CIS 731 Graduate**):

| Component | Weight (%) | Points (1000-pt Scale) | Drop / Milestone Rule |
| :--- | :---: | :---: | :--- |
| **Regular Assignments (9 Total: `HW 1`, `MP 2`, `MP 3`, `MP 5`, `PS 6`, `MP 7`, `MP 9`, `MP 10`, `PS 11`)** | **21%** | **210 pts** | **Highest 7 of 9 count** (@ 30 pts each); **lowest 2 scores dropped automatically.** |
| **Mandatory Term Project Milestones (3 Total: `PS 4` Proposal, `PS 8` Interim Report, `HW 12` Final Deliverables)** | **9%** | **90 pts** | **3 Mandatory Milestones** (@ 30 pts each); **cannot be dropped.** |
| **Term Project Execution, Codebase Verification (`make verify`), & Final Report / Presentation** | **35%** | **350 pts** | Evaluated per [`07_term_project_evaluation.md`](./07_term_project_evaluation.md) and [`08_term_project_grading_rubric.md`](./08_term_project_grading_rubric.md). |
| **Exams & Quizzes (Take-Home Final Exam / Module Quizzes)** | **30%** | **300 pts** | Take-Home Final Exam due **Fri 04 Dec 2026**. |
| **Class Participation & Asynchronous Proposal Peer Review (`PS 4 CP`)** | **5%** | **50 pts** | Includes Weeks 02–04 Project Proposal Discussion & Reading/Lab checkpoints. |
| **TOTAL** | **100%** | **1000 pts** | Standard Letter Thresholds: **A** ($\ge 90\%$), **B** ($\ge 80\%$), **C** ($\ge 70\%$), **D** ($\ge 60\%$). |

### 🎓 Section-Specific Differentiation (`CIS 531` vs. `CIS 731`)
Per course policy, undergraduate (**CIS 531**) and graduate (**CIS 731**) students share the core OSEMN lectures and CPU DevContainer baseline, but are differentiated across four technical dimensions (evaluated by the grader by hand or automatically):
1. **Schema & Ontology Authority (`PS 6`, `MP 7`, `MP 9`):** `CIS 531` teams using the standard course pipeline adopt the instructor-provided trope ontology and chunk schema unmodified (or use the fixed ground-truth label taxonomy of an approved Tier 1 benchmark such as `librispeech_asr`); `CIS 731` students (and `CIS 731` members on mixed teams) must derive, justify, and validate a custom domain ontology and Draft 2020-12 JSON Schema.
2. **Vector Database & Persistence Tier (`MP 3`, `PS 6`):** Local in-process **FAISS** is the mandatory baseline for all students; disk persistence (`faiss.write_index` / `read_index`) and optional self-hosted **Milvus** schema deployment are required/gated to `CIS 731`.
3. **Generational Drift Modeling (`Lab 8`, `MP 9`):** All students implement fixed 1-D convolutional kernels (`[0.25, 0.5, 0.25]` smoothing and `[-1, 1]` first-difference) with bootstrap confidence intervals; `CIS 731` students must additionally train a causal learned 1-D convolutional kernel (`torch.nn.Conv1d` on CPU) and compare held-out forecast error against the fixed baseline.
4. **Term Project Data Sourcing (`PS 4`, `HW 12`):** `CIS 531` teams default to Tier 1 Golden Path datasets; `CIS 731` teams may propose Tier 2 real-world APIs/benchmarks with full rate-limit, backoff, and Bronze payload archival plans.

---

## ⚠️ Late Work, Schedule Guarantees & Quota Fallback Policies

* **Schedule Lead-Time & Gap Guarantees:** Every assignment is guaranteed at least a **9-calendar-day lead time** from release to due date and at least a **6-calendar-day gap** between due dates (unless an explicit class-wide extension is granted).
* **Zero Late Work Allowed:** Late submissions are **not accepted** (0 points) unless accompanied by a pre-approved, documented Office of Student Support and Accountability (OSSA) emergency. The automatic drop of your **lowest 2 of 9 regular assignments** is specifically designed to absorb unexpected personal or technical friction without requiring ad-hoc late extensions.
* **Mandatory Milestones Cannot Be Dropped:** The three Term Project milestones (**PS 4**, **PS 8**, and **HW 12**) are excluded from the drop policy.
* **API Quota Exhaustion & Local CPU Fallback:** Commercial API and hosted compute usage is bounded by department-issued quota limits. Exhausting an external quota never grants a deadline extension; your pipeline must fall back to local CPU Whisper transcription (`base` / `base.en`) or CPU baseline inference.

---

## 🛡️ Academic Honesty & Generative AI Kit Policy

Kansas State University has an Honor System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one's work is performed honestly and without unauthorized assistance ([`k-state.edu/honor`](http://www.k-state.edu/honor)).

### 🤖 Course Generative AI Policy ([`Generative AI Kit v3.3`](../policies/generative_ai_kit_v3.md))
You are encouraged to use the course **Generative AI Kit** (and LLMs such as ChatGPT, Claude, Gemini, M365 Copilot, and Perplexity) as an epistemic co-pilot for architectural brainstorming, schema verification, and debugging, subject to three strict rules:
1. **Mandatory `GenAI.pdf` Verification Log (5% of Every Assignment):** Every submission must include your exported `GenAI.pdf` interaction log (or an explicit written statement `"No GenAI Used"`).
2. **Prohibition on Unverified Boilerplate & Fabricated Citations:** Submitting hallucinated citations, fabricated experimental metrics, or unverified full-file overwrites violates academic integrity and fails automated verification.
3. **Human Gold-Standard Attestation (`MP 9` & `HW 12`):** Human gold-standard evaluation labels (`source=gold`, capped at $\le 50$ rows / 2 hours for `MP 9` and 50–200 pooled rows for `HW 12`) must be annotated by human students—**never by an LLM or GTA**—and accompanied by a signed `attestation.md`.