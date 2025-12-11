#!/usr/bin/env python3
"""
FIX PRODUCT IMAGES PATHS
=========================

Corrige les chemins d'images corrompus dans les pages produits.
Supprime les caractères \1 et \2 qui empêchent l'affichage.

Auteur: AI Assistant
Date: December 2025
"""

import os
import re
import glob

# Configuration
PRODUITS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'

def fix_image_paths(content):
    """Corrige les chemins d'images corrompus"""
    
    # Pattern 1: \1../images/filename.jpg\2
    pattern1 = r'\\1(\.\./images/[^\\]+)\\2'
    content = re.sub(pattern1, r'\1', content)
    
    # Pattern 2: Cas où il y a des src= mal formatés
    pattern2 = r'\\1\.\./images/([^\\]+)\\2\s+class='
    content = re.sub(pattern2, r'src="../images/\1" class=', content)
    
    # Pattern 3: \1..\images (sans /)
    pattern3 = r'\\1(\.\.)\\images/([^\\]+)\\2'
    content = re.sub(pattern3, r'\1/images/\2', content)
    
    return content

def process_product_pages():
    """Traite toutes les pages produits"""
    
    print("🔧 FIX PRODUCT IMAGES PATHS")
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
            
            # Vérifier si correction nécessaire
            if '\\1' in content or '\\2' in content:
                # Backup
                backup_path = html_file + '.img_backup'
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Corriger
                fixed_content = fix_image_paths(content)
                
                # Sauvegarder
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                
                filename = os.path.basename(html_file)
                print(f"✅ Fixed: {filename}")
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
