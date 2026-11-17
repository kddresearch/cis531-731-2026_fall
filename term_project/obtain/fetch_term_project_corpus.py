"""
File: term_project/obtain/fetch_term_project_corpus.py
Course: CIS 531/731 - Fall 2026 (Term Project Infrastructure)
Description: Programmatically parses the course poem manifest Markdown file 
             (lab03_poem_list.md) into tuples/dictionaries and fetches open-access 
             text sources for downstream VDB ingestion (MP 3, MP 7, MP 9).
"""

import os
import re
import urllib.request
from pathlib import Path

# Target output directories anchored to the term project path
TERM_PROJECT_DIR = Path("term_project")
CORPUS_OUTPUT_DIR = TERM_PROJECT_DIR / "data" / "raw_corpus"
TEXT_CORPUS_DIR = CORPUS_OUTPUT_DIR / "texts"
MANIFEST_PATH = TERM_PROJECT_DIR / "docs" / "guides" / "lab03_poem_list.md" # Adjust path as structured locally

def initialize_term_project_dirs():
    TEXT_CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[Setup] Term project text corpus directory confirmed: {TEXT_CORPUS_DIR.resolve()}")

def parse_poem_manifest(markdown_file_path: Path) -> list:
    """
    Parses the Markdown table from lab03_poem_list.md into structured tuples/dictionaries.
    """
    manifest_entries = []
    if not markdown_file_path.exists():
        print(f"[Warning] Manifest not found at {markdown_file_path}. Using fallback demo manifest.")
        return [
            {"id": "04", "title": "To Germany", "author": "Charles Hamilton Sorley", "language": "en", "url": "https://www.gutenberg.org/cache/epub/26785/pg26785.txt"},
            {"id": "05", "title": "Range-finding", "author": "Robert Frost", "language": "en", "url": "https://www.gutenberg.org/cache/epub/29345/pg29345.txt"}
        ]

    with open(markdown_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.strip().startswith("|") and "---" not in line and "#" not in line:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 6:
                poem_id, title, author, reader, time_len, lang = parts[:6]
                
                # Construct query/mirror mapping for open-access text fetching (e.g., Project Gutenberg mirrors)
                # Students can map specific public-domain URIs dynamically based on author/title matching
                entry = {
                    "id": poem_id,
                    "title": title,
                    "author": author,
                    "language": lang,
                    "url": get_open_access_mirror_url(author, title)
                }
                manifest_entries.append(entry)

    print(f"[Parser] Successfully parsed {len(manifest_entries)} poem entries from manifest.")
    return manifest_entries

def get_open_access_mirror_url(author: str, title: str) -> str:
    """
    Helper mapping function to resolve open-access text endpoints (Project Gutenberg raw caches) 
    for public domain texts.
    """
    # Example deterministic mapping for demonstration and student assignments
    if "Frost" in author:
        return "https://www.gutenberg.org/cache/epub/29345/pg29345.txt"
    elif "Sorley" in author:
        return "https://www.gutenberg.org/cache/epub/26785/pg26785.txt"
    else:
        # Generic placeholder or archive fallback endpoint
        return ""

def fetch_text_corpus():
    initialize_term_project_dirs()
    
    # Parse the table dynamically from the course repository Markdown file
    text_manifest = parse_poem_manifest(MANIFEST_PATH)
    headers = {"User-Agent": "CIS531-ResearchPipeline/1.0 (KDD Lab Academic Scraper)"}
    
    for item in text_manifest:
        if not item["url"]:
            print(f"[Skip] No open-access URL mapped for '{item['title']}' by {item['author']}")
            continue
            
        filename = f"{item['id']}_{item['author'].replace(' ', '_')}_{item['title'].replace(' ', '_')}.txt"
        file_path = TEXT_CORPUS_DIR / filename
        
        print(f"[Scraping] Fetching [{item['id']}] '{item['title']}' by {item['author']}...")
        try:
            req = urllib.request.Request(item["url"], headers=headers)
            with urllib.request.urlopen(req) as response, open(file_path, "wb") as out_file:
                content = response.read()
                out_file.write(content)
                print(f" -> Saved to {file_path} ({len(content)} bytes)")
        except Exception as e:
            print(f"[Error] Failed to fetch {item['title']}: {e}")

if __name__ == "__main__":
    print("=== KDD Lab Dynamic Manifest Text Acquisition Pipeline ===")
    fetch_text_corpus()
    print("=== Text Pipeline Execution Complete ===")
