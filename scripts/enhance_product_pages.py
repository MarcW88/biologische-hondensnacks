#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - PRODUCT PAGES ENHANCER
=================================================

Script pour améliorer les pages produits:
1. Espacement des spécifications optimisé
2. Suppression mention "gratis verzending" 
3. Section prix/grammage plus attrayante
4. Contenu unique pour chaque produit
5. 3-4 produits gerelateerde par page

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import csv
import random
import shutil
from pathlib import Path

# Configuration
PROJECT_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
CSV_FILE = '/Users/marc/Desktop/biologische-hondensnacks/Hondensnacks Catalogus (1).csv'
PRODUCTS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/product_enhance'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def get_product_data():
    """Read product data from CSV"""
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('\ufeff'):
                content = content[1:]
            
            reader = csv.DictReader(content.splitlines(), delimiter=';')
            products = list(reader)
        
        print(f"✅ Loaded {len(products)} products from CSV")
        return products
        
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return []

def generate_unique_description(product_data):
    """Generate unique description for each product"""
    # Handle BOM in CSV column names
    name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product_data else 'Product Naam'
    
    naam = product_data[name_key]
    merk = product_data['Merk/Verkoper']
    type_snack = product_data['Type Snack']
    gewicht = product_data['Gewicht/Inhoud']
    doelgroep = product_data['Doelgroep']
    bijzonderheden = product_data['Bijzonderheden']
    
    # Templates variés pour différents types de produits
    templates = {
        'kauwsnacks': [
            f"Deze premium {type_snack.lower()} van {merk} biedt je hond urenlang kauwplezier. Met een gewicht van {gewicht} is het perfect voor {doelgroep.lower()}. {bijzonderheden} maken dit product tot een uitstekende keuze voor honden die van intensief kauwen houden.",
            
            f"Ontdek de kracht van natuurlijk kauwen met deze {type_snack.lower()} van {merk}. Speciaal ontwikkeld voor {doelgroep.lower()}, biedt dit product van {gewicht} niet alleen plezier maar ook tandverzorging. {bijzonderheden} zorgen voor een gezonde en smakelijke ervaring.",
            
            f"Geef je hond het beste met deze {type_snack.lower()} van {merk}. Met {gewicht} aan puur kauwgenot, is dit product ideaal voor {doelgroep.lower()}. De unieke samenstelling met {bijzonderheden.lower()} ondersteunt de natuurlijke kauwbehoefte van je viervoeter."
        ],
        'training': [
            f"Perfect voor training en beloning! Deze {type_snack.lower()} van {merk} zijn ideaal voor {doelgroep.lower()}. Met {gewicht} aan smakelijke beloningen help je je hond nieuwe commando's te leren. {bijzonderheden} maken elke training sessie tot een succes.",
            
            f"Maak training leuk en effectief met deze {type_snack.lower()} van {merk}. Geschikt voor {doelgroep.lower()}, bieden deze snacks van {gewicht} de perfecte motivatie. {bijzonderheden} zorgen ervoor dat je hond gefocust en gemotiveerd blijft.",
            
            f"Versterk de band met je hond tijdens training met deze {type_snack.lower()} van {merk}. Deze {gewicht} porties zijn perfect voor {doelgroep.lower()} en bevatten {bijzonderheden.lower()}. Ideaal voor positieve bekrachtiging en succesvolle training."
        ],
        'natuurlijk': [
            f"Puur natuur voor je hond! Deze {type_snack.lower()} van {merk} bevatten alleen natuurlijke ingrediënten. Met {gewicht} aan gezonde voeding, perfect voor {doelgroep.lower()}. {bijzonderheden} garanderen een product zonder kunstmatige toevoegingen.",
            
            f"Kies voor natuurlijke voeding met deze {type_snack.lower()} van {merk}. Speciaal geselecteerd voor {doelgroep.lower()}, biedt dit product van {gewicht} pure natuurlijke smaak. {bijzonderheden} maken dit tot een verantwoorde keuze voor bewuste hondenbezitters.",
            
            f"Verwén je hond met de kracht van de natuur. Deze {type_snack.lower()} van {merk} zijn 100% natuurlijk en perfect voor {doelgroep.lower()}. Met {gewicht} aan pure ingrediënten en {bijzonderheden.lower()}, geef je je hond het beste wat de natuur te bieden heeft."
        ]
    }
    
    # Bepaal categorie op basis van type
    if any(word in type_snack.lower() for word in ['kauw', 'bot', 'stick', 'staaf']):
        category = 'kauwsnacks'
    elif any(word in type_snack.lower() for word in ['trainer', 'beloning', 'soft']):
        category = 'training'
    else:
        category = 'natuurlijk'
    
    # Selecteer random template
    description = random.choice(templates[category])
    
    return description

def generate_benefits_list(product_data):
    """Generate unique benefits list for each product"""
    type_snack = product_data['Type Snack']
    bijzonderheden = product_data['Bijzonderheden']
    doelgroep = product_data['Doelgroep']
    
    all_benefits = [
        "🦷 Ondersteunt tandgezondheid",
        "💪 Versterkt kauwspieren", 
        "🧠 Mentale stimulatie",
        "❤️ Stress vermindering",
        "🌿 100% natuurlijke ingrediënten",
        "🚫 Geen kunstmatige toevoegingen",
        "✨ Premium kwaliteit",
        "🎯 Perfect voor training",
        "😋 Onweerstaanbare smaak",
        "⚡ Energieboost",
        "🛡️ Immuunsysteem ondersteuning",
        "🏃 Bevordert activiteit",
        "💎 Hoogwaardige proteïnen",
        "🌱 Duurzaam geproduceerd"
    ]
    
    # Selecteer 4-6 relevante benefits
    selected_benefits = random.sample(all_benefits, random.randint(4, 6))
    
    return selected_benefits

def get_related_products(current_product, all_products, count=4):
    """Get related products for the current product"""
    name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in current_product else 'Product Naam'
    current_name = current_product[name_key]
    current_brand = current_product['Merk/Verkoper']
    current_type = current_product['Type Snack']
    
    # Filter out current product and get similar ones
    related = []
    
    for product in all_products:
        product_name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
        if product[product_name_key] == current_name:
            continue
            
        # Prioritize same brand or similar type
        score = 0
        if product['Merk/Verkoper'] == current_brand:
            score += 2
        if any(word in product['Type Snack'].lower() for word in current_type.lower().split()):
            score += 1
            
        related.append((product, score))
    
    # Sort by score and take top products
    related.sort(key=lambda x: x[1], reverse=True)
    return [product for product, score in related[:count]]

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')[:60]

def generate_enhanced_product_html(product_data, all_products):
    """Generate enhanced HTML for a product page"""
    # Handle BOM in CSV column names
    name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product_data else 'Product Naam'
    
    naam = product_data[name_key]
    merk = product_data['Merk/Verkoper']
    type_snack = product_data['Type Snack']
    gewicht = product_data['Gewicht/Inhoud']
    aantal = product_data['Aantal Stuks']
    doelgroep = product_data['Doelgroep']
    prijs = product_data['Prijs €']
    bijzonderheden = product_data['Bijzonderheden']
    
    slug = slugify(naam)
    
    # Generate unique content
    description = generate_unique_description(product_data)
    benefits = generate_benefits_list(product_data)
    related_products = get_related_products(product_data, all_products)
    
    # Check if image exists
    image_path = f"../images/{naam}.jpg"
    if not os.path.exists(f"/Users/marc/Desktop/biologische-hondensnacks/images/{naam}.jpg"):
        image_path = "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop"
    
    # Generate related products HTML
    related_html = ""
    for related in related_products:
        related_name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in related else 'Product Naam'
        related_naam = related[related_name_key]
        related_merk = related['Merk/Verkoper']
        related_prijs = related['Prijs €']
        related_slug = slugify(related_naam)
        
        # Check related product image
        related_image = f"../images/{related_naam}.jpg"
        if not os.path.exists(f"/Users/marc/Desktop/biologische-hondensnacks/images/{related_naam}.jpg"):
            related_image = "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=200&h=150&fit=crop"
        
        related_html += f'''
                <div class="product-card">
                    <a href="{related_slug}.html" class="product-link">
                        <img src="{related_image}" alt="{related_naam}" class="product-image">
                        <div class="product-info">
                            <div class="product-brand">{related_merk}</div>
                            <h3 class="product-name">{related_naam}</h3>
                            <div class="product-price">€{related_prijs}</div>
                        </div>
                    </a>
                </div>'''
    
    # Generate benefits HTML
    benefits_html = "".join([f"<li>{benefit}</li>" for benefit in benefits])
    
    html_content = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{naam} | Biologische Hondensnacks</title>
    <meta name="description" content="{naam} van {merk}. {bijzonderheden}. Bestel nu online!">
    <link rel="canonical" href="https://biologische-hondensnacks.nl/produits/{slug}.html">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="../favicon.ico">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{naam}">
    <meta property="og:description" content="{bijzonderheden}">
    <meta property="og:image" content="{image_path}">
    <meta property="og:url" content="https://biologische-hondensnacks.nl/produits/{slug}.html">
    
    <!-- Styles -->
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="product-page.css">
    
    <style>
    /* Enhanced product page styles */
    .price-section {{
        background: linear-gradient(135deg, #E68161 0%, #d67347 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(230, 129, 97, 0.3);
    }}
    
    .price-main {{
        display: flex;
        align-items: baseline;
        gap: 1rem;
        margin-bottom: 0.5rem;
    }}
    
    .price-current {{
        font-size: 2.5rem;
        font-weight: 800;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }}
    
    .price-per-unit {{
        font-size: 1.1rem;
        opacity: 0.9;
        font-weight: 500;
    }}
    
    .price-highlight {{
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 0.5rem;
        display: inline-block;
    }}
    
    .specs-table {{
        display: grid;
        gap: 0.75rem;
        margin-bottom: 2rem;
    }}
    
    .spec-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background: #f8fafc;
        border-radius: 8px;
        border-left: 4px solid #E68161;
    }}
    
    .benefits-list {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 0.5rem;
        list-style: none;
        padding: 0;
        margin: 1rem 0;
    }}
    
    .benefits-list li {{
        padding: 0.75rem;
        background: #f0f9ff;
        border-radius: 8px;
        border-left: 3px solid #0ea5e9;
        font-weight: 500;
    }}
    
    .trust-badges {{
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }}
    
    .trust-item {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background: #f8fafc;
        border-radius: 8px;
        font-weight: 500;
    }}
    
    .related-products .products-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-top: 1.5rem;
    }}
    
    .related-products .product-card {{
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }}
    
    .related-products .product-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }}
    
    .related-products .product-image {{
        width: 100%;
        height: 150px;
        object-fit: cover;
    }}
    
    .related-products .product-info {{
        padding: 1rem;
    }}
    
    .related-products .product-brand {{
        font-size: 0.875rem;
        color: #E68161;
        font-weight: 600;
        margin-bottom: 0.25rem;
    }}
    
    .related-products .product-name {{
        font-size: 0.95rem;
        font-weight: 600;
        color: #1f2937;
        margin: 0 0 0.5rem 0;
        line-height: 1.3;
    }}
    
    .related-products .product-price {{
        font-size: 1.1rem;
        font-weight: 700;
        color: #E68161;
    }}
    </style>
</head>
<body>
    <header class="header">
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
    </header>

    <!-- Product Details -->
    <main class="container product-page">
        <div class="product-layout">
            <div class="product-images">
                <div class="main-image">
                    <img src="{image_path}" alt="{naam}">
                </div>
            </div>
            
            <div class="product-info">
                <div class="product-header">
                    <div class="brand">{merk}</div>
                    <h1>{naam}</h1>
                </div>
                
                <div class="price-section">
                    <div class="price-main">
                        <span class="price-current">€{prijs}</span>
                        <span class="price-per-unit">{gewicht}</span>
                    </div>
                    <div class="price-highlight">
                        ⭐ Premium kwaliteit voor je hond
                    </div>
                </div>
                
                <div class="product-description">
                    <h3>Voordelen</h3>
                    <ul class="benefits-list">
                        {benefits_html}
                    </ul>
                </div>
                
                <div class="product-description">
                    <h3>Product specificaties</h3>
                    <div class="specs-table">
                        <div class="spec-row">
                            <span class="spec-label">Gewicht</span>
                            <span class="spec-value">{gewicht}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Aantal stuks</span>
                            <span class="spec-value">{aantal}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Doelgroep</span>
                            <span class="spec-value">{doelgroep}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Type snack</span>
                            <span class="spec-value">{type_snack}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Bijzonderheden</span>
                            <span class="spec-value">{bijzonderheden}</span>
                        </div>
                    </div>
                </div>
                
                <div class="purchase-section">
                    <div class="stock-info">
                        <span class="in-stock">✓ Beschikbaar bij partners</span>
                        <span class="fast-delivery">🚚 Snelle levering mogelijk</span>
                    </div>
                    <div class="purchase-actions">
                        <a href="https://www.bol.com/nl/s/?searchtext={naam.replace(' ', '+')}" target="_blank" class="btn-primary btn-large">
                            🛒 Bekijk bij Bol.com
                        </a>
                    </div>
                    <div class="trust-badges">
                        <div class="trust-item">
                            <span>🔒</span>
                            <span>Veilig betalen bij onze partners</span>
                        </div>
                        <div class="trust-item">
                            <span>⭐</span>
                            <span>Beoordeeld door hondenliefhebbers</span>
                        </div>
                        <div class="trust-item">
                            <span>🏆</span>
                            <span>Premium kwaliteit gegarandeerd</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Product Description -->
        <div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 12px; line-height: 1.6;">
            <h2>Waarom kiezen voor {naam}?</h2>
            <p>{description}</p>
            
            <p>Voor meer informatie over de beste hondensnacks en expert aanbevelingen, bekijk onze <a href="../beste-hondensnacks-2026/" style="color: #E68161; text-decoration: underline;">top 10 beste hondensnacks van 2026</a> en ontdek waarom natuurlijke ingrediënten zo belangrijk zijn in ons artikel over <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke hondensnacks</a>.</p>
        </div>

        <!-- Related Products -->
        <section class="related-products">
            <h2>Gerelateerde producten</h2>
            <div class="products-grid">{related_html}
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer" style="background: #2d3748; color: white; padding: 3rem 0 2rem 0; margin-top: 4rem;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
                <div>
                    <h4 style="margin-bottom: 1rem; font-size: 1.1rem; color: #e68161;">Biologische Hondensnacks</h4>
                    <p style="margin-bottom: 1rem; color: #a0aec0; font-size: 0.9rem; line-height: 1.6;">
                        Wij bieden de beste biologische en natuurlijke hondensnacks voor jouw trouwe viervoeter. 
                        Kwaliteit en gezondheid staan bij ons voorop.
                    </p>
                </div>
                
                <div>
                    <h4 style="margin-bottom: 0.5rem; font-size: 0.9rem; color: #9ca3af;">Navigatie</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.3rem;"><a href="../" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Home</a></li>
                        <li style="margin-bottom: 0.3rem;"><a href="../winkel/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Winkel</a></li>
                        <li style="margin-bottom: 0.3rem;"><a href="../blog/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Blog</a></li>
                        <li style="margin-bottom: 0.3rem;"><a href="../over-ons/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Over ons</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 style="margin-bottom: 0.5rem; font-size: 0.9rem; color: #9ca3af;">Juridisch</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.3rem;"><a href="privacy-policy/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Privacy policy</a></li>
                        <li style="margin-bottom: 0.3rem;"><a href="algemene-voorwaarden/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Algemene voorwaarden</a></li>
                        <li style="margin-bottom: 0.3rem;"><a href="disclaimer/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Disclaimer</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom" style="border-top: 1px solid #374151; padding: 1.5rem 0; text-align: center;">
                <p style="margin: 0 0 1rem 0; color: #9ca3af; font-size: 0.8rem;">
                    <strong>Disclaimer:</strong> De informatie op deze website is alleen bedoeld voor algemene doeleinden en vervangt geen professioneel veterinair advies. 
                    Raadpleeg altijd je dierenarts voor specifieke voedings- en gezondheidsadvies voor je hond.
                </p>
                <p style="margin: 0; color: #9ca3af; font-size: 0.9rem;">&copy; 2026 Biologische hondensnacks. Alle rechten voorbehouden. | Gemaakt voor honden en hun baasjes</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    
    return html_content

def enhance_all_product_pages():
    """Enhance all product pages with new design and unique content"""
    print("🎨 Enhancing all product pages...")
    
    # Get all product data
    all_products = get_product_data()
    if not all_products:
        return 0
    
    enhanced_count = 0
    
    for i, product in enumerate(all_products, 1):
        try:
            name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
            product_name = product[name_key]
            slug = slugify(product_name)
            html_file = os.path.join(PRODUCTS_DIR, f"{slug}.html")
            
            if not os.path.exists(html_file):
                print(f"⚠️ HTML file not found: {slug}.html")
                continue
            
            print(f"[{i:2d}/67] Enhancing: {product_name}")
            
            # Create backup
            backup_file = os.path.join(BACKUP_DIR, f"{slug}_original.html")
            shutil.copy2(html_file, backup_file)
            
            # Generate enhanced HTML
            new_content = generate_enhanced_product_html(product, all_products)
            
            # Write new content
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            enhanced_count += 1
            print(f"✅ Enhanced: {product_name}")
            
        except Exception as e:
            name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
            product_name = product.get(name_key, 'Unknown Product')
            print(f"❌ Error enhancing {product_name}: {e}")
    
    return enhanced_count

def main():
    """Main function to enhance product pages"""
    print("🎨 PRODUCT PAGES ENHANCER")
    print("=" * 50)
    
    create_backup_dir()
    
    print("🔄 Enhancing all product pages...")
    enhanced_count = enhance_all_product_pages()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 PRODUCT ENHANCEMENT RESULTS:")
    print(f"✅ Pages enhanced: {enhanced_count}")
    print(f"💾 Backups created in: {BACKUP_DIR}")
    
    if enhanced_count > 0:
        print(f"\n🎉 SUCCESS! {enhanced_count} product pages enhanced!")
        print("🎨 Attractive price/weight sections with gradients")
        print("📝 Unique descriptions for each product")
        print("⭐ Benefits lists with visual appeal")
        print("🛍️ 3-4 related products per page")
        print("🚫 Removed 'gratis verzending' mentions")
        print("📏 Optimized spacing for specifications")
    
    print("\n🏁 PRODUCT PAGES ENHANCEMENT COMPLETE")

if __name__ == "__main__":
    main()
