#!/usr/bin/env python3
"""
Script pour extraire les snacks biologiques pour chien du product feed Bol.com
"""

import xml.etree.ElementTree as ET
import json
from pathlib import Path
import re

def parse_bol_feed(xml_file):
    """Parse le feed XML Bol.com et extrait les snacks biologiques pour chien"""
    products = []
    
    # Mots-clés pour identifier les snacks biologiques pour chien
    dog_keywords = ['hond', 'honden', 'dog', 'puppy', 'puppies']
    snack_keywords = ['snack', 'snacks', 'brok', 'brokjes', 'koek', 'koekjes', 'treat', 'treats', 'beloning', 'kauw', 'kauwsnack', 'bot', 'botje']
    bio_keywords = ['biologisch', 'bio', 'organic', 'natuurlijk', 'natuurlijke', 'grain-free', 'graanvrij', 'zonder toevoegingen']
    
    # Parser le XML
    context = ET.iterparse(xml_file, events=('start', 'end'))
    context = iter(context)
    
    # Skip the root element
    event, root = next(context)
    
    count = 0
    for event, elem in context:
        if event == 'end' and elem.tag.endswith('Product'):
            try:
                # Extraire les données du produit
                product = extract_product_data(elem)
                
                # Filtrer pour snacks biologiques pour chien
                if is_biological_dog_snack(product, dog_keywords, snack_keywords, bio_keywords):
                    products.append(product)
                    count += 1
                    if count % 100 == 0:
                        print(f"Trouvé {count} snacks biologiques pour chien...")
                
                # Clear element to save memory
                elem.clear()
            except Exception as e:
                print(f"Erreur parsing produit: {e}")
                elem.clear()
                continue
    
    return products

def extract_product_data(elem):
    """Extrait les données d'un produit"""
    # Namespaces
    ns = {'p': 'http://config.services.bol.com/schemas/product-1.1.xsd'}
    
    product = {
        'product_id': elem.find('p:productId', ns).text if elem.find('p:productId', ns) is not None else '',
        'ean': elem.find('p:ean', ns).text if elem.find('p:ean', ns) is not None else '',
        'title': elem.find('p:title', ns).text if elem.find('p:title', ns) is not None else '',
        'product_url_nl': elem.find('p:productUrlNL', ns).text if elem.find('p:productUrlNL', ns) is not None else '',
        'product_url_be': elem.find('p:productUrlBE', ns).text if elem.find('p:productUrlBE', ns) is not None else '',
        'image_url': elem.find('p:imageUrl', ns).text if elem.find('p:imageUrl', ns) is not None else '',
        'brand': elem.find('p:brand', ns).text if elem.find('p:brand', ns) is not None else '',
        'description': elem.find('p:description', ns).text if elem.find('p:description', ns) is not None else '',
    }
    
    # Prix NL
    offer_nl = elem.find('p:OfferNL', ns)
    if offer_nl is not None:
        product['price_nl'] = offer_nl.find('p:sellingPrice', ns).text if offer_nl.find('p:sellingPrice', ns) is not None else ''
        product['shipping_cost_nl'] = offer_nl.find('p:shippingCost', ns).text if offer_nl.find('p:shippingCost', ns) is not None else ''
    
    # Prix BE
    offer_be = elem.find('p:OfferBE', ns)
    if offer_be is not None:
        product['price_be'] = offer_be.find('p:sellingPrice', ns).text if offer_be.find('p:sellingPrice', ns) is not None else ''
        product['shipping_cost_be'] = offer_be.find('p:shippingCost', ns).text if offer_be.find('p:shippingCost', ns) is not None else ''
    
    # GPC (Global Product Classification)
    gpc = elem.find('p:Gpc', ns)
    if gpc is not None:
        product['segment'] = gpc.find('p:segmentName', ns).text if gpc.find('p:segmentName', ns) is not None else ''
        product['family'] = gpc.find('p:familyName', ns).text if gpc.find('p:familyName', ns) is not None else ''
        product['class'] = gpc.find('p:className', ns).text if gpc.find('p:className', ns) is not None else ''
        product['brick'] = gpc.find('p:brickName', ns).text if gpc.find('p:brickName', ns) is not None else ''
        product['chunk'] = gpc.find('p:chunkName', ns).text if gpc.find('p:chunkName', ns) is not None else ''
    
    # Category
    category = elem.find('p:Category', ns)
    if category is not None:
        product['category_unit'] = category.find('p:unit', ns).text if category.find('p:unit', ns) is not None else ''
        product['category'] = category.find('p:category', ns).text if category.find('p:category', ns) is not None else ''
        product['product_group'] = category.find('p:productgroup', ns).text if category.find('p:productgroup', ns) is not None else ''
        product['product_subgroup'] = category.find('p:productsubgroup', ns).text if category.find('p:productsubgroup', ns) is not None else ''
        product['sub_subgroup'] = category.find('p:subsubgroup', ns).text if category.find('p:subsubgroup', ns) is not None else ''
    
    return product

def is_biological_dog_snack(product, dog_keywords, snack_keywords, bio_keywords):
    """Vérifie si le produit est un snack biologique pour chien"""
    title_lower = product.get('title', '').lower()
    description_lower = product.get('description', '').lower()
    combined_text = f"{title_lower} {description_lower}"
    
    # Vérifier si c'est pour chien
    has_dog = any(keyword in combined_text for keyword in dog_keywords)
    
    # Vérifier si c'est un snack
    has_snack = any(keyword in combined_text for keyword in snack_keywords)
    
    # Vérifier si c'est biologique
    has_bio = any(keyword in combined_text for keyword in bio_keywords)
    
    # Vérifier la catégorie
    category = product.get('category', '').lower()
    product_group = product.get('product_group', '').lower()
    class_name = product.get('class', '').lower()
    brick = product.get('brick', '').lower()
    chunk = product.get('chunk', '').lower()
    
    # Catégories pertinentes pour snacks pour chiens
    relevant_categories = ['pet', 'pet supplies', 'pet food', 'dog food', 'dog treats']
    is_relevant_category = any(cat in category or cat in product_group for cat in relevant_categories)
    
    # Classes pertinentes
    relevant_classes = ['voeding', 'food', 'snack', 'treat']
    is_relevant_class = any(cls in class_name or cls in brick or cls in chunk for cls in relevant_classes)
    
    # Doit avoir au moins un mot-clé de chaque catégorie
    return has_dog and has_snack and has_bio and (is_relevant_category or is_relevant_class)

def main():
    """Fonction principale"""
    xml_file = Path('product-feed_pet-v2.xml')
    
    if not xml_file.exists():
        print(f"Erreur: {xml_file} n'existe pas")
        return
    
    print("Extraction des snacks biologiques pour chien du feed Bol.com...")
    products = parse_bol_feed(xml_file)
    
    print(f"\nTrouvé {len(products)} snacks biologiques pour chien")
    
    # Sauvegarder en JSON
    output_file = Path('biological_dog_snacks.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)
    
    print(f"Sauvegardé dans {output_file}")
    
    # Afficher quelques exemples
    print("\nExemples de produits trouvés:")
    for i, product in enumerate(products[:5]):
        print(f"\n{i+1}. {product['title']}")
        print(f"   Prix: €{product.get('price_nl', 'N/A')}")
        print(f"   Catégorie: {product.get('category', 'N/A')}")

if __name__ == '__main__':
    main()
