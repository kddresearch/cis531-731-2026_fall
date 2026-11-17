"""
File: term_project/obtain/fetch_term_project_corpus.py
Course: CIS 531/731 - Fall 2026 (Term Project Infrastructure)
Description: Programmatically parses the course poem manifest Markdown file 
             (lab03_poem_list.md) to extract metadata and fetch open-access 
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

# Path to the course manifest table (adjust relative path as needed)
MANIFEST_PATH = Path("docs/guides/lab03_poem_list.md")

def initialize_term_project_dirs():
    TEXT_CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[Setup] Term project text corpus directory confirmed: {TEXT_CORPUS_DIR.resolve()}")

def parse_poem_manifest(markdown_file_path: Path) -> list:
    """
    Parses the Markdown table from lab03_poem_list.md directly into structured dictionaries,
    extracting URLs if a URL/Source column is present.
    """
    manifest_entries = []
    if not markdown_file_path.exists():
        print(f"[Error] Manifest not found at path: {markdown_file_path.resolve()}")
        return manifest_entries

    with open(markdown_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.strip().startswith("|") and "---" not in line and "#" not in line:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 6:
                poem_id, title, author, reader, time_len, lang = parts[:6]
                
                # Check if a 7th column (URL / Source) exists in the table row
                raw_url_field = parts[6] if len(parts) > 6 else ""
                
                # Extract clean URL from Markdown link format [Text](url) or raw URL string
                url_match = re.search(r'\((https?://[^\)]+)\)', raw_url_field)
                if url_match:
                    target_url = url_match.group(1)
                elif raw_url_field.startswith("http"):
                    target_url = raw_url_field
                else:
                    target_url = "" # Fallback if unmapped in the markdown table

                manifest_entries.append({
                    "id": poem_id,
                    "title": title,
                    "author": author,
                    "language": lang,
                    "url": target_url
                })

    print(f"[Parser] Successfully parsed {len(manifest_entries)} poem entries from {markdown_file_path.name}")
    return manifest_entries

def fetch_text_corpus():
    initialize_term_project_dirs()
    
    # Parse the table dynamically from the course repository Markdown file
    text_manifest = parse_poem_manifest(MANIFEST_PATH)
    headers = {"User-Agent": "CIS531-ResearchPipeline/1.0 (KDD Lab Academic Scraper)"}
    
    success_count = 0
    for item in text_manifest:
        if not item["url"]:
            print(f"[Skip] No valid URL found in manifest for [{item['id']}] '{item['title']}' by {item['author']}")
            continue
            
        filename = f"{item['id']}_{item['author'].replace(' ', '_')}_{item['title'].replace(' ', '_')}.txt"
        file_path = TEXT_CORPUS_DIR / filename
        
        print(f"[Scraping] Fetching [{item['id']}] '{item['title']}' by {item['author']} from {item['url']}...")
        try:
            req = urllib.request.Request(item["url"], headers=headers)
            with urllib.request.urlopen(req) as response, open(file_path, "wb") as out_file:
                content = response.read()
                out_file.write(content)
                print(f" -> Saved to {file_path.name} ({len(content)} bytes)")
                success_count += 1
        except Exception as e:
            print(f"[Error] Failed to fetch {item['title']}: {e}")

    print(f"\n=== Text Pipeline Execution Complete: {success_count} files successfully ingested. ===")

if __name__ == "__main__":
    print("=== KDD Lab Dynamic Manifest Text Acquisition Pipeline ===")
    fetch_text_corpus()
