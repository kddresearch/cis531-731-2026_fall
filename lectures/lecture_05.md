# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 1:** Foundations & Tooling | **Module 02:** Cloud Tools, DevContainers & AI/LLM Tooling | **Lecture 05:** Data Scrubbing & Early Exploration | Friday, September 04, 2026 |

---

## Slide 1: Data Scrubbing & Early Exploration
### Moving from Obtain to Scrub and Explore
* **Course Context:** CIS 531/731 - Lecture 05 (Module 02)
* **Core Reading:** Miner & Shook, Chapter 5
* **The Reality of Raw Data:** Ingested data is fundamentally hostile to machine learning models.
* **Session Objective:** Applying PySpark 4 transformations to normalize, clean, and statistically profile the datasets we ingested on Wednesday.

**Speaker Notes:**
Welcome to Friday. On Wednesday, we successfully breached the Obtain gate. Whether you are pulling live audio buffers or massive static text corpora, you now have raw data sitting in a PySpark DataFrame. But as Miner and Shook emphasize in Chapter 5, raw data is inherently hostile. It contains nulls, malformed strings, HTML artifacts, and statistical impossibilities. Today, we execute the Scrub phase. We are going to write the PySpark transformations required to clean this data, followed immediately by the initial Explore phase to establish our statistical baselines.

---

## Slide 2: Scrubbing Mechanics (The PySpark Way)
### Immutability, Transformations, and String Normalization
* **Immutable DataFrames:** You cannot "edit" a PySpark DataFrame; you can only transform it into a new one.
* **The `withColumn` Function:** Overwriting or creating new columns based on logic.
* **Handling Nulls:** `df.na.drop()` vs. `df.na.fill()`.
* **String Manipulation:** Using PySpark SQL functions (`F.lower()`, `F.regexp_replace()`) to normalize text.

**Speaker Notes:**
In pandas, you might loop through a dataframe and change values in place. In PySpark, DataFrames are strictly immutable. You never edit data; you apply a transformation that outputs a brand new DataFrame. This is crucial for maintaining the integrity of the DAG. The workhorse of the Scrub phase is the `withColumn` method. We use it alongside PySpark's built-in SQL functions to normalize strings to lowercase, strip out punctuation using regular expressions, and make deliberate, mathematical decisions about how to handle missing data—whether we drop nulls entirely or fill them with a statistical mean.

---

## Slide 3: VDB Track Scrub — Text Chunking
### Preserving Semantic Context under Token Constraints
* **The Embeddings Constraint:** LLMs and vector models (like BERT) have strict token limits (e.g., 512 tokens).
* **Naive Chunking:** Splitting a book strictly by word count (destroys semantic context).
* **Semantic Chunking:** Splitting by sentence or paragraph boundaries to preserve narrative intent.
* **PySpark Implementation:** Writing User-Defined Functions (UDFs) or using `explode()` to break arrays of text into distinct rows.

**Speaker Notes:**
For the Vector Database track, your primary Scrubbing challenge is chunking. You have a massive blob of YA literature or Xianxia text. You cannot feed an entire chapter into a vector embedding model because you will blow past the token limit. You must split the text. But if you naively split every 500 words, you will slice a character's sentence in half, destroying the semantic context the model needs. Your pipeline must logically chunk the text by sentence or paragraph boundaries and use PySpark's `explode` function to convert those chunks into individual DataFrame rows while retaining the author and genre metadata.

---

## Slide 4: ASR Track Scrub — Audio to Text Normalization
### Handling Disfluencies and Managing Stream Artifacts
* **The Transcription Bridge:** Passing the audio buffers from Obtain into the ASR Engine (Whisper/API).
* **Handling Disfluencies:** Filtering out "ums," "ahs," and stuttering from live streams.
* **Punctuation Stripping:** Removing inferred punctuation from the ASR output to create a clean token stream.
* **Deduplication:** Preventing the same audio chunk from being transcribed twice due to network lag.

**Speaker Notes:**
For the ASR track, your Scrub phase is two-fold. First, you must pass the audio buffers you captured on Wednesday to your transcription engine and return the raw text back to the DataFrame. Second, you have to scrub the resulting transcript. Live human speech is messy. Your ASR model will return disfluencies—stutters, "ums," and "ahs." Depending on your downstream goals, you must write PySpark filters to either strip these out to find the core subject matter, or isolate them if you are analyzing the speaker's cognitive load.

---

## Slide 5: The Cost of User-Defined Functions (UDFs)
### Serialization Penalties and Pandas Vectorization
* **Native Spark Functions:** Written in Scala/Java, heavily optimized by the Catalyst engine.
* **Python UDFs:** Forces Spark to serialize data out of the JVM, run Python code, and deserialize it back.
* **The Bottleneck:** UDFs can cripple cluster performance on massive datasets.
* **Vectorized UDFs (Pandas UDFs):** Using Apache Arrow to drastically speed up Python-based functions.

**Speaker Notes:**
As you write these custom chunking and filtering rules, you will be tempted to write standard Python functions and apply them to the DataFrame using a PySpark UDF. I must warn you: standard Python UDFs are a massive performance bottleneck. Because Spark's core is built in Scala, using a Python UDF forces the cluster to constantly serialize data back and forth between the Java Virtual Machine and the Python interpreter. Whenever possible, use native PySpark SQL functions. If you absolutely must use Python logic, we will utilize Vectorized Pandas UDFs, which use Apache Arrow memory formats to bypass the serialization penalty.

---

## Slide 6: Entering the [E]xplore Phase
### Transitioning from Mechanical Cleaning to Statistical Profiling
* **The Transition:** Moving from mechanical cleaning to statistical profiling.
* **Trust but Verify:** Proving the Scrub phase worked before building models.
* **The `describe()` Action:** Calculating count, mean, standard deviation, min, and max.
* **Categorical Profiling:** Using `groupBy()` and `count()` to find the distribution of genres, authors, or speakers.

**Speaker Notes:**
Once your DataFrame is scrubbed and chunked, you immediately transition into the Explore phase. You never jump straight to Machine Learning. You must mathematically prove that your Scrub phase actually worked. We trigger our first major Actions here. By calling `describe()` on numeric columns, we establish statistical baselines. By using `groupBy` and `count`, we profile our categorical data. If your VDB pipeline shows that 90% of your text chunks come from one single author, your dataset is fundamentally biased, and your final model will be useless.

---

## Slide 7: Exploratory Data Analysis (EDA) at Scale
### Aggregation Strategies and Driver Pullback
* **The Visualization Problem:** You cannot plot a billion rows on a scatterplot.
* **Aggregation First:** Using PySpark to aggregate the data down to a manageable size.
* **Moving to the Driver:** `df.toPandas()` brings the summarized data back to the local node.
* **Plotting Tools:** Using Matplotlib, Seaborn, or Plotly on the aggregated results.

**Speaker Notes:**
Exploratory Data Analysis requires visualization, but you cannot plot a billion rows on a scatterplot—your GPU will crash. The big data workflow requires you to use PySpark to aggregate the data on the cluster first. You group, sum, and average the data down to a few thousand rows. Only then do you call `toPandas()`, which pulls that small, summarized dataset off the cluster and back into the memory of your local Driver node. From there, you can use standard Python tools like Matplotlib or Seaborn to visualize the trends.

---

## Slide 8: Establishing Baselines (Miner & Shook)
### Defining "Normal" and Managing Pipeline Feedback Loops
* **What is "Normal"?** You cannot detect an anomaly if you do not know the baseline.
* **VDB Baselines:** Average token count per chunk, frequency of top 50 stop-words.
* **ASR Baselines:** Average words-per-minute (WPM), frequency of dropped API calls.
* **The Feedback Loop:** If the baselines reveal systemic errors, you return to the Scrub phase.

**Speaker Notes:**
As Miner and Shook highlight, the primary goal of the Explore phase is establishing a baseline of "normal." If you don't know what the normal word-per-minute rate is for your audio stream, you cannot detect when a caller is speaking abnormally fast due to distress. If the Explore phase reveals that your average text chunk length is zero, your chunking algorithm in the Scrub phase is broken. The OSEMN pipeline is not strictly linear; the Explore phase frequently forces you to loop back and fix your Scrub logic.

---

## Slide 9: Milestone 1 Preview — The Experiment Design
### Architectural Contracts and Hypothesis Formulation
* **The Deliverable:** Your first major architectural milestone is approaching.
* **The Contract:** You must formally define the exact schema output of your Obtain/Scrub pipeline.
* **The Hypothesis:** What specific narrative trope (VDB) or acoustic anomaly (ASR) are you attempting to isolate in the Model phase?
* **Pipeline Lockdown:** Once Milestone 1 is submitted, your ingestion and cleaning logic is frozen.

**Speaker Notes:**
This brings us to your first major project deliverable: Milestone 1. You will submit your Experiment Design document. I am not looking for machine learning code yet. I am looking for the architectural contract. You must define the exact schema that your Obtain and Scrub phases will output. You must also formally state the hypothesis you intend to test during the Model phase. Once Milestone 1 is approved, your Obtain and Scrub logic is locked down, and we pivot entirely to modeling and interpretation for the rest of the semester.

---

## Slide 10: Weekend Operations
### Pipeline Validation and Next Steps
* **Goal:** Finalize the Obtain and Scrub logic for your respective tracks.
* **Validation:** Produce a clean, chunked DataFrame that is ready for aggregation.
* **Reading Assignment:** Review the PySpark API documentation on Vectorized UDFs.
* **Next Week:** We begin generating dense embeddings (VDB) and implementing sliding NLP windows (ASR) in the Model phase.

**Speaker Notes:**
Your task for the weekend is to finalize the Obtain and Scrub code for your track. I want you to arrive on Monday with a pipeline that successfully ingests your raw data and outputs a clean, chunked, perfectly typed PySpark DataFrame. If you are struggling with performance, read the PySpark documentation on Pandas Vectorized UDFs. Next week, we cross the threshold into the Model phase, where we will start converting this clean text into mathematical coordinates. Have a good weekend, and get those pipelines running.
