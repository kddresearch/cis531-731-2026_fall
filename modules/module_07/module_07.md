<!--
 Template Note: This file serves as the canonical template for module pages.
 When instantiated as `modules/module_07/module_07.md`, use relative paths 
(`../../phases/phase_04/` and `../../lectures/lecture_22.md`) to maintain correct routing.
 Note that the module name itself does not self-link, but lectures link directly to their markdown files.
 Module readings may be contiguous or separate per lecture; the module readings for the modules within a parent phase form a partition of that phase’s readings.
-->

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 4](../../phases/phase_04/):** Explore & Model | **Module 07:** Explore: Data Visualization & Dashboards | **Lectures 22-24** | Mon 19 Oct - Fri 23 Oct 2026 | [Wilke, *Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/); [UMAP-learn Documentation](https://umap-learn.readthedocs.io/en/latest/parameters.html); [scikit-learn User Guide](https://scikit-learn.org/stable/modules/manifold.html) |

---

## [Lecture 22: Explore: Data Visualization & Dashboards](../../lectures/lecture_22.md) (Mon 19 Oct 2026)

1. **Exploratory Data Analysis (EDA) Principles:** Defining the role of visualization in uncovering structural anomalies, latent patterns, and data quality issues prior to formal modeling.
2. **Visual Encoding Constraints:** Mapping continuous, discrete, and categorical variables to spatial positioning, color gradients, and geometric marks while avoiding perceptual distortion.
3. **High-Dimensional Data Challenges:** Identifying the limitations of standard bivariate scatter plots and pair plots when analyzing dense embeddings or multi-feature datasets.
4. **Dashboard Architecture (Dash/Streamlit):** Structuring interactive, web-based analytics dashboards linking UI components (sliders, dropdowns) directly to underlying Python backend callbacks.
5. **Interactive Filtering:** Implementing cross-filtering mechanics allowing users to dynamically slice datasets and immediately observe changes across multiple synchronized visualizations.
* **Assigned Reading:** [Wilke, *Fundamentals of Data Visualization* (Chs. 19–20 & Parts I–II)](https://clauswilke.com/dataviz/)

---

## [Lecture 23: Embedding-Space Visualization (UMAP)](../../lectures/lecture_23.md) (Wed 21 Oct 2026)

1. **Dimensionality Reduction Fundamentals:** Comparing the objectives of Principal Component Analysis (PCA), t-SNE, and Uniform Manifold Approximation and Projection (UMAP).
2. **The UMAP Algorithm:** Understanding the topological mechanics of UMAP—specifically how it constructs local fuzzy simplicial sets and optimizes the low-dimensional cross-entropy.
3. **Hyperparameter Tuning (`n_neighbors` & `min_dist`):** Controlling the balance between preserving local neighborhood clusters versus revealing global macroscopic structures in embedding space.
4. **Vector Database Projection:** Extracting high-dimensional text or image embeddings from a VDB and projecting them into 2D or 3D space for visual cluster analysis.
5. **Semantic Clustering & Annotation:** Applying clustering algorithms (e.g., HDBSCAN) on UMAP projections to automatically label dense semantic regions and identify out-of-distribution artifacts.
* **Assigned Reading:** [UMAP-learn Documentation: *“Basic UMAP Parameters”*](https://umap-learn.readthedocs.io/en/latest/parameters.html)

---

## [Lecture 24: Generational Drift Dashboards Lab; Wrap-Up](../../lectures/lecture_24.md) (Fri 23 Oct 2026)

1. **Time-Series Embedding Analysis:** Tracking the centroid shifts of specific semantic clusters (e.g., tropes or genres) across chronologically ordered datasets.
2. **Dashboard Integration (UMAP + Callbacks):** Embedding dynamic UMAP projections into a Streamlit or Dash application, allowing the user to scrub through time and observe cluster migration.
3. **Quantifying Generational Drift:** Utilizing cosine distance or structural similarity metrics to quantify how the semantic representation of a concept diverges across different eras or media generations.
4. **Data Storytelling Construction:** Translating the mathematical observations of embedding drift into a coherent analytical narrative demonstrating cultural or linguistic evolution.
5. **MP6 Checkpoint & MP7 Release:** Verifying completion of Machine Problem 6 (Model Selection) and outlining the deliverables for Machine Problem 7 (Exploratory Dashboards).
* **Assigned Reading:** [scikit-learn User Guide: *“Manifold Learning and t-SNE”*](https://scikit-learn.org/stable/modules/manifold.html); [Wilke, *Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/)
