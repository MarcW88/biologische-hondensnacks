#!/usr/bin/env python3
"""
ANALYZE DUPLICATES - Détecte doublons et 404 sans toucher aux données
======================================================================
"""

import json
import os
from collections import Counter

BASE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
CATALOG_JSON = os.path.join(BASE_DIR, 'winkel/products-catalog.json')
PRODUITS_DIR = os.path.join(BASE_DIR, 'produits')

def get_existing_pages():
    """Retourne les pages HTML existantes"""
    pages = set()
    for file in os.listdir(PRODUITS_DIR):
        if file.endswith('.html') and not file.endswith('.backup') and file != 'index.html':
            pages.add(file.replace('.html', ''))
    return pages

def main():
    print("\n🔍 ANALYSE DUPLICATES & 404")
    print("=" * 70)
    
    # 1. Charger le JSON
    print("\n📄 Lecture du catalog JSON...")
    try:
        with open(CATALOG_JSON, 'r', encoding='utf-8') as f:
            products = json.load(f)
        print(f"   ✅ {len(products)} produits dans le catalog")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return
    
    # 2. Charger les pages existantes
    print("\n📄 Lecture des pages HTML existantes...")
    existing_pages = get_existing_pages()
    print(f"   ✅ {len(existing_pages)} pages HTML trouvées")
    
    # 3. Analyser les doublons par nom
    print("\n🔍 Recherche de doublons par nom...")
    names = [p.get('name', 'N/A') for p in products]
    name_counts = Counter(names)
    duplicates_by_name = {name: count for name, count in name_counts.items() if count > 1}
    
    if duplicates_by_name:
        print(f"   ⚠️  {len(duplicates_by_name)} noms dupliqués trouvés:")
        for name, count in sorted(duplicates_by_name.items()):
            print(f"      - '{name}' apparaît {count} fois")
    else:
        print(f"   ✅ Aucun doublon de nom")
    
    # 4. Analyser les doublons par slug
    print("\n🔍 Recherche de doublons par slug...")
    slugs = [p.get('slug', 'N/A') for p in products]
    slug_counts = Counter(slugs)
    duplicates_by_slug = {slug: count for slug, count in slug_counts.items() if count > 1}
    
    if duplicates_by_slug:
        print(f"   ⚠️  {len(duplicates_by_slug)} slugs dupliqués trouvés:")
        for slug, count in sorted(duplicates_by_slug.items()):
            print(f"      - '{slug}' apparaît {count} fois")
            # Montrer les produits avec ce slug
            for p in products:
                if p.get('slug') == slug:
                    print(f"        → {p.get('name')} (id: {p.get('id')})")
    else:
        print(f"   ✅ Aucun doublon de slug")
    
    # 5. Analyser les 404 (produits sans page HTML)
    print("\n🔍 Recherche de produits pointant vers 404...")
    products_404 = []
    for p in products:
        slug = p.get('slug', '')
        if slug and slug not in existing_pages:
            products_404.append(p)
    
    if products_404:
        print(f"   ⚠️  {len(products_404)} produits sans page HTML (404):")
        for p in products_404[:10]:  # Montrer les 10 premiers
            print(f"      - {p.get('name')} (slug: {p.get('slug')}, id: {p.get('id')})")
        if len(products_404) > 10:
            print(f"      ... et {len(products_404) - 10} autres")
    else:
        print(f"   ✅ Tous les produits ont une page HTML")
    
    # 6. Résumé
    print(f"\n{'='*70}")
    print(f"📊 RÉSUMÉ:")
    print(f"   Total produits: {len(products)}")
    print(f"   Noms dupliqués: {len(duplicates_by_name)}")
    print(f"   Slugs dupliqués: {len(duplicates_by_slug)}")
    print(f"   Produits → 404: {len(products_404)}")
    print(f"   Pages HTML: {len(existing_pages)}")
    print(f"{'='*70}")
    
    # 7. Suggestions
    if duplicates_by_name or duplicates_by_slug or products_404:
        print(f"\n💡 RECOMMANDATIONS:")
        if duplicates_by_slug:
            print(f"   1. Supprimer les doublons de slugs")
        if products_404:
            print(f"   2. Vérifier les slugs des produits 404")
            print(f"      (peut-être des différences minimes avec les noms de fichiers)")
    else:
        print(f"\n✅ Aucun problème détecté!")

if __name__ == "__main__":
    main()
