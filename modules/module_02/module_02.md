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
| **[Phase 1](../../phases/phase_01/):** Foundations & Tooling | **Module 02:** Cloud Tools, DevContainers & AI/LLM Tooling | **Lectures 05-07** | Fri 04 Sep - Fri 11 Sep 2026 | [Brett et al., *Research Software Engineering*](https://rse-book.github.io/); [Docker Documentation](https://docs.docker.com/get-started/); [LiteLLM & Milvus Docs](https://docs.litellm.ai/docs/proxy/virtual_keys) |

---

## [Lecture 05: Data Scrubbing & Early Exploration](../../lectures/lecture_05.md) (Fri 04 Sep 2026)

1. **The Scrub Phase & Raw Data Realities:** Managing raw, hostile data containing nulls, malformed strings, and artifacts following Miner & Shook Chapter 5.
2. **PySpark DataFrame Immutability & Transformations:** Applying transformational pipelines via `withColumn`, handling nulls (`drop`/`fill`), and string normalization (`lower`, `regexp_replace`).
3. **Domain-Specific Chunking (VDB Track):** Implementing semantic sentence/paragraph chunking and `explode()` to respect token constraints without breaking context.
4. **ASR Transcript Normalization (ASR Track):** Filtering disfluencies ("ums", "ahs"), stripping punctuation, and handling rolling stream deduplication.
5. **Exploratory Data Analysis (EDA) & Baselines:** Triggering actions (`describe()`, `groupBy`, `count`) and aggregating on-cluster before pulling data via `toPandas()` to establish normal baselines.
* **Assigned Reading:** [Brett et al., *Research Software Engineering* (Chs. 1–2: Environments & Reproducibility)](https://rse-book.github.io/)

---

## [Lecture 06: DevContainers & Docker](../../lectures/lecture_06.md) (Wed 09 Sep 2026)

1. **The "It Works On My Machine" Dilemma:** Overcoming dependency hell and system drift across localized development environments.
2. **Virtual Machines vs. Containers:** Comparing heavyweight hypervisors (VMware/VirtualBox) with OS-level virtualization sharing the host kernel (Docker).
3. **Docker Fundamentals & Immutability:** Distinguishing read-only static blueprints (Images) from running execution processes (Containers).
4. **Infrastructure as Code (`Dockerfile`):** Structuring build scripts using `FROM`, `RUN`, `COPY`, and `CMD` with strategic layer caching optimization.
5. **Volumes & DevContainers:** Mounting local directories via bind mounts for data persistence and configuring `devcontainer.json` for integrated VS Code development.
* **Assigned Reading:** [Docker Documentation: *Get Started*](https://docs.docker.com/get-started/); [Official `pytorch/pytorch` Docker Hub](https://hub.docker.com/r/pytorch/pytorch); [NVIDIA Container Toolkit Install Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

---

## [Lecture 07: AI/LLM Tooling Overview](../../lectures/lecture_07.md) (Fri 11 Sep 2026)

1. **Proprietary APIs vs. Open-Weight Models:** Weighing state-of-the-art closed models (OpenAI, Anthropic) against local data sovereignty with open-weight models (Llama 3).
2. **Abstraction Layers of AI Tooling:** Navigating hardware layers (CUDA), inference engines, orchestration frameworks, and application UIs.
3. **Inference Runtimes & Quantization:** Utilizing lightweight CLI execution (Ollama) or high-throughput batch serving (vLLM), alongside 4-bit/8-bit GGUF quantization to fit models within VRAM constraints.
4. **AI-Assisted Development Environments:** Leveraging GitHub Copilot plugins and AI-first IDEs (Cursor) for structural code generation and refactoring.
5. **RAG Orchestration & Epistemic Verification:** Connecting components via LangChain/LlamaIndex, applying RAG to bypass hallucinations, and maintaining responsibility under the "Upper Beam" engineering standard.
* **Assigned Reading:** [LiteLLM Proxy: *Virtual Keys*](https://docs.litellm.ai/docs/proxy/virtual_keys) & [*Users/Teams Budgets*](https://docs.litellm.ai/docs/proxy/users); [Milvus *Quickstart*](https://milvus.io/docs/quickstart.md); [OpenAI *Whisper* README](https://github.com/openai/whisper)
