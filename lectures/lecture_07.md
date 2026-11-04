# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
**[Phase 1](../phases/phase_01/):** Foundations & Tooling | **[Module 02](../modules/module_02/):** Cloud Tools, DevContainers & AI/LLM Tooling | **Lecture 07:** AI/LLM Tooling Overview | Fri 11 Sep 2026 |

---

## Slide 1: AI/LLM Tooling Overview
### The Modern AI Developer Stack
* **Course Context:** CIS 531/731 - Lecture 07 (Module 02)
* **Core Topic:** Operational overview of AI and LLM toolchains, abstraction layers, and developer ecosystems
* **Assigned Reading:** LiteLLM Proxy (*Virtual Keys* & *Users/Teams Budgets*); Milvus *Quickstart*; OpenAI *Whisper* README
* **Tech Stack:** Proprietary APIs, Open-Weight Models, vLLM, Ollama, LangChain

**Speaker Notes:**
Welcome to Lecture 7. Over the past two sessions, we established the infrastructure required to run modern data science workloads—cloud compute and Docker containers. Today, we map out the tooling ecosystem for the fastest-moving sector in our field: Large Language Models (LLMs). This is not a lecture on how neural networks are trained; this is an operational overview of the abstraction layers, frameworks, and tools you will use to integrate Generative AI into your software and research pipelines.

---

## Slide 2: The LLM Ecosystem Map
### Proprietary APIs vs. Open-Weight Models
* **Proprietary / Closed Models:**
  * **Examples:** OpenAI (GPT-4o), Anthropic (Claude 3.5 Sonnet), Google (Gemini 1.5 Pro).
  * **Delivery:** Accessed strictly via REST APIs over the internet.
  * **Pros:** State-of-the-art reasoning, massive context windows, zero hardware overhead.
  * **Cons:** Vendor lock-in, recurring token costs, and strict data privacy concerns.
* **Open-Weight Models:**
  * **Examples:** Meta (Llama 3), Mistral (Mixtral), Alibaba (Qwen).
  * **Delivery:** Model weights are downloaded and executed on your own hardware.
  * **Pros:** Absolute data sovereignty, offline execution, fine-tuning capability.
  * **Cons:** Requires significant local compute/VRAM, higher engineering overhead to deploy.

**Speaker Notes:**
The first decision in any AI-integrated project is whether to rent the model or host the model. Proprietary APIs give you the smartest models instantly, but you are sending your research data to a third-party server. Open-weight models—often colloquially but inaccurately called "open source"—allow you to download the actual model weights. You run them locally, meaning your data never leaves your machine, which is often a strict legal requirement in funded research.

---

## Slide 3: Abstraction Layers of AI Tooling
### From Hardware to Interface
* Building an AI application requires navigating multiple layers of abstraction:
  1. **Hardware Layer:** Nvidia CUDA, Apple Metal, Google TPUs.
  2. **Inference Engine:** vLLM, llama.cpp, TensorRT-LLM (loads the weights and executes the math efficiently).
  3. **Orchestration Framework:** LangChain, LlamaIndex (connects the model to databases, APIs, and memory).
  4. **Application UI:** Streamlit, Gradio, Next.js (what the end-user actually clicks and sees).

**Speaker Notes:**
A common point of confusion is mixing up these layers. Llama 3 is a model. Ollama is an inference engine. LangChain is an orchestration framework. You cannot "build a model in LangChain," and Ollama does not have a native web interface. As research software engineers, you must understand exactly which layer of the stack a specific tool targets so you can compose them together efficiently.

---

## Slide 4: Local Execution & Inference Frameworks
### Running Open-Weight Models
* **Inference Engines (The Runtime):**
  * **Ollama:** The easiest entry point. Wraps `llama.cpp` to run models locally on CPUs and GPUs via a simple Docker-like CLI (`ollama run llama3`).
  * **vLLM:** High-throughput, production-grade serving engine for GPUs. Optimized for massive batch processing and concurrency.
  * **HuggingFace Transformers:** The underlying Python library for native model loading, fine-tuning, and granular execution control.

**Speaker Notes:**
If you want to run Llama 3 on your laptop right now, the tool you want is Ollama. It abstracts away all the complex C++ compilation and dependency hell. However, if you are deploying a model on a massive AWS GPU instance to serve hundreds of concurrent users, you would use vLLM, which utilizes advanced memory management techniques like PagedAttention to maximize throughput.

---

## Slide 5: Hardware Constraints & Quantization
### The VRAM Floor
* **The VRAM Bottleneck:** LLMs are memory-bound, not compute-bound. The model weights must fit entirely into your GPU's Video RAM (VRAM) to run at acceptable speeds.
* **Rule of Thumb:** A standard 8-billion parameter (8B) model at full precision requires ~16GB of VRAM.
* **Quantization:** Compressing the model weights from 16-bit floats to 8-bit or 4-bit integers (e.g., GGUF, AWQ, EXL2 formats).
* **The Tradeoff:** Shrinks an 8B model to fit in 6GB of VRAM with minimal loss in reasoning capability.

**Speaker Notes:**
Hardware dictates what you can run. If your laptop only has an 8GB GPU, you cannot load a full-precision 8B model, and it will offload to your system RAM, slowing inference to a crawl. The industry solution is Quantization. By rounding the massive arrays of floating-point numbers into 4-bit integers, we dramatically shrink the model's footprint. The resulting models (often packaged as GGUF files) allow us to run incredibly capable AI on consumer gaming laptops.

---

## Slide 6: AI-Assisted Development Environments
### The IDE as an AI Agent
* **GitHub Copilot (The Plugin):** Integrates into VS Code/IntelliJ. Provides autocomplete and inline chat based on the open file context.
* **Cursor (The AI-First IDE):** A fork of VS Code where AI is baked into the core architecture. Can read the entire codebase context simultaneously.
* **Features:** Inline code generation, automated refactoring, and natural language terminal commands.

**Speaker Notes:**
We are moving beyond standard autocomplete. Tools like GitHub Copilot operate as plugins, guessing your next lines of code based on the file you have open. Newer tools like Cursor are built from the ground up to understand your entire project structure. You can highlight a function, press Cmd+K, and type "rewrite this using Spark Structured Streaming instead of pandas," and it will execute the refactor across multiple files.

---

## Slide 7: Generation Best Practices
### Effectively Directing the AI
* **Context is King:** The AI only knows what is in its context window. Open the relevant files or explicitly tag the documentation it needs to reference.
* **Test-Driven Generation:** Ask the AI to write the unit tests *first*. Once you verify the tests make sense, ask it to write the code that passes those tests.
* **Iterative Refinement:** Do not ask for a 500-line architecture in one prompt. Build function by function.
* **Rubber Ducking:** Use the chat interface to explain a bug to the AI before asking for code; often, the act of formatting the prompt solves the problem.

**Speaker Notes:**
AI coding tools are incredibly fast typists, but they lack global project architecture knowledge. If you give a vague prompt, you will get hallucinated, generic code. The best practice in our workflow is Test-Driven Generation. Tell the LLM: "Write Pytest functions for a data cleaner that handles nulls and drops duplicates." Review the tests yourself. Once the tests are solid, tell the LLM, "Now write the cleaner class to pass these tests."

---

## Slide 8: LLM Orchestration
### Tying the Stack Together
* **LangChain & LlamaIndex:**
  * The dominant Python/TypeScript frameworks for building AI applications.
  * **Chains:** Linking multiple components sequentially (e.g., Prompt Template $\rightarrow$ LLM $\rightarrow$ Output Parser).
  * **Tools/Agents:** Granting the LLM the ability to execute Python code, search the web, or query SQL databases dynamically.
  * **Memory:** Managing conversation history since LLMs are inherently stateless APIs.

**Speaker Notes:**
An LLM by itself is just a text completion engine; it has no memory and cannot browse the web. Orchestration frameworks like LangChain provide the connective tissue. They allow you to define a "Chain" where the user's input is injected into a strict prompt template, sent to the model, and then the raw text output is mathematically parsed back into a JSON object that the rest of your Python software can actually use.

---

## Slide 9: Foundations of RAG
### Retrieval-Augmented Generation
* **The Problem:** LLMs hallucinate facts and do not know proprietary or recent information (their training data has a cutoff date).
* **The Solution:** RAG bypasses retraining.
* **The Workflow:**
  1. User asks a question.
  2. System searches a local database for relevant documents.
  3. System injects those documents into the LLM's prompt.
  4. LLM answers *using only the provided context*.
* *Note: We will build this pipeline extensively in Modules 5 and 8.*

**Speaker Notes:**
If you ask an LLM about internal lab data it has never seen, it will confidently lie to you. We solve this with Retrieval-Augmented Generation, or RAG. Instead of teaching the model the facts, we treat the model like an open-book test taker. We search our database, grab the relevant paragraphs, and paste them into the prompt, saying, "Answer the user's question based strictly on this text." This drastically reduces hallucinations and provides traceable citations.

---

## Slide 10: Epistemic Verification & Responsibility
### The "Upper Beam" Principle
* **AI is a Sub-Processor:** LLMs output statistically probable tokens, not objective truths. They possess no epistemic certainty.
* **The "Confidently Wrong" Fallacy:** A well-formatted, authoritative-sounding output is not proof of correctness.
* **The Upper Beam:** As the Research Software Engineer, you are the final arbiter of truth. The AI is a junior assistant; *you* own the liability for the committed code.
* **Verification:** Never push generated code or data pipelines without structural audits, unit tests, and independent verification of the logic.

**Speaker Notes:**
We end this module with a critical professional standard. You will rely heavily on these tools to speed up boilerplate and architecture. But you must remember that Large Language Models are designed to sound confident, even when they are hallucinating entirely fake API endpoints or library functions. You are the "Upper Beam" in the structural load path. You hold the liability. If a hallucinated pipeline corrupts your dataset, you cannot blame Copilot. You must audit everything it writes.
