#!/usr/bin/env python3
"""
INTEGRATE SHOP DESIGN
Intègre le design du shop avec le reste du site biologische-hondensnacks:
- Ajoute le CSS shop au CSS principal
- Remplace header/footer du winkel.html par ceux du site
- Met à jour toutes les pages produit pour utiliser le CSS principal
"""

from pathlib import Path
from bs4 import BeautifulSoup
import re

BASE_DIR = Path('/Users/marc/Desktop/biologische-hondensnacks')

# Header HTML du site
SITE_HEADER = '''<header class="header">
   <div class="container">
    <div class="header-content">
     <div class="logo">
      <a href="/" style="color: #E68161; text-decoration: none;">
       Biologische Hondensnacks
      </a>
     </div>
     <nav class="nav">
      <ul>
       <li>
        <a href="/">Home</a>
       </li>
       <li>
        <a href="/natuurlijke-hondensnacks/">Natuurlijke snacks</a>
       </li>
       <li>
        <a href="/beste-hondensnacks-2026/">Top 10 Beste</a>
       </li>
       <li>
        <a href="/hondensnacks-voor-puppy/">Puppy Snacks</a>
       </li>
       <li>
        <a href="/blog/">Blog</a>
       </li>
       <li>
        <a href="/over-ons/">Over Ons</a>
       </li>
       <li>
        <a class="nav-shop" href="/winkel.html" style="background: #E68161; color: white; padding: 0.5rem 1rem; border-radius: 6px;">Winkel</a>
       </li>
      </ul>
     </nav>
     <button class="mobile-menu-toggle"></button>
    </div>
   </div>
  </header>'''

# Footer HTML du site
SITE_FOOTER = '''<footer style="background: #374151; color: #e5e7eb; padding: 3rem 0 1rem 0;">
   <div class="container">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 3rem; margin-bottom: 2rem;">
     <div>
      <h3 style="color: #E68161; margin-bottom: 1rem; font-size: 1.25rem;">Biologische Hondensnacks</h3>
      <p style="color: #9ca3af; line-height: 1.6; margin: 0;">
       Wij bieden de beste biologische en natuurlijke hondensnacks voor jouw trouwe viervoeter. Kwaliteit en gezondheid staan bij ons voorop.
      </p>
     </div>
     <div>
      <h3 style="color: #E68161; margin-bottom: 1rem; font-size: 1.25rem;">Navigatie</h3>
      <ul style="list-style: none; padding: 0; margin: 0;">
       <li style="margin-bottom: 0.5rem;"><a href="/" style="color: #e5e7eb; text-decoration: none;">Home</a></li>
       <li style="margin-bottom: 0.5rem;"><a href="/winkel.html" style="color: #e5e7eb; text-decoration: none;">Winkel</a></li>
       <li style="margin-bottom: 0.5rem;"><a href="/blog/" style="color: #e5e7eb; text-decoration: none;">Blog</a></li>
       <li style="margin-bottom: 0.5rem;"><a href="/over-ons/" style="color: #e5e7eb; text-decoration: none;">Over ons</a></li>
      </ul>
     </div>
     <div>
      <h3 style="color: #E68161; margin-bottom: 1rem; font-size: 1.25rem;">Juridisch</h3>
      <ul style="list-style: none; padding: 0; margin: 0;">
       <li style="margin-bottom: 0.5rem;"><a href="/privacy-policy/" style="color: #e5e7eb; text-decoration: none;">Privacy policy</a></li>
       <li style="margin-bottom: 0.5rem;"><a href="/algemene-voorwaarden/" style="color: #e5e7eb; text-decoration: none;">Algemene voorwaarden</a></li>
       <li style="margin-bottom: 0.5rem;"><a href="/disclaimer/" style="color: #e5e7eb; text-decoration: none;">Disclaimer</a></li>
      </ul>
     </div>
    </div>
    <div style="border-top: 1px solid #4b5563; padding-top: 1.5rem; text-align: center;">
     <p style="margin: 0 0 1rem 0; color: #9ca3af; font-size: 0.9rem;">
      <strong>Disclaimer:</strong> De informatie op deze website is alleen bedoeld voor algemene doeleinden en vervangt geen professioneel veterinair advies. Raadpleeg altijd je dierenarts voor specifieke voedings- en gezondheidsadvies voor je hond.
     </p>
     <p style="margin: 0; color: #9ca3af; font-size: 0.9rem;">
      © 2026 Biologische hondensnacks. Alle rechten voorbehouden. | Gemaakt voor honden en hun baasjes
     </p>
    </div>
   </div>
  </footer>'''

# CSS SHOP à ajouter au CSS principal
SHOP_CSS = '''
/* ========================================
   SHOP STYLES - Biologische Hondensnacks
   ======================================== */

.shop-hero {
    background: linear-gradient(135deg, #E68161 0%, #D66F50 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
    margin-bottom: 2rem;
}

.shop-hero h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    font-weight: 700;
}

.shop-hero p {
    font-size: 1.2rem;
    opacity: 0.95;
}

/* Products Grid */
#products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.product-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.product-image-wrapper {
    width: 100%;
    height: 220px;
    background: #f8f9fa;
    border-radius: 8px;
    margin-bottom: 1rem;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.product-image-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

.product-card h3 {
    font-size: 1.1rem;
    margin-bottom: 0.8rem;
    line-height: 1.3;
    min-height: 2.6rem;
    color: #2d3748;
}

.product-brand {
    color: #6b7280;
    font-size: 0.9rem;
    display: block;
    margin-bottom: 0.5rem;
}

.product-price {
    font-size: 1.4rem;
    font-weight: bold;
    color: #E68161;
    margin: 1rem 0;
}

.btn-primary {
    background: #E68161;
    color: white;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
    text-align: center;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background: #d67347;
    transform: translateY(-2px);
}

/* Filters */
.filters-container {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
}

/* Search */
#search-input {
    width: 100%;
    padding: 1rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-size: 1rem;
    margin-bottom: 1rem;
}

/* Results count */
#results-count {
    font-weight: 600;
    color: #2d3748;
}

/* Empty state */
.empty-state {
    text-align: center;
    padding: 3rem;
    background: #f8f9fa;
    border-radius: 12px;
    margin: 2rem 0;
}

.empty-state h3 {
    color: #2d3748;
    margin-bottom: 1rem;
}

/* Mobile responsive */
@media (max-width: 768px) {
    #products-grid {
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 1rem;
    }
    
    .shop-hero h1 {
        font-size: 2rem;
    }
}
'''

def add_shop_css_to_main():
    """Ajoute le CSS shop au fichier CSS principal"""
    css_file = BASE_DIR / 'css' / 'styles.css'
    
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si le CSS shop n'est pas déjà présent
    if 'SHOP STYLES' in content:
        print("✅ CSS shop déjà présent dans styles.css")
        return
    
    # Ajouter le CSS shop à la fin
    content += '\n\n' + SHOP_CSS
    
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ CSS shop ajouté à css/styles.css")

def update_winkel_html():
    """Met à jour winkel.html avec le header/footer du site"""
    winkel_file = BASE_DIR / 'winkel.html'
    
    with open(winkel_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Remplacer le link CSS
    for link in soup.find_all('link', rel='stylesheet'):
        if 'style.css' in link.get('href', ''):
            link['href'] = 'css/styles.css'
            break
    
    # Remplacer le header
    old_header = soup.find('header')
    if old_header:
        new_header = BeautifulSoup(SITE_HEADER, 'html.parser')
        old_header.replace_with(new_header)
    
    # Remplacer le footer
    old_footer = soup.find('footer')
    if old_footer:
        new_footer = BeautifulSoup(SITE_FOOTER, 'html.parser')
        old_footer.replace_with(new_footer)
    
    # Sauvegarder
    with open(winkel_file, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    print("✅ winkel.html mis à jour avec header/footer du site")

def update_product_pages():
    """Met à jour toutes les pages produit pour utiliser css/styles.css"""
    produits_dir = BASE_DIR / 'produits'
    count = 0
    
    for product_file in produits_dir.glob('*.html'):
        with open(product_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer le lien CSS
        content = re.sub(
            r'<link\s+[^>]*href=["\']\.\./(css/product-page\.css|product-page\.css)["\'][^>]*>',
            '<link rel="stylesheet" href="../css/styles.css">',
            content
        )
        
        # Ajouter le lien si absent
        if '../css/styles.css' not in content and 'css/styles.css' not in content:
            content = content.replace(
                '</head>',
                '    <link rel="stylesheet" href="../css/styles.css">\n</head>'
            )
        
        with open(product_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        count += 1
    
    print(f"✅ {count} pages produit mises à jour")

def main():
    print("🎨 INTÉGRATION DESIGN SHOP\n")
    print("=" * 50)
    
    # 1. Ajouter CSS shop au CSS principal
    print("\n📝 Étape 1: Ajout CSS shop...")
    add_shop_css_to_main()
    
    # 2. Mettre à jour winkel.html
    print("\n📝 Étape 2: Mise à jour winkel.html...")
    update_winkel_html()
    
    # 3. Mettre à jour pages produit
    print("\n📝 Étape 3: Mise à jour pages produit...")
    update_product_pages()
    
    print("\n" + "=" * 50)
    print("✅ INTÉGRATION TERMINÉE!")
    print("\nFichiers modifiés:")
    print("  - css/styles.css (CSS shop ajouté)")
    print("  - winkel.html (header/footer site)")
    print("  - 67 pages produit (lien vers css/styles.css)")

if __name__ == '__main__':
    main()
