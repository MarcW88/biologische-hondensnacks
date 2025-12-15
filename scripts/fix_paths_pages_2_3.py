#!/usr/bin/env python3
"""
FIX PATHS PAGES 2 & 3
=====================
Corrige tous les chemins relatifs dans les pages 2 et 3
qui sont dans /winkel/page/N/ (profondeur +2)
"""

import os
import re

BASE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
WINKEL_DIR = os.path.join(BASE_DIR, 'winkel')

def fix_page_paths(page_num):
    """Corrige les chemins d'une page"""
    
    page_path = os.path.join(WINKEL_DIR, 'page', str(page_num), 'index.html')
    
    with open(page_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    print(f"\n🔧 Correction page {page_num}...")
    
    # Liste des corrections à faire
    replacements = [
        # CSS et JS dans le <head>
        (r'href="shop-styles\.css"', 'href="../../shop-styles.css"'),
        (r'src="\.\.\/js\/main\.js"', 'src="../../js/main.js"'),
        (r'src="shop\.js"', 'src="../../shop.js"'),
        (r'src="load-products\.js"', 'src="../../load-products.js"'),
        
        # Liens dans le footer (liste ul)
        (r'href="natuurlijke-hondensnacks/"', 'href="../../natuurlijke-hondensnacks/"'),
        (r'href="hondensnacks-voor-puppy/"', 'href="../../hondensnacks-voor-puppy/"'),
        (r'href="hondensnacks-voor-training/"', 'href="../../hondensnacks-voor-training/"'),
        (r'href="gezonde-kauwsnacks/"', 'href="../../gezonde-kauwsnacks/"'),
        (r'href="graanvrije-hondensnacks/"', 'href="../../graanvrije-hondensnacks/"'),
        (r'href="over-ons/"', 'href="../../over-ons/"'),
        (r'href="blog/"', 'href="../../blog/"'),
        (r'href="contact/"', 'href="../../contact/"'),
        (r'href="veelgestelde-vragen/"', 'href="../../veelgestelde-vragen/"'),
        (r'href="beste-hondensnacks-2026/"', 'href="../../beste-hondensnacks-2026/"'),
        (r'href="privacy-policy/"', 'href="../../privacy-policy/"'),
        (r'href="algemene-voorwaarden/"', 'href="../../algemene-voorwaarden/"'),
        (r'href="disclaimer/"', 'href="../../disclaimer/"'),
    ]
    
    changes_count = 0
    for pattern, replacement in replacements:
        matches = len(re.findall(pattern, html))
        if matches > 0:
            html = re.sub(pattern, replacement, html)
            changes_count += matches
            print(f"   ✅ {matches}x: {pattern}")
    
    # Sauvegarder
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"   ✅ {changes_count} corrections appliquées")
    return changes_count

def main():
    print("\n🛠️  FIX PATHS PAGES 2 & 3")
    print("=" * 70)
    
    total_changes = 0
    
    # Page 2
    total_changes += fix_page_paths(2)
    
    # Page 3
    total_changes += fix_page_paths(3)
    
    print("\n" + "=" * 70)
    print(f"✅ CHEMINS CORRIGÉS: {total_changes} corrections totales")
    print("=" * 70)
    print("\n🎯 Pages 2 et 3 ont maintenant:")
    print("   ✅ CSS correctement lié (../../shop-styles.css)")
    print("   ✅ JavaScript correctement lié (../../shop.js)")
    print("   ✅ Liens footer corrects (../../blog/, etc.)")

if __name__ == "__main__":
    main()
