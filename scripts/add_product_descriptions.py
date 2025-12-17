#!/usr/bin/env python3
"""
SCRIPT AUTOMATISATION DESCRIPTIONS PRODUITS
Ajoute des descriptions détaillées uniques à tous les produits
"""

import os
import re
import glob
from pathlib import Path

# Configuration
PRODUITS_DIR = "/Users/marc/Desktop/biologische-hondensnacks/produits"
BACKUP_DIR = "/Users/marc/Desktop/biologische-hondensnacks/scripts/backups"

# Templates de descriptions par catégorie
DESCRIPTION_TEMPLATES = {
    'puppy': {
        'title_prefix': 'Waarom {product_name}?',
        'features': [
            ('🐣', 'Speciaal voor puppy\'s', 'Deze zachte snacks zijn speciaal ontwikkeld voor puppy\'s van 8 weken tot 12 maanden. De extra zachte textuur is perfect voor melktanden en de gevoelige spijsvertering van jonge honden.'),
            ('🧠', 'Ondersteunt hersenontwikkeling', 'Verrijkt met DHA en essentiële voedingsstoffen voor gezonde hersenontwikkeling. Plus toegevoegde vitaminen en mineralen die essentieel zijn tijdens de cruciale groeifase.'),
            ('💚', 'Gemakkelijk verteerbaar', 'De zachte textuur en beperkte ingrediëntenlijst maken deze snacks extra gemakkelijk verteerbaar voor gevoelige puppy magen.')
        ],
        'gradient_color': '#8b5cf6',
        'gradient_color_dark': '#7c3aed',
        'border_color': '#8b5cf6',
        'usage_title': 'Voedingsschema voor puppy\'s',
        'usage_items': [
            ('8-16 weken', '1-2 snacks per dag'),
            ('4-6 maanden', '2-4 snacks per dag'),
            ('6-12 maanden', '4-6 snacks per dag')
        ]
    },
    'training': {
        'title_prefix': 'Waarom {product_name}?',
        'features': [
            ('🎯', 'Perfect voor training', 'De kleine formaat maakt deze snacks ideaal voor frequente beloningen tijdens training. Zachte textuur zorgt voor snelle consumptie zonder afleiding.'),
            ('💪', 'Hoge motivatie waarde', 'Irresistible smaak die honden motiveerd houdt tijdens trainingsessies. Perfect voor positieve versterking en gedragstraining.'),
            ('⚡', 'Snelle beloning', 'Kleine bites die snel geconsumeerd worden, zodat de training vlot kan doorgaan zonder lange pauzes.')
        ],
        'gradient_color': '#E68161',
        'gradient_color_dark': '#d67347',
        'border_color': '#E68161',
        'usage_title': 'Trainingsadvies',
        'usage_items': [
            ('Basis training', '2-4 snacks per sessie'),
            ('Gevorderde training', '4-8 snacks per sessie'),
            ('Gedragstraining', '6-12 snacks per sessie')
        ]
    },
    'hypoallergenic': {
        'title_prefix': 'Waarom {product_name}?',
        'features': [
            ('🛡️', 'Hypoallergeen & veilig', 'Speciaal ontwikkeld voor honden met voedselallergieën en gevoelige magen. Bevat slechts één eiwitbron en is vrij van veelvoorkomende allergenen.'),
            ('🌱', 'Beperkte ingrediënten', 'Limited ingredient formula met alleen essentiële, natuurlijke ingrediënten. Geen granen, kunstmatige toevoegingen of veelvoorkomende allergenen.'),
            ('💚', 'Gemakkelijk verteerbaar', 'De zachte textuur en beperkte ingrediëntenlijst maken deze snacks extra gemakkelijk verteerbaar voor gevoelige magen.')
        ],
        'gradient_color': '#22c55e',
        'gradient_color_dark': '#16a34a',
        'border_color': '#22c55e',
        'usage_title': 'Geschikt voor honden met allergieën',
        'usage_items': [
            ('Vrij van', 'Granen, gluten, kunstmatige toevoegingen'),
            ('Ideaal bij', 'Voedselallergieën, gevoelige maag, huidproblemen'),
            ('Introductie tip', 'Geleidelijk invoeren over 7-10 dagen')
        ]
    },
    'dental': {
        'title_prefix': 'Waarom {product_name}?',
        'features': [
            ('🦷', 'Tandverzorging', 'Speciale textuur die helpt bij het verwijderen van tandplak en tandsteen tijdens het kauwen. Ondersteunt natuurlijke tandverzorging.'),
            ('🌿', 'Frisse adem', 'Natuurlijke ingrediënten zoals munt en peterselie helpen bij het neutraliseren van geurtjes en zorgen voor frisse adem.'),
            ('💪', 'Sterke kaken', 'Het kauwen op deze snacks helpt bij het versterken van de kauwspieren en ondersteunt gezonde tandvlees.')
        ],
        'gradient_color': '#06b6d4',
        'gradient_color_dark': '#0891b2',
        'border_color': '#06b6d4',
        'usage_title': 'Tandverzorging advies',
        'usage_items': [
            ('Dagelijks', '1-2 dental chews per dag'),
            ('Na maaltijden', 'Ideaal voor tandverzorging'),
            ('Combineer met', 'Regelmatig tandenpoetsen')
        ]
    },
    'senior': {
        'title_prefix': 'Waarom {product_name}?',
        'features': [
            ('👴', 'Speciaal voor senioren', 'Aangepaste formule voor honden van 7+ jaar. Zachte textuur die gemakkelijk te kauwen is voor oudere honden met gevoelige tanden.'),
            ('🦴', 'Gewrichtondersteuning', 'Verrijkt met glucosamine en chondroïtine voor gezonde gewrichten. Helpt bij het behouden van mobiliteit en flexibiliteit.'),
            ('❤️', 'Hart & vitaliteit', 'Aangepaste voedingsstoffen die het hart ondersteunen en de vitaliteit van oudere honden behouden.')
        ],
        'gradient_color': '#f59e0b',
        'gradient_color_dark': '#d97706',
        'border_color': '#f59e0b',
        'usage_title': 'Senior voedingsadvies',
        'usage_items': [
            ('7-10 jaar', '2-4 snacks per dag'),
            ('10+ jaar', '1-3 snacks per dag'),
            ('Gezondheid', 'Regelmatige controle bij dierenarts')
        ]
    },
    'default': {
        'title_prefix': 'Waarom {product_name}?',
        'features': [
            ('🌟', 'Premium kwaliteit', 'Hoogwaardige natuurlijke ingrediënten zonder kunstmatige toevoegingen. Zorgvuldig geselecteerd voor optimale smaak en voedingswaarde.'),
            ('🌱', 'Natuurlijke ingrediënten', '100% natuurlijke ingrediënten van duurzame bronnen. Geen kunstmatige kleurstoffen, conserveermiddelen of smaakversterkers.'),
            ('💝', 'Met liefde gemaakt', 'Elke snack wordt met zorg geproduceerd volgens de hoogste kwaliteitsstandaarden voor het welzijn van je hond.')
        ],
        'gradient_color': '#E68161',
        'gradient_color_dark': '#d67347',
        'border_color': '#E68161',
        'usage_title': 'Gebruiksadvies',
        'usage_items': [
            ('Dagelijks', '2-6 snacks afhankelijk van grootte'),
            ('Als beloning', 'Perfect voor training en verwennen'),
            ('Bewaring', 'Koel en droog bewaren')
        ]
    }
}

def detect_product_category(filename, content):
    """Detecteer de categorie van het product op basis van filename en content"""
    filename_lower = filename.lower()
    content_lower = content.lower()
    
    if 'puppy' in filename_lower or 'puppy' in content_lower:
        return 'puppy'
    elif 'training' in filename_lower or 'training' in content_lower:
        return 'training'
    elif 'hypoallergenic' in filename_lower or 'hypoallergeen' in content_lower:
        return 'hypoallergenic'
    elif 'dental' in filename_lower or 'dental' in content_lower:
        return 'dental'
    elif 'senior' in filename_lower or 'senior' in content_lower:
        return 'senior'
    else:
        return 'default'

def extract_product_info(content):
    """Extraheer product informatie uit de HTML content"""
    # Extract product name from title
    title_match = re.search(r'<title>([^|]+)', content)
    product_name = title_match.group(1).strip() if title_match else "Deze premium snacks"
    
    # Extract brand if available
    brand_match = re.search(r'<div class="product-brand">([^<]+)</div>', content)
    brand = brand_match.group(1).strip() if brand_match else ""
    
    return {
        'name': product_name,
        'brand': brand
    }

def generate_description_html(category, product_info):
    """Genereer de HTML voor de product beschrijving"""
    template = DESCRIPTION_TEMPLATES[category]
    product_name = product_info['name']
    brand = product_info['brand']
    
    # Generate features HTML
    features_html = ""
    for emoji, title, description in template['features']:
        features_html += f'''
            <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <h3 style="color: #E68161; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    <span>{emoji}</span> {title}
                </h3>
                <p style="color: #4a5568; line-height: 1.6;">
                    {description}
                </p>
            </div>'''
    
    # Generate usage items HTML
    usage_html = ""
    for label, description in template['usage_items']:
        usage_html += f'''
                <div style="padding: 1rem; background: #f3f4f6; border-radius: 8px;">
                    <strong style="color: {template['border_color']};">{label}:</strong><br>
                    <span style="color: #4a5568;">{description}</span>
                </div>'''
    
    # Generate full description HTML
    description_html = f'''
            <!-- Detailed Product Description -->
            <section class="detailed-description" style="background: #f8fafc; padding: 3rem 0; margin: 2rem 0;">
                <div class="container">
                    <div style="max-width: 1000px; margin: 0 auto;">
                        <h2 style="text-align: center; margin-bottom: 2rem; color: #2d3748; font-size: 1.8rem;">{template['title_prefix'].format(product_name=product_name)}</h2>
                        
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 3rem;">{features_html}
                        </div>
                        
                        <div style="background: linear-gradient(135deg, {template['gradient_color']} 0%, {template['gradient_color_dark']} 100%); color: white; padding: 2rem; border-radius: 12px; text-align: center;">
                            <h3 style="margin-bottom: 1rem; font-size: 1.3rem;">Ingrediënten & voedingswaarden</h3>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
                                <div>
                                    <h4 style="margin-bottom: 0.5rem; opacity: 0.9;">Hoofdingrediënten:</h4>
                                    <ul style="text-align: left; opacity: 0.9; line-height: 1.6;">
                                        <li>Natuurlijke eiwitbron (vlees/vis)</li>
                                        <li>Zoete aardappel of erwten</li>
                                        <li>Natuurlijke vezels</li>
                                        <li>Vitaminen en mineralen</li>
                                    </ul>
                                </div>
                                <div>
                                    <h4 style="margin-bottom: 0.5rem; opacity: 0.9;">Voedingswaarden per 100g:</h4>
                                    <ul style="text-align: left; opacity: 0.9; line-height: 1.6;">
                                        <li>Eiwit: 25-35%</li>
                                        <li>Vet: 8-16%</li>
                                        <li>Vezels: 2-5%</li>
                                        <li>Energie: 320-400 kcal</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <div style="margin-top: 2rem; text-align: center; background: white; padding: 2rem; border-radius: 12px; border: 2px solid {template['border_color']};">
                            <h3 style="color: #2d3748; margin-bottom: 1rem;">{template['usage_title']}</h3>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; text-align: left;">{usage_html}
                            </div>
                            <p style="margin-top: 1rem; color: #64748b; font-size: 0.9rem; font-style: italic;">
                                💡 Tip: Begin altijd met kleine hoeveelheden en bouw geleidelijk op. Zorg voor voldoende vers water.
                            </p>
                        </div>
                    </div>
                </div>
            </section>'''
    
    return description_html

def add_description_to_product(file_path):
    """Voeg beschrijving toe aan een product bestand"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if description already exists
        if '<!-- Detailed Product Description -->' in content:
            print(f"⚠️  Description already exists in {os.path.basename(file_path)}")
            return False
        
        # Find insertion point (before Related Products)
        related_products_pattern = r'(\s*<!-- Related Products -->)'
        if not re.search(related_products_pattern, content):
            print(f"❌ Could not find Related Products section in {os.path.basename(file_path)}")
            return False
        
        # Extract product info
        product_info = extract_product_info(content)
        
        # Detect category
        category = detect_product_category(os.path.basename(file_path), content)
        
        # Generate description
        description_html = generate_description_html(category, product_info)
        
        # Insert description
        new_content = re.sub(
            related_products_pattern,
            description_html + r'\n            \1',
            content
        )
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Added {category} description to {os.path.basename(file_path)}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(file_path)}: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 STARTING PRODUCT DESCRIPTIONS AUTOMATION")
    print("=" * 50)
    
    # Create backup directory
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    # Get all product HTML files
    product_files = glob.glob(os.path.join(PRODUITS_DIR, "*.html"))
    product_files = [f for f in product_files if not f.endswith('/index.html')]
    
    print(f"📁 Found {len(product_files)} product files")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for file_path in product_files:
        result = add_description_to_product(file_path)
        if result is True:
            success_count += 1
        elif result is False:
            skip_count += 1
        else:
            error_count += 1
    
    print("\n" + "=" * 50)
    print("📊 AUTOMATION RESULTS:")
    print(f"✅ Successfully processed: {success_count}")
    print(f"⚠️  Skipped (already exists): {skip_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📁 Total files: {len(product_files)}")
    
    if success_count > 0:
        print(f"\n🎉 Successfully added descriptions to {success_count} products!")
    
    print("\n🏁 AUTOMATION COMPLETE")

if __name__ == "__main__":
    main()
