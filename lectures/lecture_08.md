# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
**[Phase 2](../phases/phase_02/):** Obtain & Ingest | **[Module 03](../modules/module_03/):** ASR Stream Capture & VDB Corpus Acquisition | **Lecture 08:** Obtain: ASR Stream Capture & VDB Corpus Acquisition | Mon 14 Sep 2026 |

---

## Slide 1: Module 3 — Obtain
### ASR Stream Capture & VDB Corpus Acquisition
* **Course Context:** CIS 531/731 - Lecture 08 (Module 03)
* **Core Topic:** Transitioning from static datasets to continuous Automatic Speech Recognition (ASR) stream capture and vector database (VDB) corpus preparation
* **Assigned Reading:** Jurafsky & Martin, *Speech and Language Processing* (3rd ed. draft), Ch. 16: *Automatic Speech Recognition*
* **Tech Stack:** PySpark Structured Streaming, ASR stream sockets, Vector Database ingestion pipelines

**Speaker Notes:**
Welcome to Module 3. Today, we leave static datasets behind. We are officially entering the "Obtain" phase of our responsive analytics pipeline. We are moving away from downloading pre-packaged CSVs and instead building live, continuous Automatic Speech Recognition (ASR) stream captures. Our end goal is to acquire this corpus and structure it for ingestion into a Vector Database (VDB).

---

## Slide 2: The End of the "Yelp/SEC" Grind
### Why Responsive Analytics Requires Live Data
* Static sentiment analysis datasets are pedagogical dead ends.
* Real-world data is continuous, messy, and temporal.
* Generative coding requires high-leverage, real-time data ingestion.

**Speaker Notes:**
In standard analytics courses, you often start by running sentiment analysis on Yelp reviews or SEC financial filings. We are not doing that here. Those datasets are pedagogical dead ends because they hide the actual architectural friction of data science. Real-world data doesn't wait for you to download it. It is continuous and messy. To understand why we need real-time LLMOps and vector embeddings, you have to feel the friction of capturing live data first.

---

## Slide 3: The Target: Call-In Radio Streams
### Capturing Cross-Generational Sentiment
* **The Source:** Live internet radio and ASR streaming (e.g., SiriusXM Alt-18 call-ins).
* **The Goal:** Capturing organic, unscripted human reactions and trope alignment.
* **The Challenge:** Audio is ephemeral; if we don't capture and process it live, it's gone.

**Speaker Notes:**
Our target for this pipeline is live internet radio streams—specifically, listener call-ins. Think about the cultural contrast of fans calling in to react to Olivia Rodrigo versus Cage the Elephant, or cross-generational sentiment patterns around a track from *The Bends*. We want to capture that organic, unscripted human reaction. The architectural challenge is that this media is ephemeral. If our pipeline isn't listening and buffering in real-time, the data simply vanishes.

---

## Slide 4: ASR Stream Capture Architecture
### The Ingestion Layer
* **Stream Connection:** Opening and maintaining a continuous socket/stream handle.
* **Audio Chunking:** Slicing the infinite stream into processable, overlapping audio windows.
* **Format Conversion:** Normalizing sample rates and encoding for downstream models.

**Speaker Notes:**
How do we actually grab an infinite stream? We don't download a file; we open a continuous stream handle. But an ASR model can't transcribe "infinity." We have to build an ingestion layer that chunks the audio into discrete, manageable windows—usually with a slight overlap so we don't cut a word in half. During this capture, we are also normalizing the sample rate so it matches the input expectations of our downstream transcription models.

---

## Slide 5: The Buffering Problem
### Memory vs. Latency Tradeoffs
* **In-Memory Buffers:** Extremely fast, but highly volatile (risk of OOM errors).
* **Disk Spooling:** Safer for long-running captures, but introduces I/O latency.
* **The Sweet Spot:** Ring buffers or rolling temporary files that purge processed chunks.

**Speaker Notes:**
When you are pulling live audio, you immediately hit the buffering problem. Do you hold the audio chunks in RAM? It's fast, but if your transcription engine stalls, your memory fills up and the pipeline crashes. Do you write chunks to the disk? It's safer, but you introduce I/O latency. The architectural solution we will build uses rolling buffers—holding just enough data to feed the model and purging it the millisecond transcription is confirmed.

---

## Slide 6: Vector Database (VDB) Fundamentals
### Moving Beyond Lexical Search
* **Relational/Lexical Databases:** Search by exact keyword match (e.g., SQL `LIKE '%doomed youth%'`).
* **Vector Databases (VDBs):** Search by semantic meaning and conceptual proximity.
* **The Core Mechanic:** Storing high-dimensional numerical arrays (embeddings) that represent meaning.

**Speaker Notes:**
Once we transcribe the audio, where does it go? Not into a standard SQL database. Standard databases rely on exact keyword matches. But humans on the radio don't use exact keywords; they use slang, tropes, and messy syntax. We need to search by *semantic meaning*. This is why we use Vector Databases. VDBs don't store text as flat strings; they store high-dimensional numerical arrays—called embeddings—that map the conceptual proximity of ideas.

---

## Slide 7: Structuring the Corpus for VDB Ingestion
### Preparing the Text
* **Raw ASR Output:** Messy, lacks punctuation, contains filler words (um, uh).
* **Metadata Attachment:** Timestamps, speaker diarization (caller vs. DJ), show ID.
* **Chunking for Context:** Splitting transcripts into semantically meaningful paragraphs before embedding.

**Speaker Notes:**
Raw output from an ASR model is incredibly messy. It lacks punctuation and is full of filler words. Before we can ingest this into our Vector Database, we have to clean and structure the corpus. We must attach critical metadata: When did this happen? Who is speaking? We also have to chunk the transcribed text properly. If we embed an entire hour of radio as one vector, the meaning is diluted. If we embed it sentence by sentence, we lose context. We have to find the semantic middle ground.

---

## Slide 8: Mapping Subtle Tropes
### Why We Use VDBs in this Course
* **The Use Case:** Finding subtle narrative tropes across messy audio data.
* **Example:** Matching a caller's description of a breakup to the "doomed youth" trope.
* **The Advantage:** VDBs allow single-shot or few-shot conceptual matching without training a custom classifier from scratch.

**Speaker Notes:**
The reason we are building this complex VDB architecture is leverage. By translating messy call-in transcripts into vector space, we can perform advanced trope ontologies. We can query the database for the concept of "doomed youth" and it will return callers describing their teenage angst, even if they never explicitly used the words "doomed" or "youth." It gives us the power of a trained text classifier without the massive overhead of labeling training data.

---

## Slide 9: Jurafsky & Martin Fundamentals
### Speech Inputs and Language Modeling
* **Acoustic Models:** Mapping audio waveforms to phonemes.
* **Language Models:** Predicting the most likely sequence of words given the phonemes.
* **The ASR Pipeline:** The intersection of signal processing and probabilistic sequence prediction.

**Speaker Notes:**
To ground this in your assigned reading from Jurafsky & Martin, remember that ASR is fundamentally a two-part problem. The acoustic model handles the signal processing—turning sound waves into phonetic guesses. The language model then applies probabilities to guess which actual words make sense in that sequence. Understanding this probabilistic nature helps you understand why ASR streams occasionally output bizarre hallucinations when the audio is noisy.

---

## Slide 10: Looking Ahead to Wednesday
### Local Transcription with Whisper
* **The Cloud Bottleneck:** API limits, token costs, and network latency.
* **The Solution:** OpenAI's Whisper model (open-weight, run locally).
* **Next Class:** Deep dive into Whisper's sequence-to-sequence architecture and setting up our local transcription nodes.

**Speaker Notes:**
Today we covered the theory of stream capture and VDB corpus preparation. On Wednesday, we tackle the engine that sits between them: the ASR model itself. We are not going to rely on expensive commercial APIs that throttle our bandwidth. We are going to deploy OpenAI's open-weight Whisper model to run local transcription on our own hardware. We will cover its transformer architecture and how to optimize it for our live stream. See you then.
