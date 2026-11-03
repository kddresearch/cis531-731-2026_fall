# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 5:** Evaluate & Deploy | **Module 13:** Special Topics — Agentic AI Systems, Frontier Directions & Course Synthesis | **Lectures 40-42** | Mon 07 Dec - Fri 11 Dec 2026 |

---

## Lecture 40: Special Topics: Agentic AI Systems & Testing (Mon 07 Dec)

1. **Agentic AI Workflows & Tool-Use Orchestration:** Deconstructing multi-step agentic architectures that combine dense vector retrieval, structured schema validation, and tool-calling loops with deterministic fallback gates.
2. **Test-Size Taxonomy (*Software Engineering at Google*, Chs. 11–12):** Partitioning data-science verification suites into small Hermetic Unit Tests (metric math, regex normalizers, contracts), medium Integration Tests (FAISS indexing, PySpark windows), and large End-to-End System Tests (`make verify`).
3. **Deterministic Testing of Stochastic & LLM Pipelines:** Isolating non-deterministic LLM and external API calls behind mock fixtures, cached response ledgers, and fixed-seed CPU baseline models during continuous integration runs.
4. **Continuous Integration Gates for Data & Gold Standards:** Enforcing automated pre-merge CI checks that validate Draft 2020-12 JSON schemas, verify the 50–200 pooled gold-standard row bounds, and reject unverified full-file overwrites.
5. **Dead-Week Extra-Credit Presentations Kickoff:** Launching optional extra-credit term-project presentations after lecture, including each team member's individual responses to the three standard technical reflection questions.

---

## Lecture 41: Special Topics: Frontier Directions in Responsive Analytics (Wed 09 Dec)

1. **AI API Gateway Governance (`LiteLLM` & `Bifrost`):** Architecting multi-tenant AI gateways with team-scoped virtual keys, immutable model allow-lists, RPM/TPM rate controls, and fail-closed PostgreSQL/Redis budget reservations.
2. **Hybrid Edge-to-Cloud & Local Open-Weight Routing:** Designing cost-aware inference routers that automatically fail over from commercial cloud APIs to self-hosted open-weight models (`vLLM`, local CPU Whisper, and Sentence Transformers) when team budgets exhaust.
3. **Streaming Multimodal & Low-Latency Retrieval Frontiers:** Extending micro-batch ASR and static vector indexes toward sub-second streaming speech-to-vector indexing and incremental HNSW/IVF graph maintenance.
4. **Neurosymbolic Guardrails & Hallucination Prevention:** Combining neural embeddings and LLM generators with formal ontology constraints (JSON Schema validation, competency questions, and symbolic contract checks) to prevent hallucination laundering.
5. **Benchmarking Against Classical Text Baselines:** Using reproducible `scikit-learn` TF-IDF and linear/ensemble pipelines (*scikit-learn Text Examples Gallery*) as permanent sanity checks against over-parameterized neural architectures.

---

## Lecture 42: Special Topics: Course Synthesis & Wrap-Up (Fri 11 Dec)

1. **End-to-End OSEMN Lifecycle Synthesis (`[O] -> [S] -> [E] -> [M] -> [N]`):** Tracing the complete architecture of both course tracks—from Bronze stream/corpus ingestion and FAISS/Whisper scrubbing to UMAP exploration, RAG and generational-convolution modeling, and Benjamini–Hochberg-controlled inferential interpretation.
2. **Final `hw12-final` Reproducibility Package Checklist:** Verifying that `REPORT.pdf` (at most 12 pages), `Makefile` (`make verify`), digest-pinned `Dockerfile` and lockfile, MLflow lineage export, serving smoke test, and `GenAI.pdf` audit log are complete and tagged under `hw12-final`.
3. **Gold-Standard Pooling & Inter-Annotator Agreement Verification:** Confirming that team projects pool their adjudicated MP 9 gold files into the required 50–200 labeled-example range with reported 2-way/3-way Cohen's $\kappa$ confidence intervals (or $\le 1\%$ validation fraction for solo projects).
4. **Sustainable Research Software Engineering Beyond the Course:** Carrying forward core engineering practices from *Software Engineering at Google* and *MLOps Principles*—immutable digest pinning, contract-checked interfaces, and FAIR provenance—into graduate research and production ML systems.
5. **Final Submission Window & Course Closeout:** Reviewing the hard Finals-Week deadline (**Mon 14 Dec 2026, 11:59 PM CST**) for `HW 12: Final Project Deliverables` and completing course evaluations and repository archival.
