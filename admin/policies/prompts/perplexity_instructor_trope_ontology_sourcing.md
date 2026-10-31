# Perplexity RLC + SEA Prompt: Canonical Instructor Trope & Caller-Vibe Ontology (CIS 531/731)
**Prompt Path:** `admin/policies/prompts/perplexity_instructor_trope_ontology_sourcing.md`
**Target Output Path:** `schema/instructor_trope_ontology_v1.md` and `schema/instructor_trope_schema_v1.json`

```text
[SYSTEM ROLE: PERPLEXITY RESEARCH LITERATURE CRITIC (RLC) & SYSTEMS ENGINEERING AUDITOR (SEA)]

We are finalizing the canonical instructor-provided ontology and JSON Schema (Draft 2020-12) for the default term-project pipeline in CIS 531/731 (Programming Techniques for Data Science and Analytics, Fall 2026).

### 1. ARCHITECTURAL & PEDAGOGICAL CONTEXT
The course-default analytics pipeline demonstrates how a bi-encoder (`SentenceTransformer('all-MiniLM-L6-v2')`, 384-D) and a few-shot/RAG classifier (`facebook/bart-large-mnli` and instruction-tuned small LLMs) bridge asymmetric modalities across two tracks:
- **Track 1 (ASR Broadcast Stream Track):** Spoken radio call-in requests and DJ/caller voice messages modeled on SiriusXM Alt Nation ("Alt-18" countdown call-ins), where callers describe personal moods, life events, or "vibes" (e.g., "The caller sounds really upset about their recent breakup", "I love this Cage the Elephant track, it reminds me of summer", "Sometimes I feel like our whole generation is just out of time").
- **Track 2 (VDB Text Corpus Track):** Song lyric excerpts, literary poetry archives (including the public-domain LibriVox WWI poetry benchmark containing Wilfred Owen's "Anthem for Doomed Youth"), and media synopses tagged by release decade (`1960s`–`2020s`) without reproducing full copyrighted lyrics.

### 2. BACKWARDS-COMPATIBILITY CONSTRAINTS (LABS 3b, 5, 6, AND MP 5–10)
To ensure 100% backwards compatibility with Labs 3b, 5, and 6 (already completed by students) while satisfying the 8–12 class requirement of MP 7, MP 9, and MP 10, the ontology MUST contain exactly **10 primary classes (`TR-01` through `TR-10`) plus 1 explicit out-of-distribution abstention class (`TR-00: UNKNOWN_OOD`)**:
- ** Tier A — The 4 Legacy Lab 5 / Lab 6 Anchors (Must be retained verbatim or as exact aliases):**
  1. `TR-01`: `Chosen One Fantasy` (Heroic destiny, prophecy, mythic burden)
  2. `TR-02`: `Doomed Youth / Tragedy` (Premature loss of innocence, existential dread, war/generational tragedy — anchors both Wilfred Owen's poem and modern "doomed youth" indie lyrics)
  3. `TR-03`: `Summer Romance` (Fleeting seasonal intimacy, nostalgic warmth, bittersweet departure)
  4. `TR-04`: `Sci-Fi Cyberpunk` (Technological alienation, dystopian future, synthetic identity)
- **Tier B — 6 Alt-18 Caller Vibe & Lyrical Trope Classes (Bridging Caller Speech to Song Lyrics):**
  5. `TR-05`: `Heartbreak & Breakup Recovery` (Post-relationship grief, cathartic venting, moving on)
  6. `TR-06`: `Generational Angst / Out of Time` (Quarter-life crisis, societal disillusionment, temporal drift across decades)
  7. `TR-07`: `Coming-of-Age & College Transition` (Leaving hometowns, adolescent transition, identity formation)
  8. `TR-08`: `Late-Night Driving & Escapism` (Wanderlust, highway solitude, restless motion)
  9. `TR-09`: `Social Alienation & Burnout` (Emotional exhaustion, outsider perspective, numbness)
  10. `TR-10`: `Defiant Euphoria & Anthem` (Collective catharsis, resilience, high-energy rebellion)
- **Abstention Class:**
  0. `TR-00`: `UNKNOWN / OUT OF DISTRIBUTION` (Triggered when maximum cosine similarity < 0.35 or when input is off-domain noise, e.g., an unrelated food order).

### 3. REQUIRED DELIVERABLES (EMIT IN CLEAN GITHUB-FLAVORED MARKDOWN)
1. **Literature Grounding (RLC Pass):** Cite 4–6 foundational references in Music Information Retrieval (MIR) mood/theme taxonomies (e.g., Hu & Downie MIREX mood clusters, Laurier et al., Genius/lyric trope studies) and asymmetric semantic search / zero-shot NLI verbalization (Reimers & Gurevych SBERT; Yin et al. zero-shot NLI) that justify mapping conversational caller "vibe" queries to lyrical trope definitions in shared embedding space.
2. **Canonical Ontology Codebook Table (`schema/instructor_trope_ontology_v1.md`):** For all 10 classes (`TR-01`–`TR-10`) plus `TR-00`, provide:
   - `trope_id`, `canonical_label`, and `legacy_lab5_alias` (if applicable)
   - `reference_description` (the exact 1–2 sentence bi-encoder anchor string for `all-MiniLM-L6-v2` in Lab 6 / MP 7)
   - `llm_verbalizer_tokens` (for MP 7 constrained few-shot decoding)
   - `asr_caller_exemplar` (a synthetic 1-sentence Alt-18 radio caller request)
   - `vdb_lyric_or_poetic_exemplar` (a public-domain or non-infringing 1-sentence thematic paraphrase)
   - `boundary_decision_rule` (how human annotators in MP 9 distinguish this class from its nearest neighbor, e.g., `TR-03 Summer Romance` vs. `TR-05 Heartbreak`, or `TR-02 Doomed Youth` vs. `TR-06 Generational Angst`).
3. **JSON Schema Draft 2020-12 (`schema/instructor_trope_schema_v1.json` — SEA Pass):** Emit a valid, copy-pasteable JSON Schema (Draft 2020-12) that extends the MP 5 `TranscriptChunk` / `CorpusChunk` record (`record_id`, `track`, `source_id`, `ts_start`, `ts_end`, `text`, `ingest_ts`, `license_class`) with VDB & ontology fields (`chunk_id`, `parent_doc_id`, `release_decade`, `embedding_model_id`, `vector_dim`, `trope_id`, `trope_label`, `confidence_score`, `label_source` in `{"gold", "silver", "zero_shot", "knn_prototype"}`), stating all deterministic validation properties in plain language for the grader to check by hand or automatically.
```
