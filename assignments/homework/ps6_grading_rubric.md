# PS 6: Semantic Search, Chunking, & VDB Schema — Grading Rubric (30 Points Total)
**Course:** CIS 531/731 (Fall 2026) | **Instructor:** William H. Hsu

## Scoring Breakdown (30-Point Scale)

### Part 1: Chunking, Index, and Evaluation Analysis (15 Points / 50%)
* **Chunking Cost Model (6 pts):**
  * Evaluates and compares fixed-window (with stride $s$), sentence-boundary, and structure-aware chunking methods. Accurately calculates chunks per document, index storage requirements ($N_{\text{chunks}} \times d \times 4$ bytes), overlap inflation factors ($1/(1 - \rho)$ where $\rho = 1 - s/n$), and establishes a defensible chunk-length cap tied to the embedding model's maximum sequence length and semantic granularity, grounded in sentence transformer representation principles.
* **Index and Similarity Analysis (4.5 pts):**
  * Mathematically proves that cosine similarity equals the inner product for unit-normalized vectors and explains the exact search behavior of `IndexFlatIP`. Contrasts inverted file indexes (`IndexIVFFlat` with `nlist` and `nprobe`) and hierarchical navigable small world graphs (`IndexHNSWFlat` with `M` and `efSearch`) regarding query complexity, build/memory overhead, and recall degradation. Models bi-encoder retrieval with cross-encoder re-ranking latency ($T = T_{\text{enc}} + T_{\text{ann}} + k \cdot T_{\text{ce}}$), referencing standard semantic search documentation.
* **Retrieval Evaluation Protocol (4.5 pts):**
  * Defines ranked-retrieval metrics including Precision@k, Recall@k, and Mean Reciprocal Rank (MRR) for semantic and few-shot retrieval. Establishes a clear relevance-judgment protocol for relevant chunks, drawing from standard information retrieval and language processing evaluation methodologies (Jurafsky & Martin, Ch. 11). Correctly distinguishes between gradable metrics and those requiring gold standards.

### Part 2: Schema and Contracts (13.5 Points / 45%)
* **Record Schema and Provenance (6 pts):**
  * Specifies a complete JSON Schema (Draft 2020-12) extending chunk records with required provenance fields (`chunk_id`, `doc_id`, `source_hash`, `license_class`, `corpus_type`, temporal metadata, `trope_ids[]`, embedding metadata, and vector representations). Any schema aligned with an approved PS4 term project topic is fully accepted. Details the FAISS int64-id to string `chunk_id` mapping layer (`IndexIDMap2`) with proper update and delete semantics.
* **Contracts and Invariants (4.5 pts):**
  * Writes precise programmatic contracts for `admit_document` (preconditions on license/provenance classes) and `vdb_upsert` (ensuring exactly one vector per `chunk_id`), successfully implementing EmbeddingCompleteness and NoOrphanEmbeddings invariants with clear plain-language descriptions.
* **Section-Specific Ontology Deliverable (3 pt):**
  * **CIS 531 Tracks:** Provides a complete and accurate mapping table connecting project-specific fields to the standard ontology classes without unauthorized structural modifications.
  * **CIS 731 Tracks:** Derives a coherent custom ontology (class hierarchy, relation types, and cardinalities) with justified granularity and well-formulated competency questions.

### Part 3: Generative AI Verification (1.5 Points / 5%)
* **GenAI Audit & Compliance (1.5 pts):**
  * Includes a valid `GenAI.pdf` interaction log documenting adherence to the course Generative AI Kit workflow or an explicit, compliant `"No GenAI Used"` statement.

---

## 📊 Canvas Comment Feedback Table Template

```html
<table style="width: 100%; border-collapse: collapse; font-family: 'Aptos', sans-serif; font-size: 14px;">
  <thead>
    <tr style="background-color: #4b2e83; color: white;">
      <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Evaluation Category</th>
      <th style="padding: 10px; border: 1px solid #ddd; text-align: center;">Max Pts</th>
      <th style="padding: 10px; border: 1px solid #ddd; text-align: center;">Awarded</th>
      <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Specific Evaluative Feedback &amp; Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1A: Chunking Cost Model</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">6.0</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on fixed, sentence, and structure-aware chunking storage derivations and overlap factors]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1B: Index &amp; Similarity Analysis</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">4.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on inner product/cosine equivalence, IVF vs. HNSW trade-offs, and re-ranking latency modeling]</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1C: Retrieval Evaluation Protocol</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">4.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on P@k, Recall@k, MRR definitions, and relevance-judgment protocol]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2A: Record Schema &amp; Provenance Mapping</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">6.0</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on JSON Schema validation, provenance fields, and IndexIDMap2 ID mapping layer]</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2B: Contracts &amp; Invariants</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">4.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on admit_document and vdb_upsert contracts implementing completeness/orphan checks]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2C: Ontology Deliverable (531 Mapping / 731 Custom)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">3.0</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on track-specific ontology compliance or derivation and competency questions]</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 3: Generative AI Audit Log (GenAI.pdf / Attestation)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">1.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on audit log compliance]</td>
    </tr>
    <tr style="background-color: #4b2e83; color: white; font-weight: bold;">
      <td style="padding: 10px; border: 1px solid #ddd;">TOTAL SCORE</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">30</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">[TOTAL]/30</td>
      <td>Final Assessment &amp; Readiness for MP 7 (Few-Shot Trope/Genre Classification)</td>
    </tr>
  </tbody>
</table>
