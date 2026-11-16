"""
File: term_project/scripts/fetch_term_project_corpus.py
Course: CIS 531/731 - Fall 2026 (Term Project Infrastructure)
Description: Programmatically fetches, extracts, and sanitizes the longitudinal 
             project corpus (e.g., WWI poetry / aircheck audio archives) for 
             downstream VDB ingestion (MP 3, MP 7, MP 9).
"""

import os
import urllib.request
import zipfile
from pathlib import Path

# Target output directory anchored to the term project path
TERM_PROJECT_DIR = Path("term_project")
CORPUS_OUTPUT_DIR = TERM_PROJECT_DIR / "data" / "raw_corpus"

# Source archive manifest (LibriVox WWI Poetry / Aircheck corpus baseline)
ARCHIVE_MANIFEST = {
    "title": "WWI Poetry & Broadcast Aircheck Archive",
    "zip_url": "https://archive.org/download/wwi_poetry_1407_librivox/wwi_poetry_1407_librivox_64kb_mp3.zip",
    "target_track": "wwipoem_51_owen_am_64kb.mp3" # Wilfred Owen - Anthem for Doomed Youth
}

def initialize_term_project_dirs():
    CORPUS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[Setup] Term project raw data directory confirmed: {CORPUS_OUTPUT_DIR.resolve()}")

def fetch_and_extract_corpus():
    initialize_term_project_dirs()
    
    zip_filename = "wwi_poetry_archive.zip"
    zip_path = CORPUS_OUTPUT_DIR / zip_filename
    
    print(f"[Fetching] Downloading corpus archive from Archive.org...")
    try:
        if not zip_path.exists():
            urllib.request.urlretrieve(ARCHIVE_MANIFEST["zip_url"], zip_path)
            print(f" -> Download complete. File size: {zip_path.stat().st_size / (1024*1024):.2f} MB")
        else:
            print(f" -> Archive already exists locally at {zip_path}")
            
        # Extract target track for ASR / transcription pipeline (Lab 3a / MP 3)
        target_track_name = ARCHIVE_MANIFEST["target_track"]
        extracted_file_path = CORPUS_OUTPUT_DIR / target_track_name
        
        print(f"[Extracting] Unpacking target track: {target_track_name}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extract(target_track_name, path=CORPUS_OUTPUT_DIR)
            
        print(f" -> Extraction successful. Ready for Whisper ASR pipeline at: {extracted_file_path}")
        
    except Exception as e:
        print(f"[Error] Failed to download or extract corpus archive: {e}")
        raise

if __name__ == "__main__":
    print("=== KDD Lab Term Project Corpus Ingestion Pipeline ===")
    fetch_and_extract_corpus()
    print("=== Pipeline Initialization Complete ===")
