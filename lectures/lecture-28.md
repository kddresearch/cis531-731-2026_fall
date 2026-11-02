# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 5:** Evaluate & Deploy | **Module 9:** Evaluating Models: Inferential Statistics & ASR Evaluation | **Lecture 28:** Evaluating Models: Inferential Statistics & Bootstrap CIs | Mon, Nov 02, 2026 |

---

## Slide 1: Welcome to Phase 5 — Evaluating Models & Inferential Statistics
### CIS 531/731 - Lecture 28
* **The Transition:** Moving from exploratory modeling (Phase 4) to rigorous inferential evaluation and deployment (Phase 5).
* **Prediction vs. Inference:** Understanding the fundamental difference between building a model to maximize accuracy versus building a model to understand causal relationships.
* **The Danger of Point Estimates:** Why reporting a single Macro-F1 score or Word Error Rate (WER) without a confidence interval is mathematically invalid.
* **Resampling Methods:** Introducing the Non-Parametric Bootstrap as our primary tool for quantifying uncertainty without assuming Gaussian distributions.
* **Module 9 Roadmap:** Today covers statistical foundations (ISLP Chs. 1, 5, 12); Wednesday covers the NIST OpenASR evaluation protocol; Friday is our Gold-Standard Construction Lab.

**Speaker Notes:**
Welcome to Phase 5. Up to this point, we have focused heavily on prediction—building RAG pipelines and generational convolution models to squeeze out the highest possible accuracy on our text and audio datasets. Today, we shift our focus to inference and evaluation. If your classification model achieves an F1 score of 0.82 on a test set of 50 examples, is it genuinely better than a baseline model that scores 0.79? Without inferential statistics, you cannot answer that question. Today, we are going to cover the mathematical tools—specifically resampling methods like the Bootstrap—that allow us to put rigorous confidence intervals around our metrics, transitioning our work from a programming exercise into defensible data science.

---

## Slide 2: Prediction vs. Inference
### Two Distinct Modeling Goals
* **Prediction ($Y = \hat{f}(X)$):** The goal is to accurately forecast the output variable $Y$ based on the input features $X$. The internal mechanics of $\hat{f}$ (the model) can be a "black box" as long as the predictions are accurate.
* **Inference ($Y = f(X) + \epsilon$):** The goal is to understand the true relationship between $X$ and $Y$. We want to know *which* specific features are most important, the direction of their effect, and the magnitude of that effect.
* **The Tradeoff:** Highly flexible, non-linear models (like Deep Neural Networks) excel at prediction but are extremely difficult to interpret. Rigid, linear models (like Logistic Regression) are highly interpretable for inference but may sacrifice predictive power.

**Speaker Notes:**
Before we evaluate a model, we have to know what we are evaluating it *for*. In data science, we generally build models for one of two reasons: prediction or inference. If you are building a real-time recommendation engine, you might only care about prediction—you want the most accurate model possible, even if it's a massive, uninterpretable neural network. But if you are trying to prove a generational shift in cultural tropes, as we are doing in our Track 2 VDB projects, you need inference. You need to be able to say, "The 'doomed youth' trope is statistically more prevalent in the 2020s than the 1990s." You cannot make that claim with a black-box model; you need a model that allows you to isolate and quantify the effect of specific features. 

---

## Slide 3: The Danger of Point Estimates
### Why a Single Metric is Never Enough
* **The Point Estimate:** A single number calculated from a sample dataset (e.g., a test set accuracy of 85%, or a mean difference of 2.4).
* **Sampling Variance:** Every dataset is a finite sample drawn from a larger population. If you drew a different sample of the same size, your model's accuracy would fluctuate.
* **The Illusion of Certainty:** Reporting a point estimate without acknowledging sampling variance implies that the metric is the absolute, true parameter of the population.
* **The Requirement:** We must report a range of plausible values (a Confidence Interval) to capture the uncertainty inherent in our finite sample size.

**Speaker Notes:**
One of the most common mistakes in junior data science portfolios is reporting a point estimate as if it is an absolute truth. If you tell me your new ASR transcription model achieved a Word Error Rate of 12.5% on a test set of 20 audio clips, that is a point estimate. It is just one number. Because your test set only contains 20 clips, that number is highly sensitive to the specific clips that were chosen. If we swapped out 5 of those clips for different ones, your WER might jump to 18% or drop to 9%. By reporting only 12.5%, you are masking that underlying volatility. In this course, a single metric is mathematically invalid unless accompanied by a measure of uncertainty.

---

## Slide 4: Introduction to Resampling Methods
### Estimating Variability Without New Data
* **The Problem:** To measure the variance of our model's performance, we ideally need to draw hundreds of new, independent test sets from the population—which is usually impossible or prohibitively expensive.
* **Resampling Methods:** Statistical techniques that repeatedly draw samples from the *original* dataset and refit the model (or recalculate the metric) on each new sample to estimate variability.
* **Cross-Validation (CV):** Used primarily to estimate the test error associated with a given statistical learning method (model selection and hyperparameter tuning).
* **The Bootstrap:** Used primarily to provide a measure of accuracy (standard error or confidence interval) for a parameter estimate or a specific statistical learning method.

**Speaker Notes:**
If we want to know how much our F1 score will fluctuate, the gold standard would be to gather 1,000 brand new test datasets, evaluate our model on all of them, and plot the distribution of the scores. But data collection is expensive; we almost never have that luxury. This is where resampling methods come in. Instead of gathering new data from the real world, we generate new datasets by repeatedly sampling from the data we *already have*. The two most common methods you will use in this program are Cross-Validation, which we use to tune hyperparameters and estimate out-of-sample error, and the Bootstrap, which we will use today to build confidence intervals around our performance metrics.

---

## Slide 5: The Non-Parametric Bootstrap
### Simulating the Population from the Sample
* **The Mechanism:** Given an original dataset $Z$ of size $n$, we generate $B$ new bootstrap datasets ($Z^{*1}, Z^{*2}, \dots, Z^{*B}$) by sampling $n$ observations from $Z$ *with replacement*.
* **Sampling with Replacement:** An individual observation from the original dataset can appear multiple times in a single bootstrap dataset, or not at all.
* **The Core Assumption:** If the original sample is representative of the population, then sampling with replacement from the sample mimics the process of sampling from the original population.
* **Estimating Variance:** We calculate our metric (e.g., F1 score) on all $B$ bootstrap datasets. The standard deviation of those $B$ estimates serves as an estimate of the true standard error.

**Speaker Notes:**
The Bootstrap is an incredibly powerful, elegant tool. Let's say you have an evaluation set of 100 radio caller transcripts. To run a bootstrap, you randomly draw one transcript from that set, record its ID, and *put it back*. You do this 100 times to create your first bootstrap dataset. Because you are sampling with replacement, some transcripts will be selected two or three times, and about 37% of them won't be selected at all. You then calculate your F1 score on that new dataset. You repeat this entire process $B$ times—typically at least 1,000 times. By looking at the spread of those 1,000 different F1 scores, we can accurately estimate the true variance of our model's performance without making any assumptions about normal distributions.

---

## Slide 6: Constructing Bootstrap Confidence Intervals (CIs)
### Moving from Standard Error to Percentiles
* **Normal Approximation CI:** If the bootstrap distribution is roughly symmetric and normal, we can use the bootstrap standard error ($\text{SE}_{boot}$) to construct a 95% CI: $[\hat{\theta} - 1.96 \cdot \text{SE}_{boot}, \hat{\theta} + 1.96 \cdot \text{SE}_{boot}]$.
* **The Percentile Bootstrap CI:** A more robust method that does not assume normality. We simply sort our $B$ bootstrap estimates from lowest to highest.
* **Calculating the Percentiles:** For a 95% Confidence Interval, we find the values at the 2.5th percentile and the 97.5th percentile of the sorted distribution.
* **The Interpretation:** We are 95% confident that the true population parameter falls within this interval. If the interval for a difference between two models includes $0.0$, the difference is not statistically significant.

**Speaker Notes:**
Once we have our 1,000 bootstrap estimates, how do we turn them into a confidence interval? The most robust and straightforward way is the Percentile Method. We simply take our 1,000 F1 scores and sort them from worst to best. For a 95% confidence interval, we chop off the bottom 2.5% (the 25 lowest scores) and the top 2.5% (the 25 highest scores). The remaining range is our confidence interval. This is particularly crucial when comparing two models. If Model A beats Model B by 3 points on the original test set, we bootstrap the *difference* between their scores. If the 95% confidence interval for that difference crosses zero—meaning sometimes Model B actually wins in the resamples—we cannot mathematically claim that Model A is superior. 

---

## Slide 7: Applying the Bootstrap to Generational Drift (Module 8 Link)
### Quantifying Temporal Shift
* **The Context:** In Lab 8, we applied fixed 1-D convolutional kernels to track the prevalence of cultural tropes across ordered generational cohorts.
* **The Problem:** If a trope appears in 12% of chunks in the 1980s cohort ($N=45$) and 21% in the 1990s cohort ($N=300$), is that 9% increase genuine cultural drift or small-sample noise?
* **Stratified Cohort Bootstrapping:** We must resample chunks with replacement *within each specific cohort bin* $c$, maintaining the exact sample size $N_c$ for each bin in every bootstrap replicate.
* **Visualizing Uncertainty:** By calculating the convolved trajectory for all $B=1000$ replicates, we can plot a 95% confidence ribbon around our trend line, visually proving whether the drift is statistically distinguishable from zero.

**Speaker Notes:**
Let's connect this directly to the generational convolutions we built in Module 8. You are tracking the "doomed youth" trope across decades. You see a spike in the 1990s. But look at your sample sizes: maybe you only have 45 documents from the 1980s. A small fluctuation in those 45 documents can create a massive artificial spike in your percentages. To prove that the drift is real, we apply the bootstrap. Crucially, we must use a *stratified* bootstrap: we resample the 1980s documents only from the 1980s bin, keeping the sample size at 45, and we resample the 1990s documents only from the 1990s bin, keeping the size at 300. When we plot the 95% confidence ribbon around our trendline, we can instantly see if the structural drift is larger than the sampling noise.

---

## Slide 8: Limitations and Caveats of the Bootstrap
### When Resampling Fails
* **Extreme Sparsity:** The bootstrap cannot create information that does not exist in the original sample. If a specific class or trope never appears in a cohort bin, every bootstrap resample will also have zero occurrences.
* **Dependent Data:** The standard bootstrap assumes observations are independent and identically distributed (i.i.d.). It will fail on tightly coupled time-series data or spatial data where neighboring points are highly correlated (unless specialized block-bootstrap methods are used).
* **Computational Cost:** Refitting a complex model (like training a deep neural network from scratch) $B=1000$ times is computationally prohibitive.
* **The Solution for Expensive Models:** We bootstrap the *evaluation predictions* on the frozen test set, not the training process itself.

**Speaker Notes:**
The bootstrap is a foundational tool, but you must know its limits. First, the bootstrap cannot magically invent data. If you have a decade in your dataset where a specific trope was never mentioned, resampling that decade with replacement will just give you a bunch of zeros. The confidence interval will be exactly zero, which falsely implies absolute certainty rather than a lack of data. Second, standard bootstrapping assumes your data points are independent. If you are analyzing a continuous audio stream where chunk 2 is highly dependent on chunk 1, a naive bootstrap breaks the temporal structure. Finally, computational cost. You cannot train a PyTorch model 1,000 times for a homework assignment. In practice, we train the model once, generate predictions on the test set, and then bootstrap the *evaluation metric* by resampling those paired predictions and ground-truth labels.

---

## Slide 9: Preparing for Gold-Standard Evaluation (MP 9 & HW 12)
### The Role of Human-Annotated Ground Truth
* **The Necessity of Ground Truth:** You cannot bootstrap a performance metric if you do not have definitive, correct labels to evaluate against.
* **The Gold Standard Deficit:** Many datasets (especially live ASR streams or unlabeled textual corpora) lack ground-truth labels for complex, nuanced concepts like literary tropes.
* **INV-17 Mandate:** Human gold-standard labels (`source=gold`) must be assigned by human students, never by an LLM or GTA.
* **The Annotation Cap (CIS 531/731 Rule):** To prevent burnout, individual homework annotation in MP 9 is capped at $\le 50$ objects or 2 hours. The final pooled term-project gold sets (HW 12) must contain exactly 50–200 labeled examples.

**Speaker Notes:**
Inferential statistics and bootstrapped confidence intervals are only as good as the labels you are measuring against. If you are comparing your RAG classifier to a baseline, you need to know what the *actual* correct answer is for your test set. For many of your term projects, especially those tracking nuanced cultural tropes in unlabeled lyrics or radio streams, that ground truth does not exist yet. You have to build it. Per our course invariant, INV-17, gold-standard labels must be generated by you, the human students, not by asking ChatGPT. On Friday, we will conduct our Gold-Standard Construction Lab. To protect your time, we enforce a strict cap: you will annotate a maximum of 50 examples, taking no more than 2 hours, which will serve as the mathematical foundation for your final evaluations in MP 9 and HW 12.

---

## Slide 10: Wrap-Up & Next Steps
### Transitioning to ASR Evaluation Methodology
* **Summary:** Today we covered the necessity of moving beyond point estimates by using the non-parametric bootstrap to construct 95% confidence intervals, enabling rigorous inferential claims.
* **Next Lecture (Wed, Nov 04):** We will apply these evaluation concepts specifically to the ASR track, covering the NIST OpenASR 2020 Challenge Evaluation Plan, transcript normalization, and Word Error Rate (WER) scoring.
* **Action Item 1:** Ensure you have completed the readings from ISLP (Chs. 1, 5, 12) to solidify your understanding of resampling and inference.
* **Action Item 2:** Review the NIST OpenASR Evaluation Plan prior to Wednesday's lecture, paying special attention to how insertions, deletions, and substitutions are calculated.

**Speaker Notes:**
To wrap up: a single performance metric is a red flag in a professional data science environment. You must quantify your uncertainty, and the percentile bootstrap is the most robust, model-agnostic way to do that. On Wednesday, we will get highly specific. We will look at how the National Institute of Standards and Technology (NIST) formally evaluates Automatic Speech Recognition systems, breaking down the mathematics of the Word Error Rate and the complexities of aligning a hypothesis transcript against a reference text. Please complete the ISLP readings and review the NIST OpenASR Evaluation Plan before class. I'll see you on Wednesday.
