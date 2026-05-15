#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Get all HTML files in produits directory
produits_dir = Path('/Users/marc/Desktop/biologische-hondensnacks/produits')
html_files = list(produits_dir.glob('*.html'))

# Create a mapping of normalized names to actual file names
def normalize_name(name):
    """Normalize file name for comparison"""
    # Remove special characters and convert to lowercase
    name = name.lower()
    name = re.sub(r'[^a-z0-9]', '', name)
    return name

# Create mapping
file_mapping = {}
for f in html_files:
    normalized = normalize_name(f.stem)
    file_mapping[normalized] = f.name

# Read products.js
products_js_path = Path('/Users/marc/Desktop/biologische-hondensnacks/products.js')
with open(products_js_path, 'r') as f:
    content = f.read()

# Fix pageUrls
def fix_page_url(match):
    page_url = match.group(1)
    filename = page_url.split('/')[-1]
    normalized = normalize_name(filename.replace('.html', ''))
    
    if normalized in file_mapping:
        correct_filename = file_mapping[normalized]
        return f"pageUrl: 'produits/{correct_filename}'"
    else:
        # Try to find a close match
        for norm, actual in file_mapping.items():
            if normalized in norm or norm in normalized:
                return f"pageUrl: 'produits/{actual}'"
        return match.group(0)  # Return original if no match found

# Replace pageUrls
content = re.sub(r"pageUrl:\s*['\"]([^'\"]+)['\"]", fix_page_url, content)

# Write back
with open(products_js_path, 'w') as f:
    f.write(content)

print("Fixed products.js file")
