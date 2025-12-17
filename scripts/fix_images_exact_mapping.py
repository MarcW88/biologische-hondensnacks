#!/usr/bin/env python3
"""
MAPPING EXACT: NOM PRODUIT = NOM IMAGE
=====================================

Script ultra-simple : si le nom du produit correspond exactement 
au nom d'une image, on l'utilise. Point final.

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import json

# Configuration
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
IMAGES_DIR = '/Users/marc/Desktop/biologische-hondensnacks/images'

def get_available_images():
    """Get all available product images"""
    images = {}
    
    for file in os.listdir(IMAGES_DIR):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Skip generic images
            if not any(skip in file.lower() for skip in ['gezonde', 'graanvrije', 'natuurlijke', 'zachte', 'hondensnacks', 'logotype', 'cartoon', 'seo']):
                # Use filename without extension as key
                name_without_ext = os.path.splitext(file)[0].strip()
                images[name_without_ext] = file
    
    print(f"📸 Available images: {len(images)}")
    for name, file in images.items():
        print(f"   • {name}")
    
    return images

def extract_products_from_js():
    """Extract product names from shop.js"""
    try:
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all product names
        name_pattern = r'name:\s*"([^"]+)"'
        product_names = re.findall(name_pattern, content)
        
        print(f"📦 Found {len(product_names)} products:")
        for name in product_names[:10]:  # Show first 10
            print(f"   • {name}")
        
        return product_names, content
        
    except Exception as e:
        print(f"❌ Error reading shop.js: {e}")
        return [], ""

def fix_images_exact_mapping():
    """Fix images with exact name mapping"""
    
    available_images = get_available_images()
    product_names, content = extract_products_from_js()
    
    if not content:
        return False
    
    updated_count = 0
    
    # For each available image, find the corresponding product and update it
    for image_name, image_file in available_images.items():
        
        # Look for exact match in product names
        for product_name in product_names:
            if image_name == product_name:
                print(f"🎯 EXACT MATCH: {product_name} → {image_file}")
                
                # Find and replace the image for this exact product
                # Pattern: find the product block and update its image
                pattern = rf'(\{{[^}}]*name:\s*"{re.escape(product_name)}"[^}}]*image:\s*")[^"]*(")'
                
                if re.search(pattern, content):
                    replacement = rf'\\1../images/{image_file}\\2'
                    new_content = re.sub(pattern, replacement, content)
                    if new_content != content:
                        content = new_content
                        updated_count += 1
                        print(f"✅ Updated: {product_name}")
                break
    
    # Write the updated content
    try:
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"📝 Updated {updated_count} exact matches")
        return True
        
    except Exception as e:
        print(f"❌ Error writing shop.js: {e}")
        return False

def main():
    """Main function"""
    print("🎯 EXACT IMAGE MAPPING")
    print("=" * 40)
    
    print("\\n1️⃣ SCANNING IMAGES...")
    available_images = get_available_images()
    
    print("\\n2️⃣ SCANNING PRODUCTS...")
    product_names, _ = extract_products_from_js()
    
    print("\\n3️⃣ EXACT MATCHING...")
    success = fix_images_exact_mapping()
    
    if success:
        print("\\n🎉 SUCCESS! Exact image mapping applied!")
        print("📸 Products with matching image names now use their real images")
    else:
        print("\\n❌ Failed to apply exact mapping")
    
    print("\\n🏁 EXACT MAPPING COMPLETE")

if __name__ == "__main__":
    main()
