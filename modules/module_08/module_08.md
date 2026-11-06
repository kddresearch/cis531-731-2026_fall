<!--
 Template Note: This file serves as the canonical template for module pages.
 When instantiated as `modules/module_08/module_08.md`, use relative paths 
(`../../phases/phase_04/` and `../../lectures/lecture_25.md`) to maintain correct routing.
 Note that the module name itself does not self-link, but lectures link directly to their markdown files.
 Module readings may be contiguous or separate per lecture; the module readings for the modules within a parent phase form a partition of that phase’s readings.
-->

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 4](../../phases/phase_04/):** Explore & Model | **Module 08:** Model: Retrieval-Augmented Classification & Generational Convolution | **Lectures 25-27** | Mon 26 Oct - Fri 30 Oct 2026 | [Lewis et al., *“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”*](https://arxiv.org/abs/2005.11401); [scikit-learn Example: *“Sample Pipeline for Text Feature Extraction and Evaluation”*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html); [scikit-learn *Pipeline & FeatureUnion Documentation*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html) |

---

## [Lecture 25: Modeling: Retrieval-Augmented Classification](../../lectures/lecture-25.md) (Mon 26 Oct 2026)

1. **The Retrieval-Augmented Paradigm:** Deconstructing the RAG architecture (Lewis et al.) and how integrating external knowledge bases stabilizes zero-shot and few-shot classification.
2. **Dense vs. Sparse Retrieval:** Contrasting BM25 (lexical) with dense vector embeddings for surfacing semantically relevant context anchors.
3. **Prompt Engineering for Classification:** Designing rigid, instruction-tuned prompts that constrain LLM output to valid class labels based exclusively on retrieved context.
4. **Addressing Hallucination:** Establishing evaluation criteria and temperature bounds to prevent LLMs from generating classification rationale outside the retrieved text.
5. **MP8 Release:** Introduction to the MP8 constraints, mapping the dataset and required retrieval-classification pipeline.
* **Assigned Reading:** [Lewis et al., *“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”* (arXiv:2005.11401)](https://arxiv.org/abs/2005.11401)

---

## [Lecture 26: Feature Extraction Pipelines](../../lectures/lecture-26.md) (Wed 28 Oct 2026)

1. **The scikit-learn Pipeline:** Constructing deterministic, reproducible feature extraction pipelines that prevent data leakage between training and testing sets.
2. **Text Vectorization:** Implementing `TfidfVectorizer` and `CountVectorizer` for baseline model comparison against embedding-based methods.
3. **Dimensionality Reduction:** Applying `TruncatedSVD` and `PCA` within the pipeline to optimize feature spaces for classical classifiers.
4. **Model Chaining:** Linking feature extractors directly to estimators (e.g., Logistic Regression, SVM) within a single `Pipeline` object.
5. **Hyperparameter Tuning:** Utilizing `GridSearchCV` over pipeline parameters to optimize both extraction weights and estimator bounds simultaneously.
* **Assigned Reading:** [scikit-learn Example: *“Sample Pipeline for Text Feature Extraction and Evaluation”*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

---

## [Lecture 27: Generational Convolution Models Lab; Wrap-Up](../../lectures/lecture-27.md) (Fri 30 Oct 2026)

1. **Generational Drift Modeling:** Applying time-series and rolling-window convolutions to track semantic and sentiment drift across generational cohorts.
2. **Lab Setup:** Initializing the environment and loading the temporal datasets for the convolution exercise.
3. **Implementing the Convolution:** Authoring the script to execute temporal feature extraction and map the generational shift.
4. **Integration with Classification:** Feeding the output of the generational convolution back into the classification pipeline to improve temporal accuracy.
5. **MP 7 Debrief & Wrap-Up:** Reviewing the MP 7 (submitted prior day) solutions and verifying readiness for the Module 9 Evaluation phase.
* **Assigned Reading:** [Lewis et al. (RAG)](https://arxiv.org/abs/2005.11401); [scikit-learn *Pipeline & FeatureUnion Documentation*](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)