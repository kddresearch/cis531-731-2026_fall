<!--
  Template Note: This file serves as the canonical template for module pages.
  When instantiated as `modules/module_YY/module_YY.md`, use relative paths 
  (`../../phases/phase_0X/` and `../../lectures/lecture_j.md`) to maintain correct routing.
  Note that the module name itself does not self-link, but lectures link directly to their markdown files.
  Module readings may be contiguous or separate per lecture; the module readings for the modules within a parent phase form a partition of that phase’s readings.
-->

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 3](../../phases/phase_03/):** Scrub & Embed | **Module 06:** GenAI & LLMs: Candidates, Code, Classification | **Lectures 17-21** | Mon 05 Oct - Fri 16 Oct 2026 | [Jurafsky & Martin, *SLP3* Chs. 6, 8, 10](https://web.stanford.edu/~jurafsky/slp3/6.pdf); [Hugging Face Transformers Task Guide](https://huggingface.co/docs/transformers/en/tasks/sequence_classification) |

---

## [Lecture 17: GenAI & LLMs: Candidates, Code, Classification](../../lectures/lecture_17.md) (Mon 05 Oct 2026)

1. **Language Modeling Fundamentals:** Introduction to $N$-gram models, perplexity, and the transition from count-based to dense neural representations (Jurafsky & Martin, Ch. 6).
2. **Transformer Architecture Overview:** The attention mechanism, self-attention, and the foundational architecture underlying modern Large Language Models.
3. **The Pretraining & Fine-Tuning Paradigm:** Understanding how foundational models acquire broad language representations and are subsequently tuned for specific downstream data science tasks.
4. **LLMs as Classifiers:** Shifting from generative text completion to using LLM token probabilities and embeddings for strict classification mapping.
5. **Prompting vs. Fine-Tuning Trade-offs:** Analyzing the computational cost, accuracy, and latency differences between zero/few-shot prompting and full model fine-tuning.
* **Assigned Reading:** [Jurafsky & Martin, *Speech and Language Processing* (3rd ed. draft, Aug 19, 2026), Ch. 6 (*Neural Networks* PDF)](https://web.stanford.edu/~jurafsky/slp3/6.pdf) & [Ch. 8 (*Post-Training / Alignment* PDF)](https://web.stanford.edu/~jurafsky/slp3/8.pdf)

---

## [Lecture 18: Few-Shot Trope/Genre Classification](../../lectures/lecture_18.md) (Wed 07 Oct 2026)

1. **The In-Context Learning (ICL) Paradigm:** Leveraging the LLM's pre-trained knowledge base to classify text (e.g., media tropes) without updating model weights.
2. **Prompt Engineering for Classification:** Designing strict formatting constraints and system instructions to force the LLM to output clean, parsable classification labels.
3. **The Few-Shot Exemplar Selection:** Determining how to select high-leverage $K$-shot examples that define the boundary conditions of complex genres or tropes.
4. **Hugging Face `pipeline` API:** Utilizing the `transformers` library to initialize local, open-weight text classification models.
5. **Handling Out-of-Distribution Data:** Strategies for managing LLM hallucinations or default behaviors when presented with novel genres or unseen media data.
* **Assigned Reading:** [Hugging Face Transformers Task Guide: *“Text Classification”*](https://huggingface.co/docs/transformers/en/tasks/sequence_classification)

---

## [Lecture 19: Model Selection & Embedding-Backed Classification Lab](../../lectures/lecture_19.md) (Mon 12 Oct 2026)

1. **MP6 Release & Requirements:** Reviewing the expectations for the embedding-backed classification machine problem.
2. **Embedding Models vs. Generative Models:** Understanding why a specialized embedding model (e.g., `sentence-transformers`) is often superior to a generative LLM for clustering and similarity-based classification.
3. **Distance Metrics for Classification:** Utilizing Cosine Similarity and Euclidean distance in the embedding space to classify unknown texts against known trope/genre anchors.
4. **Building the Reference Index:** Constructing the "gold standard" vector database of known tropes to serve as the classification lookup table.
5. **Thresholding and Confidence:** Establishing mathematical thresholds for "Unknown" or "Mixed" classifications when distance metrics fall in the boundary zones.
* **Assigned Reading:** [scikit-learn Tutorial: *“Working With Text Data”*](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html); [Sentence Transformers *“Semantic Search”*](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)

---

## [Lecture 20: Trope/Genre Classification Workshop](../../lectures/lecture_20.md) (Wed 14 Oct 2026)

1. **Execution Troubleshooting:** Live debugging of Hugging Face environment setups, CUDA/CPU execution issues, and memory management constraints.
2. **Pipeline Integration:** Connecting the output of the semantic search (Module 5) directly into the classification prompt or embedding comparator.
3. **Evaluating Classifier Performance:** Transitioning from subjective "looks good" evaluations to rigorous metrics (Precision, Recall, F1) for the trope classifications.
4. **Handling Ambiguous Media:** Strategies for classifying multi-genre media or texts containing conflicting tropes using weighted probabilities.
5. **Code Review & Refactoring:** Peer review of classification pipelines to ensure robust error handling and adherence to FAIR principles.
* **Assigned Reading:** [Jurafsky & Martin, *Speech and Language Processing* (3rd ed. draft, Aug 19, 2026), Ch. 10: *“Large Language Models”*](https://web.stanford.edu/~jurafsky/slp3/)

---

## [Lecture 21: Wrap-Up](../../lectures/lecture_21.md) (Fri 16 Oct 2026)

1. **MP5 Submission Review:** Common pitfalls and architectural successes observed in the GenAI/LLM Candidates submission (due prior day).
2. **Computational Cost Realities:** Analyzing the latency and hardware requirements of the deployed classification pipelines.
3. **Limitations of Few-Shot Prompting:** When does the LLM fail to capture deep semantic tropes, and when is a dedicated trained classifier mathematically necessary?
4. **Module 6 Synthesis:** Summarizing the integration of LLMs into the data science pipeline as robust, programmatic tools rather than conversational chatbots.
5. **Preview of Module 7:** Transitioning from data extraction and classification to visualization (UMAP) and generational drift dashboarding.
* **Assigned Reading:** [Hugging Face Transformers: *Sequence Classification & Evaluation*](https://huggingface.co/docs/transformers/en/tasks/sequence_classification)
