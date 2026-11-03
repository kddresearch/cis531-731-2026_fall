# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 5:** Evaluate & Deploy | **Module 10 `[N]`:** Interpret — Applying Models, Calibration & Multiple Testing | **Lectures 31-33** | Mon 09 Nov - Fri 13 Nov 2026 |

---

## Lecture 31: Interpret: Applying Models, Calibration & Multiple Testing (Mon 09 Nov)

1. **Prediction vs. Statistical Inference in Live & Held-Out Pipelines:** Distinguishing predictive optimization from defensible inferential claims about cohort-to-cohort cultural drift and speaker or demographic disparities (*ISLP*, Chs. 1–2 & 5).
2. **Evaluation Source Separation (Gold vs. Silver Pools):** Enforcing a strict boundary between graded evaluation metrics computed on the human-adjudicated gold standard (`gold_adjudicated.jsonl`) and advisory stability or power analyses run on the 1,000-chunk weak-supervision silver pool (`grading_eligible=False`).
3. **Paired System Comparison (Paired Bootstrap & McNemar's Test):** Testing whether a retrieval-augmented or learned-convolution model significantly outperforms a fixed baseline using paired index resampling ($B \ge 10,000$) and exact binomial McNemar $2 \times 2$ contingency tables on discordant predictions.
4. **Family-Wise Error Rate (FWER) vs. False Discovery Rate (FDR):** Understanding why testing multiple shot counts ($k \in \{0, 1, 3, 5, 8\}$), retrieval depths ($k \in \{3, 5, 10\}$), and cohort slices ($m \ge 6$ comparisons) inflates Type I false-positive errors when raw $p$-values are left unadjusted (*ISLP*, Ch. 13).
5. **Benjamini–Hochberg Step-Up Control:** Pre-specifying a hypothesis family of at least $m \ge 6$ comparisons prior to inspection and applying the Benjamini–Hochberg FDR procedure at $\alpha = 0.05$ to bound false discoveries across ablation tables.

---

## Lecture 32: Model Metrics, Calibration & Scoring (Wed 11 Nov)

1. **Classification Averaging Strategies & Imbalance Counterexamples:** Deriving micro-F1, macro-F1, and weighted-F1 directly from confusion matrices (`scikit-learn` Metrics & Scoring) and constructing explicit class-imbalance counterexamples where raw accuracy and macro-F1 rank two classifiers in opposite orders.
2. **Ranked Retrieval & ASR Transcription Scoring:** Formulating Precision@$k$, Recall@$k$, Mean Reciprocal Rank (MRR), nDCG@$k$, and NIST OpenASR Word Error Rate ($\text{WER} = (S + D + I) / N_{\text{ref}}$, including why high insertion counts $I$ allow $\text{WER}$ to exceed $100\%$).
3. **Contract-Checked Scoring Harnesses:** Engineering a deterministic `evaluate(model, X, y)` package with programmatic pre- and post-condition contracts verifying that bounded metrics lie in $[0, 1]$ and confusion-matrix cells sum exactly to sample size $n$.
4. **Probabilistic Calibration & Reliability Diagrams:** Diagnosing overconfident neural and LLM probability estimates using reliability diagrams and Expected Calibration Error (ECE) evaluated across both 10-bin and 15-bin partitions to measure bin-width sensitivity.
5. **Post-Hoc Probability Calibration:** Fitting temperature scaling and isotonic regression on validation splits (`scikit-learn` calibration module) to align predicted confidence scores with empirical accuracy prior to downstream decision thresholding.

---

## Lecture 33: Interpretation & Error Analysis Lab; Wrap-Up (Fri 13 Nov)

1. **Global Permutation Feature Importance:** Quantifying model sensitivity across tabular, lexical, and embedding features by running at least 30 permutation repeats on held-out evaluation sets and reporting mean metric degradation with confidence intervals.
2. **Local Retrieval-Based Explanations:** Conducting granular error analysis on at least 10 misclassified gold-standard examples by inspecting their top-$k$ nearest neighbors in the FAISS embedding space (`Sentence Transformers` semantic search) and diagnosing boundary failures.
3. **Small-$n$ Power & Stability Curves on the Silver Pool:** Subsampling the 1,000-chunk weak-supervision silver pool across $n \in \{25, 50, 100, 250, 500, 1000\}$ to chart 95% confidence-interval width ($\propto 1/\sqrt{n}$) and quantify the minimum effect size $\delta$ that an evaluation set of $n \le 50$ can and cannot resolve.
4. **Cohort-Stratified Error & Disparity Auditing:** Disaggregating precision, recall, calibration, and WER across release decades (VDB track) or broadcast event-time windows (ASR track) to surface slice-specific performance drops.
5. **MP 9 Wrap-Up & MP 10 Launch:** Finalizing the `mp9-submission` gold/silver and convolution artifacts (due Mon 16 Nov) and initializing the `mp10-submission` interpretability and metrics harness (due Wed 25 Nov).
