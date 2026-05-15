#!/usr/bin/env python3
import json
import re
from pathlib import Path

def load_products_from_html():
    """Load products from existing HTML files in produits directory"""
    products = []
    produits_dir = Path('produits')
    
    if not produits_dir.exists():
        print("✗ produits directory does not exist")
        return products
    
    html_files = list(produits_dir.glob('*.html'))
    
    for html_file in html_files[:24]:  # Limit to 24 for winkel
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'<title>(.*?)\|', content)
            title = title_match.group(1).strip() if title_match else html_file.stem.replace('-', ' ')
            
            # Extract image
            img_match = re.search(r'<img src="(https://media\.s-bol\.com/[^"]+)"', content)
            image_url = img_match.group(1) if img_match else ''
            
            # Extract price
            price_match = re.search(r'<div class="price">([^<]+)</div>', content)
            price_str = price_match.group(1) if price_match else '€0,00'
            # Convert price to float
            price = float(price_str.replace('€', '').replace(',', '.').strip()) if price_str else 0
            
            # Extract bol.com URL
            bol_url_match = re.search(r'href="(https://www\.bol\.com[^"]+)"', content)
            bol_url = bol_url_match.group(1) if bol_url_match else ''
            
            products.append({
                'title': title,
                'imageUrl': image_url,
                'price': price,
                'pageUrl': f'produits/{html_file.name}',
                'productUrl': bol_url
            })
        except Exception as e:
            print(f"  ✗ Error reading {html_file.name}: {e}")
    
    return products

def generate_product_card(product):
    """Generate HTML for a product card"""
    return f'''                        <div class="card" style="text-decoration: none;">
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

def update_winkel_page():
    """Update winkel.html with static product cards"""
    products = load_products_from_html()
    
    if not products:
        print("✗ No products found")
        return False
    
    winkel_path = Path('winkel.html')
    with open(winkel_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate product cards HTML
    product_cards = '\n'.join([generate_product_card(p) for p in products[:24]])  # Show 24 products
    
    # Replace the dynamic products grid with static HTML
    old_grid = '''<div id="products-grid" class="grid grid-3" style="gap: var(--sp-6);">
<!-- Les produits seront chargés ici via JavaScript -->
</div>'''
    
    new_grid = f'''<div id="products-grid" class="grid grid-3" style="gap: var(--sp-6);">
{product_cards}
</div>
<script src="products.js"></script>
<script>
// Products are now static HTML for SEO
// JavaScript can be used for filtering/pagination if needed
</script>'''
    
    content = content.replace(old_grid, new_grid)
    
    with open(winkel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated winkel.html with {len(products[:24])} static product cards")
    return True

def update_category_page(category_path, category_name):
    """Update category page with static product cards"""
    products = load_products_from_html()
    
    # Filter products by category
    filtered_products = []
    for product in products:
        title_lower = product['title'].lower()
        if category_name == 'kauwsnacks':
            if any(x in title_lower for x in ['kauw', 'tand', 'bot', 'ring', 'stick', 'hoef', 'gewei']):
                filtered_products.append(product)
        elif category_name == 'training':
            if any(x in title_lower for x in ['training', 'trainer', 'treat', 'beloning', 'koekje', 'zacht']):
                filtered_products.append(product)
        elif category_name == 'natuurlijk':
            if any(x in title_lower for x in ['natuurlijk', 'biologisch', 'orgaan', 'hert', 'kip', 'lam', 'vis']):
                filtered_products.append(product)
    
    index_path = Path(category_path) / 'index.html'
    if not index_path.exists():
        print(f"✗ {index_path} does not exist")
        return False
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has static products
    if 'products-grid' in content and 'Products will be loaded here via JavaScript' not in content:
        print(f"⊘ Skipped {index_path.name} (already has static products)")
        return False
    
    # Generate product cards HTML
    product_cards = '\n'.join([generate_product_card(p) for p in filtered_products[:12]])  # Show 12 products
    
    # Replace the dynamic products grid with static HTML
    old_grid = '''<div id="products-grid" class="grid grid-3" style="gap: var(--sp-6);">
                <!-- Products will be loaded here via JavaScript -->
            </div>
            <script src="../products.js"></script>
            <script>
                // Filter products by category
                function getCategoryProducts() {{
                    return products.filter(p => {{
                        const title = p.title.toLowerCase();'''
    
    new_grid = f'''<div id="products-grid" class="grid grid-3" style="gap: var(--sp-6);">
{product_cards}
</div>
<script src="../products.js"></script>
<script>
// Products are now static HTML for SEO
// JavaScript can be used for filtering/pagination if needed
</script>'''
    
    content = content.replace(old_grid, new_grid)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {index_path.name} with {len(filtered_products[:12])} static product cards")
    return True

def main():
    """Main function to generate static product cards"""
    print("Generating static HTML product cards...")
    
    # Update winkel.html
    update_winkel_page()
    
    # Update category pages
    categories = [
        ('kauwsnacks-tandverzorging', 'kauwsnacks'),
        ('hondensnacks-voor-training', 'training'),
        ('natuurlijke-hondensnacks', 'natuurlijk')
    ]
    
    base_dir = Path('/Users/marc/Desktop/biologische-hondensnacks')
    for category_path, category_name in categories:
        update_category_page(base_dir / category_path, category_name)
    
    print("\n✓ All pages updated with static HTML product cards")

if __name__ == '__main__':
    main()
