#!/usr/bin/env python3
"""
FIX PRODUCT IMAGES - COMPLETE FIX
==================================

Corrige complètement les balises img dans les pages produits.

Auteur: AI Assistant
Date: December 2025
"""

import os
import re
import glob

# Configuration
PRODUITS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'

def fix_broken_img_tags(content):
    """Répare les balises img cassées"""
    
    # Pattern: ligne avec juste le chemin + class="product-image"
    # Ex: ../images/filename.jpg class="product-image">
    pattern = r'(\s+)(\.\.\/images\/[^>]+?)\s+class="product-image">'
    
    def replacement(match):
        indent = match.group(1)
        image_path = match.group(2).strip()
        # Extraire le nom du fichier pour alt text
        alt_text = os.path.basename(image_path).replace('.jpg', '').replace('.png', '')
        return f'{indent}<img src="{image_path}" alt="{alt_text}" class="product-image">'
    
    content = re.sub(pattern, replacement, content)
    
    return content

def process_product_pages():
    """Traite toutes les pages produits"""
    
    print("🔧 FIX PRODUCT IMAGES - COMPLETE")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML dans produits/
    html_files = glob.glob(os.path.join(PRODUITS_DIR, '*.html'))
    
    print(f"📁 Found {len(html_files)} product pages\n")
    
    fixed_count = 0
    error_count = 0
    
    for html_file in html_files:
        try:
            # Lire le fichier
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Corriger
            fixed_content = fix_broken_img_tags(content)
            
            # Sauvegarder si modifié
            if fixed_content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                
                filename = os.path.basename(html_file)
                
                # Compter combien d'images corrigées
                fixes = len(re.findall(r'<img src="../images/', fixed_content)) - len(re.findall(r'<img src="../images/', original_content))
                print(f"✅ Fixed: {filename} ({fixes} images)")
                fixed_count += 1
            
        except Exception as e:
            filename = os.path.basename(html_file)
            print(f"❌ Error with {filename}: {e}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 COMPLETE!")
    print(f"✅ Fixed: {fixed_count} files")
    print(f"⏭️  Skipped: {len(html_files) - fixed_count - error_count} files (no issues)")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    process_product_pages()
