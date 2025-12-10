#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - PRODUCT PAGES LAYOUT FIXER
=====================================================

Script om de HTML structuur van alle productpagina's te corrigeren
zodat ze correct werken met de CSS styling.

Functionaliteiten:
- Corrigeert HTML structuur voor alle productpagina's
- Gebruikt juiste CSS classes
- Behoudt productspecifieke informatie
- Creëert backup van originele bestanden

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import csv
import shutil
from pathlib import Path

# Configuration
CSV_FILE = '/Users/marc/Desktop/biologische-hondensnacks/Hondensnacks Catalogus (1).csv'
PRODUCTS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/layout_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')[:60]

def get_product_data():
    """Read product data from CSV"""
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            # Handle BOM
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

def generate_product_html_content(product_data):
    """Generate the corrected HTML content for a product"""
    # Handle BOM in CSV column names
    name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product_data else 'Product Naam'
    
    # Extract product data
    naam = product_data[name_key]
    merk = product_data['Merk/Verkoper']
    type_snack = product_data['Type Snack']
    gewicht = product_data['Gewicht/Inhoud']
    aantal = product_data['Aantal Stuks']
    doelgroep = product_data['Doelgroep']
    prijs = product_data['Prijs €']
    bijzonderheden = product_data['Bijzonderheden']
    
    # Generate slug for image path
    slug = slugify(naam)
    
    # Check if image exists
    image_path = f"../images/{naam}.jpg"
    if not os.path.exists(f"/Users/marc/Desktop/biologische-hondensnacks/images/{naam}.jpg"):
        # Fallback to generic image
        image_path = "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop"
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
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
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="../">
                        <img src="../images/logotype-primary-2.png" alt="Biologische Hondensnacks" style="height: 40px;">
                    </a>
                </div>
                <nav class="nav">
                    <a href="../natuurlijke-snacks/">Natuurlijke snacks</a>
                    <a href="../beste-2026/">Beste 2026</a>
                    <a href="../hondensnacks-voor-puppy/">Puppy snacks</a>
                    <a href="../blog/">Blog</a>
                    <a href="../over-ons/">Over ons</a>
                    <a href="../winkel/" class="nav-shop">Winkel</a>
                </nav>
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
                    </div>
                    <div class="price-per-unit">{gewicht}</div>
                </div>
                
                <div class="product-description">
                    <h3>Product details</h3>
                    <div class="specs-table">
                        <div class="spec-row">
                            <span class="spec-label">Gewicht:</span>
                            <span class="spec-value">{gewicht}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Aantal:</span>
                            <span class="spec-value">{aantal}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Doelgroep:</span>
                            <span class="spec-value">{doelgroep}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Type:</span>
                            <span class="spec-value">{type_snack}</span>
                        </div>
                        <div class="spec-row">
                            <span class="spec-label">Bijzonderheden:</span>
                            <span class="spec-value">{bijzonderheden}</span>
                        </div>
                    </div>
                </div>
                
                <div class="purchase-section">
                    <div class="stock-info">
                        <span class="in-stock">✓ Op voorraad</span>
                        <span class="fast-delivery">🚚 Snelle levering</span>
                    </div>
                    <div class="purchase-actions">
                        <a href="https://www.bol.com/nl/s/?searchtext={naam.replace(' ', '+')}" target="_blank" class="btn-primary btn-large">
                            🛒 Koop bij Bol.com
                        </a>
                    </div>
                    <div class="trust-badges">
                        <div class="trust-item">
                            <span>🔒</span>
                            <span>Veilig betalen</span>
                        </div>
                        <div class="trust-item">
                            <span>📦</span>
                            <span>Gratis verzending vanaf €20</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Product Description -->
        <div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 8px; line-height: 1.6;">
            <h2>Waarom kiezen voor {naam}?</h2>
            <p>Deze premium {type_snack.lower()} van {merk} is speciaal ontwikkeld voor honden die het beste verdienen. {bijzonderheden} maken dit product tot een uitstekende keuze voor je trouwe viervoeter.</p>
            
            <p>Met een gewicht van {gewicht} en geschikt voor {doelgroep.lower()}, biedt dit product de perfecte balans tussen smaak en voeding. Zoals we uitleggen in onze <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke hondensnacks gids</a>, is kwaliteit essentieel voor je hond's gezondheid.</p>
            
            <p>Voor meer informatie over de beste hondensnacks en expert aanbevelingen, bekijk onze <a href="../top-10-beste-hondensnacks-van-2026/" style="color: #E68161; text-decoration: underline;">top 10 beste hondensnacks van 2026</a> en ontdek waarom natuurlijke ingrediënten zo belangrijk zijn in ons artikel over <a href="../biologische-voeding/" style="color: #E68161; text-decoration: underline;">biologische voeding</a>.</p>
        </div>

        <!-- Related Products -->
        <section class="related-products">
            <h2>Gerelateerde producten</h2>
            <div class="products-grid">
                <div class="product-card">
                    <img src="{image_path}" alt="Andere snack">
                    <div class="product-info">
                        <h3>Andere premium snacks</h3>
                        <p>Ontdek meer natuurlijke snacks</p>
                        <a href="../winkel/" class="btn btn-secondary">Bekijk alle producten</a>
                    </div>
                </div>
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
</html>"""
    
    return html_content

def fix_product_page(product_data):
    """Fix the HTML structure for a single product page"""
    # Handle BOM in CSV column names
    name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product_data else 'Product Naam'
    
    product_name = product_data[name_key]
    slug = slugify(product_name)
    html_file = os.path.join(PRODUCTS_DIR, f"{slug}.html")
    
    if not os.path.exists(html_file):
        print(f"⚠️ HTML file not found: {slug}.html")
        return False
    
    # Create backup
    backup_file = os.path.join(BACKUP_DIR, f"{slug}_original.html")
    shutil.copy2(html_file, backup_file)
    
    # Generate new HTML content
    new_content = generate_product_html_content(product_data)
    
    # Write updated HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """Main function to fix all product pages"""
    print("🔧 PRODUCT PAGES LAYOUT FIXER")
    print("=" * 50)
    
    # Create backup directory
    create_backup_dir()
    
    # Get product data
    products = get_product_data()
    if not products:
        print("❌ No product data found!")
        return
    
    print(f"\n🔄 Fixing layout for {len(products)} product pages...")
    
    fixed_count = 0
    failed_count = 0
    
    for i, product in enumerate(products, 1):
        try:
            # Handle BOM in CSV column names
            name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
            product_name = product[name_key]
            
            print(f"[{i:2d}/67] Fixing: {product_name}")
            
            if fix_product_page(product):
                print(f"✅ Fixed layout for: {product_name}")
                fixed_count += 1
            else:
                print(f"❌ Failed to fix: {product_name}")
                failed_count += 1
                
        except Exception as e:
            name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
            product_name = product.get(name_key, 'Unknown Product')
            print(f"❌ Error fixing {product_name}: {e}")
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 LAYOUT FIX RESULTS:")
    print(f"✅ Successfully fixed: {fixed_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"💾 Backups created in: {BACKUP_DIR}")
    
    if fixed_count > 0:
        print(f"\n🎉 SUCCESS! {fixed_count} product pages now have correct layout!")
        print("🎨 All pages use proper CSS classes and structure")
        print("📱 Mobile responsive design implemented")
        print("🛍️ Professional e-commerce layout applied")
    
    print("\n🏁 PRODUCT PAGES LAYOUT FIX COMPLETE")

if __name__ == "__main__":
    main()
