# MP 5: Data Analytics Pipelines (Structured Streaming) — Grading Rubric (30 Points Total)
**Course:** CIS 531/731 (Fall 2026) | **Instructor:** William H. Hsu

## Scoring Breakdown (30-Point Scale)

### Part 1: Contracts and Event-Time Analysis (9 Points / 30%)
* **Schema and Contracts (4.5 pts):**
  * Explicit `StructType` schema (TranscriptChunk for ASR; CorpusChunk for VDB including `record_id`, `track`, `source_id`, `ts_start`, `ts_end`, `text`, `ingest_ts`, and `license_class`) with fully justified nullability choices. Contracts rigorously enforce BoundedChunking (`chunk_duration_sec <= 30`, `ts_start < ts_end`) and provenance/whitelist gates.
* **Watermark and State Analysis (4.5 pts):**
  * Rigorous event-time calibration measuring lateness percentiles (`ingest_ts - ts_end` p50/p95/p99) grounded in event-time vs. processing-time principles (Akidau et al.). The chosen watermark delay correctly balances completeness-vs-latency-vs-cost trade-offs, with a thoroughly justified output mode and explicit state-growth bound adhering to structured streaming programming guidelines.

### Part 2: Streaming Pipeline Implementation & Evaluation (19.5 Points / 65%)
* **Query Correctness (7.5 pts):**
  * Flawless implementation of `readStream`, watermarking, and windowed aggregations (`groupBy(window(...))`). Correctly executes 60-second tumbling windows and 5-minute/1-minute sliding windows computing record counts, `approx_count_distinct` of tokens, top-10 terms, and mean ingest latency on reference replay, paired with proper sink design.
* **Fault Tolerance & Checkpointing (7.5 pts):**
  * Implements robust checkpointing (`checkpointLocation`) and append-mode sink architecture. Demonstrates successful fault injection and recovery by killing the query mid-run, restarting from checkpoints, and reconciling row counts and window keys to prove exact deduplication and window consistency without duplicate or missing keys.
* **Metrics and Reproducibility (4.5 pts):**
  * Complete `metrics.jsonl` log capturing `StreamingQueryProgress` metrics (`inputRowsPerSecond`, `processedRowsPerSecond`, `batchDuration`, `stateOperators.numRowsTotal`). Environment is pinned to the course CPU DevContainer standard, CI status is green, and (for ASR track) AssemblyAI quota usage is fully documented.

### Part 3: Generative AI Verification (1.5 Points / 5%)
* **GenAI Audit & Compliance (1.5 pts):**
  * Includes valid `GenAI.pdf` interaction log documenting adherence to the Generative AI Kit workflow or an explicit, compliant `"No GenAI Used"` statement.

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
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1A: Schema &amp; Contract Validation</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">4.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on StructType schema, nullability justifications, and BoundedChunking/whitelist contracts]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1B: Watermark &amp; State Analysis</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">4.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on lateness percentiles, watermark delay trade-offs, output mode, and state bounds]</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2A: Query Correctness &amp; Window Aggregations</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">7.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on tumbling/sliding windows, approximate counts, top terms, and ingest latency]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2B: Fault Tolerance &amp; Checkpoint Reconciliation</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">7.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on restart procedure, checkpointing, and row/window key reconciliation]</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2C: Metrics &amp; Reproducibility</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">4.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on metrics.jsonl, StreamingQueryProgress, CPU baseline CI, and quotas]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 3: Generative AI Audit Log (GenAI.pdf / Attestation)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">1.5</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on GenAI Kit compliance and audit log completeness]</td>
    </tr>
    <tr style="background-color: #4b2e83; color: white; font-weight: bold;">
      <td style="padding: 10px; border: 1px solid #ddd;">TOTAL SCORE</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">30</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">[TOTAL]/30</td>
      <td>Final Assessment &amp; Readiness for PS 6 (Semantic Search &amp; VDB Schema)</td>
    </tr>
  </tbody>
</table>
