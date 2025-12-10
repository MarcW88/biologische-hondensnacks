#!/usr/bin/env python3
"""
SCRIPT MISE À JOUR SHOP.JS
Met à jour shop.js avec les vraies données du catalogue
"""

import os
import csv
import re
import json

# Configuration
CSV_FILE = "/Users/marc/Desktop/biologische-hondensnacks/Hondensnacks Catalogus (1).csv"
SHOP_JS_FILE = "/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js"

def slugify(text):
    """Convertit un nom en slug URL-friendly"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def get_product_image(product_name, brand):
    """Retourne une image appropriée selon le type de produit"""
    name_lower = product_name.lower()
    
    if 'kauwstaaf' in name_lower or 'yak' in name_lower:
        return "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop"
    elif 'eend' in name_lower:
        return "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop"
    elif 'kip' in name_lower:
        return "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop"
    elif 'rund' in name_lower:
        return "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop"
    elif 'vis' in name_lower or 'zalm' in name_lower:
        return "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400&h=300&fit=crop"
    else:
        return "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop"

def determine_category(product_name, product_type, features):
    """Détermine la catégorie du produit"""
    name_lower = product_name.lower()
    type_lower = product_type.lower()
    features_lower = features.lower()
    
    if 'puppy' in name_lower or 'puppy' in features_lower:
        return 'puppy'
    elif 'trainer' in type_lower or 'training' in name_lower:
        return 'training'
    elif 'dental' in name_lower or 'dental' in type_lower:
        return 'dental'
    elif 'kauw' in name_lower or 'kauw' in type_lower:
        return 'kauwsnacks'
    elif 'supplement' in type_lower:
        return 'supplementen'
    else:
        return 'natuurlijk'

def determine_age_group(target_group):
    """Détermine le groupe d'âge"""
    target_lower = target_group.lower()
    
    if 'puppy' in target_lower or 'junior' in target_lower:
        return ['puppy']
    elif 'adult' in target_lower:
        return ['adult']
    elif 'senior' in target_lower:
        return ['senior']
    else:
        return ['alle leeftijden']

def determine_size(product_name, features):
    """Détermine la taille appropriée"""
    name_lower = product_name.lower()
    features_lower = features.lower()
    
    if 'kleine honden' in features_lower or 'small' in name_lower:
        return ['klein']
    elif 'grote honden' in features_lower or 'large' in name_lower or 'xl' in name_lower:
        return ['groot']
    elif 'middelgrote' in features_lower or 'medium' in name_lower:
        return ['medium']
    else:
        return ['alle maten']

def determine_features(features, product_type):
    """Détermine les caractéristiques du produit"""
    features_lower = features.lower()
    type_lower = product_type.lower()
    product_features = []
    
    if 'natuurlijk' in features_lower or '100%' in features_lower:
        product_features.append('natuurlijk')
    if 'hypoallergeen' in features_lower:
        product_features.append('hypoallergeen')
    if 'glutenvrij' in features_lower or 'glutenvrij' in type_lower:
        product_features.append('glutenvrij')
    if 'biologisch' in features_lower:
        product_features.append('biologisch')
    if 'gedroogd' in features_lower or 'gedroogd' in type_lower:
        product_features.append('gedroogd')
    if 'supplement' in type_lower:
        product_features.append('supplement')
    
    if not product_features:
        product_features.append('premium')
    
    return product_features

def convert_csv_to_js_products():
    """Convertit le CSV en données JavaScript"""
    products = []
    
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                # Handle BOM
                name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in row else 'Product Naam'
                
                name = row[name_key]
                brand = row['Merk/Verkoper']
                product_type = row['Type Snack']
                weight = row['Gewicht/Inhoud']
                target = row['Doelgroep']
                price_str = row['Prijs €'].replace(',', '.')
                features = row['Bijzonderheden']
                
                # Parse price
                try:
                    price = float(price_str)
                except:
                    price = 25.99  # Default price
                
                slug = slugify(name)
                
                product = {
                    'id': len(products) + 1,
                    'name': name,
                    'brand': brand,
                    'category': determine_category(name, product_type, features),
                    'price': price,
                    'image': get_product_image(name, brand),
                    'description': f"{name} van {brand}. {features}",
                    'weight': weight,
                    'age': determine_age_group(target),
                    'size': determine_size(name, features),
                    'features': determine_features(features, product_type),
                    'inStock': True,
                    'rating': 4.5,
                    'reviews': 25,
                    'url': f"../produits/{slug}.html"
                }
                
                products.append(product)
        
        print(f"✅ Converted {len(products)} products from CSV")
        return products
        
    except Exception as e:
        print(f"❌ Error reading CSV: {str(e)}")
        return []

def update_shop_js(products):
    """Met à jour le fichier shop.js avec les nouvelles données"""
    try:
        # Read current shop.js
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_path = SHOP_JS_FILE + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Generate JavaScript products array
        js_products = "const allProducts = [\n"
        for product in products:
            # Escape quotes in description
            description = product['description'].replace('"', '\\"')
            
            js_products += f"""    {{
        id: {product['id']},
        name: "{product['name']}",
        brand: "{product['brand']}",
        category: "{product['category']}",
        price: {product['price']},
        image: "{product['image']}",
        description: "{description}",
        weight: "{product['weight']}",
        age: {json.dumps(product['age'])},
        size: {json.dumps(product['size'])},
        features: {json.dumps(product['features'])},
        inStock: {str(product['inStock']).lower()},
        rating: {product['rating']},
        reviews: {product['reviews']},
        url: "{product['url']}"
    }},
"""
        js_products = js_products.rstrip(',\n') + "\n];"
        
        # Replace the allProducts array
        pattern = r'const allProducts = \[.*?\];'
        new_content = re.sub(pattern, js_products, content, flags=re.DOTALL)
        
        # Update filteredProducts
        new_content = re.sub(
            r'let filteredProducts = .*?;',
            'let filteredProducts = [...allProducts];',
            new_content
        )
        
        # Write updated content
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated shop.js with {len(products)} real products")
        return True
        
    except Exception as e:
        print(f"❌ Error updating shop.js: {str(e)}")
        return False

def main():
    """Main function"""
    print("🔄 STARTING SHOP.JS UPDATE")
    print("=" * 50)
    
    # Convert CSV to products
    print("📊 Converting CSV to JavaScript products...")
    products = convert_csv_to_js_products()
    
    if not products:
        print("❌ No products found, aborting update")
        return
    
    # Update shop.js
    print("🔄 Updating shop.js file...")
    success = update_shop_js(products)
    
    print("\n" + "=" * 50)
    print("📊 SHOP.JS UPDATE RESULTS:")
    
    if success:
        print(f"✅ Successfully updated shop.js")
        print(f"📦 Products: {len(products)}")
        print(f"💾 Backup created: shop.js.backup")
        
        # Show categories
        categories = set(p['category'] for p in products)
        brands = set(p['brand'] for p in products)
        
        print(f"\n📋 Categories: {', '.join(sorted(categories))}")
        print(f"🏷️ Brands: {len(brands)} unique brands")
        print(f"💰 Price range: €{min(p['price'] for p in products):.2f} - €{max(p['price'] for p in products):.2f}")
    else:
        print("❌ Failed to update shop.js")
    
    print("\n🏁 SHOP.JS UPDATE COMPLETE")

if __name__ == "__main__":
    main()
