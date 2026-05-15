#!/usr/bin/env python3
import os
import re
from pathlib import Path

def get_product_category(title):
    """Determine product category based on title"""
    title_lower = title.lower()
    
    if any(x in title_lower for x in ['kauw', 'tand', 'bot', 'ring', 'stick']):
        return 'kauwsnacks-tandverzorging', 'Kauwsnacks'
    elif any(x in title_lower for x in ['training', 'trainer', 'treat', 'beloning']):
        return 'hondensnacks-voor-training', 'Training'
    elif any(x in title_lower for x in ['puppy', 'zacht', 'koekje']):
        return 'hondensnacks-voor-puppy', 'Puppy'
    elif any(x in title_lower for x in ['graanvrij', 'hypoallergeen', 'allerge']):
        return 'hypoallergene-hondensnacks', 'Hypoallergeen'
    elif any(x in title_lower for x in ['natuurlijk', 'biologisch', 'orgaan']):
        return 'natuurlijke-hondensnacks', 'Natuurlijk'
    else:
        return 'winkel', 'Winkel'

def generate_breadcrumb(title, category_slug, category_name):
    """Generate breadcrumb navigation with category"""
    title_short = title[:60] + '...' if len(title) > 60 else title
    
    if category_slug == 'winkel':
        return f'<a href="../index.html">Home</a> / <a href="../winkel.html">Winkel</a> / <strong>{title_short}</strong>'
    else:
        return f'<a href="../index.html">Home</a> / <a href="../winkel.html">Winkel</a> / <a href="../{category_slug}/">{category_name}</a> / <strong>{title_short}</strong>'

def update_file_breadcrumb(file_path):
    """Update breadcrumb in a single file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<title>(.*?)\s*\|', content)
    if not title_match:
        print(f"  ⊘ Skipped (no title): {file_path.name}")
        return False
    
    title = title_match.group(1)
    category_slug, category_name = get_product_category(title)
    new_breadcrumb = generate_breadcrumb(title, category_slug, category_name)
    
    # Replace breadcrumb
    old_breadcrumb_pattern = r'<nav class="product-breadcrumb">.*?</nav>'
    new_breadcrumb_html = f'<nav class="product-breadcrumb">\n{new_breadcrumb}\n</nav>'
    
    new_content = re.sub(old_breadcrumb_pattern, new_breadcrumb_html, content, flags=re.DOTALL)
    
    if new_content == content:
        print(f"  ⊘ Skipped (no change): {file_path.name}")
        return False
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Updated: {file_path.name}")
    return True

def main():
    """Main function to update breadcrumbs in all product pages"""
    produits_dir = Path('/Users/marc/Desktop/biologische-hondensnacks/produits')
    
    if not produits_dir.exists():
        print(f"Error: Directory {produits_dir} does not exist")
        return
    
    html_files = list(produits_dir.glob('*.html'))
    print(f"Found {len(html_files)} HTML files to process")
    
    updated = 0
    skipped = 0
    
    for file_path in html_files:
        try:
            if update_file_breadcrumb(file_path):
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ✗ Error processing {file_path.name}: {e}")
    
    print(f"\n✓ Updated {updated} files")
    print(f"⊘ Skipped {skipped} files")
    print(f"Total processed: {updated + skipped}")

if __name__ == '__main__':
    main()
