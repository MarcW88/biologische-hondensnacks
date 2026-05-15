#!/usr/bin/env python3
import os
from pathlib import Path

def add_product_grid_to_category(category_path, category_name):
    """Add product grid to category page"""
    index_path = Path(category_path) / 'index.html'
    
    if not index_path.exists():
        print(f"  ✗ {index_path} does not exist")
        return False
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if product grid already exists
    if 'products-grid' in content:
        print(f"  ⊘ Skipped: {index_path.name} (product grid already exists)")
        return False
    
    # Find where to insert the product grid (before the closing </main> tag)
    product_grid = f'''
    <!-- Product Grid -->
    <section class="section" style="padding: 2rem 0;">
        <div class="container">
            <h2 style="font-family: var(--font-display); margin-bottom: var(--sp-2);">Onze selectie</h2>
            <p class="text-dim" style="margin-bottom: var(--sp-6); max-width: 560px;">De beste {category_name} voor jouw hond.</p>
            <div id="products-grid" class="grid grid-3" style="gap: var(--sp-6);">
                <!-- Products will be loaded here via JavaScript -->
            </div>
        </div>
    </section>
    <script src="../products.js"></script>
    <script>
        // Filter products by category
        function getCategoryProducts() {{
            return products.filter(p => {{
                const title = p.title.toLowerCase();
                if ('{category_name}' === 'kauwsnacks') {{
                    return title.includes('kauw') || title.includes('tand') || title.includes('bot') || title.includes('ring') || title.includes('stick') || title.includes('hoef') || title.includes('gewei');
                }} else if ('{category_name}' === 'training') {{
                    return title.includes('training') || title.includes('trainer') || title.includes('treat') || title.includes('beloning') || title.includes('koekje') || title.includes('zacht');
                }} else if ('{category_name}' === 'natuurlijk') {{
                    return title.includes('natuurlijk') || title.includes('biologisch') || title.includes('orgaan') || title.includes('hert') || title.includes('kip') || title.includes('lam') || title.includes('vis');
                }}
                return true;
            }});
        }}

        function displayProducts() {{
            const grid = document.getElementById('products-grid');
            const filteredProducts = getCategoryProducts().slice(0, 12); // Show max 12 products
            
            filteredProducts.forEach((product, index) => {{
                const card = document.createElement('div');
                card.className = 'card';
                card.style.textDecoration = 'none';
                card.style.color = 'inherit';
                
                card.innerHTML = `
                    <a href="../produits/${{product.pageUrl.split('/').pop()}}" style="text-decoration: none; color: inherit;">
                        <img src="${{product.imageUrl}}" alt="${{product.title}}" loading="lazy" 
                             style="width: 100%; height: 180px; object-fit: contain; border-radius: 0.5rem; padding: 1rem; background: #fafafa; margin-bottom: 1rem;">
                        <h3 style="font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text);">
                            ${{product.title.substring(0, 60)}}...
                        </h3>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                            <span style="font-size: 1.2rem; font-weight: 700; color: var(--primary);">
                                €${{product.price.toFixed(2)}}
                            </span>
                            <span style="font-size: 0.75rem; font-weight: 600; color: var(--primary); background: #f5ede5; padding: 0.15rem 0.5rem; border-radius: 0.3rem;">Bol.com</span>
                        </div>
                        <a href="${{product.productUrl}}" rel="nofollow noopener" target="_blank" 
                           style="display: block; text-align: center; padding: 0.75rem; background: linear-gradient(135deg,#8B5A2B,#6B4423); color: white; text-decoration: none; border-radius: 0.5rem; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                            Koop product
                        </a>
                        <a href="../produits/${{product.pageUrl.split('/').pop()}}" 
                           style="display: block; text-align: center; padding: 0.5rem; border: 1px solid var(--border); color: var(--text-dim); text-decoration: none; border-radius: 0.5rem; font-size: 0.8rem;">
                            Details
                        </a>
                    </a>
                `;
                
                grid.appendChild(card);
            }});
        }}

        // Load products when page loads
        document.addEventListener('DOMContentLoaded', displayProducts);
    </script>
'''
    
    # Insert before closing </main> tag
    content = content.replace('</main>', product_grid + '\n    </main>')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Added product grid to {index_path.name}")
    return True

def main():
    """Main function to add product grids to category pages"""
    categories = [
        ('kauwsnacks-tandverzorging', 'kauwsnacks'),
        ('hondensnacks-voor-training', 'training'),
        ('natuurlijke-hondensnacks', 'natuurlijk')
    ]
    
    base_dir = Path('/Users/marc/Desktop/biologische-hondensnacks')
    
    fixed_count = 0
    for category_path, category_name in categories:
        if add_product_grid_to_category(base_dir / category_path, category_name):
            fixed_count += 1
    
    print(f"\n✓ Added product grids to {fixed_count} category pages")

if __name__ == '__main__':
    main()
