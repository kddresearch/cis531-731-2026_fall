# MP 3: Real-Time ASR & Vector Database Ingestion — Grading Rubric (30 Points Total)
**Course:** CIS 531/731 (Fall 2026) | **Instructor:** William H. Hsu

## Scoring Breakdown (30-Point Normalized Scale)

### Part 1: PySpark Scrub Pipeline & Regex Modification (13 Points / 43.3%)
* **Regex Hyphenation Handling & TF-IDF Vectorization (13 pts):** 
  * **[13 pts]:** Successfully executed the complete Lab 2 notebook (`lab02.ipynb`) inside the SparkSession, with the `regexp_replace` function properly modified to retain hyphenated compound words (e.g., `large-scale`) as single tokens, culminating in valid TF-IDF sparse vector representations.
  * **[7-12 pts]:** Pipeline executes successfully, but the regex adjustment is incomplete (leading to stripped or split hyphens) or tokenization outputs show minor formatting flaws.
  * **[0-6 pts]:** Missing or unexecuted Lab 2 code, broken Spark environment initialization, or absence of regex modification.

### Part 2: ASR Transcription, VDB Integration & CIS 731 Extension (14 Points / 46.7%)
* **End-to-End ASR, Ingestion & Semantic Retrieval (14 pts):**
  * **[14 pts]:** Successfully completed Lab 3a (`lab03a.ipynb`) using Whisper to transcribe the LibriVox audio track, successfully ingested the transcript into the vector space in Lab 3b (`lab03b.ipynb`), indexed vectors via FAISS, and verified semantic retrieval using the `"doomed youth"` query[cite: 17, 19, 20]. *Note for CIS 731 Graduate Students:* Correctly implemented disk I/O serialization (`faiss.write_index`) and loading routines for the FAISS index[cite: 17, 20].
  * **[7-13 pts]:** Transcribed and queried successfully, but missing the CIS 731 disk persistence extension or displaying minor integration disconnects between Whisper output text and the FAISS ingestion block.
  * **[0-6 pts]:** Incomplete notebook execution, failure to run local Whisper transcription, or non-functional FAISS indexing code.

### Part 3: Generative AI Verification (3 Points / 10%)
* **GenAI Audit & Compliance (3 pts):**
  * **[3 pts]:** Includes valid `GenAI.pdf` interaction log or an explicit, compliant `"No GenAI Used"` statement.
  * **[0-1.5 pts]:** Missing audit log or unverified AI usage without proper attribution.

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
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1: PySpark Scrub Pipeline &amp; Regex Hyphenation</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">13</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on Lab 2 execution, modified regex parsing for hyphenated units, and TF-IDF vectors]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2: ASR Whisper Transcription, FAISS &amp; CIS 731 Disk I/O</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">14</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on Lab 3a audio extraction, Whisper text mapping, Lab 3b FAISS ingestion, semantic query verification, and graduate disk persistence extension]</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 3: Generative AI Audit Log (GenAI.pdf / Attestation)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">3</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on audit log compliance]</td>
    </tr>
    <tr style="background-color: #4b2e83; color: white; font-weight: bold;">
      <td style="padding: 10px; border: 1px solid #ddd;">TOTAL SCORE</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">30</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">[TOTAL]/30</td>
      <td>Final Grade Assessment &amp; Readiness for Module 4 / MP 5 (Structured Streaming)</td>
    </tr>
  </tbody>
</table>
