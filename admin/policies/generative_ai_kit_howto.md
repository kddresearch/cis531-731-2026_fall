# How to Prime the Generative AI Kit (v1.0)
**Path:** `admin/policies/generative_ai_kit_howto.md`

To use the Generative AI Kit effectively, you must "ground" the AI in the reality of this course. If you ask a generic AI "Is my project good?", it will hallucinate a positive response. You must force the AI to read the **05_term_project_taxonomy.md** and **06_term_project_sourcing_guide.md** files before evaluating your ideas.

Below are the exact procedures for priming the five major platforms. 

**Instructor Recommendation:** 
*   Use **ChatGPT / M365 Copilot** or **Claude / Qwen** for general QA, architectural reasoning, and drafting. 
*   Use **Gemini** or **Perplexity** for sourcing, filtering, and ranking references interactively. This ensures you maintain *stakeholdership* in pre-vetting candidate datasets, cloud platforms, and toolchains before you commit to them.

---

### 1. ChatGPT or M365 Copilot
*Best for: General QA, methodology brainstorming, and robust Python code reasoning.*
*   **The Setup:** Open a new chat (GPT-4o or M365 Copilot). 
*   **Grounding:** Click the attachment (paperclip) icon. Upload both `05_term_project_taxonomy.md` and `06_term_project_sourcing_guide.md` as files.
*   **Priming:** Paste the `[SYSTEM INSTRUCTION]` block from the GenAI Kit into the chat box. Add: *"Read the two attached markdown files. Do not respond until you have fully ingested the course taxonomy and feasibility rubric. Once ready, ask me for my project category and dataset."*

### 2. Claude (Anthropic) or Qwen
*Best for: Deep context synthesis, strict adherence to formatting rubrics, and academic writing critique.*
*   **The Setup:** If using Claude, create a new "Project" (if on Pro) or a standard chat. 
*   **Grounding:** In a Claude Project, upload the `05` and `06` `.md` files to the "Project Knowledge" base. If using standard chat, attach the files directly.
*   **Priming:** Paste the `[SYSTEM INSTRUCTION]` into the "Custom Instructions" box of the Project, or as your first prompt. Claude is highly obedient to constraints; explicitly tell it: *"Act as a strict Socratic gatekeeper. Reject any proposed dataset that falls into Tier 3 of the sourcing guide."*

### 3. Gemini (Google)
*Best for: Massive context windows (Gemini 1.5 Pro) and interactive reference filtering.*
*   **The Setup:** Open Gemini Advanced (or Gemini 1.5 Pro via Google AI Studio).
*   **Grounding:** Use the `+` icon to upload the `05` and `06` `.md` files, or paste the raw text of both documents directly into the prompt if file uploads are restricted.
*   **Priming:** Paste the `[SYSTEM INSTRUCTION]` block. **Crucial:** Ask Gemini to actively rank and filter candidate datasets for your specific topic. *Example: "Based on the Tier 1/Tier 2 sourcing guide I provided, search for 3 candidate datasets for [My Topic] and rank them by how easily I can execute the 'Obtain' stage."*

### 4. Perplexity
*Best for: Live literature reviews, finding SOTA baselines, and discovering datasets with active links.*
*   **The Setup:** Open a new Perplexity Pro Search thread.
*   **Grounding:** Because Perplexity excels at web search but drops long context, use a condensed grounding. Attach the `06_term_project_sourcing_guide.md` file using the `Attach` button.
*   **Priming:** Use Perplexity specifically for the **Obtain** and **Literature** stages. *Prompt Example: "I am building a predictive model for CIS 531. Read the attached sourcing guidelines. Search Hugging Face and Kaggle for datasets matching [My Topic] that strictly meet the 'Tier 1 or Tier 2' requirements outlined in my document. Provide direct links."*

### 5. Grok (xAI)
*Best for: Real-time social data analysis, identifying trending topics, and rapid code generation.*
*   **The Setup:** Open a new Grok chat.
*   **Grounding:** Paste the raw text of the `05_term_project_taxonomy.md` directly into the prompt (Grok handles raw text pasting very well).
*   **Priming:** Combine the taxonomy with the system instruction. *Prompt Example: "Acting as the CIS 531 Research Design Coordinator, evaluate my idea for a [Insert Category] pipeline. Here is the course taxonomy: [Paste Taxonomy]."*
