#!/usr/bin/env python3
import os
import re
from pathlib import Path
import random

def fix_cta_color(file_path):
    """Fix the white-on-white CTA color issue"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix CTA background gradient from CSS variables to actual colors
    old_cta = r'background:linear-gradient\(135deg,var\(--primary\),var\(--primary-dark\)\)'
    new_cta = 'background:linear-gradient(135deg,#8B5A2B,#6B4423)'
    
    content = re.sub(old_cta, new_cta, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def fix_similar_products(file_path):
    """Fix similar products section with actual product data"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if similar products section has xxx placeholders
    if 'XXXXXX' not in content and '€XX,XX' not in content:
        return False  # No placeholders to fix
    
    # Get similar products from actual files
    produits_dir = Path('/Users/marc/Desktop/biologische-hondensnacks/produits')
    html_files = list(produits_dir.glob('*.html'))
    
    # Select 4 random products (excluding current file)
    current_name = file_path.name
    other_files = [f for f in html_files if f.name != current_name]
    similar_files = random.sample(other_files, min(4, len(other_files)))
    
    # Generate similar products cards
    cards = []
    for file_path_sim in similar_files[:4]:
        try:
            with open(file_path_sim, 'r', encoding='utf-8') as f:
                sim_content = f.read()
            
            # Extract image
            img_match = re.search(r'<img src="(https://media\.s-bol\.com/[^"]+)"', sim_content)
            img = img_match.group(1) if img_match else 'https://media.s-bol.com/n3nX8ZxwXvMY/yrwpooP/1200x1200.jpg'
            
            # Extract title
            title_match = re.search(r'<title>(.*?)\|', sim_content)
            title = title_match.group(1).strip() if title_match else file_path_sim.stem.replace('-', ' ')
            
            # Extract price
            price_match = re.search(r'<div class="price">([^<]+)</div>', sim_content)
            price = price_match.group(1) if price_match else '€XX,XX'
            
            # Create card
            cards.append(f'''<a href="{file_path_sim.name}" class="similar-card">
<img src="{img}" alt="{title}" loading="lazy" onerror="this.style.display='none'">
<h4>{title[:60]}...</h4>
<span class="card-price">{price}</span>
</a>''')
        except:
            # Fallback to placeholder if error
            cards.append(f'''<a href="{file_path_sim.name}" class="similar-card">
<img src="https://media.s-bol.com/n3nX8ZxwXvMY/yrwpooP/1200x1200.jpg" alt="Product" loading="lazy">
<h4>{file_path_sim.stem.replace('-', ' ')[:60]}...</h4>
<span class="card-price">€XX,XX</span>
</a>''')
    
    # Replace similar products section
    similar_section_pattern = r'<div class="similar-grid">.*?</div>'
    new_similar_section = f'<div class="similar-grid">\n{"".join(cards)}\n</div>'
    
    content = re.sub(similar_section_pattern, new_similar_section, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Main function to fix all product pages"""
    produits_dir = Path('/Users/marc/Desktop/biologische-hondensnacks/produits')
    
    if not produits_dir.exists():
        print(f"Error: Directory {produits_dir} does not exist")
        return
    
    html_files = list(produits_dir.glob('*.html'))
    print(f"Found {len(html_files)} HTML files to process")
    
    cta_fixed = 0
    similar_fixed = 0
    
    for file_path in html_files:
        try:
            # Fix CTA color
            if fix_cta_color(file_path):
                cta_fixed += 1
            
            # Fix similar products
            if fix_similar_products(file_path):
                similar_fixed += 1
                
        except Exception as e:
            print(f"  ✗ Error processing {file_path.name}: {e}")
    
    print(f"\n✓ Fixed CTA colors in {cta_fixed} files")
    print(f"✓ Fixed similar products in {similar_fixed} files")

if __name__ == '__main__':
    main()
