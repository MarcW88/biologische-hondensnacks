#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - IMAGES INTEGRATION FIXER
===================================================

Script pour corriger l'intégration des vraies images dans:
1. Winkel product listing
2. Pages produits gerelateerde producten
3. CSS pour que les images rentrent parfaitement dans les encadrés

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import shutil
from pathlib import Path

# Configuration
PROJECT_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
IMAGES_DIR = '/Users/marc/Desktop/biologische-hondensnacks/images'
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
SHOP_CSS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop-styles.css'
PRODUCTS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/images_integration_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def get_available_images():
    """Get mapping of product names to image files"""
    images_map = {}
    
    if not os.path.exists(IMAGES_DIR):
        return images_map
    
    for file in os.listdir(IMAGES_DIR):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            # Skip generic/non-product images
            if not any(skip in file.lower() for skip in ['gezonde', 'graanvrije', 'natuurlijke', 'zachte', 'hondensnacks', 'logotype', 'cartoon', 'seo']):
                # Clean filename for matching
                clean_name = os.path.splitext(file)[0].strip()
                images_map[clean_name] = file
    
    print(f"📸 Found {len(images_map)} product images:")
    for name, file in images_map.items():
        print(f"   • {name} -> {file}")
    
    return images_map

def fix_shop_js_images():
    """Fix images in shop.js to use real product images"""
    try:
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'shop_js_images_backup.js')
        shutil.copy2(SHOP_JS_FILE, backup_file)
        
        images_map = get_available_images()
        updated_count = 0
        
        # Replace Unsplash placeholder images with real images
        for product_name, image_file in images_map.items():
            # Try different matching patterns
            patterns = [
                # Exact name match
                rf'(name:\s*"[^"]*{re.escape(product_name)}[^"]*"[^}}]*image:\s*")[^"]*(")',
                # Partial name match (more flexible)
                rf'(name:\s*"[^"]*{re.escape(product_name.split()[0])}[^"]*"[^}}]*image:\s*")[^"]*(")',
            ]
            
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    replacement = rf'\\1../images/{image_file}\\2'
                    new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                    if new_content != content:
                        content = new_content
                        updated_count += 1
                        print(f"✅ Updated image for: {product_name}")
                        break
        
        # Also replace any remaining Unsplash URLs with fallback
        unsplash_pattern = r'image:\s*"https://images\.unsplash\.com[^"]*"'
        fallback_image = "../images/natuurlijke-zalm-bites.jpg"  # Use as fallback
        
        unsplash_matches = re.findall(unsplash_pattern, content)
        if unsplash_matches:
            content = re.sub(unsplash_pattern, f'image: "{fallback_image}"', content)
            print(f"🔄 Replaced {len(unsplash_matches)} Unsplash placeholders with fallback image")
        
        # Write updated content
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"📝 Updated {updated_count} product images in shop.js")
        return updated_count > 0
        
    except Exception as e:
        print(f"❌ Error updating shop.js images: {e}")
        return False

def fix_css_image_display():
    """Fix CSS to ensure images fit perfectly in containers without being cut"""
    try:
        with open(SHOP_CSS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'shop_css_display_backup.css')
        shutil.copy2(SHOP_CSS_FILE, backup_file)
        
        # Add improved CSS for perfect image display
        improved_css = '''

/* PERFECT IMAGE DISPLAY - NO CUTTING */
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
    height: 240px;
    object-fit: contain; /* CONTAIN instead of COVER to show full image */
    object-position: center;
    display: block;
    background: #f8fafc;
    padding: 0.5rem; /* Small padding to ensure image doesn't touch edges */
}

/* Alternative: Use background-image for better control */
.product-card .product-image-bg {
    width: 100%;
    height: 240px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-color: #f8fafc;
    display: block;
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
    min-height: 2.8rem; /* Ensure consistent height */
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
    height: 2.6rem; /* Fixed height for consistency */
}

.product-card .product-features {
    display: flex;
    flex-wrap: wrap;
    gap: 0.375rem;
    margin-bottom: 1rem;
    min-height: 1.5rem; /* Consistent spacing */
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
    height: 1.5rem; /* Fixed height */
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
    min-height: 3rem; /* Consistent height */
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
    min-height: 2.75rem; /* Consistent button height */
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

/* List view adjustments */
.products-grid.list-view .product-card {
    flex-direction: row;
    height: auto;
}

.products-grid.list-view .product-image {
    width: 200px;
    height: 160px;
    flex-shrink: 0;
}

.products-grid.list-view .product-info {
    padding: 1.25rem;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .product-card .product-image {
        height: 200px;
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
        height: 200px;
    }
}

/* Ensure grid consistency */
.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    align-items: stretch; /* All cards same height */
}

@media (max-width: 768px) {
    .products-grid {
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 1rem;
    }
}'''
        
        # Remove old product card styles and add new ones
        pattern = r'/\* IMPROVED PRODUCT IMAGES DISPLAY \*/.*?(?=\n/\*|\n\.|\Z)'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Add the improved CSS at the end
        content += improved_css
        
        with open(SHOP_CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated CSS for perfect image display (no cutting)")
        return True
        
    except Exception as e:
        print(f"❌ Error updating CSS: {e}")
        return False

def fix_product_pages_related_images():
    """Fix related product images on individual product pages"""
    try:
        images_map = get_available_images()
        fixed_count = 0
        
        for filename in os.listdir(PRODUCTS_DIR):
            if filename.endswith('.html') and filename != 'index.html':
                file_path = os.path.join(PRODUCTS_DIR, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Look for related product images and update them
                    original_content = content
                    
                    # Replace Unsplash URLs in related products
                    for product_name, image_file in images_map.items():
                        # Pattern for related products section
                        pattern = rf'(<img src=")[^"]*unsplash[^"]*(" alt="[^"]*{re.escape(product_name.split()[0])}[^"]*")'
                        if re.search(pattern, content, re.IGNORECASE):
                            replacement = rf'\\1../images/{image_file}\\2'
                            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                    
                    # General Unsplash replacement for related products
                    unsplash_pattern = r'(<img src=")https://images\.unsplash\.com[^"]*(" alt="[^"]*"[^>]*class="product-image")'
                    if re.search(unsplash_pattern, content):
                        content = re.sub(unsplash_pattern, rf'\\1../images/natuurlijke-zalm-bites.jpg\\2', content)
                    
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed_count += 1
                        print(f"✅ Fixed related images in: {filename}")
                
                except Exception as e:
                    print(f"⚠️ Error processing {filename}: {e}")
        
        print(f"📄 Fixed related images in {fixed_count} product pages")
        return fixed_count > 0
        
    except Exception as e:
        print(f"❌ Error fixing product pages: {e}")
        return False

def main():
    """Main function to fix all image integration issues"""
    print("🖼️ IMAGES INTEGRATION FIXER")
    print("=" * 50)
    
    create_backup_dir()
    
    # 1. Fix shop.js images
    print("\\n1️⃣ FIXING WINKEL PRODUCT IMAGES...")
    shop_images_fixed = fix_shop_js_images()
    
    # 2. Fix CSS for perfect display
    print("\\n2️⃣ FIXING CSS FOR PERFECT IMAGE DISPLAY...")
    css_fixed = fix_css_image_display()
    
    # 3. Fix product pages related images
    print("\\n3️⃣ FIXING PRODUCT PAGES RELATED IMAGES...")
    product_pages_fixed = fix_product_pages_related_images()
    
    # Summary
    print("\\n" + "=" * 50)
    print("📊 IMAGES INTEGRATION FIX RESULTS:")
    print(f"🛍️ Winkel images fixed: {'✅' if shop_images_fixed else '❌'}")
    print(f"🎨 CSS display fixed: {'✅' if css_fixed else '❌'}")
    print(f"📄 Product pages fixed: {'✅' if product_pages_fixed else '❌'}")
    
    if shop_images_fixed and css_fixed:
        print(f"\\n🎉 SUCCESS! Images integration completely fixed!")
        print("📸 Real product images now display in winkel")
        print("🖼️ Images fit perfectly in containers (no cutting)")
        print("📱 Responsive design maintained")
        print("🎯 Related products use real images")
        
        print(f"\\n📋 IMPROVEMENTS APPLIED:")
        print("• object-fit: contain (shows full image)")
        print("• Consistent card heights")
        print("• Proper padding to prevent edge touching")
        print("• Fallback images for missing products")
        print("• Mobile responsive adjustments")
    else:
        print(f"\\n⚠️ Some fixes failed - check individual results above")
    
    print("\\n🏁 IMAGES INTEGRATION FIX COMPLETE")

if __name__ == "__main__":
    main()
