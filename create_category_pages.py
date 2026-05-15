#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

def load_products():
    """Load products from products.js"""
    with open('products.js', 'r') as f:
        content = f.read()
    # Extract the products array from the JavaScript file
    # The file has: const products = [...]
    start = content.find('[')
    end = content.rfind(']') + 1
    products_json = content[start:end]
    # Convert JavaScript to JSON by adding quotes around property names
    # Replace unquoted property names with quoted ones
    products_json = re.sub(r'(\w+):', r'"\1":', products_json)
    # Parse as JSON
    products = json.loads(products_json)
    return products

def categorize_product(title):
    """Determine category based on product title"""
    title_lower = title.lower()
    
    if any(x in title_lower for x in ['kauw', 'tand', 'bot', 'ring', 'stick', 'hoef', 'gewei']):
        return 'kauwsnacks'
    elif any(x in title_lower for x in ['training', 'trainer', 'treat', 'beloning', 'koekje', 'zacht']):
        return 'trainingssnacks'
    elif any(x in title_lower for x in ['natuurlijk', 'biologisch', 'orgaan', 'hert', 'kip', 'lam', 'vis']):
        return 'biologisch'
    else:
        return 'biologisch'  # Default to biologisch

def create_category_page(category_name, products):
    """Create a category page with product listings"""
    category_map = {
        'kauwsnacks': 'kauwsnacks-tandverzorging',
        'trainingssnacks': 'hondensnacks-voor-training',
        'biologisch': 'natuurlijke-hondensnacks'
    }
    
    category_slug = category_map[category_name]
    
    # Read existing index.html if it exists
    index_path = Path(f'{category_slug}/index.html')
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where to insert product grid (after main content or before footer)
        # For now, let's append products at the end of main content
        product_grid = generate_product_grid(products)
        
        # Add products before the closing </main> tag
        content = content.replace('</main>', f'{product_grid}\n    </main>')
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Updated {category_slug}/index.html with {len(products)} products")
    else:
        print(f"  ✗ {category_slug}/index.html does not exist")

def generate_product_grid(products):
    """Generate HTML for product grid"""
    grid_html = '''
                <!-- Producten -->
                <section class="products-section">
                    <h2>Onze selectie</h2>
                    <div class="grid grid-3" style="gap: 2rem; margin-top: 2rem;">
'''
    for product in products[:12]:  # Show max 12 products
        grid_html += f'''
                        <div class="card" style="text-decoration: none;">
                            <a href="produits/{product['pageUrl'].split('/')[-1]}" style="text-decoration: none; color: inherit;">
                                <img src="{product['imageUrl']}" alt="{product['title']}" loading="lazy" 
                                     style="width: 100%; height: 180px; object-fit: contain; border-radius: 0.5rem; padding: 1rem; background: #fafafa; margin-bottom: 1rem;">
                                <h3 style="font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text);">
                                    {product['title'][:60]}...
                                </h3>
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                                    <span style="font-size: 1.2rem; font-weight: 700; color: var(--primary);">
                                        €{product['price']:.2f}
                                    </span>
                                    <span style="font-size: 0.75rem; font-weight: 600; color: var(--primary); background: #f5ede5; padding: 0.15rem 0.5rem; border-radius: 0.3rem;">Bol.com</span>
                                </div>
                                <a href="{product['productUrl']}" rel="nofollow noopener" target="_blank" 
                                   style="display: block; text-align: center; padding: 0.75rem; background: linear-gradient(135deg,#8B5A2B,#6B4423); color: white; text-decoration: none; border-radius: 0.5rem; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                                    Koop product
                                </a>
                                <a href="produits/{product['pageUrl'].split('/')[-1]}" 
                                   style="display: block; text-align: center; padding: 0.5rem; border: 1px solid var(--border); color: var(--text-dim); text-decoration: none; border-radius: 0.5rem; font-size: 0.8rem;">
                                    Details
                                </a>
                            </a>
                        </div>'''
    
    grid_html += '''
                    </div>
                </section>
'''
    return grid_html

def main():
    """Main function to create category pages"""
    products = load_products()
    
    # Categorize products
    categories = {
        'kauwsnacks': [],
        'trainingssnacks': [],
        'biologisch': []
    }
    
    for product in products:
        category = categorize_product(product['title'])
        categories[category].append(product)
    
    print(f"Total products: {len(products)}")
    print(f"Kauwsnacks: {len(categories['kauwsnacks'])}")
    print(f"Trainingssnacks: {len(categories['trainingssnacks'])}")
    print(f"Biologisch: {len(categories['biologisch'])}")
    
    # Create category pages
    for category_name, category_products in categories.items():
        if category_products:
            create_category_page(category_name, category_products)

if __name__ == '__main__':
    main()
