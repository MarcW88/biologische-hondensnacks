#!/usr/bin/env python3
"""
Script pour générer le fichier products.js avec les données des produits
"""

import json
from pathlib import Path
import html as html_mod

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = text.replace(' ', '-')
    text = ''.join(c for c in text if c.isalnum() or c == '-')
    return text.strip('-')

def escape_js(text):
    """Escape text for JavaScript"""
    return json.dumps(text)

def main():
    """Fonction principale"""
    # Charger les produits
    products = json.load(open('filtered_dog_snacks.json', encoding='utf-8'))
    
    # Générer le fichier JavaScript
    js_content = "// Données des produits biologiques pour chien\nconst products = [\n"
    
    for i, product in enumerate(products):
        title = product.get('title', '')
        price = product.get('price_nl', '')
        image_url = product.get('image_url', '')
        product_url = product.get('product_url_nl', '')
        brand = product.get('brand', '')
        description = product.get('description', '')
        slug = slugify(title)
        
        if price:
            try:
                price_float = float(price)
            except:
                price_float = 0.0
        else:
            price_float = 0.0
        
        js_content += f"  {{\n"
        js_content += f"    id: {i + 1},\n"
        js_content += f"    title: {escape_js(title)},\n"
        js_content += f"    price: {price_float},\n"
        js_content += f"    imageUrl: {escape_js(image_url)},\n"
        js_content += f"    productUrl: {escape_js(product_url)},\n"
        js_content += f"    brand: {escape_js(brand)},\n"
        js_content += f"    description: {escape_js(description[:200])},\n"
        js_content += f"    slug: {escape_js(slug)},\n"
        js_content += f"    pageUrl: 'produits/{slug}.html'\n"
        js_content += f"  }}"
        
        if i < len(products) - 1:
            js_content += ",\n"
        else:
            js_content += "\n"
    
    js_content += "];\n"
    
    # Sauvegarder
    output_file = Path('products.js')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Fichier products.js généré avec {len(products)} produits")

if __name__ == '__main__':
    main()
