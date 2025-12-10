#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - PRODUCT IMAGES UPDATER
=================================================

Script om echte productafbeeldingen te koppelen aan de juiste producten
zowel in shop.js (product listing) als in individuele productpagina's.

Functionaliteiten:
- Scant images/ directory voor productafbeeldingen
- Matcht afbeeldingen met productnamen via fuzzy matching
- Update shop.js met juiste image paths
- Update alle individuele productpagina's met juiste afbeeldingen
- Creëert backup van originele bestanden

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import json
import shutil
from pathlib import Path
from difflib import SequenceMatcher

# Configuration
IMAGES_DIR = '/Users/marc/Desktop/biologische-hondensnacks/images'
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
PRODUCTS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/images'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def get_available_images():
    """Get list of available product images"""
    images = []
    
    if not os.path.exists(IMAGES_DIR):
        print(f"❌ Images directory not found: {IMAGES_DIR}")
        return images
    
    for file in os.listdir(IMAGES_DIR):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            # Skip generic images
            if not any(generic in file.lower() for generic in ['gezonde', 'graanvrije', 'natuurlijke', 'zachte', 'hondensnacks', 'logotype', 'images']):
                images.append(file)
    
    print(f"📸 Found {len(images)} product images:")
    for img in sorted(images):
        print(f"   • {img}")
    
    return images

def similarity(a, b):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def clean_name_for_matching(name):
    """Clean product name for better matching"""
    # Remove common words and characters that might interfere
    cleaned = name.lower()
    cleaned = re.sub(r'[^\w\s]', ' ', cleaned)  # Remove punctuation
    cleaned = re.sub(r'\s+', ' ', cleaned)      # Normalize spaces
    return cleaned.strip()

def find_best_image_match(product_name, available_images):
    """Find the best matching image for a product"""
    cleaned_product = clean_name_for_matching(product_name)
    
    best_match = None
    best_score = 0
    
    for image in available_images:
        # Remove extension and clean image name
        image_name = os.path.splitext(image)[0]
        cleaned_image = clean_name_for_matching(image_name)
        
        # Calculate similarity
        score = similarity(cleaned_product, cleaned_image)
        
        # Bonus for exact word matches
        product_words = set(cleaned_product.split())
        image_words = set(cleaned_image.split())
        common_words = product_words.intersection(image_words)
        word_bonus = len(common_words) * 0.1
        
        total_score = score + word_bonus
        
        if total_score > best_score:
            best_score = total_score
            best_match = image
    
    return best_match, best_score

def extract_products_from_shop_js():
    """Extract product data from shop.js"""
    try:
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the allProducts array
        pattern = r'const allProducts = \[(.*?)\];'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            print("❌ Could not find allProducts array in shop.js")
            return []
        
        # Extract product objects (this is a simplified approach)
        products_text = match.group(1)
        
        # Split by product objects (looking for id: pattern)
        product_matches = re.findall(r'\{[^}]*id:\s*(\d+)[^}]*name:\s*"([^"]+)"[^}]*\}', products_text, re.DOTALL)
        
        products = []
        for match in product_matches:
            products.append({
                'id': int(match[0]),
                'name': match[1]
            })
        
        print(f"📦 Extracted {len(products)} products from shop.js")
        return products
        
    except Exception as e:
        print(f"❌ Error reading shop.js: {e}")
        return []

def update_shop_js_images(image_mappings):
    """Update shop.js with correct image paths"""
    try:
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'shop_js_backup.js')
        shutil.copy2(SHOP_JS_FILE, backup_file)
        print(f"💾 Backup created: {backup_file}")
        
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_count = 0
        
        for product_name, image_file in image_mappings.items():
            if image_file:
                # Replace the image URL for this product
                # Look for the product and replace its image URL
                pattern = rf'(name:\s*"{re.escape(product_name)}"[^}}]*image:\s*")[^"]*(")'
                replacement = rf'\1../images/{image_file}\2'
                
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    content = new_content
                    updated_count += 1
                    print(f"✅ Updated image for: {product_name} → {image_file}")
        
        # Write updated content
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"📝 Updated {updated_count} product images in shop.js")
        return updated_count
        
    except Exception as e:
        print(f"❌ Error updating shop.js: {e}")
        return 0

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')[:60]

def update_product_page_images(image_mappings):
    """Update individual product pages with correct images"""
    updated_count = 0
    
    for product_name, image_file in image_mappings.items():
        if not image_file:
            continue
            
        try:
            slug = slugify(product_name)
            html_file = os.path.join(PRODUCTS_DIR, f"{slug}.html")
            
            if not os.path.exists(html_file):
                print(f"⚠️ HTML file not found: {slug}.html")
                continue
            
            # Create backup
            backup_file = os.path.join(BACKUP_DIR, f"{slug}_backup.html")
            shutil.copy2(html_file, backup_file)
            
            # Read HTML content
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace image sources
            # Look for img tags and update src
            img_patterns = [
                r'(<img[^>]*src=")[^"]*(")',
                r'(<img[^>]*class="product-image"[^>]*src=")[^"]*(")',
                r'(<img[^>]*class="hero-image"[^>]*src=")[^"]*(")'
            ]
            
            updated = False
            for pattern in img_patterns:
                new_content = re.sub(pattern, rf'\1../images/{image_file}\2', content)
                if new_content != content:
                    content = new_content
                    updated = True
            
            if updated:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Updated image in: {slug}.html → {image_file}")
                updated_count += 1
            
        except Exception as e:
            print(f"❌ Error updating {product_name}: {e}")
    
    print(f"📄 Updated {updated_count} product pages with images")
    return updated_count

def main():
    """Main function to update product images"""
    print("📸 PRODUCT IMAGES UPDATER")
    print("=" * 50)
    
    # Create backup directory
    create_backup_dir()
    
    # Get available images
    available_images = get_available_images()
    if not available_images:
        print("❌ No product images found!")
        return
    
    # Extract products from shop.js
    products = extract_products_from_shop_js()
    if not products:
        print("❌ No products found in shop.js!")
        return
    
    print(f"\n🔍 Matching {len(products)} products with {len(available_images)} images...")
    
    # Create image mappings
    image_mappings = {}
    used_images = set()
    
    for product in products:
        product_name = product['name']
        
        # Find best matching image
        best_image, score = find_best_image_match(product_name, available_images)
        
        if best_image and score > 0.3:  # Minimum similarity threshold
            if best_image not in used_images:
                image_mappings[product_name] = best_image
                used_images.add(best_image)
                print(f"✅ {product_name[:40]:<40} → {best_image} (score: {score:.2f})")
            else:
                print(f"⚠️ {product_name[:40]:<40} → {best_image} (already used)")
                image_mappings[product_name] = None
        else:
            print(f"❌ {product_name[:40]:<40} → No good match found (best score: {score:.2f})")
            image_mappings[product_name] = None
    
    # Summary of mappings
    mapped_count = sum(1 for img in image_mappings.values() if img is not None)
    print(f"\n📊 Successfully mapped {mapped_count}/{len(products)} products to images")
    
    if mapped_count == 0:
        print("❌ No images could be mapped. Check image names and product names.")
        return
    
    # Update shop.js
    print(f"\n🔄 Updating shop.js...")
    shop_updates = update_shop_js_images(image_mappings)
    
    # Update product pages
    print(f"\n🔄 Updating product pages...")
    page_updates = update_product_page_images(image_mappings)
    
    # Final summary
    print("\n" + "=" * 50)
    print("📊 PRODUCT IMAGES UPDATE RESULTS:")
    print(f"📸 Images available: {len(available_images)}")
    print(f"📦 Products processed: {len(products)}")
    print(f"✅ Successfully mapped: {mapped_count}")
    print(f"🛍️ Shop.js updated: {shop_updates} products")
    print(f"📄 Product pages updated: {page_updates} pages")
    print(f"💾 Backups created in: {BACKUP_DIR}")
    
    if mapped_count > 0:
        print(f"\n🎉 SUCCESS! {mapped_count} products now have real images!")
        print("🔍 Both product listing and individual pages updated")
        print("📈 This will significantly improve visual appeal and user experience")
    
    print("\n🏁 PRODUCT IMAGES UPDATE COMPLETE")

if __name__ == "__main__":
    main()
