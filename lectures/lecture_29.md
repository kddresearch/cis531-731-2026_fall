# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **[Phase 5](../phases/phase_05/):** Evaluate & Deploy | **[Module 09](../modules/module_09/):** Evaluating Models: Inferential Statistics & ASR Evaluation | **Lecture 29:** ASR Evaluation Methodology & Gold-Standard Design | Wed 04 Nov 2026 |

---

## Slide 1: Welcome to Lecture 29 — ASR Evaluation
### CIS 531/731 - Lecture 29
* **The ASR Challenge:** Translating audio into text introduces unique, sequential error modes that standard classification metrics (like Accuracy or F1) cannot capture.
* **The Standard:** We rely on the methodologies defined by the National Institute of Standards and Technology (NIST), specifically the OpenASR Challenge.
* **The Metric:** The Word Error Rate (WER) is the absolute industry standard for speech recognition evaluation.
* **The Complexity:** Aligning a machine's guess (the hypothesis) with the human truth (the reference) requires dynamic programming algorithms.
* **Today's Goal:** Deconstructing WER, understanding transcript normalization, and architecting unbiased gold-standard evaluation sets.

**Speaker Notes:**
Welcome back to Phase 5. On Monday, we covered the non-parametric bootstrap to put confidence intervals around our metrics. Today, we are going to dive deep into the specific metrics we use for Track 1: Automatic Speech Recognition (ASR). If you are building a text classifier, you just compare the predicted label to the true label. It is a 1-to-1 mapping. ASR is not 1-to-1. The model might hallucinate extra words, drop words entirely, or misspell them. You cannot use a simple "accuracy" score. We have to use sequence alignment mathematics, and the industry standard for this is defined by NIST. We are going to look closely at their OpenASR evaluation plan today.

---

## Slide 2: The Core ASR Metric: Word Error Rate (WER)
### Beyond Simple Accuracy
* **The Formula:** $\text{WER} = \frac{S + D + I}{N}$
* **Components:**
  * **$S$ (Substitutions):** A word in the reference is replaced by an incorrect word in the hypothesis (e.g., "cat" $\rightarrow$ "bat").
  * **$D$ (Deletions):** A word in the reference is missing from the hypothesis.
  * **$I$ (Insertions):** An extra word is added to the hypothesis that was not in the reference.
  * **$N$ (Total Words):** The total number of words in the *reference* transcript ($N = S + D + C$).
* **The $C$ Variable:** $C$ represents the number of Correct words.
* **The Consequence:** Because of Insertions ($I$), a WER can mathematically exceed 100%.

**Speaker Notes:**
This is the Word Error Rate, or WER. This is the only metric that matters when you are evaluating a Whisper model or an AssemblyAI stream. It is calculated as the sum of Substitutions, Deletions, and Insertions, divided by the total number of words in the true reference transcript. A Substitution is when the model hears "ball" instead of "call." A Deletion is when the model misses a word entirely because of static. An Insertion is when the model hallucinates a word that wasn't spoken. Because the model can hallucinate an infinite number of inserted words, the numerator can actually be larger than the denominator, meaning your WER can be 150% or 200%. Lower is always better. Zero is perfect.

---

## Slide 3: Sequence Alignment (The Levenshtein Distance)
### Mapping Hypothesis to Reference
* **The Problem:** How does the computer know which words to compare if the lengths of the two transcripts don't match?
* **Reference:** `the quick brown fox jumped`
* **Hypothesis:** `a quick brown fox leaped`
* **The Algorithm:** Minimum Edit Distance (Levenshtein distance) using Dynamic Programming.
* **The Matrix:** The algorithm builds a cost matrix to find the alignment path that minimizes the total number of edits (Substitutions, Deletions, Insertions).
* **ASR Implementations:** Python libraries like `jiwer` handle this dynamic programming alignment for you.

**Speaker Notes:**
If I have a reference transcript with 10 words, and the ASR model spits out 9 words, how do I know which one was deleted? We can't just compare word 1 to word 1, and word 2 to word 2, because an early deletion will misalign the entire rest of the sentence. We solve this using the Minimum Edit Distance, specifically the Levenshtein distance algorithm. It uses dynamic programming to build a matrix and find the absolute cheapest path to turn the hypothesis string into the reference string. In practice, you do not have to write this matrix yourself; we will use the `jiwer` library in Python to automatically calculate the alignments and extract the exact count of S, D, and I.

---

## Slide 4: Transcript Normalization (The Epistemic Baseline)
### Comparing Apples to Apples
* **The Artifact:** ASR models output raw text, often lacking punctuation or capitalization, or conversely, formatting numbers as digits (`10`) instead of words (`ten`).
* **The Penalty:** If the reference says "Mr. Smith" and the model outputs "mr smith", a naive WER calculation counts two substitutions due to capitalization and punctuation.
* **Normalization:** Applying rigorous regex rules to both the reference and hypothesis *before* calculating WER.
* **NIST Standards:** The OpenASR protocol mandates lowercasing everything, removing all punctuation, expanding contractions (sometimes), and converting all digits to spoken word forms.
* **The Goal:** We want to measure the model's ability to hear phonemes, not its formatting choices.

**Speaker Notes:**
If you run an ASR evaluation without normalization, your results are scientifically invalid. Imagine your human reference transcript says "Hello, World!" and your Whisper model outputs "hello world". If you run a naive WER, the computer will flag both words as Substitutions because the capital 'H' and the comma don't match. You are artificially inflating your error rate over formatting. Before you ever calculate WER, you must pass both the reference and the hypothesis through a strict normalization pipeline. In accordance with NIST guidelines, we lowercase everything, strip out all punctuation, and typically convert digits into words (like turning the number '5' into the letters f-i-v-e). We are evaluating acoustic recognition, not orthography.

---

## Slide 5: Handling Disfluencies and Hesitations
### The Messiness of Spontaneous Speech
* **The Human Element:** Real radio broadcasts and debates are full of "um," "uh," stutters, and false starts.
* **NIST Protocol:** How should the ground-truth reference handle these?
  * **Verbatim Transcription:** Transcribe every single "um" and "uh" exactly as spoken.
  * **Filtering:** Remove all disfluencies from both the reference and the hypothesis during normalization.
* **The Decision:** Your pipeline must explicitly declare how it handles disfluencies. If the ASR model filters them out automatically (like some Whisper settings), you must filter them from the reference to ensure a fair comparison.
* **Overlap (Crosstalk):** Segments where two speakers talk simultaneously are often excluded from standard WER calculations because human annotators cannot reliably transcribe them.

**Speaker Notes:**
Spontaneous human speech is incredibly messy. We stutter, we say "um," we restart sentences. This creates a massive headache for ASR evaluation. If the human annotator types out every single "um," but the ASR model is programmed to ignore filler words and output clean text, your Deletion rate will skyrocket. The NIST protocol requires you to define a strict rule. Generally, the most scientifically robust method is to map all filler words (um, uh, er) to a special `<hesitation>` token, or strip them entirely from both transcripts before calculating WER. Furthermore, when two people yell over each other on a radio broadcast, NIST often recommends ignoring that audio segment entirely, as the ground truth itself becomes subjective.

---

## Slide 6: The NIST OpenASR 2020 Challenge
### The Benchmark Standard
* **The Dataset:** High-entropy conversational telephone speech across multiple low-resource languages.
* **The Objective:** To advance ASR technologies in highly constrained, noisy environments.
* **Evaluation Tiers:** NIST categorizes evaluations into constrained (using only provided training data) and unconstrained (allowing external language models and datasets).
* **The Scoring Tool:** NIST historically relies on tools like `sclite` (part of the SCTK suite) to compute alignments and generate detailed error reports.
* **The Takeaway for CIS 531/731:** We adopt the strictness of the NIST protocol. You must normalize, you must document your handling of disfluencies, and you must report the exact S, D, and I counts alongside the final WER.

**Speaker Notes:**
In this course, we do not invent our own evaluation methodologies. We anchor to federal and industry standards. The NIST OpenASR challenge provides the definitive blueprint for how to evaluate speech recognition in difficult, noisy environments. While we won't force you to compile the C-based `sclite` toolkit they use, we are adopting their philosophical rigor. When you report your ASR metrics in your final project, you cannot just give me a single WER percentage. You must provide the exact count of Substitutions, Deletions, and Insertions, and you must include a markdown cell explicitly defining the regex normalization pipeline you applied to the text before scoring it.

---

## Slide 7: Architecting the Gold-Standard
### Human-Annotated Ground Truth
* **The Dependency:** WER requires a reference transcript. For your custom radio or podcast streams, this reference does not exist.
* **The Mandate (INV-17):** You must create the Gold-Standard manually. **You cannot use an LLM or an ASR model to generate your ground truth.**
* **The Threat of Circularity:** If you use Whisper to transcribe the audio, and then use that transcript as your reference to evaluate a different Whisper model, you are measuring model agreement, not accuracy.
* **The Protocol:** Human students must listen to the audio and manually type the verbatim transcript according to the agreed-upon normalization rules.

**Speaker Notes:**
Where does the reference transcript come from? If you are analyzing a local radio broadcast for your term project, nobody has transcribed it for you. You have to build the Gold Standard. I must be incredibly clear on this point, per course invariant INV-17: you cannot use an AI to generate your ground truth. If you run the audio through a massive Whisper model and use that output as your reference to test a smaller model, you are committing methodological circularity. You aren't measuring how accurate the small model is; you are only measuring how closely it mimics the big model. To establish true scientific baseline accuracy, the gold standard must be typed by a human ear.

---

## Slide 8: The Gold-Standard Construction Lab (Preview)
### Balancing Rigor with Thermal Load
* **The Workload Trap:** Transcribing 1 hour of messy audio can take a human 4 to 6 hours. This is an unacceptable thermal drain for a homework assignment.
* **The Cap:** For Friday's Lab (and MP 9), you are strictly capped at annotating $\le 50$ objects (sentences/utterances) or a maximum of 2 hours of labor.
* **Stratified Sampling:** To make those 50 utterances count, do not just transcribe the first 5 minutes of the broadcast.
* **The Strategy:** Sample randomly across the entire corpus. Include clean speech, noisy speech, different speakers, and different accents to ensure your 50-utterance gold standard represents the true variance of the dataset.

**Speaker Notes:**
Building a gold standard is exhausting, grueling work. Professional transcriptionists take about 4 hours to transcribe 1 hour of messy, multi-speaker audio. I am not going to ask you to do that. On Friday, we will run the Gold-Standard Construction Lab. To protect your time and prevent burnout, we are enforcing a hard cap: you will only annotate a maximum of 50 utterances, or 2 hours of work, whichever comes first. Because your sample size is small, you must sample intelligently. Do not just transcribe the first two minutes of the audio file. You need to randomly sample 5-second clips from the beginning, middle, and end of the broadcast so your evaluation set captures all the different speakers, background noises, and acoustic environments.

---

## Slide 9: Beyond WER: Downstream Task Evaluation
### Does ASR Accuracy Equal Task Success?
* **The Open IE Objective:** We are not transcribing audio just to read it; we are transcribing it to extract topics, relations, and claims.
* **The Disconnect:** An ASR model might have a high WER (e.g., 25%) because it misses filler words and articles ("the", "a"), but it might perfectly capture the core nouns and verbs.
* **Entity Error Rate (EER):** Evaluating ASR accuracy specifically on Named Entities (people, places, concepts) rather than every single word.
* **The Pipeline View:** A 15% WER model might yield better downstream extraction results than a 10% WER model if the 10% model hallucinates critical domain vocabulary while the 15% model only drops stop words.
* **The Requirement:** You must evaluate the final structured output (the extracted topics or tropes), not just the intermediate ASR transcript.

**Speaker Notes:**
Finally, we need to apply systems thinking to our evaluation. We are in an Open Information Extraction course. We care about the final extracted facts. WER treats every word equally. A substitution on the word "the" penalizes the model exactly the same amount as a substitution on the critical noun "vaccine." This means a model with a terrible WER might actually be perfectly fine for our pipeline if the errors are all on stop words, and a model with a great WER might be useless if it consistently mishears our target scientific vocabulary. You must evaluate the pipeline end-to-end. Measure the WER, yes, but then measure the precision and recall of your final extracted topics.

---

## Slide 10: Wrap-Up & Next Steps
### Preparing for the Annotation Lab
* **Summary:** We deconstructed the Word Error Rate (WER) metric, examined the necessity of strict transcript normalization based on NIST standards, and established the rules for manual gold-standard generation.
* **Next Lecture (Fri, Nov 06):** Gold-Standard Construction Lab. You will manually transcribe and normalize your 50-utterance baseline.
* **Action Item 1:** Ensure your local development environments (Jupyter/VS Code) are ready for Friday's lab.
* **Action Item 2:** Review the `scikit-learn` documentation on Precision and Recall in preparation for downstream metric evaluation.

**Speaker Notes:**
To wrap up: today we learned that evaluating speech recognition requires dynamic programming to align sequences, and strict normalization to ensure we are testing acoustics, not orthography. The Word Error Rate is your primary diagnostic tool. On Friday, we will execute the Gold-Standard Construction Lab. You will put on your headphones and generate the 50-utterance ground truth that will mathematically anchor the rest of your term project. Please ensure your Python environments are ready to go, and review the precision-recall documentation so we can discuss how to evaluate the downstream classifications once the ASR layer is complete. I will see you on Friday.
