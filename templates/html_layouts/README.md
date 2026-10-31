<!--
yaml_schema_version: "2.2"
document_version: "2.0"
document_last_updated_date: "2026-10-31"
-->

# Course Architecture: Golden HTML Templates
**Status:** ACTIVE | **Format:** Dehydrated HTML

## Overview
This directory contains the Single Source of Truth (SSOT) dehydrated HTML layouts for the KDD Lab course ecosystem. These templates enforce strict visual consistency across Canvas and GitHub Pages deployments.

## Hydration Protocol
These templates rely on inline CSS to survive Canvas/LMS sanitization filters. 
* **Primary Hydration Node:** `[Claude][Sov] Requirements-to-Spec`
* **Execution:** AI nodes must execute exact string replacement on `{{VARIABLE_NAME}}` tokens. Nodes are **STRICTLY FORBIDDEN** from altering inline `style="..."` attributes, modifying hex codes, or changing DOM nesting.

## Template Index
* [`golden_template.html`](golden_template.html) - Base structural layout.
* [`golden_template_universal_assignment_index_page.html`](golden_template_universal_assignment_index_page.html) - Listing of all planned assignments for the course.
* [`golden_template_universal_assignment_page.html`](golden_template_universal_assignment_page.html) - Standardized homework and machine problem specs.
* [`golden_template_universal_lecture_page.html`](golden_template_universal_lecture_page.html) - Individual lecture landing pages with slide/video routing.
* [`golden_template_universal_module_page.html`](golden_template_universal_module_page.html) - Weekly module wrappers with learning objectives.
* [`golden_template_universal_phase_page.html`](golden_template_universal_phase_page.html) - High-level course progression blocks.
* [`golden_template_universal_term_project_proposal_page.html`](golden_template_universal_term_project_proposal_page.html) - Capstone scope and taxonomy definitions.
