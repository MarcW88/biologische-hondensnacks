#!/usr/bin/env python3
"""
Script pour filtrer et limiter les snacks biologiques pour chien
"""

import json
from pathlib import Path

def filter_products(products, max_products=500):
    """Filtre et limite les produits"""
    filtered = []
    
    for product in products:
        # Filtrer par disponibilité
        if not product.get('product_id'):
            continue
        
        # Filtrer par prix (éviter les prix trop bas ou trop élevés)
        price_nl = product.get('price_nl')
        if price_nl:
            try:
                price = float(price_nl)
                if price < 2 or price > 100:
                    continue
            except:
                continue
        else:
            continue
        
        # Filtrer par titre (éviter les titres trop génériques)
        title = product.get('title', '')
        if len(title) < 10 or len(title) > 200:
            continue
        
        # Filtrer par image
        if not product.get('image_url'):
            continue
        
        filtered.append(product)
        
        if len(filtered) >= max_products:
            break
    
    return filtered

def main():
    """Fonction principale"""
    input_file = Path('biological_dog_snacks.json')
    
    if not input_file.exists():
        print(f"Erreur: {input_file} n'existe pas")
        return
    
    # Charger les produits
    with open(input_file, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"Produits totaux: {len(products)}")
    
    # Filtrer
    filtered_products = filter_products(products, max_products=500)
    
    print(f"Produits filtrés: {len(filtered_products)}")
    
    # Sauvegarder
    output_file = Path('filtered_dog_snacks.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_products, f, indent=2, ensure_ascii=False)
    
    print(f"Sauvegardé dans {output_file}")
    
    # Afficher quelques exemples
    print("\nExemples de produits filtrés:")
    for i, product in enumerate(filtered_products[:5]):
        print(f"\n{i+1}. {product['title']}")
        print(f"   Prix: €{product.get('price_nl', 'N/A')}")
        print(f"   Marque: {product.get('brand', 'N/A')}")

if __name__ == '__main__':
    main()
