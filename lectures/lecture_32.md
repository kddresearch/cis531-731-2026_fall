# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../../phases/phase_05/):** Evaluate & Deploy | **[Module 10](../modules/module_10/):** Interpret: Applying Models, Calibration & Multiple Testing | **Lecture 32:** Model Metrics, Calibration & Scoring | Wed 11 Nov 2026 | [scikit-learn Documentation: *“Metrics and Scoring: Quantifying the Quality of Predictions”*](https://scikit-learn.org/stable/modules/model_evaluation.html) |

---

## Slide 1: Lecture Overview & Agenda
### CIS 531/731 - Lecture 32
* **Core Focus:** Evaluating model prediction quality, probability calibration, and scoring metric selection in analytics pipelines.
* **Assigned Reading:** [scikit-learn Documentation: *“Metrics and Scoring: Quantifying the Quality of Predictions”*](https://scikit-learn.org/stable/modules/model_evaluation.html)
* **Beyond Raw Accuracy:** Precision, recall, F1-score, and ROC-AUC under class-imbalanced conditions.
* **Probability Calibration:** Aligning model-output confidence scores with true empirical likelihoods.
* **Pipeline Evaluation:** Assessing classification thresholds and semantic search retrieval metrics.

**Speaker Notes:**
Good afternoon, everyone. Welcome to Lecture 32 of CIS 531/731. Today we move beyond simple training loss and raw accuracy to examine rigorous model evaluation. We will explore why default probability outputs are often miscalibrated and how to select metrics that reflect real-world analytical and operational constraints.

---

## Slide 2: Quantifying Prediction Quality
### Limitations of Raw Accuracy in Analytics
* **The Accuracy Paradox:** Why high overall accuracy fails as a metric under severe class imbalance (e.g., 99% negative class baselines).
* **Precision & Recall Trade-Offs:** Balancing false positives (precision) against false negatives (recall) depending on domain tolerance.
* **F1-Score & Harmonic Mean:** Combining precision and recall into a single scalar metric for balanced performance tracking.
* **ROC-AUC & Precision-Recall Curves:** Evaluating ranking performance across all possible classification decision thresholds.

**Speaker Notes:**
Accuracy assumes uniform costs for errors and balanced classes—assumptions that almost never hold true in real-world data science applications. Whether we are detecting fraud or retrieving medical records, we must use precision, recall, and ROC-AUC to understand where our models fail.

---

## Slide 3: Probability Calibration
### Bridging Model Confidence and Empirical Likelihood
* **Well-Calibrated Models:** Ensuring that when a model predicts a positive class with 80% confidence, it is correct 80% of the time in expectation.
* **Overconfident vs. Underconfident Models:** Diagnosing distorted probability distributions common in deep networks and boosted trees.
* **Reliability Diagrams (Calibration Curves):** Visualizing the discrepancy between predicted probability bins and actual empirical outcomes.
* **Platt Scaling & Isotonic Regression:** Parametric and non-parametric post-processing techniques used to map raw model scores to calibrated probabilities.

**Speaker Notes:**
A model can rank instances correctly (high AUC) while outputting completely distorted probabilities. Probability calibration is mandatory whenever model scores feed into downstream decision engines where thresholds dictate automated actions.

---

## Slide 4: Scoring Metrics in `scikit-learn`
### Leveraging Built-In Evaluation Frameworks
* **The `sklearn.metrics` API:** Standardized interfaces for classification, regression, and clustering evaluation.
* **Custom Scoring Functions:** Passing custom evaluation callables into `cross_val_score` and `GridSearchCV`.
* **Multiclass and Multi-Label Extensions:** Managing macro-averaging, micro-averaging, and weighted metrics across complex response structures.
* **Avoiding Data Leakage:** Ensuring evaluation metrics are computed strictly on held-out validation or test folds.

**Speaker Notes:**
Scikit-learn provides an exhaustive suite of scoring functions. However, developers must take care to choose the correct average parameter for multiclass tasks and ensure that evaluation pipelines remain strictly isolated from training loops to prevent leakage.

---

## Slide 5: Cost-Sensitive Decision Thresholding
### Aligning Thresholds with Asymmetric Real-World Costs
* **Default 0.5 Threshold Fallacy:** Why the default classification boundary is rarely optimal when false positive and false negative costs differ.
* **Cost Matrices & Expected Value:** Quantifying the financial or operational penalty of each error type.
* **Youden's J Statistic & F-Beta Optimization:** Mathematically deriving optimal decision thresholds from ROC and Precision-Recall curves.
* **Operational Constraints:** Adjusting thresholds dynamically based on downstream resource limits (e.g., human reviewer capacity).

**Speaker Notes:**
In production pipelines, the decision threshold is a business parameter, not a fixed mathematical constant. Shifting the threshold allows us to adapt a single trained model to changing operational costs without retraining weights.

---

## Slide 6: Evaluating Retrieval Pipelines
### Assessing Semantic Search and Information Retrieval
* **Relevance Judgments (Gold Standards):** Defining binary or graded relevance scores for query-document pairs.
* **Precision@K and Recall@K:** Measuring retrieval accuracy restricted to the top $K$ returned results.
* **Mean Reciprocal Rank (MRR):** Evaluating systems based on the position of the first relevant item retrieved.
* **Normalized Discounted Cumulative Gain (NDCG):** Accounting for graded relevance and position bias in ranked search lists.

**Speaker Notes:**
When evaluating vector embeddings and semantic search pipelines, standard classification metrics fall short. We rely on ranking metrics like MRR and NDCG to measure whether the most relevant documents appear at the very top of our retrieval lists.

---

## Slide 7: Cross-Validation Strategies for Evaluation
### Ensuring Generalizability Across Resampled Folds
* **K-Fold & Stratified K-Fold:** Preserving class proportions across validation splits in imbalanced classification tasks.
* **Group K-Fold:** Preventing data leakage when instances share underlying cluster or entity identifiers.
* **Time Series Split:** Respecting temporal ordering during cross-validation to prevent future-state leakage in sequential data.
* **Bootstrap Validation:** Estimating confidence intervals for performance metrics via resampling with replacement.

**Speaker Notes:**
A metric is only as good as the validation strategy behind it. If your data contains groups or temporal dependencies standard random splitting will cause severe optimistic bias in your reported evaluation scores.

---

## Slide 8: Diagnostic Error Analysis
### Moving Beyond Aggregate Scalars to Inspect Failures
* **Confusion Matrix Deep Dive:** Isolating specific confusion patterns between confusable categories.
* **Worst-Case Error Inspection:** Manually reviewing instances with the highest residual error or lowest calibration confidence.
* **Slicing Analysis:** Evaluating performance disparities across demographic, spatial, or temporal data slices.
* **Feature Attribution Alignment:** Checking whether models make correct predictions for the right reasons using feature importance diagnostics.

**Speaker Notes:**
Aggregate numbers like F1 or AUC hide localized failures. Rigorous data science requires systematic error analysis—inspecting the exact samples where the model fails catastrophically before approving it for deployment.

---

## Slide 9: Practical Implementation & Best Practices
### Operationalizing Metrics in Production Code
* **Logging & Monitoring Metrics:** Tracking evaluation drift between training distributions and live production data.
* **Automated Testing for Models:** Implementing assertion checks on minimum acceptable metric floors in CI/CD pipelines.
* **Reproducibility & Random Seeds:** Locking down data splits and initialization states to ensure metric stability.
* **Documentation Standards:** Reporting confidence intervals and evaluation parameters alongside primary score tables.

**Speaker Notes:**
As models graduate from notebooks to production pipelines, metric monitoring becomes an ongoing engineering requirement. Automated checks ensure that data drift or pipeline updates do not silently degrade model performance.

---

## Slide 10: Summary & Upcoming Lab Transition
### Consolidating Evaluation and Preparing for Lab 33
* **Key Takeaways:** Metrics must align with business costs; probabilities must be calibrated; retrieval systems require specialized ranking measures.
* **Readings for Next Time:** Review scikit-learn probability calibration guides and Sentence Transformers semantic search documentation ahead of Friday's lab.
* **Module Transition:** In Friday's lab (Lecture 33), we will implement Platt scaling, inspect embedding space drift, and address pending MP 9 milestones.

**Speaker Notes:**
To summarize: evaluating models is a multi-dimensional engineering discipline requiring careful metric selection, probability calibration, and rigorous error analysis. Bring your notebooks on Friday as we put these calibration and diagnostic techniques into practice. See you then!
