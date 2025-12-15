#!/usr/bin/env python3
"""
FIX TOP 10 LAYOUT - Applique le layout 2-colonnes à tous les produits
======================================================================

Applique le pattern: Image gauche + Contenu droite + Encadré visible
aux produits #3 à #10 de la page Top 10.

Auteur: AI Assistant
Date: Décembre 2025
"""

import re
import os

FILE_PATH = '/Users/marc/Desktop/biologische-hondensnacks/beste-hondensnacks-2026/index.html'

def fix_product_layout(content, product_num):
    """Applique le nouveau layout à un produit spécifique"""
    
    # Pattern pour détecter le début d'un produit review
    pattern = rf'(<!-- Product #{product_num}.*?-->.*?)<div class="product-review mb-lg" id="top-{product_num}">'
    
    # Remplacement avec encadré + border
    replacement = rf'\1<div class="product-review mb-lg" id="top-{product_num}" style="position: relative; background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border: 2px solid #e5e7eb; margin-bottom: 3rem;">'
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Pattern pour restructurer le grid (trouver la div grid-2 du produit)
    # Chercher après id="top-X" jusqu'au prochain <!-- Product
    pattern_grid = rf'(id="top-{product_num}"[^>]*>.*?)<div class="grid grid-2"[^>]*>(.*?)(?=<p class="mt-md"|</div>\s*<!-- Product)'
    
    def replace_grid(match):
        before = match.group(1)
        grid_content = match.group(2)
        
        # Extraire l'image
        img_match = re.search(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>', grid_content)
        if not img_match:
            return match.group(0)  # Pas de changement si pas d'image
        
        img_src = img_match.group(1)
        img_alt = img_match.group(2)
        
        # Tout après l'image est le contenu
        content_after_img = grid_content[img_match.end():]
        
        # Reconstruire avec le nouveau layout
        new_grid = f'''<div class="grid grid-2" style="align-items: start; gap: 2rem;">
      <!-- Image à gauche -->
      <div>
       <img alt="{img_alt}" src="{img_src}" style="width: 100%; height: auto; border-radius: 12px; display: block;"/>
      </div>
      <!-- Contenu à droite -->
      <div>{content_after_img}</div>
     </div>'''
        
        return before + new_grid
    
    content = re.sub(pattern_grid, replace_grid, content, flags=re.DOTALL)
    
    return content

def main():
    print("\n🔧 FIX TOP 10 LAYOUT - Products #3 to #10")
    print("=" * 70)
    
    # Lire le fichier
    print(f"\n📄 Lecture du fichier...")
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    backup_path = FILE_PATH + '.layout_backup'
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"   ✅ Backup créé: {backup_path}")
    
    # Appliquer les corrections pour les produits 3 à 10
    products_fixed = []
    for product_num in range(3, 11):
        print(f"\n🔨 Traitement produit #{product_num}...")
        content = fix_product_layout(content, product_num)
        products_fixed.append(product_num)
        print(f"   ✅ Produit #{product_num} restructuré")
    
    # Sauvegarder
    print(f"\n💾 Sauvegarde des modifications...")
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*70}")
    print(f"✅ LAYOUT APPLIQUÉ AVEC SUCCÈS!")
    print(f"   Produits corrigés: {', '.join(f'#{p}' for p in products_fixed)}")
    print(f"   Total: {len(products_fixed)} produits")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
