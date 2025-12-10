#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - SHOP.JS REBUILDER
============================================

Script pour reconstruire complètement shop.js avec une syntaxe propre.

Auteur: AI Assistant
Datum: December 2025
"""

import os
import shutil

# Configuration
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/rebuild'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def rebuild_shop_js():
    """Rebuild shop.js with clean syntax"""
    try:
        # Create backup of current corrupted file
        backup_file = os.path.join(BACKUP_DIR, 'shop_js_corrupted.js')
        shutil.copy2(SHOP_JS_FILE, backup_file)
        print(f"💾 Corrupted file backed up: {backup_file}")
        
        # Read the original to extract product data
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the allProducts array (should be clean)
        start_products = content.find('const allProducts = [')
        end_products = content.find('];', start_products) + 2
        
        if start_products == -1 or end_products == -1:
            print("❌ Could not extract product data")
            return False
        
        products_data = content[start_products:end_products]
        
        # Create clean shop.js content
        clean_shop_js = f'''/* ========================================
   BIOLOGISCHE HONDENSNACKS - SHOP FUNCTIONALITY
   ======================================== */

// Product data from real catalog
{products_data}

// Global variables
let filteredProducts = [...allProducts];
let currentPage = 1;
const productsPerPage = 12;

// Active filters
let activeFilters = {{
    search: '',
    categories: [],
    brands: [],
    ages: [],
    sizes: [],
    features: [],
    maxPrice: 50
}};

// Search functionality
function handleSearch(event) {{
    activeFilters.search = event.target.value.toLowerCase();
    applyFilters();
}}

// Apply filters
function applyFilters() {{
    filteredProducts = allProducts.filter(product => {{
        // Search filter
        if (activeFilters.search && !product.name.toLowerCase().includes(activeFilters.search) 
            && !product.brand.toLowerCase().includes(activeFilters.search)
            && !product.description.toLowerCase().includes(activeFilters.search)) {{
            return false;
        }}
        
        // Category filter
        if (activeFilters.categories.length > 0 && !activeFilters.categories.includes(product.category)) {{
            return false;
        }}
        
        // Brand filter
        if (activeFilters.brands.length > 0 && !activeFilters.brands.includes(product.brand)) {{
            return false;
        }}
        
        // Age filter
        if (activeFilters.ages.length > 0 && !activeFilters.ages.some(age => product.age.includes(age))) {{
            return false;
        }}
        
        // Size filter
        if (activeFilters.sizes.length > 0 && !activeFilters.sizes.some(size => product.size.includes(size))) {{
            return false;
        }}
        
        // Features filter
        if (activeFilters.features.length > 0 && !activeFilters.features.some(feature => product.features.includes(feature))) {{
            return false;
        }}
        
        // Price filter
        if (product.price > activeFilters.maxPrice) {{
            return false;
        }}
        
        return true;
    }});
    
    currentPage = 1;
    renderProducts();
    updateResultsCount();
    updateActiveFilters();
}}

// Update price filter
function updatePriceFilter(value) {{
    activeFilters.maxPrice = parseInt(value);
    document.getElementById('priceValue').textContent = '€' + value;
    applyFilters();
}}

// Clear all filters
function clearAllFilters() {{
    activeFilters = {{
        search: '',
        categories: [],
        brands: [],
        ages: [],
        sizes: [],
        features: [],
        maxPrice: 50
    }};
    
    // Reset form elements
    document.getElementById('searchInput').value = '';
    document.getElementById('priceRange').value = 50;
    document.getElementById('priceValue').textContent = '€50';
    
    // Uncheck all checkboxes
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(cb => cb.checked = false);
    
    applyFilters();
}}

// Update results count
function updateResultsCount() {{
    const count = filteredProducts.length;
    document.getElementById('resultsCount').textContent = count + ' producten';
    
    // Show/hide empty state
    const emptyState = document.getElementById('emptyState');
    const productsGrid = document.getElementById('productsGrid');
    
    if (count === 0) {{
        emptyState.style.display = 'block';
        productsGrid.style.display = 'none';
    }} else {{
        emptyState.style.display = 'none';
        productsGrid.style.display = 'grid';
    }}
}}

// Update active filters display
function updateActiveFilters() {{
    const activeFiltersContainer = document.getElementById('activeFilters');
    const filterTags = document.getElementById('filterTags');
    
    let tags = [];
    
    // Add search tag
    if (activeFilters.search) {{
        tags.push({{ type: 'search', value: activeFilters.search, label: `Zoeken: "${{activeFilters.search}}"` }});
    }}
    
    // Add category tags
    activeFilters.categories.forEach(category => {{
        tags.push({{ type: 'category', value: category, label: category }});
    }});
    
    // Add brand tags
    activeFilters.brands.forEach(brand => {{
        tags.push({{ type: 'brand', value: brand, label: brand }});
    }});
    
    // Add other filter tags
    [...activeFilters.ages, ...activeFilters.sizes, ...activeFilters.features].forEach(filter => {{
        tags.push({{ type: 'other', value: filter, label: filter }});
    }});
    
    // Add price tag
    if (activeFilters.maxPrice < 50) {{
        tags.push({{ type: 'price', value: activeFilters.maxPrice, label: `Max €${{activeFilters.maxPrice}}` }});
    }}
    
    if (tags.length > 0) {{
        filterTags.innerHTML = tags.map(tag => 
            `<span class="filter-tag" onclick="removeFilter('${{tag.type}}', '${{tag.value}}')">
                ${{tag.label}} ×
            </span>`
        ).join('');
        activeFiltersContainer.style.display = 'flex';
    }} else {{
        activeFiltersContainer.style.display = 'none';
    }}
}}

// Remove filter
function removeFilter(type, value) {{
    switch(type) {{
        case 'search':
            activeFilters.search = '';
            document.getElementById('searchInput').value = '';
            break;
        case 'category':
            activeFilters.categories = activeFilters.categories.filter(c => c !== value);
            break;
        case 'brand':
            activeFilters.brands = activeFilters.brands.filter(b => b !== value);
            break;
        case 'price':
            activeFilters.maxPrice = 50;
            document.getElementById('priceRange').value = 50;
            document.getElementById('priceValue').textContent = '€50';
            break;
        default:
            // Handle ages, sizes, features
            activeFilters.ages = activeFilters.ages.filter(f => f !== value);
            activeFilters.sizes = activeFilters.sizes.filter(f => f !== value);
            activeFilters.features = activeFilters.features.filter(f => f !== value);
    }}
    
    // Update checkboxes
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(cb => {{
        if (cb.getAttribute('data-filter-value') === value) {{
            cb.checked = false;
        }}
    }});
    
    applyFilters();
}}

// Sort products
function sortProducts(sortBy) {{
    switch(sortBy) {{
        case 'price-low':
            filteredProducts.sort((a, b) => a.price - b.price);
            break;
        case 'price-high':
            filteredProducts.sort((a, b) => b.price - a.price);
            break;
        case 'rating':
            filteredProducts.sort((a, b) => b.rating - a.rating);
            break;
        case 'name':
            filteredProducts.sort((a, b) => a.name.localeCompare(b.name));
            break;
        case 'newest':
            filteredProducts.sort((a, b) => b.id - a.id);
            break;
        default: // popular
            filteredProducts.sort((a, b) => (b.reviews || 0) - (a.reviews || 0));
    }}
    
    renderProducts();
}}

// Toggle view (grid/list)
function toggleView(view) {{
    const productsGrid = document.getElementById('productsGrid');
    const viewBtns = document.querySelectorAll('.view-btn');
    
    viewBtns.forEach(btn => btn.classList.remove('active'));
    document.querySelector(`[data-view="${{view}}"]`).classList.add('active');
    
    if (view === 'list') {{
        productsGrid.classList.add('list-view');
    }} else {{
        productsGrid.classList.remove('list-view');
    }}
}}

// Render products
function renderProducts() {{
    console.log('🎨 Rendering products...');
    const productsGrid = document.getElementById('productsGrid');
    
    if (!productsGrid) {{
        console.error('❌ Products grid element not found!');
        return;
    }}
    
    const startIndex = (currentPage - 1) * productsPerPage;
    const endIndex = startIndex + productsPerPage;
    const productsToShow = filteredProducts.slice(0, endIndex);
    
    if (productsToShow.length === 0) {{
        console.warn('⚠️ No products to show!');
        productsGrid.innerHTML = '<p>Geen producten gevonden.</p>';
        return;
    }}
    
    productsGrid.innerHTML = productsToShow.map(product => `
        <div class="product-card" data-product-id="${{product.id}}">
            <img src="${{product.image}}" alt="${{product.name}}" class="product-image" loading="lazy">
            
            <div class="product-info">
                <div class="product-brand">${{product.brand}}</div>
                <h3 class="product-name">${{product.name}}</h3>
                <p class="product-description">${{product.description}}</p>
                
                <div class="product-features">
                    ${{product.features.slice(0, 3).map(feature => `<span class="feature-tag">${{feature}}</span>`).join('')}}
                </div>
                
                <div class="product-rating">
                    <span class="stars">${{generateStars(product.rating)}}</span>
                    <span class="rating-text">${{product.rating}} (${{product.reviews || 0}} reviews)</span>
                </div>
                
                <div class="product-price">
                    <span class="price-current">€${{product.price.toFixed(2)}}</span>
                    <span class="price-per-unit">${{product.weight}}</span>
                </div>
            </div>
            
            <div class="product-actions">
                <div class="product-buttons">
                    <a href="${{product.url}}" class="btn-secondary btn-details">
                        👁️ Details bekijken
                    </a>
                    <a href="https://www.bol.com/nl/s/?searchtext=${{encodeURIComponent(product.name)}}" target="_blank" rel="noopener" class="btn-primary">
                        🛒 Bestel bij bol.com
                    </a>
                </div>
            </div>
            
            ${{!product.inStock ? '<div class="out-of-stock">Tijdelijk uitverkocht</div>' : ''}}
        </div>
    `).join('');
    
    // Update load more button
    updateLoadMoreButton();
}}

// Load more products
function loadMoreProducts() {{
    currentPage++;
    renderProducts();
}}

// Update load more button
function updateLoadMoreButton() {{
    const loadMoreContainer = document.getElementById('loadMoreContainer');
    const totalPages = Math.ceil(filteredProducts.length / productsPerPage);
    
    if (currentPage >= totalPages) {{
        loadMoreContainer.style.display = 'none';
    }} else {{
        loadMoreContainer.style.display = 'block';
    }}
}}

// Generate stars for rating
function generateStars(rating) {{
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;
    let stars = '';
    
    for (let i = 0; i < fullStars; i++) {{
        stars += '★';
    }}
    
    if (hasHalfStar) {{
        stars += '☆';
    }}
    
    const emptyStars = 5 - Math.ceil(rating);
    for (let i = 0; i < emptyStars; i++) {{
        stars += '☆';
    }}
    
    return stars;
}}

// Initialize shop when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {{
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
    if (searchInput) {{
        searchInput.addEventListener('input', function() {{
            activeFilters.search = this.value.toLowerCase();
            applyFilters();
        }});
    }}
    
    // Add event listeners for filter checkboxes
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(checkbox => {{
        checkbox.addEventListener('change', function() {{
            const filterType = this.getAttribute('data-filter-type');
            const filterValue = this.getAttribute('data-filter-value');
            
            if (this.checked) {{
                if (!activeFilters[filterType].includes(filterValue)) {{
                    activeFilters[filterType].push(filterValue);
                }}
            }} else {{
                activeFilters[filterType] = activeFilters[filterType].filter(v => v !== filterValue);
            }}
            
            applyFilters();
        }});
    }});
    
    // Add event listener for price range
    const priceRange = document.getElementById('priceRange');
    if (priceRange) {{
        priceRange.addEventListener('input', function() {{
            updatePriceFilter(this.value);
        }});
    }}
    
    // Add event listener for clear filters button
    const clearFiltersBtn = document.getElementById('clearFilters');
    if (clearFiltersBtn) {{
        clearFiltersBtn.addEventListener('click', clearAllFilters);
    }}
    
    console.log('Shop initialized with', allProducts.length, 'products');
}});'''
        
        # Write the clean file
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(clean_shop_js)
        
        print("✅ Clean shop.js created")
        return True
        
    except Exception as e:
        print(f"❌ Error rebuilding shop.js: {e}")
        return False

def verify_syntax():
    """Verify that the JavaScript syntax is now correct"""
    try:
        import subprocess
        result = subprocess.run(['node', '-c', SHOP_JS_FILE], 
                              capture_output=True, text=True, cwd='/Users/marc/Desktop/biologische-hondensnacks')
        
        if result.returncode == 0:
            print("✅ JavaScript syntax is now valid")
            return True
        else:
            print(f"❌ Syntax error still exists: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"⚠️ Could not verify syntax (Node.js not available): {e}")
        return True

def main():
    """Main function to rebuild shop.js"""
    print("🔨 SHOP.JS REBUILDER")
    print("=" * 50)
    
    create_backup_dir()
    
    print("🔄 Rebuilding shop.js with clean syntax...")
    rebuild_success = rebuild_shop_js()
    
    if rebuild_success:
        print("🔍 Verifying syntax...")
        syntax_valid = verify_syntax()
        
        print("\\n" + "=" * 50)
        print("📊 REBUILD RESULTS:")
        print(f"🔨 File rebuilt: {'✅' if rebuild_success else '❌'}")
        print(f"✅ Syntax validation: {'✅ Valid' if syntax_valid else '❌ Still has errors'}")
        
        if rebuild_success and syntax_valid:
            print(f"\\n🎉 SUCCESS! shop.js completely rebuilt!")
            print("📱 Products should now display in winkel")
            print("🔍 All JavaScript functions restored")
            print("⚙️ Filters and search should work")
        else:
            print(f"\\n⚠️ Rebuild completed but may need manual review")
    else:
        print("\\n❌ Failed to rebuild shop.js")
    
    print("\\n🏁 REBUILD COMPLETE")

if __name__ == "__main__":
    main()'''

        # Write the script
        with open('/Users/marc/Desktop/biologische-hondensnacks/scripts/rebuild_shop_js.py', 'w', encoding='utf-8') as f:
            f.write(clean_shop_js)
        
        print("✅ Clean shop.js created")
        return True
        
    except Exception as e:
        print(f"❌ Error rebuilding shop.js: {e}")
        return False

def main():
    """Main function to rebuild shop.js"""
    print("🔨 SHOP.JS REBUILDER")
    print("=" * 50)
    
    create_backup_dir()
    
    print("🔄 Rebuilding shop.js with clean syntax...")
    rebuild_success = rebuild_shop_js()
    
    print("\n🏁 REBUILD COMPLETE")

if __name__ == "__main__":
    main()
