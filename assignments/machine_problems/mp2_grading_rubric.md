# 📂 File: assignments/machine_problems/mp2_grading_rubric.md

# MP 2: DevContainer Deployment & Manifest Verification — Grading Rubric (30 Points Total)
**Course:** CIS 531/731 (Fall 2026) | **Instructor:** William H. Hsu[cite: 14]

## Scoring Breakdown (30-Point Normalized Scale)

### Part 1: Manifest Compliance & Environment Verification (13 Points / 43.3%)
* **Exact Version Matching & `verify_env.py` Output (13 pts):** 
  * **[13 pts]:** DevContainer cleanly builds with strict dependency pinning (PySpark 3.5.x, PyTorch 2.x, Transformers, OpenAI Whisper, MLflow, FAISS)[cite: 14], and execution of `verify_env.py` produces the exact required SHA-256 runtime digest matching course specifications[cite: 14].
  * **[7-12 pts]:** Container builds with minor configuration tweaks, but version pinning is floating or the SHA-256 verification string diverges slightly from the standard manifest.
  * **[0-6 pts]:** Build fails due to unpinned dependencies, missing packages, or absent verification execution logs.

### Part 2: Compute Allocation, Fallback Logic & CIS 731 Extension (14 Points / 46.7%)
* **Compute Probe & Fallback Script (`probe_compute.py`) (14 pts):**
  * **[14 pts]:** `probe_compute.py` correctly detects hardware context and outputs the precise fallback state string (`GPU Pool Active - Batch Embedding/Whisper Ready` or `CPU-Only Fallback Active`)[cite: 14, 15]. *Note for CIS 731 Graduate Students:* Also successfully configures conditional base image container pulls for hardware-differentiated environments[cite: 14, 15].
  * **[7-13 pts]:** Script executes and checks for CUDA availability, but fallback string formatting is incomplete or CIS 731 conditional pulling is missing/untested.
  * **[0-6 pts]:** Script fails to execute, lacks hardware detection logic, or throws unhandled import errors.

### Part 3: Generative AI Verification (3 Points / 10%)
* **GenAI Audit & Compliance (3 pts):**
  * **[3 pts]:** Includes valid `GenAI.pdf` interaction log or an explicit, compliant `"No GenAI Used"` statement[cite: 14].
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
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1: Manifest Compliance &amp; verify_env.py Digest</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">13</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on container build success, version pinning parity, and SHA-256 verification log matching]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2: Compute Probe, Fallback Logic &amp; CIS 731 Extension</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">14</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on probe execution, GPU/CPU fallback routing strings, and graduate extension config]</td>
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
      <td>Final Grade Assessment &amp; Readiness for Module 3 / MP 3 (ASR &amp; VDB Ingestion)</td>
    </tr>
  </tbody>
</table>
