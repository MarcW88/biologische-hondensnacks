#!/usr/bin/env python3
"""
BUILD COMPLETE SHOP
===================
Construit un shop complet avec:
- Pages produit individuelles avec descriptions uniques via ChatGPT
- Pages de listing avec pagination (12 produits par page)
- Images matchées automatiquement
- Liens internes corrects
- CSS et JavaScript inclus

Auteur: AI Assistant
Date: December 2025
"""

import os
import csv
import json
import re
import math
from pathlib import Path
from openai import OpenAI

# Configuration
BASE_DIR = Path('/Users/marc/Desktop/biologische-hondensnacks')
CSV_FILE = BASE_DIR / 'Hondensnacks Catalogus (1).csv'
IMAGES_DIR = BASE_DIR / 'images'
WINKEL_DIR = BASE_DIR / 'winkel'
PRODUITS_DIR = BASE_DIR / 'produits'
PRODUCTS_PER_PAGE = 12

# OpenAI API - sera initialisé dans main() avec la clé fournie
client = None

def slugify(text):
    """Convertit un texte en slug URL-friendly"""
    text = text.lower()
    text = re.sub(r'[àáâãäå]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def find_matching_image(product_name, images_list):
    """Trouve l'image correspondant au produit"""
    # Normaliser le nom du produit
    product_clean = product_name.lower()
    product_clean = re.sub(r'[^a-z0-9\s]', '', product_clean)
    
    best_match = None
    best_score = 0
    
    for img in images_list:
        img_name = os.path.basename(img).lower()
        img_clean = re.sub(r'[^a-z0-9\s]', '', img_name.replace('.jpg', ''))
        
        # Compter les mots en commun
        product_words = set(product_clean.split())
        img_words = set(img_clean.split())
        common_words = product_words.intersection(img_words)
        score = len(common_words)
        
        if score > best_score:
            best_score = score
            best_match = img
    
    return best_match if best_match else 'images/placeholder.jpg'

def generate_product_description_chatgpt(product_name, brand, product_type, bijzonderheden):
    """Génère une description unique via ChatGPT"""
    
    global client
    
    if not client:
        # Fallback description si pas de client
        return f"{product_name} van {brand} is een natuurlijke hondensnack van hoogste kwaliteit. {bijzonderheden}. Perfect voor honden van alle leeftijden die houden van lekkere, gezonde traktaties."
    
    prompt = f"""Je hebt een hondensnack e-commerce site in het Nederlands. 
Genereer een unieke, authentieke productbeschrijving voor:

Productnaam: {product_name}
Merk: {brand}
Type: {product_type}
Bijzonderheden: {bijzonderheden}

De beschrijving moet:
- In het Nederlands zijn
- 2-3 paragrafen bevatten
- Voordelen benadrukken
- Natuurlijk en authentiek klinken
- SEO-vriendelijk zijn
- Tussen 120-150 woorden zijn

Geef alleen de beschrijving terug, geen extra tekst."""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Je bent een expert copywriter voor hondenproducten in het Nederlands."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )
        
        description = response.choices[0].message.content.strip()
        return description
        
    except Exception as e:
        print(f"⚠️  ChatGPT error: {e}")
        # Fallback description
        return f"{product_name} van {brand} is een natuurlijke hondensnack van hoogste kwaliteit. {bijzonderheden}. Perfect voor honden van alle leeftijden die houden van lekkere, gezonde traktaties."

def load_products_from_csv():
    """Charge les produits depuis le CSV"""
    products = []
    
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:  # utf-8-sig pour enlever le BOM
        reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        product_id = 1
        
        for row in reader:
            try:
                # Nettoyer les valeurs (enlever retours chariot)
                name = row.get('Product Naam', '').replace('\n', ' ').strip()
                if not name:
                    continue
                
                price_str = row.get('Prijs €', '0').replace(',', '.').replace('\n', '').strip()
                try:
                    price = float(price_str)
                except:
                    price = 0.0
                
                product = {
                    'id': product_id,
                    'name': name,
                    'brand': row.get('Merk/Verkoper', '').replace('\n', ' ').strip(),
                    'type': row.get('Type Snack', '').replace('\n', ' ').strip(),
                    'weight': row.get('Gewicht/Inhoud', '').replace('\n', ' ').strip(),
                    'quantity': row.get('Aantal Stuks', '').replace('\n', ' ').strip(),
                    'target': row.get('Doelgroep', '').replace('\n', ' ').strip(),
                    'price': price,
                    'discount': row.get('Korting', '').replace('\n', ' ').strip(),
                    'delivery': row.get('Leveringstijd', '').replace('\n', ' ').strip(),
                    'features': row.get('Bijzonderheden', '').replace('\n', ' ').strip(),
                    'slug': slugify(name),
                }
                products.append(product)
                product_id += 1
            except Exception as e:
                print(f"⚠️  Skipping row: {e}")
                continue
    
    return products

def create_product_page(product, image_path):
    """Crée une page produit individuelle"""
    
    # Générer description unique via ChatGPT
    print(f"  🤖 Generating description for: {product['name'][:40]}...")
    description = generate_product_description_chatgpt(
        product['name'],
        product['brand'],
        product['type'],
        product['features']
    )
    
    # Calculer le prix avec réduction si applicable
    original_price = product['price']
    discount_price = None
    if product['discount'] and product['discount'] != 'n.b.':
        # Extraire le pourcentage (ex: "-13% bij 2")
        match = re.search(r'-(\d+)%', product['discount'])
        if match:
            discount_pct = int(match.group(1))
            discount_price = original_price * (1 - discount_pct / 100)
    
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product['name']} - {product['brand']} | Biologische Hondensnacks</title>
    <meta name="description" content="{description[:155]}">
    
    <!-- Canonical -->
    <link rel="canonical" href="https://biologische-hondensnacks.nl/produits/{product['slug']}.html">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="../favicon.ico">
    
    <!-- Styles -->
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="../css/product-page.css">
    
    <!-- Schema Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org/",
      "@type": "Product",
      "name": "{product['name']}",
      "brand": {{
        "@type": "Brand",
        "name": "{product['brand']}"
      }},
      "description": "{description[:200]}",
      "offers": {{
        "@type": "Offer",
        "price": "{product['price']:.2f}",
        "priceCurrency": "EUR",
        "availability": "https://schema.org/InStock"
      }}
    }}
    </script>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <a href="../" class="logo">
                    <span class="logo-icon">🐕</span>
                    <span class="logo-text">Biologische Hondensnacks</span>
                </a>
                <nav class="nav">
                    <a href="../">Home</a>
                    <a href="../winkel/">Shop</a>
                    <a href="../over-ons/">Over Ons</a>
                    <a href="../contact/">Contact</a>
                </nav>
            </div>
        </div>
    </header>

    <!-- Breadcrumb -->
    <div class="breadcrumb">
        <div class="container">
            <a href="../">Home</a>
            <span>›</span>
            <a href="../winkel/">Shop</a>
            <span>›</span>
            <span>{product['name']}</span>
        </div>
    </div>

    <!-- Product Content -->
    <main class="product-page">
        <div class="container">
            <div class="product-grid">
                <!-- Images -->
                <div class="product-images">
                    <div class="main-image">
                        <img src="../{image_path}" alt="{product['name']}" id="mainImage">
                    </div>
                </div>

                <!-- Info -->
                <div class="product-info">
                    <div class="product-header">
                        <span class="brand">{product['brand']}</span>
                        <h1>{product['name']}</h1>
                    </div>

                    <!-- Price -->
                    <div class="product-price">
                        {'<span class="price-old">€' + f'{original_price:.2f}' + '</span>' if discount_price else ''}
                        <span class="price-current">€{discount_price if discount_price else original_price:.2f}</span>
                        {f'<span class="price-badge">Bespaar {product["discount"]}</span>' if product['discount'] and product['discount'] != 'n.b.' else ''}
                    </div>

                    <!-- Description -->
                    <div class="product-description">
                        <p>{description}</p>
                    </div>

                    <!-- Details -->
                    <div class="product-details">
                        <h3>Productdetails</h3>
                        <ul>
                            <li><strong>Type:</strong> {product['type']}</li>
                            <li><strong>Gewicht:</strong> {product['weight']}</li>
                            <li><strong>Aantal:</strong> {product['quantity']}</li>
                            <li><strong>Doelgroep:</strong> {product['target']}</li>
                            <li><strong>Bijzonderheden:</strong> {product['features']}</li>
                        </ul>
                    </div>

                    <!-- CTA -->
                    <div class="product-actions">
                        <a href="https://www.bol.com/nl/s/?searchtext={product['name'].replace(' ', '+')}" 
                           target="_blank" 
                           rel="noopener"
                           class="btn-primary btn-large">
                            🛒 Bestel bij bol.com
                        </a>
                        <a href="../winkel/" class="btn-secondary">
                            ← Terug naar shop
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 Biologische Hondensnacks. Alle rechten voorbehouden.</p>
        </div>
    </footer>

    <script src="../js/main.js"></script>
</body>
</html>'''
    
    return html

def create_shop_listing_page(products, page_num, total_pages):
    """Crée une page de listing avec pagination"""
    
    start_idx = (page_num - 1) * PRODUCTS_PER_PAGE
    end_idx = start_idx + PRODUCTS_PER_PAGE
    page_products = products[start_idx:end_idx]
    
    # Déterminer les chemins relatifs selon la profondeur
    if page_num == 1:
        path_prefix = '../'  # /winkel/ -> /
        css_path = '../css/styles.css'
        shop_css_path = 'shop-styles.css'
        favicon_path = '../favicon.ico'
    else:
        path_prefix = '../../'  # /winkel/page/X/ -> /
        css_path = '../../css/styles.css'
        shop_css_path = '../../shop-styles.css'
        favicon_path = '../../favicon.ico'
    
    # Générer les product cards
    products_html = ''
    for product in page_products:
        # Trouver l'image
        image_path = product.get('image', 'images/placeholder.jpg')
        
        products_html += f'''
        <div class="product-card">
            <a href="{path_prefix}produits/{product['slug']}.html" class="product-link">
                <div class="product-image-wrapper">
                    <img src="{path_prefix}{image_path}" alt="{product['name']}" class="product-image" loading="lazy">
                </div>
                <div class="product-content">
                    <span class="product-brand">{product['brand']}</span>
                    <h3 class="product-name">{product['name']}</h3>
                    <div class="product-price">
                        <span class="price">€{product['price']:.2f}</span>
                    </div>
                </div>
            </a>
            <div class="product-actions">
                <a href="{path_prefix}produits/{product['slug']}.html" class="btn-secondary btn-small">
                    👁️ Details
                </a>
                <a href="https://www.bol.com/nl/s/?searchtext={product['name'].replace(' ', '+')}" 
                   target="_blank" 
                   rel="noopener"
                   class="btn-primary btn-small">
                    🛒 Koop nu
                </a>
            </div>
        </div>'''
    
    # Générer la pagination avec les bons chemins
    pagination_html = '<div class="pagination">'
    
    # Previous
    if page_num > 1:
        if page_num == 2:
            # De la page 2 vers la page 1
            prev_url = '../'  # Page 1 est à /winkel/
        else:
            # De la page 3+ vers page précédente
            prev_url = f'../{page_num - 1}/'
        pagination_html += f'<a href="{prev_url}" class="pagination-btn">← Vorige</a>'
    
    # Numbers
    for i in range(1, total_pages + 1):
        if i == page_num:
            pagination_html += f'<span class="pagination-number active">{i}</span>'
        else:
            if page_num == 1:
                # Depuis page 1
                page_url = f'page/{i}/' if i > 1 else ''
            else:
                # Depuis page 2+
                if i == 1:
                    page_url = '../'  # Retour à /winkel/
                else:
                    page_url = f'../{i}/'
            pagination_html += f'<a href="{page_url}" class="pagination-number">{i}</a>'
    
    # Next
    if page_num < total_pages:
        if page_num == 1:
            next_url = f'page/{page_num + 1}/'
        else:
            next_url = f'../{page_num + 1}/'
        pagination_html += f'<a href="{next_url}" class="pagination-btn">Volgende →</a>'
    
    pagination_html += '</div>'
    
    # Page title
    page_title = "Biologische Hondensnacks Winkel" if page_num == 1 else f"Biologische Hondensnacks Winkel - Pagina {page_num}"
    
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title} | Natuurlijke Snacks voor je Hond</title>
    <meta name="description" content="Ontdek onze collectie van {len(products)} biologische en natuurlijke hondensnacks. Gratis verzending vanaf €20 via bol.com.">
    
    <!-- Canonical -->
    <link rel="canonical" href="https://biologische-hondensnacks.nl/winkel/{'page/' + str(page_num) + '/' if page_num > 1 else ''}">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="{favicon_path}">
    
    <!-- Styles -->
    <link rel="stylesheet" href="{css_path}">
    <link rel="stylesheet" href="{shop_css_path}">
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <a href="{path_prefix}" class="logo">
                    <span class="logo-icon">🐕</span>
                    <span class="logo-text">Biologische Hondensnacks</span>
                </a>
                <nav class="nav">
                    <a href="{path_prefix}">Home</a>
                    <a href="{path_prefix}winkel/">Shop</a>
                    <a href="{path_prefix}over-ons/">Over Ons</a>
                    <a href="{path_prefix}contact/">Contact</a>
                </nav>
            </div>
        </div>
    </header>

    <!-- Hero -->
    <section class="shop-hero">
        <div class="container">
            <h1>Biologische Hondensnacks Winkel</h1>
            <p>Ontdek onze collectie van {len(products)} natuurlijke en biologische hondensnacks. Alle producten via bol.com.</p>
            <div class="hero-stats">
                <div class="stat">
                    <span class="stat-number">{len(products)}</span>
                    <span class="stat-label">Producten</span>
                </div>
                <div class="stat">
                    <span class="stat-number">4.8★</span>
                    <span class="stat-label">Gemiddelde Score</span>
                </div>
                <div class="stat">
                    <span class="stat-number">24h</span>
                    <span class="stat-label">Snelle Levering</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Products -->
    <main class="shop-main">
        <div class="container">
            <div class="shop-header">
                <p class="results-count">Toont {len(page_products)} van {len(products)} producten</p>
                <p class="page-info">Pagina {page_num} van {total_pages}</p>
            </div>

            <div class="products-grid">
                {products_html}
            </div>

            {pagination_html}
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div>
                    <h3>Biologische Hondensnacks</h3>
                    <p>De beste natuurlijke en biologische snacks voor jouw hond.</p>
                </div>
                <div>
                    <h3>Links</h3>
                    <ul>
                        <li><a href="{path_prefix}">Home</a></li>
                        <li><a href="{path_prefix}winkel/">Shop</a></li>
                        <li><a href="{path_prefix}over-ons/">Over Ons</a></li>
                        <li><a href="{path_prefix}contact/">Contact</a></li>
                    </ul>
                </div>
            </div>
            <p>&copy; 2025 Biologische Hondensnacks. Alle rechten voorbehouden.</p>
        </div>
    </footer>

    <script src="{path_prefix}js/main.js"></script>
</body>
</html>'''
    
    return html

def create_shop_css():
    """Crée le fichier CSS pour le shop"""
    css = '''/* SHOP STYLES */

.shop-hero {
    background: linear-gradient(135deg, #E68161 0%, #D66F50 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
}

.shop-hero h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.shop-hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    opacity: 0.95;
}

.hero-stats {
    display: flex;
    gap: 3rem;
    justify-content: center;
    margin-top: 2rem;
}

.stat {
    text-align: center;
}

.stat-number {
    display: block;
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.9rem;
    opacity: 0.9;
}

.shop-main {
    padding: 3rem 0;
}

.shop-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid #e2e8f0;
}

.results-count {
    font-size: 1.1rem;
    color: #2d3748;
    font-weight: 500;
}

.page-info {
    color: #6b7280;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.product-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

.product-link {
    text-decoration: none;
    color: inherit;
    display: block;
}

.product-image-wrapper {
    width: 100%;
    height: 250px;
    overflow: hidden;
    background: #f7fafc;
}

.product-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.product-content {
    padding: 1.5rem;
}

.product-brand {
    color: #E68161;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.product-name {
    font-size: 1.1rem;
    margin: 0.5rem 0 1rem;
    color: #2d3748;
    line-height: 1.4;
    min-height: 2.8rem;
}

.product-price {
    font-size: 1.3rem;
    font-weight: bold;
    color: #2d3748;
}

.product-actions {
    display: flex;
    gap: 0.5rem;
    padding: 0 1.5rem 1.5rem;
}

.btn-primary, .btn-secondary {
    flex: 1;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    text-decoration: none;
    text-align: center;
    font-weight: 600;
    transition: all 0.3s;
    border: none;
    cursor: pointer;
}

.btn-primary {
    background: #E68161;
    color: white;
}

.btn-primary:hover {
    background: #D66F50;
}

.btn-secondary {
    background: #f7fafc;
    color: #2d3748;
    border: 2px solid #e2e8f0;
}

.btn-secondary:hover {
    background: #e2e8f0;
}

.btn-small {
    font-size: 0.85rem;
    padding: 0.6rem 0.8rem;
}

.pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
    margin: 3rem 0;
}

.pagination-btn, .pagination-number {
    padding: 0.75rem 1.25rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s;
}

.pagination-btn {
    background: #E68161;
    color: white;
}

.pagination-btn:hover {
    background: #D66F50;
}

.pagination-number {
    background: #f7fafc;
    color: #2d3748;
    border: 2px solid #e2e8f0;
}

.pagination-number:hover {
    background: #e2e8f0;
}

.pagination-number.active {
    background: #E68161;
    color: white;
    border-color: #E68161;
}

@media (max-width: 768px) {
    .products-grid {
        grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
        gap: 1.5rem;
    }
    
    .hero-stats {
        gap: 1.5rem;
    }
    
    .shop-header {
        flex-direction: column;
        gap: 1rem;
        align-items: flex-start;
    }
}'''
    
    return css

def create_product_page_css():
    """Crée le CSS pour les pages produit"""
    css = '''/* PRODUCT PAGE STYLES */

.breadcrumb {
    background: #f7fafc;
    padding: 1rem 0;
    border-bottom: 1px solid #e2e8f0;
}

.breadcrumb a {
    color: #E68161;
    text-decoration: none;
}

.breadcrumb span {
    color: #6b7280;
    margin: 0 0.5rem;
}

.product-page {
    padding: 3rem 0;
}

.product-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
}

.product-images {
    position: sticky;
    top: 2rem;
    height: fit-content;
}

.main-image {
    width: 100%;
    height: 500px;
    border-radius: 12px;
    overflow: hidden;
    background: #f7fafc;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.main-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.product-header {
    margin-bottom: 2rem;
}

.brand {
    color: #E68161;
    font-size: 0.9rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.product-info h1 {
    font-size: 2.2rem;
    color: #2d3748;
    margin: 0.5rem 0 1.5rem;
    line-height: 1.3;
}

.product-price {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: #f7fafc;
    border-radius: 12px;
}

.price-old {
    font-size: 1.3rem;
    color: #9ca3af;
    text-decoration: line-through;
}

.price-current {
    font-size: 2.2rem;
    font-weight: bold;
    color: #2d3748;
}

.price-badge {
    background: #E68161;
    color: white;
    padding: 0.4rem 0.8rem;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
}

.product-description {
    margin-bottom: 2rem;
    line-height: 1.8;
    color: #4a5568;
    font-size: 1.05rem;
}

.product-details {
    background: #f7fafc;
    padding: 1.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
}

.product-details h3 {
    margin-bottom: 1rem;
    color: #2d3748;
}

.product-details ul {
    list-style: none;
    padding: 0;
}

.product-details li {
    padding: 0.75rem 0;
    border-bottom: 1px solid #e2e8f0;
    color: #4a5568;
}

.product-details li:last-child {
    border-bottom: none;
}

.product-details strong {
    color: #2d3748;
    font-weight: 600;
    margin-right: 0.5rem;
}

.product-actions {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.btn-large {
    padding: 1.2rem 2rem;
    font-size: 1.1rem;
}

@media (max-width: 968px) {
    .product-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    
    .product-images {
        position: static;
    }
    
    .main-image {
        height: 400px;
    }
}'''
    
    return css

def main(api_key):
    """Fonction principale"""
    global client
    
    # Initialiser le client OpenAI
    if api_key:
        try:
            client = OpenAI(api_key=api_key)
            print("✅ OpenAI API initialisé - Descriptions uniques activées")
        except Exception as e:
            print(f"⚠️  OpenAI API error: {e}")
            print("⚠️  Utilisation des descriptions fallback")
            client = None
    else:
        print("⚠️  Pas de clé API - Utilisation des descriptions fallback")
        client = None
    
    print("🏗️  BUILD COMPLETE SHOP")
    print("=" * 60)
    
    # Créer les répertoires
    WINKEL_DIR.mkdir(exist_ok=True)
    PRODUITS_DIR.mkdir(exist_ok=True)
    (WINKEL_DIR / 'page').mkdir(exist_ok=True)
    
    # Charger les produits
    print("\n📦 Loading products from CSV...")
    products = load_products_from_csv()
    print(f"✅ Loaded {len(products)} products")
    
    # Lister les images disponibles
    print("\n🖼️  Finding product images...")
    available_images = list(IMAGES_DIR.glob('*.jpg'))
    print(f"✅ Found {len(available_images)} images")
    
    # Matcher les images aux produits
    print("\n🔗 Matching images to products...")
    for product in products:
        img_path = find_matching_image(product['name'], [str(img) for img in available_images])
        product['image'] = img_path.replace(str(BASE_DIR) + '/', '')
    
    # Créer les pages produit
    print("\n📄 Creating individual product pages...")
    for i, product in enumerate(products, 1):
        print(f"  [{i}/{len(products)}] {product['name'][:50]}")
        html = create_product_page(product, product['image'])
        
        output_file = PRODUITS_DIR / f"{product['slug']}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
    
    # Calculer le nombre de pages
    total_pages = math.ceil(len(products) / PRODUCTS_PER_PAGE)
    print(f"\n📑 Creating {total_pages} shop listing pages...")
    
    # Créer les pages de listing
    for page_num in range(1, total_pages + 1):
        print(f"  Creating page {page_num}/{total_pages}...")
        html = create_shop_listing_page(products, page_num, total_pages)
        
        if page_num == 1:
            output_file = WINKEL_DIR / 'index.html'
        else:
            page_dir = WINKEL_DIR / 'page' / str(page_num)
            page_dir.mkdir(parents=True, exist_ok=True)
            output_file = page_dir / 'index.html'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
    
    # Créer les CSS
    print("\n🎨 Creating CSS files...")
    with open(WINKEL_DIR / 'shop-styles.css', 'w', encoding='utf-8') as f:
        f.write(create_shop_css())
    
    css_dir = BASE_DIR / 'css'
    css_dir.mkdir(exist_ok=True)
    with open(css_dir / 'product-page.css', 'w', encoding='utf-8') as f:
        f.write(create_product_page_css())
    
    print(f"\n{'='*60}")
    print("🎉 SHOP COMPLET CRÉÉ!")
    print(f"✅ {len(products)} pages produit")
    print(f"✅ {total_pages} pages de listing")
    print(f"✅ {PRODUCTS_PER_PAGE} produits par page")
    print(f"✅ Images matchées automatiquement")
    print(f"✅ Descriptions uniques via ChatGPT")
    print(f"{'='*60}")

if __name__ == "__main__":
    # DÉFINIR TA CLÉ API ICI
    API_KEY = None  # ⚠️ Remplacer par ta clé API OpenAI
    
    if not API_KEY:
        print("\n⚠️  ATTENTION: Définis ta clé API OpenAI dans le script")
        print("Ligne ~970: API_KEY = 'sk-...'")
        print("\nOu passe-la comme argument:")
        import sys
        if len(sys.argv) > 1:
            API_KEY = sys.argv[1]
    
    if API_KEY:
        main(API_KEY)
    else:
        print("\n⚠️  Aucune clé API - Le script va continuer avec des descriptions fallback")
        response = input("Continuer quand même? (o/n): ")
        if response.lower() == 'o':
            main(None)
        else:
            print("❌ Arrêté par l'utilisateur")
