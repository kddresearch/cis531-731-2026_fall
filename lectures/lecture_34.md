# CIS 536/736: Computer Graphics

| Phase | Module | Lecture | Date | Assigned Reading |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 5](../phases/phase_05/):** Visualization, VFX & Capstone Synthesis | **[Module 10](../modules/module_10/):** Color Theory & Data/Info Visualization I | **Lecture 34:** Data/Info Visualization II: Objects & Processes | Mon 16 Nov 2026 | Healy, *Data Visualization*, Ch. 5–6 (`socviz.co`) |

---

## Slide 1: Overview & Agenda — Visualizing Objects & Processes
### CIS 536/736 - Lecture 34
* **From Raw Quantities to Complex Structures:** Moving beyond single-variable bar and scatter charts to multi-layer declarative graphics, statistical model outputs, and spatial/relational processes.
* **Assigned Reading:** Kieran Healy, *Data Visualization: A Practical Introduction*, Chapters 5–6 (`socviz.co`).
* **Multi-Layer Grammar of Graphics:** Decoupling data transformations (`stats`), geometric marks (`geoms`), aesthetic mappings, and coordinate panels.
* **Multivariate & Distribution Encodings:** Comparing groups across continuous and categorical axes using boxplots, violin plots, Cleveland dot plots, and small multiples.
* **Modeling & Process Visualization:** Displaying statistical regressions, confidence intervals, residuals, and marginal effects alongside raw observations.
* **Graphics Pipeline Integration:** Translating declarative 2D/3D visual encodings into interactive Unity 6 scene graphs and UI Toolkit canvases.

**Speaker Notes:**
Welcome to Lecture 34. In our last module, we covered perceptual color spaces and elementary visual channels. Today, grounded in Chapters 5 and 6 of Kieran Healy's *Data Visualization*, we scale up from plotting isolated quantities to visualizing structured objects, statistical processes, and multi-dimensional relationships—and examine how those declarative principles map directly onto 2D/3D computer graphics scene graphs.

---

## Slide 2: Multi-Layer Declarative Grammar of Graphics
### Separating Data, Transforms, Geoms & Scales
* **Orthogonal Pipeline Stages:** A declarative visualization separates Data, Aesthetic Mappings (`x`, `y`, `color`, `size`), Statistical Transformations, Geometric Primitives (`geom_point`, `geom_line`), and Coordinate Systems.
* **Layer Composition (`+` Operator Semantics):** Complex plots are constructed by stacking independent layers that either inherit global data/mappings or override them with local data subsets.
* **Graphics Engine Analogy:** Mirrors modern GPU rendering passes and Unity/OpenUSD scene graphs—separating underlying mesh/point geometry, shader material uniforms, compute/geometry-node modifiers, and camera projection matrices.

**Speaker Notes:**
Notice how closely the Layered Grammar of Graphics mirrors a modern graphics pipeline. In Blender Geometry Nodes or a Unity shader pipeline, you never hardcode pixel positions by hand; you bind attributes to fields, run procedural transformations, and project through a camera coordinate space. When building analytical overlays in Unity 6, keeping your statistical aggregation separate from your mesh or UI Toolkit rendering layer prevents visual clutter and makes interactive filtering trivial.

---

## Slide 3: Visualizing Grouped Comparisons & Distributions
### Preserving Granularity Without Overplotting
* **Summary-Only Traps:** Bar charts of group means conceal sample size, skewness, and multimodality while wasting ink below the baseline.
* **Distributional Geoms:** Combining boxplots or violin plots with jittered raw points exposes both summary quantiles and underlying sample density.
* **Cleveland Dot Plots & Range Plots:** Replacing heavy bars with high-precision position encodings along a common aligned scale—ideal for comparing ranked categories.
* **Handling High-Density Overplotting:** Mitigating visual saturation via alpha-blending, 2D hexagonal binning, and contour density estimation.

**Speaker Notes:**
Healy Chapter 5 emphasizes showing the distribution behind the summary. When you visualize telemetry in your term project, never show just a mean bar. Pair a violin or boxplot summary with translucent jittered observations, or use a Cleveland dot plot when comparing ordered categorical metrics so the viewer's visual system uses position along a common scale rather than area.

---

## Slide 4: Small Multiples & Faceting
### Trading Spaghetti Plots for Aligned Coordinate Panels
* **The Spaghetti Plot Failure Mode:** Overlaying many time-series curves on a single axis overloads color discrimination and creates severe occlusion.
* **Small Multiples Principle:** Partitioning data by categorical variables into an array of small, identically scaled panels.
* **Cognitive Efficiency:** Shared axes allow the viewer's eye to scan structural differences across conditions without repeatedly re-reading legends.
* **Background Context Layering:** Plotting the pooled dataset as a faint silhouette in every facet panel anchors each subset against the global distribution.

**Speaker Notes:**
Whenever a multi-line chart turns into an unreadable tangle, decompose it into small multiples. By holding the axes fixed across a grid of panels, you shift the cognitive burden from legend lookup to rapid spatial pattern recognition. In a 3D viewport or Unity HUD, small multiples translate cleanly into synchronized multi-camera viewports or tiled UI Toolkit panels.

---

## Slide 5: Direct Labeling & Annotation Hygiene
### Eliminating Legend-Lookup Friction
* **Direct Text & Callout Labels:** Placing category labels directly adjacent to terminal data points eliminates horizontal eye saccades back and forth to a detached legend.
* **Selective Outlier Highlighting:** Using subset filters to annotate only statistically notable points rather than every vertex.
* **Repulsion & Collision Avoidance:** Algorithmic label placement prevents overlapping typography in dense 2D screen space and 3D billboarded HUDs.

**Speaker Notes:**
Detached legends force the viewer to hold color-to-name mappings in working memory. Direct labeling keeps the reader's gaze inside the data region. For your Unity 6 visualization pipelines, apply the exact same rule: project 3D world-space anchor coordinates to screen space and run a lightweight screen-space bounding-box repulsion pass before drawing text labels.

---

## Slide 6: Modeling & Statistical Process Visualization
### Plotting Models as First-Class Geometric Objects
* **Models Are Not Separate From Data:** Statistical models generate fitted values, standard errors, and residuals that should be rendered directly over empirical observations.
* **Explicit Uncertainty Ribbons:** Rendering 95% confidence bands or error bars alongside point estimates prevents viewers from treating noisy estimates as deterministic constants.
* **Comparing Multiple Model Specifications:** Using coefficient plots and marginal effects curves to compare parameter estimates and uncertainty intervals across competing models.

**Speaker Notes:**
Moving into Healy Chapter 6, the core insight is that statistical models and simulation processes are themselves objects to be visualized. Whether you are displaying a regression trend over empirical sensor readings or plotting predicted trajectories in a simulation, always render the uncertainty envelope explicitly so the viewer sees where the model is well-constrained versus extrapolating.

---

## Slide 7: Residual Diagnostics & Simulation Trajectory Processes
### Visualizing Error Structure & Time-Varying State
* **Residual-vs-Fitted Diagnostics:** Plotting model residuals against fitted values exposes heteroscedasticity and non-linear bias invisible in raw summaries.
* **Process & State-Transition Trajectories:** Encoding temporal processes using directional paths ordered by time rather than sorted by the x-axis, with color/size encoding velocity or age.
* **Bootstrapped & Ensemble Spaghetti:** Rendering an ensemble of simulated paths at low opacity behind a bold median trajectory communicates stochastic variance directly.

**Speaker Notes:**
Notice the distinction between a line that sorts observations left-to-right and a path that connects points in sequential time order. Whenever you visualize a dynamic process—such as a particle trajectory, a camera path, or a phase-space state loop—you must preserve sequential ordering and encode progression through luminance or vector arrowheads.

---

## Slide 8: Spatial & Network Process Encodings
### Maps, Choropleths, Flows & Graph Topologies
* **Coordinate Reference Systems & Projections:** Transforming geographic coordinates via explicit map projections while accounting for area distortion.
* **Choropleths vs. Proportional Symbols:** Normalizing rates per capita before coloring polygons to avoid the "population map" fallacy.
* **Force-Directed & Hierarchical Graph Layouts:** Visualizing relational objects using force layouts, radial trees, or adjacency matrices.

**Speaker Notes:**
Spatial and relational data introduce an explicit geometric transformation step before rendering. Never shade raw counts onto geographic regions of unequal area—always normalize to rates or use proportional point symbols. Similarly, when visualizing hierarchical scene graphs or dependency networks in your projects, choose deterministic tree layouts for strict DAGs and force-directed layouts only when community clustering is the primary analytical question.

---

## Slide 9: Bridging Declarative InfoVis to Unity 6
### Real-Time 2D/3D Data Visualization Architecture
* **Data-to-Visual Pipeline Mapping:** Tabular Data to ComputeBuffers, Visual Channels to Shader uniforms, Geometric Marks to GPU-instanced meshes.
* **Perceptual Safety in 3D Scenes:** Applying colorblind-safe palettes and avoiding unlit neon saturation so data encodings remain legible under scene lighting.
* **Lab 6a to Lab 6b Continuity:** Integrating your visualization canvas directly into your interim project scene.

**Speaker Notes:**
How does all of this connect to your Unity 6 code? Treat Unity's UI Toolkit or instanced rendering APIs as your geometry backend. Keep your statistical aggregations in clean data structures so your rendering loop only reads pre-mapped attributes. If you render 3D data glyphs inside a lit HDRP scene, remember that post-processing bloom and directional shadows can distort hue and luminance, so use unlit or UI-overlay shaders for quantitative color channels.

---

## Slide 10: Summary & Transition to VFX
### Key Takeaways & Next Steps
* **Declarative Composition:** Stack orthogonal layers to visualize complex objects without clutter.
* **Distributions & Uncertainty:** Replace single-point summaries with distribution geoms and render confidence intervals explicitly.
* **Next Lecture (Wed 18 Nov — Lecture 35):** Special Topics: VFX & Particle Systems Survey.
* **Friday Lab (Fri 20 Nov — Lecture 36):** Lab 6b Term Project Interim Integration Check-In.

**Speaker Notes:**
To wrap up: good visualization of objects and processes comes down to structural honesty—showing full distributions, aligning panels, labeling directly, and rendering model uncertainty explicitly. On Wednesday in Lecture 35, we shift from static visualizations to dynamic physical simulation with VFX and particle systems, preparing you for Friday's Lab 6b Term Project Interim Integration Check-In before Fall Break.
