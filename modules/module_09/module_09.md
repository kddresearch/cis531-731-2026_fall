# CIS 536/736: Computer Graphics and Animation

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 4:** Cloud Rendering & Visualization | **Module 09:** Cloud Render Farms — AWS Deadline Cloud | **Lectures 28-30** | Mon 02 Nov - Fri 06 Nov 2026 |

---

## Lecture 28: Cloud Rendering Concepts: Distributed Rendering, Cost/Scale Tradeoffs (Mon 02 Nov)

1. **Distributed Rendering Architectures:** Transitioning from monolithic local workstation rendering to distributed, elastic cloud environments (AWS Deadline Cloud).
2. **Fleets and Queues:** Understanding the decoupling of job queues from compute fleets, and configuring worker node allocation strategies.
3. **Cost/Scale Tradeoffs:** Evaluating how instance types (e.g., Spot vs. On-Demand), core counts, memory footprints, and frame sampling affect compute-hour billing.
4. **Scene Complexity Reduction:** Identifying scene optimization strategies—such as Level of Detail (LOD) swaps and reduced sampling—to stay under strict credit allocations.
5. **Open Job Description (OpenJD):** Deconstructing the YAML-based standard for defining compute environments, parameters, and render tasks across agnostic workers.

---

## Lecture 29: AWS Deadline Cloud Walkthrough (Wed 04 Nov)

1. **Environment & Identity Configuration:** Establishing IAM roles, permissions, and AWS Educate/Academy credentials for Deadline Cloud access.
2. **Infrastructure Initialization (Instructor Demo):** Walking through the AWS Console to provision a functional queue and attach a cost-controlled fleet.
3. **Job Bundle Architecture:** Authoring the `template.yaml` (step definitions) and `parameter_values.yaml` (variables) required for a complete OpenJD job bundle.
4. **CLI Submission Workflows:** Using the AWS Deadline Cloud CLI (`deadline bundle submit`) to dispatch cross-pillar OpenUSD or Blender scenes to the farm.
5. **Worker Telemetry and Logging:** Diagnosing render failures by inspecting AWS CloudWatch logs, container startup overhead, and task chunking latency.

---

## Lecture 30: Lab 5b - Capped AWS Educate/Academy Credit Render Task (Fri 06 Nov)

1. **Budget Estimation (Pre-Flight):** Calculating a strict mathematical compute-hour and USD cost estimate before deploying a workload to prevent quota exhaustion.
2. **OpenUSD Cross-Pillar Audit:** Auditing local OpenUSD stages to ensure all texture and payload references use portable, relative paths before cloud upload.
3. **Cost-Aware Job Execution:** Dispatching a constrained render job (e.g., 1080p, 128 SPP) that remains safely within the 80% threshold of the capped credit allocation.
4. **Local vs. Cloud Render Parity:** Validating that the cloud-rendered output frames match expected local lighting and materials (MSE/PSNR checks).
5. **Cost Discrepancy Analysis:** Executing a formal post-mortem to compare the estimated compute budget against the actual telemetry and overhead billed by AWS.
