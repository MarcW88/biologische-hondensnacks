#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - WINKEL DISPLAY FIXER
===============================================

Script pour diagnostiquer et corriger le problème d'affichage
des produits dans la page winkel.

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import shutil

# Configuration
PROJECT_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
WINKEL_HTML = '/Users/marc/Desktop/biologische-hondensnacks/winkel/index.html'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/winkel_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def fix_shop_js():
    """Fix the shop.js file to ensure products display correctly"""
    try:
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'shop_js_backup.js')
        shutil.copy2(SHOP_JS_FILE, backup_file)
        print(f"💾 Backup created: {backup_file}")
        
        # Fix the filter initialization that might be broken
        # Replace the problematic debug code with clean version
        debug_pattern = r'// DEBUG: Log filter initialization.*?applyFilters\(\);'
        
        clean_filter_code = '''// Add event listeners for filter checkboxes
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const filterType = this.getAttribute('data-filter-type');
            const filterValue = this.getAttribute('data-filter-value');
            
            if (this.checked) {
                if (!activeFilters[filterType].includes(filterValue)) {
                    activeFilters[filterType].push(filterValue);
                }
            } else {
                activeFilters[filterType] = activeFilters[filterType].filter(v => v !== filterValue);
            }
            
            applyFilters();
        });
    });'''
        
        new_content = re.sub(debug_pattern, clean_filter_code, content, flags=re.DOTALL)
        
        # Ensure renderProducts function is clean and working
        render_pattern = r'function renderProducts\(\) \{.*?\}'
        
        clean_render_function = '''function renderProducts() {
    console.log('🎨 Rendering products...');
    const productsGrid = document.getElementById('productsGrid');
    
    if (!productsGrid) {
        console.error('❌ Products grid element not found!');
        return;
    }
    
    const startIndex = (currentPage - 1) * productsPerPage;
    const endIndex = startIndex + productsPerPage;
    const productsToShow = filteredProducts.slice(0, endIndex);
    
    if (productsToShow.length === 0) {
        console.warn('⚠️ No products to show!');
        productsGrid.innerHTML = '<p>Geen producten gevonden.</p>';
        return;
    }
    
    productsGrid.innerHTML = productsToShow.map(product => `
        <div class="product-card" data-product-id="${product.id}">
            <img src="${product.image}" alt="${product.name}" class="product-image" loading="lazy">
            
            <div class="product-info">
                <div class="product-brand">${product.brand}</div>
                <h3 class="product-name">${product.name}</h3>
                <p class="product-description">${product.description}</p>
                
                <div class="product-features">
                    ${product.features.slice(0, 3).map(feature => `<span class="feature-tag">${feature}</span>`).join('')}
                </div>
                
                <div class="product-rating">
                    <span class="stars">${generateStars(product.rating)}</span>
                    <span class="rating-text">${product.rating} (${product.reviews || 0} reviews)</span>
                </div>
                
                <div class="product-price">
                    <span class="price-current">€${product.price.toFixed(2)}</span>
                    <span class="price-per-unit">${product.weight}</span>
                </div>
            </div>
            
            <div class="product-actions">
                <div class="product-buttons">
                    <a href="${product.url}" class="btn-secondary btn-details">
                        👁️ Details bekijken
                    </a>
                    <a href="https://www.bol.com/nl/s/?searchtext=${encodeURIComponent(product.name)}" target="_blank" rel="noopener" class="btn-primary">
                        🛒 Bestel bij bol.com
                    </a>
                </div>
            </div>
            
            ${!product.inStock ? '<div class="out-of-stock">Tijdelijk uitverkocht</div>' : ''}
        </div>
    `).join('');
    
    // Update load more button
    updateLoadMoreButton();
}'''
        
        # Only replace if the function exists and seems broken
        if 'function renderProducts()' in new_content:
            new_content = re.sub(render_pattern, clean_render_function, new_content, flags=re.DOTALL)
        
        # Ensure DOMContentLoaded is clean
        dom_pattern = r'document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{.*?\}\);'
        
        clean_dom_code = '''document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Shop initialization starting...');
    console.log('📦 Total products:', allProducts.length);
    
    // Initialize with real products
    filteredProducts = [...allProducts];
    console.log('✅ Filtered products initialized:', filteredProducts.length);
    
    // Render initial products
    renderProducts();
    updateResultsCount();
    
    // Add event listeners for search
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            activeFilters.search = this.value.toLowerCase();
            applyFilters();
        });
    }
    
    // Add event listeners for filter checkboxes
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const filterType = this.getAttribute('data-filter-type');
            const filterValue = this.getAttribute('data-filter-value');
            
            if (this.checked) {
                if (!activeFilters[filterType].includes(filterValue)) {
                    activeFilters[filterType].push(filterValue);
                }
            } else {
                activeFilters[filterType] = activeFilters[filterType].filter(v => v !== filterValue);
            }
            
            applyFilters();
        });
    });
    
    // Add event listener for price range
    const priceRange = document.getElementById('priceRange');
    if (priceRange) {
        priceRange.addEventListener('input', function() {
            updatePriceFilter(this.value);
        });
    }
});'''
        
        # Replace the last DOMContentLoaded (the problematic one)
        dom_matches = list(re.finditer(dom_pattern, new_content, re.DOTALL))
        if dom_matches:
            # Replace the last occurrence
            last_match = dom_matches[-1]
            new_content = new_content[:last_match.start()] + clean_dom_code + new_content[last_match.end():]
        
        # Write the fixed content
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ Fixed shop.js JavaScript")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing shop.js: {e}")
        return False

def check_winkel_html():
    """Check if winkel HTML has the correct structure"""
    try:
        with open(WINKEL_HTML, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for essential elements
        checks = {
            'productsGrid': 'id="productsGrid"' in content,
            'searchInput': 'id="searchInput"' in content,
            'resultsCount': 'id="resultsCount"' in content,
            'shop.js': 'shop.js' in content
        }
        
        print("🔍 HTML Structure Check:")
        for element, exists in checks.items():
            status = "✅" if exists else "❌"
            print(f"   {status} {element}: {'Found' if exists else 'Missing'}")
        
        return all(checks.values())
        
    except Exception as e:
        print(f"❌ Error checking HTML: {e}")
        return False

def add_debug_to_html():
    """Add debug console logs to HTML"""
    try:
        with open(WINKEL_HTML, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'winkel_html_backup.html')
        shutil.copy2(WINKEL_HTML, backup_file)
        
        # Add debug script before closing body tag
        debug_script = '''
    <script>
    // Debug script to check if elements exist
    document.addEventListener('DOMContentLoaded', function() {
        console.log('🔍 DEBUG: Checking page elements...');
        console.log('📋 productsGrid:', document.getElementById('productsGrid'));
        console.log('🔍 searchInput:', document.getElementById('searchInput'));
        console.log('📊 resultsCount:', document.getElementById('resultsCount'));
        console.log('🛍️ allProducts defined:', typeof allProducts !== 'undefined');
        if (typeof allProducts !== 'undefined') {
            console.log('📦 allProducts length:', allProducts.length);
        }
    });
    </script>
</body>'''
        
        # Replace closing body tag
        new_content = content.replace('</body>', debug_script)
        
        with open(WINKEL_HTML, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ Added debug script to HTML")
        return True
        
    except Exception as e:
        print(f"❌ Error adding debug to HTML: {e}")
        return False

def main():
    """Main function to fix winkel display issues"""
    print("🔧 WINKEL DISPLAY FIXER")
    print("=" * 50)
    
    create_backup_dir()
    
    # 1. Check HTML structure
    print("\n1️⃣ CHECKING HTML STRUCTURE...")
    html_ok = check_winkel_html()
    
    # 2. Fix JavaScript
    print("\n2️⃣ FIXING JAVASCRIPT...")
    js_fixed = fix_shop_js()
    
    # 3. Add debug to HTML
    print("\n3️⃣ ADDING DEBUG LOGGING...")
    debug_added = add_debug_to_html()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 WINKEL FIX RESULTS:")
    print(f"🏗️ HTML structure: {'✅ OK' if html_ok else '❌ Issues found'}")
    print(f"⚙️ JavaScript fixed: {'✅' if js_fixed else '❌'}")
    print(f"🐛 Debug added: {'✅' if debug_added else '❌'}")
    
    if js_fixed and debug_added:
        print(f"\n🎉 SUCCESS! Winkel display should be fixed!")
        print("🔍 Check browser console for debug logs")
        print("📱 Refresh the page and check if products appear")
        print("🛠️ If still not working, check console for errors")
    else:
        print(f"\n⚠️ Some fixes failed - check individual results above")
    
    print("\n🏁 WINKEL DISPLAY FIX COMPLETE")

if __name__ == "__main__":
    main()
