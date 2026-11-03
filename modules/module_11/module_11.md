# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 5:** Evaluate & Deploy | **Module 11:** Presenting Results — Ethics, Data Storytelling & Documentation Standards | **Lectures 34-36** | Mon 16 Nov - Fri 20 Nov 2026 |

---

## Lecture 34: Presenting Results: Ethics & Data Storytelling (Mon 16 Nov)

1. **Audience Analysis & Decision-Centered Technical Writing:** Identifying the target operational or research audience, the specific decision they must make from the pipeline's output, and the one-sentence "so what" thesis (*Technical Writing Essentials*, Chs. 1–3).
2. **Provenance, Licensing, & Broadcast Privacy Audits:** Auditing every ingested corpus and audio stream for verified license classes, broadcast terms of use, and personally identifiable information (PII) in call-in speech, paired with concrete redaction and retention/deletion policies.
3. **Ecological Fallacy & Selection Bias in Generational Claims:** Distinguishing media release decades from listener or reader demographics (avoiding the ecological fallacy) and analyzing survivorship and selection bias in historical lyric, literary, and radio archives.
4. **Acoustic & Demographic Error Disparity:** Auditing ASR Word Error Rate (WER) and classification recall disparities across speaker dialects, vocal registers, and background-noise conditions in streaming audio pipelines.
5. **LLM Pipeline Risks & Copyright Guardrails:** Designing concrete defenses against hallucinated trope attributions and indirect prompt injection inside transcribed or scraped text, while strictly prohibiting full song-lyric reproduction beyond approved short excerpts.

---

## Lecture 35: Documentation, Provenance & Notebook Presentation Standards (Wed 18 Nov)

1. **FAIR Data Stewardship in Analytical Reporting:** Applying Findable, Accessible, Interoperable, and Reusable (*FAIR Guiding Principles*, Wilkinson et al.) metadata standards to Bronze, Silver, and Gold data tables and exported evaluation artifacts.
2. **Literate Programming & Computational Narrative Structure:** Structuring Jupyter notebooks (*Project Jupyter Documentation*) so Markdown narrative arguments, mathematical metric derivations, executable code cells, and interpreted figures form a cohesive technical report.
3. **Clean-State Reproducibility (`Restart & Run All`):** Enforcing deterministic random-seed pinning, relative file path hygiene, and lockfile consistency so every analytical notebook executes cleanly from top to bottom inside the pinned CPU DevContainer.
4. **Evidence-Anchored Claims & Traceability:** Binding every quantitative and qualitative claim in the ethics memo and interim/final reports to an explicit figure number, confusion matrix, contract excerpt, or `results.json` entry.
5. **Static & Interactive Export Workflows:** Compiling executed notebooks and prototype dashboards into standalone HTML and PDF deliverables suitable for archival review under Git tag `ps11-submission`.

---

## Lecture 36: Dashboard Design & Limitations Panel Workshop; Wrap-Up (Fri 20 Nov)

1. **Five-View Analytical Storyboarding:** Designing a focused dashboard storyboard of at most 5 views, specifying for each view its analytical question, visual encoding, source columns from the MP 10 outputs, and refresh cadence.
2. **Perceptual Encoding & Accessible Color Palettes:** Applying Wilke's visualization principles (*Fundamentals of Data Visualization*, Parts I–II), including colorblind-safe palettes (Okabe–Ito / Viridis), redundant shape-and-color coding, and direct data labeling.
3. **Visualizing Uncertainty & Calibration:** Embedding 95% bootstrap confidence intervals, cohort drift ribbons, and 10/15-bin reliability diagrams directly into dashboard views so point estimates are never displayed without uncertainty bounds.
4. **Mandatory Provenance & Limitations Panels:** Engineering a persistent dashboard disclosure panel that displays source `license_class` metadata, small-$n$ statistical power limits, known selection biases, and the last-refresh timestamp.
5. **Pre-Fall Break Checkpoint & PS 11 Release Prep:** Auditing the MP 10 interpretability harness ahead of its Wed 25 Nov deadline and preparing the PS 11 ethics memo and prototype dashboard milestone (released Wed 25 Nov, due Fri 04 Dec before Dead Week).
