# CIS 531 / 731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 4:** Explore & Model | **Module 8:** Model: Retrieval-Augmented Classification & Generational Convolution | **Lecture 27:** Generational Convolution Models Lab; Wrap-Up | Fri, October 30, 2026 |

---

## Slide 1: Generational Convolution Models Lab & Module 8 Wrap-Up
### CIS 531 / 731 - Lecture 27
* **Generational Drift Modeling:** Applying time-series and rolling-window 1-D convolutions to track semantic, trope, and sentiment drift across ordered generational cohorts.
* **Lab 8 Environment & Dataset Setup:** Initializing the pinned CPU DevContainer environment (`lab08.ipynb`) and loading provenance-admitted temporal datasets for the convolution exercise.
* **Implementing Fixed & Learned Convolutions:** Authoring deterministic scripts for smoothing (`[0.25, 0.5, 0.25]`) and first-difference (`[-1, 1]`) kernels with bootstrap confidence intervals, plus the **CIS 731** learned 1-D PyTorch convolutional kernel.
* **Integration with Classification Pipelines:** Feeding convolved temporal cohort features back into `scikit-learn` (`Pipeline` / `FeatureUnion`) and retrieval-augmented classification pipelines to improve temporal accuracy.
* **MP 7 Debrief & Transition to Module 9:** Reviewing the MP 7 few-shot classification workflow, PS 8 Interim Report integration, and readiness for the Module 9 Evaluation phase.

**Speaker Notes:**
Welcome to Lecture 27, the hands-on lab and wrap-up session for Module 8 on Retrieval-Augmented Classification and Generational Convolution. On Monday (Lecture 25), we deconstructed the Retrieval-Augmented Generation paradigm of Lewis et al. and showed how retrieving top-$k$ exemplars from a FAISS index grounds zero-shot and few-shot classification. On Wednesday (Lecture 26), we built deterministic, leakage-free text feature extraction pipelines in `scikit-learn` using `Pipeline`, `FeatureUnion`, `TfidfVectorizer`, and `TruncatedSVD`. Today, we bring the temporal and generational dimension into the loop: you will bin classified chunks along an ordered cohort axis, apply 1-D convolutional kernels in `lab08.ipynb` to quantify generational semantic drift with bootstrap confidence intervals, feed those temporal features back into your classifier, and debrief MP 7 ahead of next week's transition into Module 9 on Inferential Statistics and Gold-Standard Evaluation.

---

## Slide 2: Bridging Lectures 25 & 26 to Temporal Cohort Dynamics
### Why Static Classification Misses Generational Shift
* **The Static I.I.D. Fallacy:** Standard text classifiers and unconditioned RAG retrievers treat documents as independent and identically distributed (i.i.d.), ignoring when a song, document, or broadcast segment was produced.
* **Semantic & Trope Drift Across Cohorts:** Cultural tropes (such as "doomed youth" or "out of time") and colloquial expressions shift in both prevalence and lexical realization across release decades and broadcast windows.
* **Unifying Module 8:** We combine **Lecture 25** (RAG exemplar retrieval) and **Lecture 26** (`scikit-learn` `FeatureUnion` pipelines) with **1-D discrete convolutions** over an ordered cohort axis to model longitudinal drift explicitly.

**Speaker Notes:**
Why do we need generational convolution models on top of the RAG classifiers and `scikit-learn` feature pipelines we built earlier this week? Because language and media corpora are non-stationary. If you classify tropes across a multi-decade corpus of song lyrics, literature, or historical archives—or across a multi-hour live radio call-in stream—treating every chunk as timeless i.i.d. data throws away vital structural signal. A phrase or trope that peaks in one decade or broadcast hour often mutates or decays in the next. By ordering our chunks along a canonical cohort axis and applying discrete 1-D convolutions across cohort bins, we can separate smooth longitudinal trends from noisy bin-to-bin fluctuations and use those temporal signals to sharpen classification accuracy.

---

## Slide 3: Defining the Ordered Cohort Axis — VDB Track vs. ASR Track
### Constructing the Cohort-by-Trope Frequency Matrix
* **VDB Text Corpus Track (`release_decade`):** Chunks are binned along an ordered generational cohort axis defined as `generation_cohort := f(release_decade)` (e.g., 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s) or publication era.
* **ASR Broadcast Stream Track (`window_index`):** Transcribed audio segments ($\le 30\text{s}$ chunks from whitelisted or instructor-provided streams) are binned by their ordered event-time window index $t_w \in \{1, 2, \dots, T\}$.
* **Per-Cohort Trope Frequency Vectors:** For each ordered cohort bin $c \in \{1, \dots, T\}$ and label space of size $K$ (8–12 trope/genre or ASR labels), we aggregate chunk predictions into a normalized probability vector $\mathbf{p}_c \in \Delta^{K-1}$ where $\sum_{k=1}^K p_{c,k} = 1.0$.

**Speaker Notes:**
Before we can convolve anything, we must define a strictly ordered 1-D axis appropriate to your locked project track. Remember that your track—either Vector Database text corpora or Automatic Speech Recognition streams—was fixed at the PS 4 proposal stage. If you are on the VDB track, your ordered cohort axis maps document publication or release timestamps into discrete generational cohorts, such as `release_decade`. If you are on the ASR track, your ordered cohort axis is the sequential event-time window index produced by your Module 4 Structured Streaming pipeline. Within each cohort bin $c$, we count the frequency of each of our $K$ trope or genre classes and normalize by the total chunks $N_c$ in that bin, yielding a $(T \times K)$ matrix $P$ where every row sums to `1.0` within `1e-6`—a deterministic property for the grader to check by hand or automatically.

---

## Slide 4: Lab 8 Setup — Environment Initialization & Temporal Dataset Loading
### Preparing `lab08.ipynb` on the Pinned CPU DevContainer Baseline
* **CPU Baseline & Manifest Verification:** Launch `lab08.ipynb` inside the pinned CPU DevContainer (all package versions and SHA-256 digests locked to the course manifest; GPU access is optional and never required).
* **Provenance & Admissibility Pre-Check:** Verify that every loaded record carries a valid `license_class` in `{public_domain, instructor_provided}` (for VDB corpora) or an approved stream `source_id` (for ASR streams), with zero Yelp or SEC-filing records.
* **Sparse Cohort Guard & Pivot Table Construction:** Group admitted chunks by `(cohort_index, label)`, inspect per-cohort sample counts $N_c$, and construct the raw $(T \times K)$ frequency tensor in NumPy/Pandas.

**Speaker Notes:**
Let's open `lab08.ipynb` inside your pinned CPU DevContainer. Every step of today's lab—and all downstream tasks in MP 9—is 100% solvable on the CPU baseline without requiring a GPU. In Cell 1 of the notebook, we load our chunk dataset and run a quick provenance assertion—for the grader to check by hand or automatically—confirming that every VDB record carries `license_class` in `{public_domain, instructor_provided}` (and never reproduces full copyrighted song lyrics) or that every ASR segment comes from the instructor whitelist. Next, we pivot the chunk-level trope predictions into a $(T \times K)$ DataFrame indexed by `cohort_index` in strictly ascending chronological order, logging the sample size $N_c$ of each cohort bin so we can account for sparse early or late bins during uncertainty estimation.

---

## Slide 5: Implementing Fixed 1-D Convolution Kernels
### Smoothing (`[0.25, 0.5, 0.25]`) vs. First-Difference Drift (`[-1, 1]`)
* **Discrete 1-D Convolution Along the Cohort Axis:** For each trope $k \in \{1, \dots, K\}$, we convolve the 1-D cohort trajectory $p_{1:T, k}$ with a discrete filter kernel $w$:
  $$(p_{:, k} * w)[c] = \sum_{m} p_{c - m, k} \, w[m]$$
* **Low-Pass Smoothing Kernel (`w_smooth = [0.25, 0.5, 0.25]`):** A 3-tap binomial filter (weights summing to `1.0`) that suppresses single-cohort sampling noise while preserving multi-cohort generational waves.
* **High-Pass First-Difference Kernel (`w_diff = [-1, 1]`):** A 2-tap derivative filter (weights summing to `0.0`) that computes the exact cohort-to-cohort rate of change $\Delta p_{c, k} = p_{c, k} - p_{c-1, k}$, isolating sharp emergence or decay inflection points.

**Speaker Notes:**
In Part 2 of `lab08.ipynb`, we implement our two canonical fixed kernels across the ordered cohort axis using `numpy.convolve` or `scipy.ndimage.convolve1d`. Why these specific two kernels? First, the 3-tap smoothing kernel `[0.25, 0.5, 0.25]` acts as a low-pass filter: it weights the current cohort at 50% and its immediate predecessor and successor cohorts at 25% each, smoothing out jagged fluctuations caused by finite sample sizes in individual decades or time windows. Second, the 2-tap first-difference kernel `[-1, 1]` acts as a discrete first derivative: positive spikes pinpoint the exact cohort transition where a trope surges in popularity, while negative troughs mark where a trope fades out. Make sure you explicitly document your boundary padding mode—such as `'edge'` (replicate) or `'valid'`—so that endpoint cohorts are handled reproducibly for the grader to check by hand or automatically.

---

## Slide 6: Quantifying Uncertainty on Generational Drift
### Non-Parametric Bootstrap Confidence Intervals Across Cohort Bins
* **Why Point Estimates of Drift Are Insufficient:** If Cohort $c_1$ has $N_{c_1} = 25$ chunks and Cohort $c_2$ has $N_{c_2} = 400$ chunks, a raw difference $\Delta p_{c, k} = +0.08$ may be pure multinomial sampling variance rather than true generational drift.
* **Stratified Cohort Bootstrap Protocol ($B \ge 1,000$):** Within each cohort bin $c$, resample $N_c$ chunks with replacement for $b = 1, \dots, B$, recompute the normalized vector $\mathbf{p}_c^{(b)}$, and re-apply both `w_smooth` and `w_diff`.
* **95% Percentile Confidence Bands:** Extract the 2.5th and 97.5th percentiles of the $B$ convolved trajectories at every cohort index $c$; a cohort-to-cohort drift $\Delta p_{c, k}$ is statistically distinguishable from zero only when its 95% CI excludes `0.0`.

**Speaker Notes:**
Just as we never report a classifier's Macro-F1 without a confidence interval, we never claim that a trope "drifted" between the 1980s and 1990s—or between Window 4 and Window 5—based on a naked line plot. If one cohort bin only has 20 documents, a swing of 10 percentage points can happen by chance alone! To separate genuine generational shift from small-sample noise, we wrap our convolution function in a non-parametric bootstrap loop with at least $B = 1,000$ resamples. In each bootstrap replicate, we resample chunks with replacement inside each cohort bin, recompute the frequency matrix, and pass it through `[0.25, 0.5, 0.25]` and `[-1, 1]`. Plotting the 95% confidence ribbon around both curves immediately reveals which generational shifts are statistically supported—and prepares your uncertainty visualizations directly for PS 8 and MP 9.

---

## Slide 7: CIS 731 Graduate Extension — Learned 1-D Convolutional Kernels
### Training a PyTorch `Conv1d` Forecaster Against Fixed-Kernel Baselines
* **From Fixed Filters to Learned Temporal Kernels (CIS 731 Requirement):** While fixed kernels apply identical weights to all tropes, a learned 1-D convolutional layer (`torch.nn.Conv1d` in PyTorch 2.x on CPU) learns trope-specific temporal filters from historical cohort sequences.
* **Causal / Forward-Only Splitting (No Future Leakage):** Train the 1-D convolution on causal sliding windows of length $L$ over early cohorts $c \in \{1, \dots, T_{\text{train}}\}$ to predict the trope distribution $\hat{\mathbf{p}}_{c+1}$ of the next cohort, holding out the final cohorts $c > T_{\text{train}}$ for evaluation.
* **Held-Out Forecast Error Comparison:** Compare Mean Absolute Error (MAE) and Mean Squared Error (MSE) of the learned `Conv1d` kernel against the fixed `[0.25, 0.5, 0.25]` persistence/extrapolation baseline on the held-out cohorts.

**Speaker Notes:**
For students enrolled in CIS 731—and mixed teams whose graduate members own the modeling extension—both today's lab and MP 9 include an additional analytical comparison: fitting a learned 1-D convolutional kernel in PyTorch 2.x on the CPU and comparing its held-out forecast error against the fixed kernels. Using `torch.nn.Conv1d(in_channels=K, out_channels=K, kernel_size=3)`, you train a lightweight causal filter on early cohorts to forecast the trope distribution of the subsequent cohort. Two rules are paramount here for the grader to check by hand or automatically: first, enforce strict causal windowing so future cohorts never leak into training features; second, regularize your `Conv1d` weights (via weight decay or depthwise separable channels) and report honestly when the 3-tap fixed kernel outperforms the learned kernel on small cohort counts $T$.

---

## Slide 8: Integrating Convolved Temporal Priors into Classification Pipelines
### Closing the Loop with Lecture 25 (RAG) and Lecture 26 (`scikit-learn` Pipelines)
* **Temporal Prior Injection (`FeatureUnion` / `ColumnTransformer`):** Concatenate the smoothed cohort prior vector $\tilde{\mathbf{p}}_{c(x)} = (P * w_{\text{smooth}})[c(x)]$ with the TF-IDF / SVD text features from Lecture 26 inside a unified `scikit-learn` `Pipeline` + `FeatureUnion`.
* **Cohort-Aware RAG Exemplar Conditioning (Lecture 25 Link):** When retrieving top-$k$ demonstrations ($k \in \{3, 5, 10\}$) from the FAISS `IndexFlatIP` index, evaluate how weighting or filtering candidate exemplars by cohort proximity affects downstream Macro-F1.
* **Ablation Discipline:** Compare text-only classification (`MP 7` baseline) against text + convolved cohort features on held-out evaluation data to quantify the net accuracy gain from temporal context.

**Speaker Notes:**
Step 4 of today's lab closes the loop across all three lectures of Module 8. Once we have computed the smoothed trope distribution for each cohort using `[0.25, 0.5, 0.25]` (exclusively from training splits so we never leak test labels!), how do we feed that signal back into our classifier? In a `scikit-learn` workflow from Lecture 26, we use a `FeatureUnion` or `ColumnTransformer`: Branch 1 extracts `TfidfVectorizer` + `TruncatedSVD` features from the chunk text, while Branch 2 attaches the $K$-dimensional convolved cohort prior for that chunk's timestamp or decade. Alternatively, in a probabilistic or RAG classifier from Lecture 25, we can combine the classifier's text likelihood with the smoothed cohort prior via Bayes' rule or use cohort distance to break ties among retrieved FAISS exemplars.

---

## Slide 9: MP 7 Debrief & Final Submission Check
### Protocol Lock, Failure-Mode Controls, and Evaluation Source Separation
* **Schedule Reminder:** As announced on Canvas and in the course repository, the **MP 7** due date was extended to **Tue 03 Nov 2026 (11:59 PM CST)**; all subsequent due dates (**PS 8** on Sat 07 Nov, **MP 9** on Mon 16 Nov) remain unchanged.
* **Unified `Classifier` Interface & Simplex Validation:** Confirm that your (i) embedding-prototype, (ii) FAISS `IndexFlatIP` kNN, and (iii) fixed-demonstration few-shot LLM classifiers implement one shared interface whose `predict_proba` outputs are non-negative, sum to `1.0` within `1e-6`, and map strictly to valid labels—for the grader to check by hand or automatically.
* **Prompt Failure Controls & Evaluation Separation:** Verify that `protocol.md` was committed prior to sweep execution, that demonstration-order permutation is active across your $\ge 5$ seeds, and that graded Macro-F1 (with 95% bootstrap CIs) is computed strictly via `compute_graded_metric` on the instructor held-out set (`eval_mp7.jsonl`), keeping `compute_dev_metric` (`grading_eligible=False`) separate.

**Speaker Notes:**
Let's take five minutes to debrief MP 7 and verify everyone's checklist before the extended Tuesday, November 3 submission deadline. First, double-check that your `protocol.md` file—specifying your 8–12 label space, shot sweep $k \in \{0, 1, 3, 5, 8\}$, $\ge 5$ random seeds, and bootstrap CI method—is committed in your Git history *prior* to your results commit. Second, verify that your `report.md` explicitly documents concrete controls for all three prompt failure modes: majority-label bias, demonstration-position bias (using permutation across seeds), and label leakage. Third, ensure strict evaluation source separation—for the grader to check by hand or automatically: every headline Macro-F1 table in `report.md` must come from `compute_graded_metric` on the instructor-provided evaluation set and be 100% reproducible from your committed `predictions.jsonl` file.

---

## Slide 10: Module 8 Wrap-Up & Transition to Module 9
### Preparing for PS 8 (Sat 07 Nov) and Inferential Evaluation (Mon 02 Nov)
* **Module 8 Synthesis:** You now have the complete modeling toolkit connecting **MP 7** (fixed-demo few-shot & FAISS kNN baselines) $\rightarrow$ **PS 8** (Interim Report baselines & UMAP/drift visuals) $\rightarrow$ **MP 9** (top-$k$ RAG classification + cohort convolutions).
* **Immediate Milestone — PS 8 Interim Report (Due Sat 07 Nov 2026):** Use the Generative AI Kit (v3.3) to red-team your 5-item quantified Risk Register, generate your $\ge 3$ Wilke-compliant exploratory figures (including UMAP sensitivity sweeps and today's cohort drift plot with uncertainty), and specify your 50–200 gold-standard annotation plan.
* **Next Week — Module 9 (Lectures 28–30, Starting Mon 02 Nov):** We transition into **Evaluating Models: Inferential Statistics, NIST OpenASR 2020 WER Methodology, and Human-in-the-Loop Gold-Standard Construction** (capped at $\le 50$ objects / 2 hours for homework).

**Speaker Notes:**
That wraps up the conceptual portion of Module 8! Let's review how everything we did this week feeds directly into your next two major deliverables. First, your **PS 8 Interim Report** is due next Saturday, November 7 (and remember: PS 4, PS 8, and HW 12 are mandatory, undroppable project milestones). The cohort drift plot with bootstrap confidence intervals that you build in `lab08.ipynb` today can serve directly as one of your three required exploratory figures in Section 3 of PS 8! Second, starting Monday, November 2 in Lecture 28, we launch **Module 9: Evaluating Models**, where we cover resampling and inferential statistics from James et al. (*ISLP*), the NIST OpenASR 2020 Word Error Rate evaluation protocol on Wednesday, and our hands-on Gold-Standard Construction Lab (enforcing the $\le 50$-row / 2-hour homework annotation ceiling and Cohen's $\kappa$ inter-annotator agreement) on Friday. Open `lab08.ipynb` in your DevContainer now, and let's run the generational convolution pipeline!
