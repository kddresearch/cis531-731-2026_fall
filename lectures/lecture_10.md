# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **[Phase 2](../phases/phase_02/):** Obtain & Ingest | **[Module 03](../modules/module_03/):** Obtain: ASR Stream Capture / VDB Corpus Acquisition | **Lecture 10:** Corpus Acquisition Lab & Wrap-Up | Friday, September 18, 2026 |

---

## Slide 1: Corpus Acquisition Lab & Wrap-Up
### Live ASR Streams, VDB Integration, and MP2 Debrief
* **Course Context:** CIS 531/731 - Lecture 10 (Module 03, Phase 2)
* **Core Topic:** Hands-on lab execution for live ASR stream capture, VDB routing, and Module 3 wrap-up.
* **Assigned Reading:** [Meta AI Research, *FAISS Documentation & Repository*](https://github.com/facebookresearch/faiss); [UFAL, *Whisper-Streaming Repository*](https://github.com/ufal/whisper_streaming) (indexed in the [Readings Master Index](../reading_materials/readings_by_lecture.md))
* **Associated Hands-On Lab:** [`lab03b.ipynb`](../assignments/homework/lab03b.ipynb)
* **Related Deliverable:** [`MP 3: Real-Time ASR & Vector Database Ingestion`](../assignments/machine_problems/mp3_real_time_asr_vector_database_ingestion.md)

**Speaker Notes:**
Welcome to Lecture 10. Today is Friday, September 18th, which means we are closing out Module 3. On Wednesday, we broke down the sequence-to-sequence architecture of OpenAI's Whisper model and the mechanics of local transcription. Today, we put that theory into practice. We are moving directly into our hands-on lab to initialize our live ASR stream capture and route it into a Vector Database. But first, we need to debrief yesterday’s machine problem submission.

---

## Slide 2: MP2 Debrief — OpenUSD Scene Assembly
### Bridging the Visual and Analytics Tracks
* **Submission Review:** MP2 (OpenUSD Scene Assembly) was due yesterday.
* **Data is Data:** Whether it is a USD scene graph for a 3D renderer or a JSON payload for a Vector Database, the core principle is strict, hierarchical schema enforcement.
* **Common Pitfalls:** We saw issues with composition arcs and missing references.
* **Grading:** TAs will have grades pushed to the repository by Monday.

**Speaker Notes:**
Before we fire up our audio streams, let's briefly review MP2: OpenUSD Scene Assembly, which you submitted yesterday. I saw some excellent work, but a few common pitfalls emerged around composition arcs and broken reference paths. Remember, whether you are building a USD scene graph for the CV track or a semantic text payload for the Analytics track, data is data. If your schema is malformed, the pipeline breaks. The TAs are reviewing your pull requests now and grades will be finalized by Monday. Let's pivot back to analytics.

---

## Slide 3: Lab Architecture Overview
### The "Obtain" Pipeline in Action
* **Stage 1: Ingestion:** `ffmpeg` hooks into a live internet radio stream and buffers raw audio.
* **Stage 2: Chunking:** Voice Activity Detection (VAD) slices the buffer into clean 30-second WAV files.
* **Stage 3: Inference:** The local PyTorch/Whisper daemon transcribes the WAV file into timestamped text.
* **Stage 4: Injection:** The text is formatted as JSON and pushed into the Vector Database (VDB) staging queue.

**Speaker Notes:**
This is the architecture you are building today on your local machines. It is a four-stage pipeline. First, we use FFmpeg to hook into a live HTTP audio stream. Second, we buffer and slice that stream using VAD to ensure we don't cut off words. Third, our local Whisper daemon wakes up, transcribes the chunk, and outputs text. Finally, we structure that text and inject it into our Vector Database target. You are building the complete "Obtain" phase of a modern data pipeline today.

---

## Slide 4: Initializing the ASR Stream Capture
### Wrangling Infinite Data
* **The FFmpeg Subprocess:** Running stream capture as a background Python subprocess.
* **Memory Management:** Do not buffer infinite streams in RAM. Write chunks to a temporary disk directory.
* **The Target:** For today’s lab, we will use a live, 24/7 public news radio feed as our testing stream.

**Speaker Notes:**
Open up your terminals. Your first task is to initialize the FFmpeg stream capture. You will launch this as an asynchronous Python subprocess. A critical warning here: do not attempt to buffer an infinite live stream entirely in your system RAM, or your machine will hard-crash within an hour. You must write the buffered chunks to a temporary directory on your SSD. We have provided a link to a live 24/7 public news radio stream in the lab instructions for you to use as your data source.

---

## Slide 5: Connecting the Whisper Daemon
### Inference on the Fly
* **Directory Watcher:** Implementing a `watchdog` script to monitor the temporary audio folder.
* **Cold Starts vs. Warm Starts:** Keep the Whisper model loaded in VRAM. Loading the weights from disk for every chunk will destroy your real-time latency.
* **Execution:** Transcribe the file, extract the string, and immediately delete the source WAV to clear disk space.

**Speaker Notes:**
Once your audio is chunking, you need to wake up Whisper. You are writing a daemon—a directory watcher—that listens for new WAV files. Here is the trick that separates good pipelines from failing ones: you must keep the Whisper model loaded in your GPU's VRAM. If you reload the 1.5-gigabyte model from your SSD every time a 30-second chunk arrives, you will fall behind the live stream and the pipeline will collapse. Transcribe, extract, and delete the audio.

---

## Slide 6: Structuring for the VDB Target
### Formatting the Corpus
* **Raw Text is Useless:** A continuous block of text cannot be queried effectively.
* **The Payload:** Constructing a JSON object containing the `text`, `absolute_timestamp`, `source_stream`, and `chunk_id`.
* **The Handoff:** Pushing this JSON payload into a local staging directory or a Redis queue for the VDB ingestion layer.

**Speaker Notes:**
Whisper gives us a raw text string. As data engineers, we know raw text is useless. If we just append it to a massive text file, we can't perform vector searches on it later. You must package the Whisper output into a structured JSON payload. It needs the text, the absolute timestamp we calculated, the stream source, and a unique chunk ID. Once formatted, you push this payload into a staging queue where our Vector Database can pick it up.

---

## Slide 7: Troubleshooting — Buffering & Latency
### When the Stream Falls Behind
* **The Bottleneck:** Whisper inference takes longer than 30 seconds to transcribe a 30-second chunk.
* **The Symptom:** The temporary folder fills up with unprocessed WAV files until the hard drive is full.
* **The Fix:** Downgrade the model size (e.g., from `base` to `tiny`), enable FP16 precision, or upgrade the GPU.

**Speaker Notes:**
As you run this, you will encounter bottlenecks. The most common is transcription latency. If your GPU takes 35 seconds to transcribe 30 seconds of audio, you are operating at a net loss. The temporary folder will fill up with WAV files faster than you can process them, eventually crashing the system. If you see your queue growing infinitely, you must downgrade your Whisper model from `base` to `tiny` or force PyTorch to use FP16 half-precision to speed up the math.

---

## Slide 8: Troubleshooting — The OOM Reaper
### Managing VRAM Constraints
* **Out of Memory (OOM):** PyTorch throws a `CUDA out of memory` error and terminates the script.
* **The Cause:** Another application is hoarding VRAM, or memory leaks in your Python loop are failing to clear old tensors.
* **The Fix:** Use `torch.cuda.empty_cache()` at the end of each loop and ensure your desktop window manager isn't eating your GPU resources.

**Speaker Notes:**
The second major hurdle is the OOM Reaper: the `CUDA out of memory` exception. PyTorch is unforgiving. If you exceed your VRAM limit by a single megabyte, the script dies. This usually happens because you have a memory leak in your Python loop—you are holding onto old audio tensors instead of overwriting them. Make sure you call Python's garbage collector and empty the CUDA cache at the end of every transcription loop.

---

## Slide 9: Module 3 Wrap-Up
### The "Obtain" Phase is Complete
* **Objective Met:** We successfully bypassed commercial APIs to build a sovereign, local data ingestion engine.
* **The Corpus:** We now have an automated mechanism to generate an infinite, structured text corpus from ephemeral audio streams.
* **The Foundation:** This raw, timestamped data is the required fuel for all downstream AI analytics.

**Speaker Notes:**
By the end of today's lab, you will have a fully functioning ingestion pipeline. Let's wrap up Module 3. We successfully achieved our goal: we bypassed the commercial cloud and built a sovereign, local data capture engine. We took ephemeral, vanishing radio waves and turned them into an infinite, structured text corpus. The "Obtain" phase is now complete. We have the fuel we need.

---

## Slide 10: Staging for Module 4
### Entering the Analytics Phase
* **Next Week:** Module 4 kicks off on Monday.
* **The Shift:** Moving from Data Capture (Obtain) to Data Processing and Search.
* **The Tech:** Introducing Vector Databases (Chroma/Milvus) and embedding models to turn our text corpus into mathematical coordinates.
* **Final Task:** Keep your streams running over the weekend. We need a large corpus waiting for us on Monday morning.

**Speaker Notes:**
This sets the stage for Module 4, which begins next week. We are shifting from data capture to data analytics. We will take the JSON payloads you generated today, pass them through an embedding model, and inject them into a Vector Database so we can perform real-time semantic search. Your final task for today: once your pipeline is stable, leave it running over the weekend. We need a massive corpus of text waiting for us on Monday morning to analyze. Let's get to work on the lab.
