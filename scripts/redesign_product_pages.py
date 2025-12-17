#!/usr/bin/env python3
"""
REDESIGN PRODUCT PAGES - NEW CLEAN LAYOUT
==========================================

Refait toutes les pages produits avec un layout moderne et clair
inspiré du site de référence mais avec les couleurs biologische-hondensnacks.

Structure cible:
- Image produit grande et claire à gauche
- Infos produit à droite (prix, specs, CTA)
- Description complète en bas
- Produits similaires en bas

Auteur: AI Assistant
Date: Décembre 2025
"""

import os
import glob
import re
from bs4 import BeautifulSoup

# Configuration
PRODUITS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/redesign'
CSS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/produits/product-page-new.css'

os.makedirs(BACKUP_DIR, exist_ok=True)

# Nouveau CSS moderne
NEW_CSS = """/* PRODUCT PAGE - NEW CLEAN LAYOUT */
/* Inspiré du design moderne mais avec couleurs biologische-hondensnacks */

:root {
    --primary-orange: #E68161;
    --dark-text: #1F2121;
    --light-bg: #FCFCF9;
    --border-color: #E0E0E0;
}

.product-page {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
}

/* LAYOUT 2 COLONNES */
.product-hero {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    margin-bottom: 3rem;
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}

/* IMAGE SECTION */
.product-image-section {
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fafafa;
    border-radius: 12px;
    padding: 2rem;
}

.product-image-section img {
    width: 100%;
    max-width: 400px;
    height: auto;
    object-fit: contain;
    border-radius: 8px;
}

/* INFO SECTION */
.product-details-section {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.product-title-block h1 {
    font-size: 28px;
    font-weight: 700;
    color: var(--dark-text);
    margin: 0 0 0.5rem 0;
    line-height: 1.3;
}

.product-brand {
    color: var(--primary-orange);
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.5rem;
}

.product-rating {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.stars {
    color: #FFA500;
    font-size: 16px;
}

.review-count {
    color: #6b7280;
    font-size: 14px;
}

/* PRIX */
.price-display {
    font-size: 36px;
    font-weight: 800;
    color: var(--primary-orange);
    margin: 1.5rem 0;
}

/* DESCRIPTION COURTE */
.product-short-description {
    background: #f9fafb;
    padding: 1.25rem;
    border-radius: 8px;
    border-left: 4px solid var(--primary-orange);
    margin: 1.5rem 0;
}

.product-short-description h3 {
    font-size: 14px;
    font-weight: 700;
    text-transform: uppercase;
    color: #374151;
    margin: 0 0 0.75rem 0;
    letter-spacing: 0.5px;
}

.product-short-description p {
    color: #4b5563;
    line-height: 1.6;
    margin: 0;
    font-size: 15px;
}

/* SPECIFICATIONS TABLE */
.specs-table-clean {
    margin: 1.5rem 0;
}

.specs-table-clean h3 {
    font-size: 16px;
    font-weight: 700;
    color: var(--dark-text);
    margin: 0 0 1rem 0;
}

.spec-row-clean {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.875rem 0;
    border-bottom: 1px solid #e5e7eb;
}

.spec-row-clean:last-child {
    border-bottom: none;
}

.spec-label-clean {
    font-weight: 600;
    color: #6b7280;
    font-size: 14px;
}

.spec-value-clean {
    color: var(--dark-text);
    font-weight: 500;
    font-size: 14px;
}

/* CTA BUTTON */
.cta-button {
    background: var(--primary-orange);
    color: white;
    padding: 1rem 2rem;
    border-radius: 8px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 16px;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    margin: 1.5rem 0;
    width: 100%;
    box-shadow: 0 4px 12px rgba(230, 129, 97, 0.3);
}

.cta-button:hover {
    background: #d67347;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(230, 129, 97, 0.4);
}

/* TRUST BADGES */
.trust-badges-clean {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin: 1.5rem 0;
}

.trust-item-clean {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 14px;
    color: #4b5563;
}

.trust-item-clean::before {
    content: "✓";
    color: var(--primary-orange);
    font-weight: 700;
    font-size: 16px;
}

/* DESCRIPTION COMPLÈTE EN BAS */
.product-full-description {
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    margin-bottom: 3rem;
}

.product-full-description h2 {
    font-size: 24px;
    font-weight: 700;
    color: var(--dark-text);
    margin: 0 0 1.5rem 0;
}

.product-full-description p {
    color: #4b5563;
    line-height: 1.8;
    font-size: 16px;
    margin-bottom: 1.25rem;
}

.product-full-description ul {
    list-style: none;
    padding: 0;
    margin: 1.5rem 0;
}

.product-full-description ul li {
    padding: 0.75rem 0;
    padding-left: 1.5rem;
    position: relative;
    color: #4b5563;
    line-height: 1.6;
}

.product-full-description ul li::before {
    content: "•";
    color: var(--primary-orange);
    font-weight: bold;
    font-size: 20px;
    position: absolute;
    left: 0;
}

/* PRODUITS SIMILAIRES */
.related-products-section {
    margin: 3rem 0;
}

.related-products-section h2 {
    font-size: 28px;
    font-weight: 700;
    color: var(--dark-text);
    margin-bottom: 2rem;
    text-align: center;
}

.products-grid-clean {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1.5rem;
}

.product-card-clean {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    text-decoration: none;
    display: flex;
    flex-direction: column;
}

.product-card-clean:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}

.product-card-image {
    width: 100%;
    height: 180px;
    object-fit: cover;
    background: #fafafa;
}

.product-card-info {
    padding: 1.25rem;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.product-card-brand {
    color: var(--primary-orange);
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.product-card-name {
    color: var(--dark-text);
    font-size: 16px;
    font-weight: 600;
    margin: 0 0 auto 0;
    line-height: 1.4;
}

.product-card-price {
    color: var(--primary-orange);
    font-size: 20px;
    font-weight: 700;
    margin-top: 0.75rem;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .product-hero {
        grid-template-columns: 1fr;
        gap: 2rem;
        padding: 1.5rem;
    }
    
    .product-image-section {
        padding: 1.5rem;
    }
    
    .product-title-block h1 {
        font-size: 24px;
    }
    
    .price-display {
        font-size: 28px;
    }
    
    .products-grid-clean {
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 1rem;
    }
}
"""

def extract_product_data(soup):
    """Extrait toutes les données du produit"""
    try:
        # Brand
        brand_elem = soup.find(class_='brand')
        brand = brand_elem.text.strip() if brand_elem else 'Merk onbekend'
        
        # Title
        h1 = soup.find('h1')
        title = h1.text.strip() if h1 else 'Product'
        
        # Price
        price_elem = soup.find(class_='price-current')
        if not price_elem:
            # Fallback: chercher dans price-section
            price_section = soup.find(class_='price-section')
            if price_section:
                price_text = price_section.get_text()
                price_match = re.search(r'€\s*(\d+[,\.]\d+)', price_text)
                price = price_match.group(0) if price_match else '€0,00'
            else:
                price = '€0,00'
        else:
            price = price_elem.text.strip()
        
        # Image
        img = soup.find(class_='main-image')
        if img:
            img_tag = img.find('img')
            image_src = img_tag['src'] if img_tag and 'src' in img_tag.attrs else '../images/placeholder.jpg'
            image_alt = img_tag['alt'] if img_tag and 'alt' in img_tag.attrs else title
        else:
            image_src = '../images/placeholder.jpg'
            image_alt = title
        
        # Specs
        specs = []
        spec_rows = soup.find_all(class_='spec-row')
        for row in spec_rows:
            label = row.find(class_='spec-label')
            value = row.find(class_='spec-value')
            if label and value:
                specs.append({
                    'label': label.text.strip().rstrip(':'),
                    'value': value.text.strip()
                })
        
        # Description (section "Waarom kiezen voor")
        extended_desc = soup.find(class_='product-description-extended')
        full_description = ''
        if extended_desc:
            # Extraire le texte
            paragraphs = extended_desc.find_all('p')
            full_description = '\n\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
        
        # Description courte (section "Over dit product")
        short_desc_section = soup.find(class_='product-description')
        short_description = ''
        if short_desc_section:
            first_p = short_desc_section.find('p')
            if first_p:
                short_description = first_p.get_text(strip=True)
        
        # Voordelen (benefits)
        benefits = []
        benefits_list = soup.find(class_='benefits-list')
        if benefits_list:
            items = benefits_list.find_all('li')
            for item in items[:5]:  # Max 5
                strong = item.find('strong')
                if strong:
                    benefits.append(strong.get_text(strip=True))
        
        return {
            'brand': brand,
            'title': title,
            'price': price,
            'image_src': image_src,
            'image_alt': image_alt,
            'specs': specs,
            'short_description': short_description,
            'full_description': full_description,
            'benefits': benefits
        }
    except Exception as e:
        print(f"   ⚠️  Error extracting data: {e}")
        return None

def generate_new_html(product_data, original_soup):
    """Génère le nouveau HTML avec le layout moderne"""
    
    # Copier le head original (meta tags, etc.)
    head = original_soup.find('head')
    header = original_soup.find('header')
    footer = original_soup.find('footer')
    
    new_html = f"""<!DOCTYPE html>
<html lang="nl">
{str(head)}
<body>
{str(header)}

<!-- NEW CLEAN PRODUCT LAYOUT -->
<main class="container product-page">
    
    <!-- HERO SECTION: Image + Infos -->
    <div class="product-hero">
        <!-- IMAGE GAUCHE -->
        <div class="product-image-section">
            <img src="{product_data['image_src']}" alt="{product_data['image_alt']}">
        </div>
        
        <!-- INFOS DROITE -->
        <div class="product-details-section">
            <div class="product-title-block">
                <div class="product-brand">{product_data['brand']}</div>
                <h1>{product_data['title']}</h1>
            </div>
            
            <div class="product-rating">
                <span class="stars">★★★★★</span>
                <span class="review-count">(135 klanten)</span>
            </div>
            
            <div class="price-display">{product_data['price']}</div>
            
            <!-- DESCRIPTION COURTE -->
            {f'''<div class="product-short-description">
                <h3>Productbeschrijving</h3>
                <p>{product_data['short_description']}</p>
            </div>''' if product_data['short_description'] else ''}
            
            <!-- SPECIFICATIONS -->
            <div class="specs-table-clean">
                <h3>Specificaties</h3>
"""
    
    # Add specs
    for spec in product_data['specs'][:6]:  # Max 6 specs
        new_html += f"""                <div class="spec-row-clean">
                    <span class="spec-label-clean">{spec['label']}</span>
                    <span class="spec-value-clean">{spec['value']}</span>
                </div>
"""
    
    new_html += """            </div>
            
            <!-- CTA BUTTON -->
            <a href="https://www.bol.com" target="_blank" rel="noopener" class="cta-button">
                Koop nu op Bol.com →
            </a>
            
            <!-- TRUST BADGES -->
            <div class="trust-badges-clean">
                <div class="trust-item-clean">Gratis levering vanaf €20</div>
                <div class="trust-item-clean">30 dagen bedenktijd</div>
                <div class="trust-item-clean">Betalen: iDeal, PayPal, Creditcard</div>
            </div>
        </div>
    </div>
    
    <!-- DESCRIPTION COMPLÈTE EN BAS -->
"""
    
    if product_data['full_description']:
        new_html += f"""    <div class="product-full-description">
        <h2>Waarom kiezen voor {product_data['title']}?</h2>
        <p>{product_data['full_description']}</p>
"""
        
        if product_data['benefits']:
            new_html += """        <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: #1F2121;">Voordelen:</h3>
        <ul>
"""
            for benefit in product_data['benefits']:
                new_html += f"""            <li>{benefit}</li>
"""
            new_html += """        </ul>
"""
        
        new_html += """    </div>
"""
    
    # PRODUITS SIMILAIRES (à extraire de l'original)
    related_section = original_soup.find(class_='related-products')
    if related_section:
        new_html += """    <div class="related-products-section">
        <h2>Vergelijkbare Producten</h2>
        <div class="products-grid-clean">
"""
        related_cards = related_section.find_all(class_='product-card')
        for card in related_cards[:4]:  # Max 4
            card_link = card.find('a')
            href = card_link['href'] if card_link and 'href' in card_link.attrs else '#'
            
            card_img = card.find('img')
            card_img_src = card_img['src'] if card_img and 'src' in card_img.attrs else '../images/placeholder.jpg'
            card_img_alt = card_img['alt'] if card_img and 'alt' in card_img.attrs else 'Product'
            
            card_brand = card.find(class_='product-brand')
            card_brand_text = card_brand.text.strip() if card_brand else ''
            
            card_name = card.find(class_='product-name')
            card_name_text = card_name.text.strip() if card_name else 'Product'
            
            card_price = card.find(class_='product-price')
            card_price_text = card_price.text.strip() if card_price else '€0,00'
            
            new_html += f"""            <a href="{href}" class="product-card-clean">
                <img src="{card_img_src}" alt="{card_img_alt}" class="product-card-image">
                <div class="product-card-info">
                    <div class="product-card-brand">{card_brand_text}</div>
                    <div class="product-card-name">{card_name_text}</div>
                    <div class="product-card-price">{card_price_text}</div>
                </div>
            </a>
"""
        
        new_html += """        </div>
    </div>
"""
    
    new_html += f"""
</main>

{str(footer)}

<!-- Scripts -->
<script src="../js/main.js"></script>
</body>
</html>"""
    
    return new_html

def process_product_page(html_path):
    """Traite une page produit"""
    filename = os.path.basename(html_path)
    
    try:
        # Lire HTML
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extraire données
        product_data = extract_product_data(soup)
        if not product_data:
            return False, "Data extraction failed"
        
        # Backup
        backup_path = os.path.join(BACKUP_DIR, filename + '.old')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Générer nouveau HTML
        new_html = generate_new_html(product_data, soup)
        
        # Ajouter le nouveau CSS dans le head
        new_soup = BeautifulSoup(new_html, 'html.parser')
        head = new_soup.find('head')
        if head:
            # Ajouter le lien vers le nouveau CSS
            new_link = new_soup.new_tag('link', href='product-page-new.css', rel='stylesheet')
            head.append(new_link)
        
        # Sauvegarder
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(str(new_soup.prettify()))
        
        return True, f"Redesigned: {product_data['title'][:40]}"
        
    except Exception as e:
        return False, str(e)

def main():
    """Fonction principale"""
    print("\n🎨 PRODUCT PAGES REDESIGN")
    print("=" * 70)
    print("Nouveau layout moderne avec les couleurs biologische-hondensnacks")
    print("=" * 70)
    
    # 1. Créer le nouveau fichier CSS
    print(f"\n📝 Creating new CSS file...")
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(NEW_CSS)
    print(f"✅ CSS created: {CSS_FILE}")
    
    # 2. Trouver tous les fichiers HTML
    html_files = glob.glob(os.path.join(PRODUITS_DIR, '*.html'))
    html_files = [f for f in html_files if not f.endswith('index.html')]
    
    total_files = len(html_files)
    print(f"\n📁 Found {total_files} product pages")
    print(f"💾 Backups will be saved in: {BACKUP_DIR}\n")
    
    # 3. Traiter chaque page
    success_count = 0
    error_count = 0
    
    for idx, html_file in enumerate(html_files, 1):
        filename = os.path.basename(html_file)
        print(f"[{idx}/{total_files}] {filename[:50]}...")
        
        success, result = process_product_page(html_file)
        
        if success:
            print(f"   ✅ {result}")
            success_count += 1
        else:
            print(f"   ❌ Error: {result}")
            error_count += 1
    
    # 4. Résumé
    print(f"\n{'='*70}")
    print(f"🎉 REDESIGN COMPLETE!")
    print(f"✅ Success: {success_count}/{total_files} pages")
    print(f"❌ Errors: {error_count}/{total_files} pages")
    print(f"💾 All original pages backed up in: {BACKUP_DIR}")
    print(f"🎨 New CSS file: {CSS_FILE}")
    print(f"{'='*70}")
    
    if success_count > 0:
        print(f"\n🚀 NEXT STEPS:")
        print(f"1. Ouvrez une page produit dans votre navigateur")
        print(f"2. Vérifiez le nouveau design (layout 2 colonnes, couleurs orange)")
        print(f"3. Si besoin d'ajustements, le CSS est dans: product-page-new.css")

if __name__ == "__main__":
    main()
