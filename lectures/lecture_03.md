# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 1:** Foundations & Tooling | **Module 01:** PySpark Intro: RDDs & DataFrames | **Lecture 03:** RDD Transformations & Actions Lab | Monday, August 31, 2026 |

---

## Slide 1: CIS 531/731 – PySpark 4 & The OSEMN Pipeline
### Moving from Local Scripts to Distributed Architecture
* **Course Context:** CIS 531/731 - Lecture 03 (Module 01)
* **Core Topic:** Moving from local scripts to distributed architecture
* **Assigned Reading:** McKinney, *Python for Data Analysis (3rd ed.)* & VanderPlas, *Python Data Science Handbook*[cite: 12]
* **Tech Stack:** PySpark 4, Docker, Beocat
* **Objective:** Understand lazy evaluation, initial data profiling, and select your Term Project track

**Speaker Notes:**
Welcome to Week 2. Today, we bridge the gap between writing Python scripts on your laptop and engineering data pipelines that run on clusters. We will cover core data exploration and array/dataframe manipulation concepts from McKinney and VanderPlas, but we are executing them on the bleeding edge: PySpark 4[cite: 12]. By the end of this lecture, you will understand how Spark manages memory, and you will choose the foundational architecture for your term project.

---

## Slide 2: The Limits of Local Computing
### Scaling Bottlenecks in Single-Node Environments
* **The Single-Node Bottleneck:** pandas loads datasets entirely into RAM
* **Out of Memory (OOM) Crashes:** What happens when your corpus exceeds 16GB or 32GB?
* **Vertical vs. Horizontal Scaling:** Buying a bigger CPU (Vertical) vs. networking multiple standard machines together (Horizontal)
* **The Big Data Imperative:** We need a framework that abstracts the network away from the programmer

**Speaker Notes:**
If you have used pandas, you are used to loading a CSV and manipulating it instantly. That works until your dataset is larger than your system RAM. If you try to load a massive, live-captured audio transcript stream or a million-document text corpus into pandas, your kernel will crash. You can only scale vertically—buying a more expensive computer—for so long. Spark allows us to scale horizontally, distributing the data across many machines while letting you write code as if it were sitting on one.

---

## Slide 3: PySpark 4 Architecture
### Decoupled Client-Server & Catalyst Optimization
* **The Driver and the Executors:** Who gives the orders, and who does the work
* **The Death of RDDs:** Why Resilient Distributed Datasets are legacy, and why we use the DataFrame API
* **Spark Connect:** The new PySpark 4 decoupled client-server architecture
* **ANSI SQL Compliance:** Stricter typing and error handling in modern Spark

**Speaker Notes:**
Spark operates on a Master/Worker architecture. Your code runs on the Driver, which figures out how to chop up the data and send it to Executor nodes. In older versions of Spark, you had to manually map and reduce Resilient Distributed Datasets (RDDs). In PySpark 4, we exclusively use the DataFrame API, which looks a lot like pandas but is backed by the Catalyst Optimizer. PySpark 4 also introduces Spark Connect, which decouples your client from the cluster, making it much easier to run from your IDE without dragging massive JVM dependencies onto your local machine.

---

## Slide 4: Lazy Evaluation & The DAG
### Transformations, Actions, and Execution Blueprints
* **Transformations:** Operations that define what to do (e.g., `filter()`, `select()`, `withColumn()`)
* **Actions:** Operations that demand a result now (e.g., `count()`, `show()`, `write()`)
* **Lazy Evaluation:** Spark does absolutely nothing until an Action is called
* **Directed Acyclic Graph (DAG):** Spark's internal blueprint for optimizing your pipeline before execution

**Speaker Notes:**
This is the most critical conceptual shift you must make this week: Spark is lazy. If you tell Spark to filter a billion rows, it does nothing. It simply writes down: "When the time comes, I need to filter these rows." These instructions are called Transformations. Spark builds a map of these transformations called a Directed Acyclic Graph (DAG). It only actually processes the data when you call an Action, like `show()` or `count()`. This allows Spark's optimizer to look at your entire pipeline and find the fastest mathematical route to the answer before moving a single byte of data.

---

## Slide 5: Data Exploration & Profiling
### Establishing Statistical Baselines Early
* **First Look:** Understanding what data you actually obtained
* **Inspecting the Schema:** `df.printSchema()` ensures data types match reality
* **Summarization:** `df.describe()` for statistical baselines (mean, variance, min, max)
* **Agile Exploration:** Slicing the data quickly to find anomalies before building models

**Speaker Notes:**
Jumping straight into modeling without exploring your data is a recipe for disaster. The moment you ingest data, you must inspect it. Does the schema match what you expect? If a column containing timestamps is loaded as a String, your downstream analytics will silently fail. We use tools like `describe()` to check the statistical distribution of the data. If the minimum value of an age column is negative 50, you have a scrubbing task ahead of you.

---

## Slide 6: The OSEMN Pipeline
### 5-Stage Methodological Framework
* **[O] Obtain:** Sourcing and ingesting the raw streams/corpora
* **[S] Scrub:** Chunking, cleaning, normalizing, and handling nulls
* **[E] Explore:** UMAP/t-SNE embedding visualizations and dashboarding
* **[M] Model:** Retrieval-augmented classification, clustering
* **[N] Interpret:** Applying models to live streams to track cohort propagation

**Speaker Notes:**
Exploration is just one phase of the data lifecycle. In this course, we structure our work around the OSEMN pipeline: Obtain, Scrub, Explore, Model, and Interpret. You will not just be writing arbitrary code; you will be building a rigorous, 5-stage pipeline. The choices you make in the Obtain and Scrub phases will permanently constrain what you are mathematically allowed to conclude in the Interpret phase.

---

## Slide 7: Term Project Architecture (Track Selection)
### Mandatory Track Locking & Convergence
* **The Mandate:** You must commit to one of two parallel data tracks
* **Track 1 (ASR):** Live Radio/Call-in Stream Capture $\rightarrow$ Streaming Transcription
* **Track 2 (VDB):** Lyrics / YA-Lit / Xianxia Corpus $\rightarrow$ Vector Database Embeddings
* **Track Immutability:** Once selected, your track is locked to maintain your DAG scope
* **Convergence:** Both tracks converge at Module 07 (Explore) for Generational Convolution

**Speaker Notes:**
For your term projects, I am doing away with generic, solved datasets like Yelp reviews or SEC financial filings. We are building systems that process complex, messy reality. You must choose between two tracks. Track 1 is the ASR track, dealing with live audio streams. Track 2 is the Vector Database track, dealing with deep semantic literature and lyrics. Choose carefully, because once you lock in your track at Module 03, you cannot switch. The beautiful part is that regardless of which pipeline you build, both teams will converge in Module 07 to analyze the same sociological outputs.

---

## Slide 8: Track 1 Overview — ASR Live Stream Ingest
### Real-Time Streaming & Latency Management
* **Obtain:** Securely hooking into live radio/call-in audio streams
* **Scrub:** Real-time chunking of audio buffers (max 30 seconds)
* **The Engine:** OpenAI Whisper (Local GPU) or Deepgram/AssemblyAI APIs
* **Challenges:** Managing latency, throughput SLAs, and unbounded buffer growth

**Speaker Notes:**
If you choose the ASR track, you are operating in the domain of real-time streaming. You will use PySpark Structured Streaming to capture live call-in audio. Your challenge is not just transcription; it is latency. You must manage audio chunks, ship them to an ASR model like Whisper, and retrieve the text before your memory buffer overflows. You are building the nervous system of an autonomous listener.

---

## Slide 9: Track 2 Overview — Vector Database (VDB) Text
### Dense Vector Embeddings & Narrative Retrieval
* **Obtain:** Sourcing massive, domain-specific text corpora (e.g., Wuxia scripts, YA literature)
* **Scrub:** Semantic text chunking and generating dense vector embeddings
* **The Engine:** FAISS, Milvus, or Pinecone to store and query the $N$-dimensional vectors
* **Challenges:** Schema design, avoiding "orphan" embeddings, maintaining provenance

**Speaker Notes:**
If you choose the VDB track, you are operating in the domain of deep semantic retrieval. You will ingest large literary corpora, but you cannot search them with basic keywords. You will generate embeddings—converting concepts into 768-dimensional coordinates. Your challenge is scrubbing the data so that your chunking strategy preserves the context of the story. You will build a database that allows you to execute "few-shot trope retrieval" to identify narrative patterns across generations.

---

## Slide 10: Next Steps & Hands-On Preparation
### Preparing for Upcoming Lab & Hands-on Sessions
* **Task 1:** Finalize your team and lock in your Track Selection (ASR or VDB)
* **Task 2:** Ensure Docker is installed or your Beocat access is active
* **Task 3:** Read the PySpark 4 Quickstart documentation & assigned McKinney/VanderPlas chapters[cite: 12]
* **Wednesday Goal:** Bring your laptops; we are spinning up PySpark sessions and initiating the Obtain phase

**Speaker Notes:**
That covers the theoretical architecture. For Wednesday’s lab, you need to have your team formed and your track decided. We are going to get our hands dirty immediately. Ensure your environments are configured according to the syllabus checklist. On Wednesday, we spin up the clusters, connect to our data sources, and execute the Obtain stage of your pipelines. I will see you then.
