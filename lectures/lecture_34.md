# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../phases/phase_05/):** Evaluate & Deploy | **[Module 11](../modules/module_11/):** Presenting Results: Ethics & Data Storytelling | **Lecture 34:** Presenting Results: Ethics & Data Storytelling | Mon 16 Nov 2026 | [Last, *Technical Writing Essentials* (Chs. 1–3)](https://pressbooks.bccampus.ca/technicalwriting/)[cite: 42, 45] |

---

## Slide 1: Overview & Agenda — Presenting Results
### CIS 531/731 - Lecture 34
* **Technical Storytelling:** Structuring analytical reports and presentations for clarity, impact, and audience alignment.
* **Assigned Reading:** Last, *Technical Writing Essentials* (Chs. 1–3).
* **Audience Adaptation:** Translating complex algorithmic mechanics into actionable insights for diverse domains.
* **Ethical Data Presentation:** Avoiding misleading visual scales, cherry-picked metrics, and biased sample reporting.
* **Communicating Uncertainty:** Transparently presenting confidence intervals, error bounds, and model limitations to stakeholders.
* **Effective Documentation Structure:** Organizing technical findings following established writing essentials.

**Speaker Notes:**
Welcome to Phase 5, Module 11. Now that you have built, tuned, and evaluated your machine learning pipelines, the final hurdle is communicating those results. Today, we focus on technical storytelling and ethical data presentation. We will cover how to adapt complex data science concepts for non-technical stakeholders, structure your final reports using established technical writing frameworks, and ethically present uncertainty and limitations so your audience can make informed, safe decisions.

---

## Slide 2: Technical Storytelling
### Structuring the Analytical Narrative
* **The "So What?" Principle:** Every data science presentation must answer the operational "so what?" in the first two minutes. Do not make stakeholders wait until the end of a chronological pipeline walkthrough to find out if the model works.
* **Bottom-Line Up Front (BLUF):** Lead with your primary findings, key metrics, and recommended actions, then unpack the methodology and data provenance that support those conclusions.
* **Cohesive Computational Arguments:** Ensure that your exploratory figures, model metrics, and final dashboards all point toward answering the original operational decision or research question formulated in your proposal.

**Speaker Notes:**
Data scientists often fall into the trap of presenting their project chronologically—starting with data cleaning, moving to feature engineering, and finally revealing the model accuracy. Stakeholders do not care about your scrubbing pain; they care about the business or scientific impact. Lead with the Bottom-Line Up Front (BLUF). State the outcome, then prove it.

---

## Slide 3: Audience Adaptation
### Translating Mechanics into Actionable Insights
* **Stakeholder Mapping:** Differentiate between the engineering team (who needs to know about hyperparameter tuning and container digests) and the executive/domain team (who needs to know about false positive costs, ROI, and systemic risks).
* **Algorithmic Translation:** Replace hyper-specific ML jargon with domain-equivalent concepts. Instead of saying "we optimized the F1-score threshold," explain that "we balanced the risk of missing a fraudulent transaction against the cost of auditing legitimate ones."
* **Contextualizing Metrics:** Raw numbers are meaningless without a baseline. Always present your model's performance relative to the existing human baseline, the naive heuristic, or the prior system.

**Speaker Notes:**
Your HW 12 final report will be read by both technical peers and domain experts. When addressing the latter, you must translate algorithmic mechanics into actionable domain insights. A 92% accuracy rate means nothing in a vacuum. Is that a 5% improvement over the current system? Does it save 40 hours of manual review per week? Contextualize your metrics.

---

## Slide 4: Effective Documentation Structure
### Organizing Technical Findings
* **Executive Summary / Abstract:** A dense, one-paragraph summary of the problem, dataset, chosen architecture, primary metric outcome, and core limitation.
* **Methods and Architecture:** A clear, reproducible description of the pipeline. Must include software versions, exact data provenance, and invariant constraints.
* **Evaluation & Results:** The quantitative core. Includes gold-standard performance, ablation studies, and significance tests.
* **Ethics & Limitations:** A mandatory section detailing what the model *cannot* do, where the data is biased, and what safeguards are required.

**Speaker Notes:**
This structure directly mirrors your HW 12 deliverable requirements. Technical writing is not about suspense; it is about scanability and reproducibility. A reader should be able to jump directly to the Evaluation section and find your 95% confidence intervals, or jump to the Architecture section and find your component versions. 

---

## Slide 5: Ethical Data Presentation
### Intellectual Honesty in Reporting
* **The Completeness Principle:** You must report the performance of your system on the *entire* held-out gold standard, not just the cohorts or slices where the model performed well.
* **Disclosing Selection Bias:** If your training data or evaluation set suffers from survivorship bias, geographic bounding, or temporal degradation, it must be explicitly stated alongside the headline metrics.
* **Avoiding the Ecological Fallacy:** Do not claim that aggregate metric improvements guarantee equitable performance across all individual demographic or systemic subgroups.

**Speaker Notes:**
Ethical data science requires intellectual honesty. It is incredibly easy to hide poor model performance by burying the results of minority classes or filtering out noisy data streams post-hoc. If your model fails on a specific cohort, that is a finding, not a failure. Report it. Disclosing selection bias protects the downstream users of your system.

---

## Slide 6: Misleading Visual Scales & Cherry-Picking
### Defending Against Visual Manipulation
* **Truncated Axes (The Y-Axis Lie):** Starting a bar chart's y-axis at 0.85 instead of 0.0 to make a 2% improvement look like a 50% leap in performance. (Line charts tracking small deltas over time are exceptions, but must be clearly labeled).
* **Cherry-Picked Baselines:** Comparing your advanced neural network to a deliberately crippled baseline (e.g., a decision tree with a depth of 1) to inflate the perceived value of your architecture.
* **Dual/Secondary Axes:** Avoid plotting two entirely different metrics on the same chart with different scales (e.g., accuracy on the left, loss on the right) as it implies false correlations where lines cross. 

**Speaker Notes:**
As we transition into visual storytelling, beware of visual manipulation. Truncating the y-axis on a bar chart is a classic deceptive technique. If you are comparing model F1 scores, and Model A gets 0.82 and Model B gets 0.84, plotting them on an axis that starts at 0.80 makes Model B look twice as good. Use absolute scales, and never cherry-pick a weak baseline just to make your model look better.

---

## Slide 7: Communicating Uncertainty
### Error Bounds and Probabilistic Language
* **Confidence Intervals (CIs):** Never present a point estimate (e.g., "Accuracy is 87%") without its associated 95% bootstrap confidence interval or margin of error. 
* **Calibration Visualization:** Use reliability diagrams and Expected Calibration Error (ECE) to show stakeholders whether the model's confidence scores actually align with real-world probabilities.
* **Probabilistic Framing:** Train stakeholders to think in probabilities rather than binary truths. A model does not "know" a transaction is fraudulent; it assigns an 85% probability based on historical feature distributions.

**Speaker Notes:**
Stakeholders crave certainty, but data science is probabilistic. If you give a stakeholder a single number, they will treat it as a law of physics. By presenting 95% confidence intervals and calibration curves, you force the audience to acknowledge the noise in the system. This manages expectations and prevents catastrophic over-reliance on the model.

---

## Slide 8: Disclosing Model Limitations
### The Limitations Panel
* **Operational Boundaries:** Clearly define the environmental bounds where the model operates safely, and where it degrades (e.g., "This ASR model degrades significantly in environments with >15dB background noise").
* **Prompt Injection & Hallucination Risks:** For generative or RAG pipelines, explicitly document the risk of context-window poisoning, hallucinated citations, and prompt extraction attacks.
* **Mitigation Implementation:** Do not just list risks—document the concrete programmatic guardrails (e.g., output parsers, abstention thresholds, anomaly detectors) you built into the pipeline to catch them.

**Speaker Notes:**
Every operational dashboard and final report must include a Limitations Panel. This is not a boilerplate legal disclaimer; it is a technical spec sheet of the system's operational boundaries. If your RAG pipeline is vulnerable to prompt injection via retrieved web text, you must document it. More importantly, you must document the specific guardrails you implemented to mitigate that risk.

---

## Slide 9: Review and Refinement
### The Technical Writing Workflow
* **Iterative Drafting:** Write the methodology and architecture sections while you code. Do not wait until the night before the deadline to reconstruct your pipeline decisions from memory.
* **Peer & Advisor Review:** Subject your narratives to adversarial review. Ask peers to find logical leaps, missing assumptions, or unsupported claims in your draft.
* **Version Control for Documents:** Treat your reports and Markdown documentation with the same GitOps rigor as your Python code. Commit frequently, track changes, and use pull requests for major revisions.

**Speaker Notes:**
Good technical writing is an iterative process. As outlined in the *Technical Writing Essentials* reading, you should be drafting your methodology alongside your codebase. We enforce this through our GitOps workflows—your `REPORT.md` and `ethics_memo.md` should evolve with your repository. Rely on your team to red-team your claims before they reach the final milestone.

---

## Slide 10: Wrap-Up & Next Steps
### Transitioning to Documentation & Notebooks
* **Ethics is Continuous:** Ethical presentation is not a checkbox; it is the lens through which every table, chart, and metric must be evaluated.
* **Next Lecture (Wed 18 Nov — Lecture 35):** Documentation, Provenance & Notebook Presentation Standards. We will cover FAIR data principles and reproducible Jupyter notebook architectures.
* **Upcoming Lab (Fri 20 Nov — Lecture 36):** Dashboard Design & Limitations Panel Workshop. You will build the actual visual and ethical disclosures required for your term project.

**Speaker Notes:**
To summarize: technical storytelling requires you to adapt your message to your audience, lead with the bottom line, and defend your claims with transparent, ethically presented data that explicitly communicates uncertainty. On Wednesday, we will move from prose to code documentation, looking at how to make your Jupyter notebooks reproducible and compliant with FAIR data principles. Have a great afternoon.
