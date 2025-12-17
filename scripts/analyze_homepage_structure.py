#!/usr/bin/env python3
"""
Analyze homepage structure
"""

from bs4 import BeautifulSoup

with open('/Users/marc/Desktop/biologische-hondensnacks/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("SECTIONS FOUND:")
print("=" * 60)

for idx, section in enumerate(soup.find_all('section'), 1):
    section_id = section.get('id', 'NO ID')
    section_class = section.get('class', ['NO CLASS'])
    
    # Trouver le premier h2 ou h3
    title = section.find(['h2', 'h3'])
    title_text = title.get_text().strip()[:50] if title else 'NO TITLE'
    
    print(f"\nSection {idx}:")
    print(f"  ID: {section_id}")
    print(f"  Class: {section_class}")
    print(f"  Title: {title_text}")
    
print("\n" + "=" * 60)
