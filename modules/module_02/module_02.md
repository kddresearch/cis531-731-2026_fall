# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **[Phase 1](../../phases/phase_01/):** Foundations & Tooling | **Module 02:** Cloud Tools, DevContainers & AI/LLM Tooling | **Lectures 05-07** | Fri 04 Sep - Fri 11 Sep 2026 |

---

## [Lecture 05: Data Scrubbing & Early Exploration](../../lectures/lecture_05.md) (Fri 04 Sep 2026)

1. **The Scrub Phase & Raw Data Realities:** Managing raw, hostile data containing nulls, malformed strings, and artifacts following Miner & Shook Chapter 5.
2. **PySpark DataFrame Immutability & Transformations:** Applying transformational pipelines via `withColumn`, handling nulls (`drop`/`fill`), and string normalization (`lower`, `regexp_replace`).
3. **Domain-Specific Chunking (VDB Track):** Implementing semantic sentence/paragraph chunking and `explode()` to respect token constraints without breaking context.
4. **ASR Transcript Normalization (ASR Track):** Filtering disfluencies ("ums", "ahs"), stripping punctuation, and handling rolling stream deduplication.
5. **Exploratory Data Analysis (EDA) & Baselines:** Triggering actions (`describe()`, `groupBy`, `count`) and aggregating on-cluster before pulling data via `toPandas()` to establish normal baselines.

---

## [Lecture 06: DevContainers & Docker](../../lectures/lecture_06.md) (Wed 09 Sep 2026)

1. **The "It Works On My Machine" Dilemma:** Overcoming dependency hell and system drift across localized development environments.
2. **Virtual Machines vs. Containers:** Comparing heavyweight hypervisors (VMware/VirtualBox) with OS-level virtualization sharing the host kernel (Docker).
3. **Docker Fundamentals & Immutability:** Distinguishing read-only static blueprints (Images) from running execution processes (Containers).
4. **Infrastructure as Code (`Dockerfile`):** Structuring build scripts using `FROM`, `RUN`, `COPY`, and `CMD` with strategic layer caching optimization.
5. **Volumes & DevContainers:** Mounting local directories via bind mounts for data persistence and configuring `devcontainer.json` for integrated VS Code development.

---

## [Lecture 07: AI/LLM Tooling Overview](../../lectures/lecture_07.md) (Fri 11 Sep 2026)

1. **Proprietary APIs vs. Open-Weight Models:** Weighing state-of-the-art closed models (OpenAI, Anthropic) against local data sovereignty with open-weight models (Llama 3).
2. **Abstraction Layers of AI Tooling:** Navigating hardware layers (CUDA), inference engines, orchestration frameworks, and application UIs.
3. **Inference Runtimes & Quantization:** Utilizing lightweight CLI execution (Ollama) or high-throughput batch serving (vLLM), alongside 4-bit/8-bit GGUF quantization to fit models within VRAM constraints.
4. **AI-Assisted Development Environments:** Leveraging GitHub Copilot plugins and AI-first IDEs (Cursor) for structural code generation and refactoring.
5. **RAG Orchestration & Epistemic Verification:** Connecting components via LangChain/LlamaIndex, applying RAG to bypass hallucinations, and maintaining responsibility under the "Upper Beam" engineering standard.
