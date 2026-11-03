# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 5:** Evaluate & Deploy | **Module 12:** PaaS/IaaS, MLOps/AIOps & Project Wrap-Up | **Lectures 37-39** | Mon 30 Nov - Fri 04 Dec 2026 |

---

## Lecture 37: PaaS/IaaS, MLOps/AIOps & Drift Monitoring (Mon 30 Nov)

1. **MLOps Lifecycle Principles & Joint Versioning:** Synchronizing reproducibility across four coupled axes—source code (Git commit SHA), runtime environment (`Dockerfile` digest and lockfile hash), data assets (Bronze/Silver/Gold SHA-256 hashes), and model configurations (*ML-Ops.org Principles*).
2. **PaaS/IaaS Compute Topologies & CPU Baseline Portability:** Architecting analytical pipelines that execute deterministically on the course's pinned CPU DevContainer baseline while supporting optional digest-pinned GPU overlays on campus or national HPC clusters.
3. **Distribution Shift Taxonomy (Covariate, Prior, & Concept Drift):** Distinguishing shifts in input audio or text embedding distributions from shifts in trope base rates or evolving cultural definitions across temporal windows.
4. **Statistical Drift Detection (PSI & Two-Sample KS Tests):** Implementing Population Stability Index (PSI) and two-sample Kolmogorov–Smirnov (KS) tests over feature, embedding, and confidence distributions with explicit numerical alert thresholds.
5. **Operational Drift Runbooks & Quota Failover:** Authoring production MLOps runbooks that define alert triggers, automatic failover to local CPU Whisper and baseline models upon external API quota exhaustion, and human-in-the-loop recalibration procedures.

---

## Lecture 38: MLflow Tracking, Lineage & Model Registry (Wed 02 Dec)

1. **MLflow Tracking Instrumentation:** Instrumenting training, retrieval, and evaluation pipelines (*MLflow Tracking Documentation*) to log hyperparameters, random seeds, shot counts, retrieval depths, and stratified metrics to a local or containerized tracking server.
2. **Cryptographic Provenance Tagging:** Recording the active Git commit SHA, dataset SHA-256 manifest, and dependency lockfile hash as immutable MLflow run tags to guarantee end-to-end lineage between code and reported tables.
3. **Artifact Logging & Multi-Run Ablation Comparison:** Persisting confusion matrices, reliability diagrams, UMAP projections, and `results.json` summaries as MLflow artifacts and querying across runs to verify ablation improvements.
4. **Model Registry & Stage Transitions:** Registering the final validated pipeline in the MLflow Model Registry with explicit semantic versioning and lifecycle stage transitions (`Staging` $\rightarrow$ `Production`).
5. **Automated Report-to-Ledger Reconciliation:** Auditing the final technical report (`REPORT.pdf`) against exported MLflow run logs so every headline metric, confidence interval, and p-value traces to a verifiable run ID.

---

## Lecture 39: Service Containerization & Wrap-Up (Fri 04 Dec)

1. **Containerized Serving Architectures:** Packaging the registered pipeline into a digest-pinned Docker container (*FastAPI in Containers — Docker*) exposing either an HTTP/CLI retrieval and classification service (VDB track) or a continuous Structured Streaming consumer (ASR track).
2. **Stateful Checkpointing & Restart Recovery (ASR Track):** Configuring PySpark Structured Streaming `checkpointLocation` directories and write-ahead logs and verifying clean, zero-data-loss restart recovery after a simulated process interruption.
3. **Deterministic Serving Smoke Tests (VDB & ASR Tracks):** Implementing automated health-check and smoke-test scripts that dispatch fixture requests to the containerized service and assert schema compliance, bounded latency, and valid predictions.
4. **The `make verify` Reproducibility Harness:** Constructing a top-level `Makefile` target (`make verify`) that validates container digests, executes unit and contract tests, enforces the 50–200 gold-standard range gate, and reproduces headline metrics within stated tolerance on the CPU baseline.
5. **Module 12 Wrap-Up & HW 12 Capstone Launch:** Completing PS 11 and the Take-Home Final Exam (due Fri 04 Dec) and launching the final HW 12 deliverables package (`hw12-final`, released Sat 05 Dec, due Mon 14 Dec).
