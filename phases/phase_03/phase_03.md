<!--
  Template Note: This file serves as the canonical instantiation for phase_03.md.
  Generic Templatized Link Formats (Relative GFM):
   - Module directory/file link: `../../modules/module_05/` or `../../modules/module_05/module_05.md`
   - Lecture markdown link: `../../lectures/lecture_14.md`
   - Sibling phase link: `../../phases/phase_02/`
  
  Note: The assigned readings for Phase 3 are the exact union of readings from Module 05 and Module 06.
-->

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Description | Modules | Date Range | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 3:** Scrub, Embed & Classify | Data scrubbing, chunking, dense vector embeddings, VDB schema design, and GenAI few-shot classification pipelines | [`Module 05`](../../modules/module_05/) - [`Module 06`](../../modules/module_06/) | Mon 28 Sep - Fri 16 Oct 2026 | [Jurafsky & Martin, *SLP3* Chs. 6, 8, 10, 11](https://web.stanford.edu/~jurafsky/slp3/11.pdf); [Sentence Transformers](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html); [FAISS / Milvus](https://github.com/facebookresearch/faiss); [Hugging Face Transformers Task Guide](https://huggingface.co/docs/transformers/en/tasks/sequence_classification); [scikit-learn Text Data Tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) |

---

## 📖 Phase Overview & Objectives

* **Core Pedagogical Theme:** Transitioning from raw data ingestion (Obtain) to structured text chunking, vector space modeling, semantic indexing, and Large Language Model classification (Scrub & Embed phase of the OSEMN framework).
* **Included Modules:** 
  * [`Module 05`](../../modules/module_05/): Scrub: Chunking, Embedding Generation & VDB Schema Design (Lectures 14–16)
  * [`Module 06`](../../modules/module_06/): GenAI & LLMs: Candidates, Code, Classification (Lectures 17–21)
* **Phase Deliverables / Milestones:** Problem Set 4 Proposal (`PS 4`), Machine Problem 3 (`MP 3` due), Problem Set 6 (`PS 6`), Machine Problem 5 (`MP 5`), and Machine Problem 7 (`MP 7`).

---

## 🗂️ Phase Structure (Included Modules)

| Module Directory | Topic / Description | Lectures | Date Range | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| [`module_05/`](../../modules/module_05/) | **Scrub: Chunking, Embedding Generation & VDB Schema Design:** Recursive character chunking, boundary problem mitigation, vector space models, Sentence Transformers, and FAISS/Milvus vector database schema design. | Lectures 14–16 | Mon 28 Sep - Fri 02 Oct 2026 | [Jurafsky & Martin, *SLP3* Ch. 11](https://web.stanford.edu/~jurafsky/slp3/11.pdf); [Sentence Transformers Documentation](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html); [Meta AI FAISS & Milvus Docs](https://github.com/facebookresearch/faiss) |
| [`module_06/`](../../modules/module_06/) | **GenAI & LLMs: Candidates, Code, Classification:** Neural language modeling, transformer architecture, prompt engineering, few-shot trope/genre classification, embedding-backed classifiers, and Hugging Face pipeline integration. | Lectures 17–21 | Mon 05 Oct - Fri 16 Oct 2026 | [Jurafsky & Martin, *SLP3* Chs. 6, 8, 10](https://web.stanford.edu/~jurafsky/slp3/6.pdf); [Hugging Face Transformers Task Guide](https://huggingface.co/docs/transformers/en/tasks/sequence_classification); [scikit-learn Tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) |
