<!--
  Template Note: This file serves as the canonical template for module pages.
  When instantiated as `modules/module_03/module_03.md`, use relative paths 
  (`../../phases/phase_02/` and `../../lectures/lecture_08.md`) to maintain correct routing.
  Note that the module name itself does not self-link, but lectures link directly to their markdown files.
  Module readings may be contiguous or separate per lecture; the module readings for the modules within a parent phase form a partition of that phase’s readings.
-->

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) | Assigned Reading(s) |
| :--- | :--- | :--- | :--- | :--- |
| **[Phase 2](../../phases/phase_02/):** Obtain & Ingest | **Module 03:** Obtain: ASR Stream Capture & VDB Corpus Acquisition | **Lectures 08-10** | Mon 14 Sep - Fri 18 Sep 2026 | [Jurafsky & Martin, *SLP3* Ch. 16](https://web.stanford.edu/~jurafsky/slp3/); [OpenAI Whisper](https://github.com/openai/whisper); [FAISS & Whisper-Streaming](https://github.com/facebookresearch/faiss) |

---

## [Lecture 08: Obtain: ASR Stream Capture & VDB Corpus Acquisition](../../lectures/lecture_08.md) (Mon 14 Sep 2026)

1. **Stream Capture Architecture:** Establishing continuous socket handles, audio windowing, and format normalization to capture infinite internet radio feeds.
2. **The Buffering Problem:** Managing memory versus latency trade-offs through ring buffers and rolling temporary disk files.
3. **Vector Database Fundamentals:** Transitioning from exact keyword matching in lexical databases to semantic proximity search using high-dimensional embeddings.
4. **Corpus Structuring & Metadata:** Cleaning raw ASR outputs, attaching timestamps and speaker diarization, and performing semantic chunking.
5. **Jurafsky & Martin Fundamentals:** Applying acoustic models for phoneme mapping and language models for probabilistic word sequence prediction.
* **Assigned Reading:** [Jurafsky & Martin, *Speech and Language Processing* (3rd ed. draft, Aug 19, 2026), Ch. 16: *Automatic Speech Recognition*](https://web.stanford.edu/~jurafsky/slp3/)

---

## [Lecture 09: Whisper Architecture & Local Transcription](../../lectures/lecture_09.md) (Wed 16 Sep 2026)

1. **The Cloud Bottleneck & Thanos Rule:** Bypassing commercial API latency, rate limits, and safety filters by deploying local open-weight models.
2. **OpenAI's Whisper ASR:** Utilizing an open-weight robust speech recognition system trained on 680,000 hours of multilingual data for zero-shot performance.
3. **Seq2Seq Transformer Mechanics:** Converting raw audio into Log-Mel Spectrograms, processing acoustic context via the encoder, and autoregressively predicting tokens via the decoder.
4. **Local Hardware & VRAM Constraints:** Sizing model tiers from `tiny` to `large` against available hardware VRAM and optimizing via FP16 precision.
5. **Audio Chunking & Timestamp Alignment:** Managing 30-second windows with Voice Activity Detection and mapping relative chunk timestamps to absolute clock time.
* **Assigned Reading:** [Radford et al. / OpenAI *Whisper* Repository & Model Card](https://github.com/openai/whisper)

---

## [Lecture 10: Corpus Acquisition Lab & Wrap-Up](../../lectures/lecture_10.md) (Fri 18 Sep 2026)

1. **MP2 Debrief & Schema Enforcement:** Reviewing OpenUSD scene assembly outcomes and reinforcing strict hierarchical schema enforcement across tracks.
2. **Lab Architecture Overview:** Executing the four-stage obtain pipeline: FFmpeg ingestion, VAD chunking, Whisper transcription daemon, and JSON VDB staging.
3. **Stream Capture Management:** Running FFmpeg as an asynchronous background subprocess and spooling rolling chunks to temporary disk storage to prevent OOM errors.
4. **Whisper Daemon & VRAM Persistence:** Maintaining model weights in GPU VRAM to avoid latency penalties while using directory watchers for file processing.
5. **Troubleshooting Latency & OOM:** Resolving processing bottlenecks by adjusting model tiers, enabling FP16 precision, and clearing CUDA cache with `torch.cuda.empty_cache()`.
* **Assigned Reading:** [Meta AI Research, *FAISS Documentation & Repository*](https://github.com/facebookresearch/faiss); [UFAL, *Whisper-Streaming Repository*](https://github.com/ufal/whisper_streaming)
