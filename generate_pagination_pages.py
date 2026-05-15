#!/usr/bin/env python3
"""
Generate static HTML pages for shop pagination
Creates static HTML files for each page of the shop with self-canonical tags
"""

import re
import os

def load_products():
    """Load products from existing HTML product pages"""
    products = []
    
    # Try to load from products directory
    produits_dir = 'produits'
    if not os.path.exists(produits_dir):
        print(f"Error: {produits_dir} directory not found")
        return []
    
    # Read all HTML files in the produits directory
    for filename in os.listdir(produits_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(produits_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract product information from HTML
            # Look for title, image, price, etc.
            title_match = re.search(r'<title>(.*?)</title>', content)
            image_match = re.search(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"', content)
            
            if title_match:
                title = title_match.group(1)
                # Extract price from title or content
                price_match = re.search(r'€(\d+[.,]\d+)', content)
                price = float(price_match.group(1).replace(',', '.')) if price_match else 0.00
                
                image_url = image_match.group(1) if image_match else ''
                alt_text = image_match.group(2) if image_match else title
                
                # Extract Bol.com link
                bol_match = re.search(r'https://www\.bol\.com[^"]*', content)
                product_url = bol_match.group(0) if bol_match else ''
                
                product = {
                    'id': len(products) + 1,
                    'title': alt_text,
                    'price': price,
                    'imageUrl': image_url,
                    'productUrl': product_url,
                    'pageUrl': f'produits/{filename}'
                }
                products.append(product)
    
    print(f"Successfully loaded {len(products)} products from HTML files")
    return products

def generate_product_card(product, position):
    """Generate HTML for a product card"""
    return f'''
            <div class="card" style="height: 100%; display: flex; flex-direction: column;">
                <div style="display: flex; flex-direction: column; height: 100%;">
                    <div style="font-size: 0.8rem; color: var(--text-light); margin-bottom: 0.5rem;">
                        #{position}
                    </div>
                    <a href="{product['pageUrl']}" style="text-decoration: none;">
                        <img src="{product['imageUrl']}" alt="{product['title']}"
                             onerror="this.src='images/placeholder-product.jpg'" 
                             style="width: 100%; height: 160px; object-fit: contain; border-radius: var(--r-lg); padding: 1rem; background: #fafafa; margin-bottom: 1rem;">
                    </a>
                    <h3 style="font-size: var(--fs-base); font-weight: 600; color: var(--text); margin: var(--sp-4) 0 var(--sp-2); flex: 1;">
                        <a href="{product['pageUrl']}" style="text-decoration: none; color: var(--text);">
                            {product['title'][:80]}...
                        </a>
                    </h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--sp-4);">
                        <span style="font-size: var(--fs-xl); font-weight: 700; color: var(--primary);">
                            €{product['price']:.2f}
                        </span>
                        <span style="font-size: 0.72rem; font-weight: 600; color: var(--primary); background: #f5ede5; padding: 0.15rem 0.5rem; border-radius: 0.3rem;">Bol.com</span>
                    </div>
                    <a href="{product['productUrl']}" rel="nofollow noopener" target="_blank" class="btn btn-primary" style="display: block; text-align: center; margin-bottom: 0.4rem;">
                        Koop product
                    </a>
                    <a href="{product['pageUrl']}" style="display: block; text-align: center; padding: 0.45rem; border: 1px solid var(--border); color: var(--text-dim); text-decoration: none; border-radius: 0.3rem; font-size: 0.78rem;">
                        Details
                    </a>
                </div>
            </div>'''

def generate_pagination_html(current_page, total_pages):
    """Generate HTML for pagination links"""
    pagination_html = '<div id="pagination" style="display: flex; gap: 0.5rem; justify-content: center; margin-top: var(--sp-8); flex-wrap: wrap;">'
    
    # Previous button
    if current_page > 1:
        pagination_html += f'<a href="winkel.html?page={current_page - 1}" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: white; border-radius: 0.25rem; text-decoration: none; color: var(--text); font-size: 0.82rem;">← Vorige</a>'
    
    # Page numbers
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)
    
    for i in range(start_page, end_page + 1):
        if i == current_page:
            pagination_html += f'<a href="winkel.html?page={i}" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: var(--primary); color: white; border-radius: 0.25rem; text-decoration: none; font-size: 0.82rem; min-width: 36px; text-align: center;">{i}</a>'
        else:
            pagination_html += f'<a href="winkel.html?page={i}" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: white; border-radius: 0.25rem; text-decoration: none; color: var(--text); font-size: 0.82rem; min-width: 36px; text-align: center;">{i}</a>'
    
    # Next button
    if current_page < total_pages:
        pagination_html += f'<a href="winkel.html?page={current_page + 1}" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: white; border-radius: 0.25rem; text-decoration: none; color: var(--text); font-size: 0.82rem;">Volgende →</a>'
    
    pagination_html += '</div>'
    return pagination_html

def generate_page(page_num, products, total_pages):
    """Generate a static HTML page for a specific pagination page"""
    products_per_page = 12
    start_idx = (page_num - 1) * products_per_page
    end_idx = min(start_idx + products_per_page, len(products))
    page_products = products[start_idx:end_idx]
    
    # Generate product cards HTML
    products_html = ''
    for idx, product in enumerate(page_products, start=start_idx + 1):
        products_html += generate_product_card(product, idx)
    
    # Generate pagination HTML with query parameters
    pagination_html = '<div id="pagination" style="display: flex; gap: 0.5rem; justify-content: center; margin-top: var(--sp-8); flex-wrap: wrap;">'
    
    # Previous button
    if page_num > 1:
        pagination_html += f'<a href="page-{page_num - 1}.html" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: white; border-radius: 0.25rem; text-decoration: none; color: var(--text); font-size: 0.82rem;">← Vorige</a>'
    
    # Page numbers
    start_page = max(1, page_num - 2)
    end_page = min(total_pages, page_num + 2)
    
    for i in range(start_page, end_page + 1):
        if i == page_num:
            pagination_html += f'<a href="page-{i}.html" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: var(--primary); color: white; border-radius: 0.25rem; text-decoration: none; font-size: 0.82rem; min-width: 36px; text-align: center;">{i}</a>'
        else:
            pagination_html += f'<a href="page-{i}.html" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: white; border-radius: 0.25rem; text-decoration: none; color: var(--text); font-size: 0.82rem; min-width: 36px; text-align: center;">{i}</a>'
    
    # Next button
    if page_num < total_pages:
        pagination_html += f'<a href="page-{page_num + 1}.html" style="padding: 0.5rem 0.75rem; border: 1px solid var(--border); background: white; border-radius: 0.25rem; text-decoration: none; color: var(--text); font-size: 0.82rem;">Volgende →</a>'
    
    pagination_html += '</div>'
    
    # Read the base winkel.html template
    with open('winkel.html', 'r', encoding='utf-8') as f:
        base_html = f.read()
    
    # Replace the dynamic product grid with static products
    # Find the products-grid div and replace its content
    products_grid_pattern = r'<div id="products-grid" class="grid grid-3" style="gap: var(--sp-6);">.*?</div>'
    products_grid_replacement = f'<div id="products-grid" class="grid grid-3" style="gap: var(--sp-6);">{products_html}</div>'
    
    # Replace pagination
    pagination_pattern = r'<div id="pagination".*?</div>'
    pagination_replacement = pagination_html
    
    # Add self-canonical tag with query parameter
    canonical_tag = f'<link rel="canonical" href="https://biologische-hondensnacks.nl/winkel.html?page={page_num}"/>'
    
    # Insert canonical tag after any existing link tags
    if '<link rel="canonical"' not in base_html:
        base_html = base_html.replace('<link href="data:image/svg+xml', f'{canonical_tag}\n    <link href="data:image/svg+xml')
    else:
        base_html = re.sub(r'<link rel="canonical"[^>]*>', canonical_tag, base_html)
    
    # Replace products grid and pagination
    base_html = re.sub(products_grid_pattern, products_grid_replacement, base_html, flags=re.DOTALL)
    base_html = re.sub(pagination_pattern, pagination_replacement, base_html, flags=re.DOTALL)
    
    # Update page title
    base_html = re.sub(
        r'<title>.*?</title>',
        f'<title>Winkel - Pagina {page_num} | Biologische Hondensnacks</title>',
        base_html
    )
    
    # Remove JavaScript pagination code since we're using static pages
    # Remove the script that handles dynamic pagination
    script_pattern = r'<script>.*?function changePage.*?</script>'
    base_html = re.sub(script_pattern, '', base_html, flags=re.DOTALL)
    
    return base_html

def main():
    """Main function to generate all pagination pages"""
    print("Loading products...")
    products = load_products()
    
    if not products:
        print("Error: No products loaded")
        return
    
    print(f"Loaded {len(products)} products")
    
    products_per_page = 12
    total_pages = (len(products) + products_per_page - 1) // products_per_page
    
    print(f"Generating {total_pages} pagination pages...")
    
    # Create output directory if it doesn't exist
    output_dir = 'winkel-pages'
    os.makedirs(output_dir, exist_ok=True)
    
    for page_num in range(1, total_pages + 1):
        print(f"Generating page {page_num}/{total_pages}...")
        
        page_html = generate_page(page_num, products, total_pages)
        
        # Save the page
        filename = os.path.join(output_dir, f'page-{page_num}.html')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        print(f"  Saved {filename}")
    
    print(f"\nSuccessfully generated {total_pages} pagination pages in '{output_dir}' directory")
    print("You should now update winkel.html to link to these static pages")

if __name__ == '__main__':
    main()
