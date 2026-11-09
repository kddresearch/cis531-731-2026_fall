# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../../phases/phase_05/):** Evaluate & Deploy | **Module 10:** Interpret: Applying Models, Calibration & Multiple Testing | **Lectures 31-33** | Mon 09 Nov - Fri 13 Nov 2026 | [James et al., *ISLP* (2023)](https://www.statlearning.com/resources-python); [scikit-learn *Metrics and Scoring*](https://scikit-learn.org/stable/modules/model_evaluation.html); [Sentence Transformers *Semantic Search*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)[span_1](start_span)[span_1](end_span) |

---

## [Lecture 31: Interpret: Applying Models, Calibration & Multiple Testing](../../lectures/lecture_31.md) (Mon 09 Nov 2026)

1. **Model Interpretation Foundations:** Bridging predictive performance and explanatory validity in high-dimensional analytical pipelines.
2. **Multiple Hypothesis Testing:** Understanding the statistical hazards of family-wise error rates when performing concurrent significance tests across model features.
3. **The Benjamini–Hochberg Procedure:** Controlling the False Discovery Rate (FDR) in large-scale feature evaluation and retrieval ranking tasks.
4. **Resampling and Validation Strategies:** Applying rigorous cross-validation and resampling techniques from ISLP chapters to ensure generalizability[span_2](start_span)[span_2](end_span).
5. **Epistemic Humility in Modeling:** Recognizing the limits of automated inference when dealing with sparse or non-stationary data distributions.
* **Assigned Reading:** [James et al., *An Introduction to Statistical Learning with Applications in Python* (ISLP, 2023), Chs. 1–2, 4, 5, & 13](https://www.statlearning.com/resources-python)[span_3](start_span)[span_3](end_span)

---

## [Lecture 32: Model Metrics, Calibration & Scoring](../../lectures/lecture_32.md) (Wed 11 Nov 2026)

1. **Quantifying Prediction Quality:** Moving beyond raw accuracy to examine precision, recall, F1-score, and ROC-AUC under class-imbalanced conditions.
2. **Probability Calibration:** Ensuring that model-output confidence scores accurately reflect true empirical likelihoods.
3. **Scoring Metrics in `scikit-learn`:** Leveraging built-in evaluation tools to quantify classification and regression performance rigorously[span_4](start_span)[span_4](end_span).
4. **Cost-Sensitive Decision Thresholding:** Adjusting classification boundaries based on asymmetric business or research error costs.
5. **Evaluating Retrieval Pipelines:** Assessing the alignment between semantic search outputs and gold-standard relevance judgments.
* **Assigned Reading:** [scikit-learn Documentation: *“Metrics and Scoring: Quantifying the Quality of Predictions”*](https://scikit-learn.org/stable/modules/model_evaluation.html)[span_5](start_span)[span_5](end_span)

---

## [Lecture 33: Interpretation & Error Analysis Lab; Wrap-Up](../../lectures/lecture_33.md) (Fri 13 Nov 2026)

1. **Systematic Error Dissection:** Inspecting false positives and false negatives to uncover systemic failure modes in feature extraction.
2. **Probability Calibration Lab:** Implementing Platt scaling and isotonic regression in Python to calibrate pipeline confidence scores.
3. **Embedding Space Diagnostics:** Using semantic search similarity distributions to audit retrieval drift[span_6](start_span)[span_6](end_span).
4. **Module 10 Wrap-Up:** Consolidating model interpretation, calibration, and hypothesis testing principles ahead of Module 11.
5. **Milestone Transition:** Reconciling evaluation findings for upcoming MP 9 submission and MP 10 release.
* **Assigned Reading:** [scikit-learn *Metrics & Probability Calibration Guide*](https://scikit-learn.org/stable/modules/model_evaluation.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)[span_7](start_span)[span_7](end_span)