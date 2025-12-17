#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - PRODUCT IMAGES DISPLAY FIXER
=======================================================

Script pour corriger l'affichage des images dans le winkel et les pages produits
afin qu'elles s'affichent correctement dans leurs encadrés.

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import csv
import shutil
from pathlib import Path

# Configuration
PROJECT_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
IMAGES_DIR = '/Users/marc/Desktop/biologische-hondensnacks/images'
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
SHOP_CSS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop-styles.css'
PRODUCTS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'
PRODUCT_CSS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/produits/product-page.css'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/images_display_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def get_available_images():
    """Get list of available product images"""
    images = {}
    
    if not os.path.exists(IMAGES_DIR):
        print(f"❌ Images directory not found: {IMAGES_DIR}")
        return images
    
    for file in os.listdir(IMAGES_DIR):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            # Skip generic images
            if not any(generic in file.lower() for generic in ['gezonde', 'graanvrije', 'natuurlijke', 'zachte', 'hondensnacks', 'logotype', 'images', 'cartoon']):
                # Use filename without extension as key
                name_key = os.path.splitext(file)[0]
                images[name_key] = file
    
    print(f"📸 Found {len(images)} product images")
    return images

def update_shop_css():
    """Update shop CSS for better image display"""
    try:
        with open(SHOP_CSS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'shop-styles_backup.css')
        shutil.copy2(SHOP_CSS_FILE, backup_file)
        
        # Add improved CSS for product images
        improved_css = '''

/* IMPROVED PRODUCT IMAGES DISPLAY */
.product-card {
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    overflow: hidden;
    background: white;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.product-card .product-image {
    width: 100%;
    height: 220px;
    object-fit: cover;
    object-position: center;
    display: block;
    background: #f8fafc;
}

.product-card .product-info {
    padding: 1.25rem;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.product-card .product-brand {
    font-size: 0.875rem;
    color: #E68161;
    font-weight: 600;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.product-card .product-name {
    font-size: 1rem;
    font-weight: 600;
    color: #1f2937;
    margin: 0 0 0.75rem 0;
    line-height: 1.4;
    flex-grow: 1;
}

.product-card .product-description {
    font-size: 0.875rem;
    color: #6b7280;
    margin-bottom: 1rem;
    line-height: 1.5;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.product-card .product-features {
    display: flex;
    flex-wrap: wrap;
    gap: 0.375rem;
    margin-bottom: 1rem;
}

.product-card .feature-tag {
    background: #f0f9ff;
    color: #0369a1;
    padding: 0.25rem 0.75rem;
    border-radius: 16px;
    font-size: 0.75rem;
    font-weight: 500;
    border: 1px solid #e0f2fe;
}

.product-card .product-rating {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.product-card .stars {
    color: #fbbf24;
    font-size: 1rem;
}

.product-card .rating-text {
    font-size: 0.875rem;
    color: #6b7280;
}

.product-card .product-price {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.25rem;
    padding: 0.75rem;
    background: #f8fafc;
    border-radius: 8px;
    border-left: 4px solid #E68161;
}

.product-card .price-current {
    font-size: 1.375rem;
    font-weight: 700;
    color: #E68161;
}

.product-card .price-per-unit {
    font-size: 0.875rem;
    color: #6b7280;
    font-weight: 500;
}

.product-card .product-actions {
    border-top: 1px solid #f3f4f6;
    padding-top: 1rem;
    margin-top: auto;
}

.product-card .product-buttons {
    display: flex;
    gap: 0.75rem;
}

.product-card .btn-secondary,
.product-card .btn-primary {
    flex: 1;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    text-decoration: none;
    text-align: center;
    font-size: 0.875rem;
    font-weight: 600;
    transition: all 0.3s;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.product-card .btn-secondary {
    background: white;
    color: #374151;
    border: 2px solid #e5e7eb;
}

.product-card .btn-secondary:hover {
    background: #f9fafb;
    border-color: #E68161;
    color: #E68161;
    transform: translateY(-1px);
}

.product-card .btn-primary {
    background: #E68161;
    color: white;
    border: 2px solid #E68161;
}

.product-card .btn-primary:hover {
    background: #d67347;
    border-color: #d67347;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(230, 129, 97, 0.3);
}

.product-card .out-of-stock {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: #dc2626;
    color: white;
    padding: 0.375rem 0.75rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    z-index: 10;
}

/* List view adjustments */
.products-grid.list-view .product-card {
    flex-direction: row;
    height: auto;
}

.products-grid.list-view .product-image {
    width: 180px;
    height: 140px;
    flex-shrink: 0;
}

.products-grid.list-view .product-info {
    padding: 1.25rem;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .product-card .product-image {
        height: 180px;
    }
    
    .product-card .product-buttons {
        flex-direction: column;
        gap: 0.5rem;
    }
    
    .products-grid.list-view .product-card {
        flex-direction: column;
    }
    
    .products-grid.list-view .product-image {
        width: 100%;
        height: 180px;
    }
}'''
        
        # Remove old product card styles and add new ones
        # First remove the old PRODUCT CARD IMAGE FIX section
        pattern = r'/\* PRODUCT CARD IMAGE FIX \*/.*?(?=\n/\*|\n\.|\Z)'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Add the improved CSS at the end
        content += improved_css
        
        with open(SHOP_CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated shop CSS for better image display")
        return True
        
    except Exception as e:
        print(f"❌ Error updating shop CSS: {e}")
        return False

def update_product_page_css():
    """Update product page CSS for better image display"""
    try:
        with open(PRODUCT_CSS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'product-page_backup.css')
        shutil.copy2(PRODUCT_CSS_FILE, backup_file)
        
        # Update main image styles
        main_image_pattern = r'\.main-image img \{[^}]*\}'
        new_main_image_css = '''.main-image img {
    width: 100%;
    height: 450px;
    object-fit: cover;
    object-position: center;
    display: block;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}'''
        
        content = re.sub(main_image_pattern, new_main_image_css, content)
        
        # Update related products images
        related_image_pattern = r'\.related-products \.product-image \{[^}]*\}'
        new_related_image_css = '''.related-products .product-image {
    width: 100%;
    height: 180px;
    object-fit: cover;
    object-position: center;
    border-radius: 8px;
}'''
        
        content = re.sub(related_image_pattern, new_related_image_css, content)
        
        with open(PRODUCT_CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated product page CSS for better image display")
        return True
        
    except Exception as e:
        print(f"❌ Error updating product page CSS: {e}")
        return False

def verify_image_paths_in_shop_js():
    """Verify and update image paths in shop.js"""
    try:
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        available_images = get_available_images()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'shop_js_images_backup.js')
        shutil.copy2(SHOP_JS_FILE, backup_file)
        
        updated_count = 0
        
        # Find all image references and update them
        for product_name, image_file in available_images.items():
            # Try to match product names in the JavaScript
            # Look for name: "Product Name" and update the corresponding image
            pattern = rf'(name:\s*"[^"]*{re.escape(product_name)}[^"]*"[^}}]*image:\s*")[^"]*(")'
            
            if re.search(pattern, content, re.IGNORECASE):
                replacement = rf'\1../images/{image_file}\2'
                new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                if new_content != content:
                    content = new_content
                    updated_count += 1
                    print(f"✅ Updated image for: {product_name}")
        
        # Write updated content
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"📝 Updated {updated_count} image paths in shop.js")
        return updated_count > 0
        
    except Exception as e:
        print(f"❌ Error updating shop.js image paths: {e}")
        return False

def main():
    """Main function to fix product images display"""
    print("🖼️ PRODUCT IMAGES DISPLAY FIXER")
    print("=" * 50)
    
    create_backup_dir()
    
    # 1. Update shop CSS
    print("\n1️⃣ UPDATING SHOP CSS...")
    shop_css_updated = update_shop_css()
    
    # 2. Update product page CSS
    print("\n2️⃣ UPDATING PRODUCT PAGE CSS...")
    product_css_updated = update_product_page_css()
    
    # 3. Verify image paths in shop.js
    print("\n3️⃣ VERIFYING IMAGE PATHS...")
    images_updated = verify_image_paths_in_shop_js()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 IMAGES DISPLAY FIX RESULTS:")
    print(f"🎨 Shop CSS updated: {'✅' if shop_css_updated else '❌'}")
    print(f"📄 Product page CSS updated: {'✅' if product_css_updated else '❌'}")
    print(f"🖼️ Image paths verified: {'✅' if images_updated else '❌'}")
    
    if shop_css_updated and product_css_updated:
        print(f"\n🎉 SUCCESS! Image display improved!")
        print("📸 Images now fit perfectly in their containers")
        print("🎨 Better styling for product cards")
        print("📱 Mobile responsive image display")
        print("🖼️ Proper object-fit and positioning")
        
        print(f"\n📋 IMPROVEMENTS APPLIED:")
        print("• Product images: 220px height with cover fit")
        print("• Product page images: 450px height with cover fit")
        print("• Better hover effects and shadows")
        print("• Improved mobile responsiveness")
        print("• Enhanced visual hierarchy")
    else:
        print(f"\n⚠️ Some updates failed - check individual results above")
    
    print("\n🏁 IMAGES DISPLAY FIX COMPLETE")

if __name__ == "__main__":
    main()
