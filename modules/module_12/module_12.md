# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../../phases/phase_05/):** Evaluate & Deploy | **Module 12:** PaaS/IaaS, MLOps/AIOps & Drift Monitoring | **Lectures 37-39** | Mon 30 Nov - Fri 04 Dec 2026 | [ML-Ops.org, *MLOps Principles*](https://ml-ops.org/content/mlops-principles); [MLflow Tracking Guide](https://mlflow.org/docs/latest/ml/tracking/); [FastAPI Docker Deployment](https://fastapi.tiangolo.com/deployment/docker/)

---

## [Lecture 37: PaaS/IaaS, MLOps/AIOps & Drift Monitoring](../../lectures/lecture_37.md) (Mon 30 Nov 2026)

1. **MLOps Core Principles:** Moving machine learning models from local scripts to robust, automated production pipelines.
2. **Infrastructure Abstraction:** Understanding the trade-offs between Platform-as-a-Service (PaaS) and Infrastructure-as-a-Service (IaaS) for AI workloads.
3. **Concept & Data Drift:** Detecting degradation in model performance caused by shifting real-world data distributions.
4. **Continuous Monitoring:** Implementing automated health checks and telemetry logging for deployed endpoints.
5. **Reproducible Deployments:** Ensuring environment parity between development, staging, and production clusters.
* **Assigned Reading:** [ML-Ops.org, *“MLOps Principles”*](https://ml-ops.org/content/mlops-principles)

---

## [Lecture 38: MLflow Tracking, Lineage & Model Registry](../../lectures/lecture_38.md) (Wed 02 Dec 2026)

1. **Experiment Tracking:** Logging parameters, metrics, and artifacts systematically using MLflow
2. **Data and Code Lineage:** Tracing every deployed model back to its exact training dataset, git commit, and configuration.
3. **Model Registry Workflows:** Managing model staging, versioning, promotion, and archiving in enterprise environments.
4. **Artifact Storage Backends:** Configuring secure, scalable storage for model weights and evaluation plots.
5. **Collaborative Experimentation:** Enabling multi-developer visibility into shared lab model training runs.
* **Assigned Reading:** [MLflow Documentation: *MLflow Tracking*](https://mlflow.org/docs/latest/ml/tracking/)

---

## [Lecture 39: Service Containerization & Wrap-Up](../../lectures/lecture_39.md) (Fri 04 Dec 2026)

1. **Containerizing Inference Services:** Packaging Python machine learning pipelines into standardized Docker containers
2. **FastAPI Microservices:** Exposing models via high-performance asynchronous REST endpoints.
3. **Resource Bounding:** Setting CPU, memory, and GPU constraints on containerized services to prevent cluster starvation.
4. **Module 12 Wrap-Up:** Consolidating MLOps tracking, containerization, and drift monitoring workflows.
5. **Milestone Closing:** Finalizing preparations for HW 12 release and term project completion.
* **Assigned Reading:** [FastAPI Documentation: *“FastAPI in Containers — Docker”*](https://fastapi.tiangolo.com/deployment/docker/); [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/)