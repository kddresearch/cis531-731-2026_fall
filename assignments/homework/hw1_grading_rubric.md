# HW 1: DevContainer Bring-Up & Term Project Architecture — Grading Rubric (30 Points Total)
**Course:** CIS 531/731 (Fall 2026) | **Instructor:** William H. Hsu

## Scoring Breakdown (30-Point Normalized Scale)

### Part 1: Environment Verification (9 Points / 30%)
* **PySpark 4 & Spark Web UI Proof (9 pts):** 
  * **[9 pts]:** Screenshot clearly displays custom schema DataFrame `.show()` output alongside an active Spark Web UI (port `4040`) interface.
  * **[4-8 pts]:** Screenshot is present and shows `.show()` output, but the Spark Web UI port 4040 is omitted or unverified.
  * **[0-3 pts]:** Missing verification artifact or invalid PySpark initialization output.

### Part 2: Project Architecture & Matrix Selection (18 Points / 60%)
* **Team Roster, Track, Category, & Task Allocation (11 pts):**
  * **[11 pts]:** Valid roster (1–3 students), single immutable track selected (**Track 1: ASR Live Stream** or **Track 2: VDB Text Corpora**), valid category mapping, and distinct task allocations per member (no overlapping duplicate tasks; shared tasks explicitly differentiate baseline vs. alternative models).
  * **[6-10 pts]:** Minor omissions in task uniqueness or incomplete roster/category mapping.
  * **[0-5 pts]:** Missing track selection, overlapping unassigned tasks, or invalid architecture structure.
* **Coherent Problem Statement (7 pts):**
  * **[7 pts]:** Concise 3–4 sentence problem statement seamlessly integrating the chosen track, category, and assigned task pipeline.
  * **[3-6 pts]:** Statement is present but vague, overly verbose, or omits track/task integration.
  * **[0-3 pts]:** Missing or incoherent problem statement.

### Part 3: Generative AI Verification (3 Points / 10%)
* **GenAI Audit & Compliance (3 pts):**
  * **[3 pts]:** Includes valid `GenAI.pdf` interaction log or an explicit, compliant `"No GenAI Used"` statement.
  * **[0-1.5 pts]:** Missing audit log or unverified AI usage without attribution.

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
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 1: Environment Verification (PySpark 4 &amp; Port 4040 UI)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">9</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on Spark session output and Web UI proof]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2A: Roster, Track, Category &amp; Task Allocations</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">11</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on track selection and matrix allocations]</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 2B: Coherent Problem Statement (3–4 Sentences)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">7</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on architectural pipeline clarity]</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; border: 1px solid #ddd;"><strong>Part 3: Generative AI Audit Log (GenAI.pdf / Attestation)</strong></td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">3</td>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">[SCORE]</td>
      <td style="padding: 8px; border: 1px solid #ddd;">[Insert feedback on audit log compliance]</td>
    </tr>
    <tr style="background-color: #4b2e83; color: white; font-weight: bold;">
      <td style="padding: 10px; border: 1px solid #ddd;">TOTAL SCORE</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">30</td>
      <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">[TOTAL]/30</td>
      <td>Final Grade Assessment &amp; Next Steps for MP 2 / PS 4</td>
    </tr>
  </tbody>
</table>
