#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Get all HTML files in produits directory
produits_dir = Path('/Users/marc/Desktop/biologische-hondensnacks/produits')
html_files = list(produits_dir.glob('*.html'))

# Read products.js
products_js_path = Path('/Users/marc/Desktop/biologische-hondensnacks/products.js')
with open(products_js_path, 'r') as f:
    content = f.read()

# Extract pageUrls from products.js using regex
page_urls = re.findall(r"pageUrl:\s*['\"]([^'\"]+)['\"]", content)

print(f"Total products in products.js: {len(page_urls)}")
print(f"Total HTML files in produits: {len(html_files)}")

# Check for mismatches
html_file_names = set(f.name for f in html_files)
page_url_names = set(url.split('/')[-1] for url in page_urls)

missing_in_js = html_file_names - page_url_names
missing_in_produits = page_url_names - html_file_names

print(f"\nFiles in produits but not in products.js: {len(missing_in_js)}")
for f in sorted(missing_in_js)[:10]:
    print(f"  - {f}")

print(f"\nFiles in products.js but not in produits: {len(missing_in_produits)}")
for f in sorted(missing_in_produits)[:10]:
    print(f"  - {f}")
