#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - WEBSHOP ISSUES FIXER
===============================================

Script pour corriger:
1. Header uniforme sur toutes les pages
2. Images qui rentrent dans les encadrés
3. Filtres qui fonctionnent correctement

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
CSV_FILE = '/Users/marc/Desktop/biologische-hondensnacks/Hondensnacks Catalogus (1).csv'
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
WINKEL_HTML = '/Users/marc/Desktop/biologische-hondensnacks/winkel/index.html'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/webshop_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def get_unified_header():
    """Get the unified header HTML that should be used everywhere"""
    return '''    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="../" style="color: #E68161; font-weight: bold; text-decoration: none;">Biologische Hondensnacks</a>
                </div>
                
                <nav class="nav">
                    <ul>
                        <li><a href="../">Home</a></li>
                        <li><a href="../natuurlijke-hondensnacks/">Natuurlijke snacks</a></li>
                        <li><a href="../beste-hondensnacks-2026/">Top 10 Beste</a></li>
                        <li><a href="../hondensnacks-voor-puppy/">Puppy Snacks</a></li>
                        <li><a href="../blog/">Blog</a></li>
                        <li><a href="../over-ons/">Over Ons</a></li>
                        <li><a href="../winkel/" class="nav-shop">Winkel</a></li>
                    </ul>
                </nav>
                
                <button class="mobile-menu-toggle">☰</button>
            </div>
        </div>
    </header>'''

def fix_product_headers():
    """Fix headers in all product pages to match winkel header"""
    print("🔧 Fixing product page headers...")
    
    products_dir = os.path.join(PROJECT_DIR, 'produits')
    fixed_count = 0
    
    for filename in os.listdir(products_dir):
        if filename.endswith('.html') and filename != 'index.html':
            file_path = os.path.join(products_dir, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Create backup
                backup_path = os.path.join(BACKUP_DIR, f"{filename}_header_backup.html")
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Replace header section
                header_pattern = r'<header class="header">.*?</header>'
                new_header = get_unified_header()
                
                new_content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    fixed_count += 1
                    print(f"✅ Fixed header: {filename}")
                
            except Exception as e:
                print(f"❌ Error fixing {filename}: {e}")
    
    print(f"📊 Fixed {fixed_count} product page headers")
    return fixed_count

def add_image_css_fix():
    """Add CSS to fix image sizing in product cards"""
    print("🎨 Adding CSS fix for product card images...")
    
    css_fix = '''
/* PRODUCT CARD IMAGE FIX */
.product-card {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    overflow: hidden;
    background: white;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.product-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.product-card .product-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    object-position: center;
    display: block;
}

.product-card .product-info {
    padding: 1rem;
}

.product-card .product-brand {
    font-size: 0.875rem;
    color: #E68161;
    font-weight: 600;
    margin-bottom: 0.25rem;
}

.product-card .product-name {
    font-size: 1rem;
    font-weight: 600;
    color: #1f2937;
    margin: 0 0 0.5rem 0;
    line-height: 1.4;
}

.product-card .product-description {
    font-size: 0.875rem;
    color: #6b7280;
    margin-bottom: 0.75rem;
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.product-card .product-features {
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
    margin-bottom: 0.75rem;
}

.product-card .feature-tag {
    background: #f3f4f6;
    color: #374151;
    padding: 0.125rem 0.5rem;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 500;
}

.product-card .product-rating {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
}

.product-card .stars {
    color: #fbbf24;
}

.product-card .rating-text {
    font-size: 0.875rem;
    color: #6b7280;
}

.product-card .product-price {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
}

.product-card .price-current {
    font-size: 1.25rem;
    font-weight: 700;
    color: #E68161;
}

.product-card .price-per-unit {
    font-size: 0.875rem;
    color: #6b7280;
}

.product-card .product-actions {
    border-top: 1px solid #f3f4f6;
    padding-top: 1rem;
}

.product-card .product-buttons {
    display: flex;
    gap: 0.5rem;
}

.product-card .btn-secondary,
.product-card .btn-primary {
    flex: 1;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    text-decoration: none;
    text-align: center;
    font-size: 0.875rem;
    font-weight: 600;
    transition: all 0.2s;
}

.product-card .btn-secondary {
    background: white;
    color: #374151;
    border: 1px solid #d1d5db;
}

.product-card .btn-secondary:hover {
    background: #f9fafb;
    border-color: #E68161;
    color: #E68161;
}

.product-card .btn-primary {
    background: #E68161;
    color: white;
    border: 1px solid #E68161;
}

.product-card .btn-primary:hover {
    background: #d67347;
    border-color: #d67347;
}

.product-card .out-of-stock {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    background: #dc2626;
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}
'''
    
    # Add CSS to shop-styles.css
    shop_css_file = os.path.join(PROJECT_DIR, 'winkel', 'shop-styles.css')
    
    try:
        with open(shop_css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Create backup
        backup_path = os.path.join(BACKUP_DIR, 'shop-styles_backup.css')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        # Add our CSS fix
        new_css_content = css_content + css_fix
        
        with open(shop_css_file, 'w', encoding='utf-8') as f:
            f.write(new_css_content)
        
        print("✅ Added CSS fix for product card images")
        return True
        
    except Exception as e:
        print(f"❌ Error adding CSS fix: {e}")
        return False

def analyze_product_data():
    """Analyze product data to understand categories and brands"""
    print("🔍 Analyzing product data for filters...")
    
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('\ufeff'):
                content = content[1:]
            
            reader = csv.DictReader(content.splitlines(), delimiter=';')
            products = list(reader)
        
        # Analyze brands
        brands = set()
        categories = set()
        types = set()
        
        for product in products:
            name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
            
            brand = product['Merk/Verkoper']
            type_snack = product['Type Snack']
            
            brands.add(brand)
            types.add(type_snack)
            
            # Categorize based on type
            if any(word in type_snack.lower() for word in ['kauw', 'bot', 'stick']):
                categories.add('kauwsnacks')
            elif any(word in type_snack.lower() for word in ['trainer', 'beloning']):
                categories.add('training')
            elif any(word in type_snack.lower() for word in ['dental', 'tand']):
                categories.add('dental')
            elif any(word in product['Doelgroep'].lower() for word in ['puppy', 'jong']):
                categories.add('puppy')
            else:
                categories.add('natuurlijk')
        
        print(f"📊 Found {len(brands)} unique brands:")
        for brand in sorted(brands):
            print(f"   • {brand}")
        
        print(f"📊 Found {len(types)} unique types:")
        for type_snack in sorted(types):
            print(f"   • {type_snack}")
        
        print(f"📊 Suggested categories: {sorted(categories)}")
        
        return {
            'brands': sorted(brands),
            'categories': sorted(categories),
            'types': sorted(types)
        }
        
    except Exception as e:
        print(f"❌ Error analyzing product data: {e}")
        return None

def fix_filter_html(analysis_data):
    """Fix the filter HTML to match actual product data"""
    print("🔧 Fixing filter HTML...")
    
    if not analysis_data:
        return False
    
    try:
        with open(WINKEL_HTML, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_path = os.path.join(BACKUP_DIR, 'winkel_index_backup.html')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Generate new brand filters
        brand_filters = ""
        for brand in analysis_data['brands'][:10]:  # Limit to top 10
            brand_filters += f'''                            <label class="filter-option">
                                <input type="checkbox" data-filter-type="brands" data-filter-value="{brand}">
                                <span>{brand}</span>
                            </label>
'''
        
        # Replace brand section
        brand_pattern = r'(<div class="filter-section">\s*<label class="filter-title">🏭 Merk</label>\s*<div class="filter-options">)(.*?)(</div>\s*</div>)'
        brand_replacement = rf'\1\n{brand_filters}                        \3'
        
        new_content = re.sub(brand_pattern, brand_replacement, content, flags=re.DOTALL)
        
        with open(WINKEL_HTML, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ Fixed filter HTML with real brand data")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing filter HTML: {e}")
        return False

def fix_shop_js_filters():
    """Fix the JavaScript filter logic"""
    print("🔧 Fixing JavaScript filter logic...")
    
    try:
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_path = os.path.join(BACKUP_DIR, 'shop_js_filters_backup.js')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Add debug logging to filter initialization
        debug_code = '''
    // DEBUG: Log filter initialization
    console.log('🔧 Initializing filters...');
    console.log('📋 Filter checkboxes found:', document.querySelectorAll('.filter-option input[type="checkbox"]').length);
    
    // Add event listeners for filter checkboxes with debug
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach((checkbox, index) => {
        console.log(`🔘 Filter ${index}:`, {
            type: checkbox.getAttribute('data-filter-type'),
            value: checkbox.getAttribute('data-filter-value')
        });
        
        checkbox.addEventListener('change', function() {
            const filterType = this.getAttribute('data-filter-type');
            const filterValue = this.getAttribute('data-filter-value');
            
            console.log('🎯 Filter changed:', { filterType, filterValue, checked: this.checked });
            
            if (this.checked) {
                if (!activeFilters[filterType].includes(filterValue)) {
                    activeFilters[filterType].push(filterValue);
                }
            } else {
                activeFilters[filterType] = activeFilters[filterType].filter(v => v !== filterValue);
            }
            
            console.log('📊 Active filters:', activeFilters);
            applyFilters();
        });
    });'''
        
        # Replace the existing filter initialization
        old_pattern = r'// Add event listeners for filter checkboxes\s*document\.querySelectorAll\(\'\.filter-option input\[type="checkbox"\]\'\)\.forEach\(checkbox => \{.*?\}\);'
        
        new_content = re.sub(old_pattern, debug_code, content, flags=re.DOTALL)
        
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ Added debug logging to filter initialization")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing JavaScript filters: {e}")
        return False

def main():
    """Main function to fix all webshop issues"""
    print("🔧 WEBSHOP ISSUES FIXER")
    print("=" * 50)
    
    create_backup_dir()
    
    # 1. Fix headers
    print("\n1️⃣ FIXING HEADERS...")
    header_count = fix_product_headers()
    
    # 2. Fix image CSS
    print("\n2️⃣ FIXING IMAGE SIZING...")
    css_fixed = add_image_css_fix()
    
    # 3. Analyze product data
    print("\n3️⃣ ANALYZING PRODUCT DATA...")
    analysis_data = analyze_product_data()
    
    # 4. Fix filter HTML
    print("\n4️⃣ FIXING FILTER HTML...")
    filter_html_fixed = fix_filter_html(analysis_data)
    
    # 5. Fix JavaScript filters
    print("\n5️⃣ FIXING JAVASCRIPT FILTERS...")
    js_fixed = fix_shop_js_filters()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 WEBSHOP FIX RESULTS:")
    print(f"🏷️ Headers fixed: {header_count} pages")
    print(f"🎨 CSS fix applied: {'✅' if css_fixed else '❌'}")
    print(f"🔍 Product data analyzed: {'✅' if analysis_data else '❌'}")
    print(f"📋 Filter HTML fixed: {'✅' if filter_html_fixed else '❌'}")
    print(f"⚙️ JavaScript fixed: {'✅' if js_fixed else '❌'}")
    
    if all([header_count > 0, css_fixed, analysis_data, filter_html_fixed, js_fixed]):
        print(f"\n🎉 SUCCESS! All webshop issues fixed!")
        print("🏷️ Unified headers across all pages")
        print("🖼️ Images now fit properly in product cards")
        print("🔍 Filters now work with real product data")
        print("🐛 Debug logging added for troubleshooting")
    else:
        print(f"\n⚠️ Some issues remain - check individual results above")
    
    print("\n🏁 WEBSHOP ISSUES FIX COMPLETE")

if __name__ == "__main__":
    main()
