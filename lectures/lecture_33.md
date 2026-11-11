# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../../phases/phase_05/):** Evaluate & Deploy | **[Module 10](../modules/module_10/):** Interpret: Applying Models, Calibration & Multiple Testing | **Lecture 33:** Interpretation & Error Analysis Lab; Wrap-Up | Fri 13 Nov 2026 | [scikit-learn *Metrics & Probability Calibration Guide*](https://scikit-learn.org/stable/modules/model_evaluation.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) |

---

## Slide 1: Lecture Overview & Agenda
### CIS 531/731 - Lecture 33
* **Core Focus:** Hands-on error analysis, probability calibration implementation, and embedding space diagnostics.
* **Assigned Reading:** [scikit-learn *Metrics & Probability Calibration Guide*](https://scikit-learn.org/stable/modules/model_evaluation.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)
* **Systematic Error Dissection:** Pinpointing false positives and false negatives in analytical pipelines.
* **Probability Calibration Lab:** Writing code for Platt scaling and isotonic regression in Python.
* **Milestone Alignment:** Reconciling evaluation findings for upcoming MP 9 submission and MP 10 release.

**Speaker Notes:**
Good afternoon, everyone. Welcome to Lecture 33 and our Module 10 hands-on lab. Today we transition from theory to practice. We will systematically inspect model errors, implement probability calibration from scratch using scikit-learn, audit semantic retrieval drift, and review our progress ahead of the Milestone 9 deadline.

---

## Slide 2: Systematic Error Dissection
### Isolating Model Failure Modes
* **[Confusion Matrix Inspection]:** Programmatically isolating cross-class confusions to identify systematic feature overlap.
* **[Residual Analysis in Regression]:** Plotting prediction errors against target values to detect heteroscedasticity or non-linear bias.
* **[Worst-Case Instance Auditing]:** Inspecting the top 10 highest-loss samples to uncover data labeling errors or missing features.
* **[Slicing Data by Subpopulations]:** Checking metric consistency across distinct data slices to ensure equitable performance.

**Speaker Notes:**
Aggregate metrics hide structural flaws. In our first lab exercise today, we will write code to slice our evaluation dataset, isolate high-residual predictions, and identify whether our classification errors stem from noisy labels or genuine feature ambiguity.

---

## Slide 3: Probability Calibration Lab
### Implementing Platt Scaling and Isotonic Regression
* **[The Calibration Problem]:** Observing uncalibrated confidence distributions in tree-based models or deep classifiers.
* **[Platt Scaling (`CalibratedClassifierCV`)]:** Fitting a secondary logistic regression model on decision outputs to straighten reliability curves.
* **[Isotonic Regression]:** Applying non-parametric piecewise constant functions for flexible probability mapping.
* **[Evaluating Calibration Gains]:** Comparing Brier scores before and after calibration across validation folds.

**Speaker Notes:**
Next, we will implement probability calibration in Python. Using scikit-learn's `CalibratedClassifierCV`, we will wrap an uncalibrated classifier and compare how Platt scaling versus isotonic regression alters our reliability diagrams and Brier scores.

---

## Slide 4: Embedding Space Diagnostics
### Auditing Semantic Search and Retrieval Drift
* **[Cosine Similarity Distributions]:** Analyzing the spread of similarity scores between queries and relevant versus irrelevant documents.
* **[Retrieval Drift Detection]:** Monitoring shifts in embedding space density when applying models to out-of-distribution corpora.
* **[Precision@K and MRR Computation]:** Writing custom evaluation loops to score semantic search retrieval outputs against gold standards.
* **[Visualizing Latent Spaces]:** Using dimensionality reduction (PCA/UMAP) to inspect cluster separation in vector databases.

**Speaker Notes:**
For those working with NLP and retrieval pipelines, our third exercise focuses on embedding space diagnostics. We will compute MRR and Precision@K manually to understand how well our semantic search model separates relevant items from noise.

---

## Slide 5: Module 10 Wrap-Up
### Consolidating Interpretation and Hypothesis Testing
* **[Model Interpretation Summary]:** Reconciling predictive performance with feature validity and epistemic limits.
* **[False Discovery Rate Control]:** Reviewing the role of the Benjamini-Hochberg procedure when conducting mass feature evaluations.
* **[Epistemic Humility]:** Acknowledging that metrics and calibrations only reflect historical data distributions, not absolute truth.
* **[The Evaluation Lifecycle]:** Closing the loop from training to calibration, testing, and production monitoring.

**Speaker Notes:**
As we wrap up Module 10, remember that model evaluation is not a single checklist step—it is an ongoing process of skepticism and verification. By combining multiple hypothesis testing, rigorous calibration, and error analysis, we build trustworthy systems.

---

## Slide 6: Milestone 9 & 10 Transition
### Status Check and Delivery Expectations
* **[Milestone 9 Submission]:** Finalizing evaluation code, calibration metrics, and performance reports due this week.
* **[Milestone 10 Preview]:** Introducing the final module's focus on deployment architectures, serving frameworks, and monitoring.
* **[Code Quality & Repository Hygiene]:** Ensuring all lab scripts and analysis notebooks are cleanly committed to lab Git repositories.
* **[Office Hours & Support]:** Reviewing remaining troubleshooting channels for pipeline debugging before submission.

**Speaker Notes:**
Let's take a brief moment to check our project pacing. Milestone 9 is due shortly, wrapping up our evaluation and interpretation deliverables. Milestone 10 will follow immediately, shifting our focus toward deployment and production serving.

---

## Slide 7: Lab Exercise 1 — Error Slicing & Debugging
### Practical Coding Task: Residual Analysis
* **[Task Objective]:** Write a Python script to compute per-sample error, sort by residual magnitude, and plot the worst-performing data slices.
* **[Provided Utilities]:** Pre-loaded data splits, baseline model weights, and evaluation helper functions.
* **[Expected Output]:** A structured error-analysis report highlighting the top three feature clusters associated with model failure.
* **[Peer Discussion]:** Comparing error patterns across different hyperparameter configurations.

**Speaker Notes:**
For our first hands-on block today, open up the provided notebook and complete Exercise 1 on error slicing. Focus on identifying whether your model's errors are randomly distributed or concentrated in specific regions of the feature space.

---

## Slide 8: Lab Exercise 2 — Calibration Curves
### Practical Coding Task: Reliability Diagrams
* **[Task Objective]:** Generate reliability diagrams for an uncalibrated gradient boosting model and re-plot after applying Platt scaling.
* **[Metrics to Track]:** Brier score loss before and after calibration.
* **[Validation Check]:** Ensuring calibration is fit exclusively on validation folds to prevent data leakage.
* **[Deliverable]:** Annotated calibration curves included in your lab submission repository.

**Speaker Notes:**
In Exercise 2, you will build reliability diagrams from scratch. Verify that your Brier score decreases after calibration and ensure you are using strict cross-validation splits to avoid leaking test labels into your calibration mapping.

---

## Slide 9: Open Lab & Troubleshooting
### Collaborative Debugging and Code Review
* **[Staff Support]:** TAs and instructors circulating to assist with scikit-learn pipeline errors and embedding metric calculations.
* **[Repository Commits]:** Pushing incremental lab solutions to your assigned student repository branches.
* **[Peer Code Review]:** Collaborating with lab partners to audit calibration curves and error analysis summaries.
* **[Questions & Edge Cases]:** Addressing specific metric anomalies encountered in custom datasets.

**Speaker Notes:**
The remaining lab time is open for collaborative coding, TA support, and repository commits. Make sure your calibration scripts and error analysis reports are fully documented before you leave today.

---

## Slide 10: Summary & Looking Ahead to Module 11
### Closing Thoughts and Next Steps
* **[Key Takeaways]:** Error analysis reveals hidden assumptions; calibration ensures trustworthy probabilities; rigorous metrics prevent false confidence.
* **[Readings for Next Module]:** Watch for announcements regarding Module 11 reading assignments on model deployment and monitoring.
* **[Have a Great Weekend]:** Complete your lab commits, finish up Milestone 9, and we will see you Monday for Module 11!

**Speaker Notes:**
To summarize Module 10: we've covered interpretation, multiple testing, calibration, and hands-on error analysis. Complete your lab commits, finish up your milestone deliverables, and have a fantastic weekend. See you Monday!
