#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - UNIQUE DESCRIPTIONS GENERATOR
========================================================

Script om unieke, SEO-geoptimaliseerde productbeschrijvingen te genereren
voor alle 67 producten op basis van hun specifieke eigenschappen.

Functionaliteiten:
- Analyseert CSV data voor unieke kenmerken
- Genereert gepersonaliseerde beschrijvingen per product
- Gebruikt templates gebaseerd op type snack en eigenschappen
- Integreert SEO keywords natuurlijk
- Creëert variatie om duplicatie te vermijden
- Update alle product HTML pagina's

Auteur: AI Assistant
Datum: December 2025
"""

import csv
import os
import re
import random
from pathlib import Path

# Configuration
CSV_FILE = '/Users/marc/Desktop/biologische-hondensnacks/Hondensnacks Catalogus (1).csv'
PRODUCTS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/descriptions'

# Description templates per product type
DESCRIPTION_TEMPLATES = {
    'yak_kaas': [
        "Ontdek de {naam} van {merk}, een premium {type_snack} van {gewicht} die perfect is voor {doelgroep_text}. Deze {bijzonderheden_text} kauwsnack biedt langdurig kauwplezier en ondersteunt de tandgezondheid van je hond. {size_text} {special_features}",
        
        "De {naam} van {merk} is een authentieke {type_snack} van {gewicht} die {doelgroep_text} veel kauwplezier biedt. {bijzonderheden_text}, deze natuurlijke snack is perfect voor honden die van intensief kauwen houden. {size_text} {special_features}",
        
        "Geef je hond het beste met de {naam} van {merk}. Deze {type_snack} van {gewicht} is speciaal ontwikkeld voor {doelgroep_text} en biedt {bijzonderheden_text} kwaliteit. Een ideale keuze voor langdurig kauwplezier. {size_text} {special_features}"
    ],
    
    'vlees_filet': [
        "De {naam} van {merk} is een premium {type_snack} van {gewicht} die {doelgroep_text} een smaakvolle en gezonde traktatie biedt. {bijzonderheden_text}, deze gedroogde lekkernij is rijk aan proteïnen en perfect als beloning. {special_features}",
        
        "Verwén je hond met de {naam} van {merk}, een heerlijke {type_snack} van {gewicht}. Speciaal geschikt voor {doelgroep_text}, deze {bijzonderheden_text} snack is een natuurlijke bron van proteïnen en smaakt geweldig. {special_features}",
        
        "Kies voor kwaliteit met de {naam} van {merk}. Deze {type_snack} van {gewicht} is perfect voor {doelgroep_text} en biedt {bijzonderheden_text} voeding. Een gezonde en smakelijke traktatie die je hond zal waarderen. {special_features}"
    ],
    
    'trainers': [
        "De {naam} van {merk} zijn premium {type_snack} van {gewicht} die ideaal zijn voor {doelgroep_text}. Deze {bijzonderheden_text} trainingssnacks zijn perfect voor het aanleren van nieuwe commando's en het belonen van goed gedrag. {special_features}",
        
        "Train je hond effectief met de {naam} van {merk}. Deze {type_snack} van {gewicht} zijn speciaal ontwikkeld voor {doelgroep_text} en bieden {bijzonderheden_text} kwaliteit. Ideaal voor dagelijkse training en positieve versterking. {special_features}",
        
        "Maak training een plezier met de {naam} van {merk}. Deze {type_snack} van {gewicht} zijn perfect voor {doelgroep_text} en combineren {bijzonderheden_text} ingrediënten met een onweerstaanbare smaak. {special_features}"
    ],
    
    'zachte_snacks': [
        "De {naam} van {merk} zijn zachte {type_snack} van {gewicht} die perfect zijn voor {doelgroep_text}. Deze {bijzonderheden_text} lekkernijen zijn gemakkelijk te kauwen en ideaal voor training of als dagelijkse traktatie. {special_features}",
        
        "Geniet van de {naam} van {merk}, zachte {type_snack} van {gewicht} die {doelgroep_text} zullen bekoren. {bijzonderheden_text}, deze snacks zijn perfect voor honden die van zachte texturen houden. {special_features}",
        
        "Kies voor de {naam} van {merk}, premium zachte {type_snack} van {gewicht}. Speciaal geschikt voor {doelgroep_text}, deze {bijzonderheden_text} traktaties zijn zowel lekker als gezond. {special_features}"
    ],
    
    'sticks_gedraaid': [
        "De {naam} van {merk} zijn premium {type_snack} van {aantal} stuks die perfect zijn voor {doelgroep_text}. Deze {bijzonderheden_text} gedraaide sticks bieden langdurig kauwplezier en zijn een gezonde keuze voor je hond. {special_features}",
        
        "Ontdek de {naam} van {merk}, {type_snack} in een verpakking van {aantal} stuks. Ideaal voor {doelgroep_text}, deze {bijzonderheden_text} sticks combineren smaak met gezondheid. {special_features}",
        
        "Verwén je hond met de {naam} van {merk}. Deze {type_snack} van {aantal} stuks zijn speciaal ontwikkeld voor {doelgroep_text} en bieden {bijzonderheden_text} kwaliteit in elke hap. {special_features}"
    ],
    
    'assortiment': [
        "Het {naam} van {merk} is een gevarieerd {type_snack} van {gewicht} dat perfect is voor {doelgroep_text}. Deze {bijzonderheden_text} mix biedt verschillende smaken en texturen voor optimale afwisseling. {special_features}",
        
        "Verras je hond met het {naam} van {merk}, een rijk {type_snack} van {gewicht}. Speciaal samengesteld voor {doelgroep_text}, dit pakket biedt {bijzonderheden_text} variatie en kwaliteit. {special_features}",
        
        "Kies voor diversiteit met het {naam} van {merk}. Dit {type_snack} van {gewicht} is ideaal voor {doelgroep_text} en combineert {bijzonderheden_text} ingrediënten in één praktische verpakking. {special_features}"
    ],
    
    'default': [
        "De {naam} van {merk} is een premium {type_snack} van {gewicht} die perfect is voor {doelgroep_text}. Deze {bijzonderheden_text} hondensnack biedt uitstekende kwaliteit en smaak die je hond zal waarderen. {special_features}",
        
        "Ontdek de {naam} van {merk}, een hoogwaardige {type_snack} van {gewicht}. Speciaal ontwikkeld voor {doelgroep_text}, deze {bijzonderheden_text} traktatie is een perfecte keuze voor je trouwe viervoeter. {special_features}",
        
        "Geef je hond het beste met de {naam} van {merk}. Deze {type_snack} van {gewicht} is ideaal voor {doelgroep_text} en biedt {bijzonderheden_text} kwaliteit in elke hap. {special_features}"
    ]
}

# Special features based on characteristics
SPECIAL_FEATURES = {
    'natuurlijk': "Gemaakt van 100% natuurlijke ingrediënten zonder kunstmatige toevoegingen.",
    'hypoallergeen': "Hypoallergeen en geschikt voor honden met voedselgevoeligheden.",
    'belgisch': "Geproduceerd in België volgens de hoogste kwaliteitsnormen.",
    'supplement': "Bevat waardevolle supplementen voor optimale gezondheid.",
    'training': "Speciaal geformuleerd voor effectieve training en positieve versterking.",
    'bestseller': "Een populaire keuze onder hondenliefhebbers wereldwijd.",
    'himalaya': "Gebaseerd op traditionele Himalaya recepten.",
    'premium': "Premium kwaliteit voor de meest veeleisende honden.",
    'proteïne': "Rijk aan hoogwaardige proteïnen voor spierontwikkeling.",
    'tandgezondheid': "Ondersteunt de tandgezondheid door natuurlijke reiniging.",
    'digestie': "Bevordert een gezonde spijsvertering.",
    'energie': "Biedt langdurige energie voor actieve honden."
}

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

def determine_product_type(type_snack, product_name):
    """Determine the product category for template selection"""
    type_lower = type_snack.lower()
    name_lower = product_name.lower()
    
    if 'yak' in type_lower or 'kaas' in type_lower or 'baton' in type_lower:
        return 'yak_kaas'
    elif 'filet' in type_lower or 'eend' in type_lower or 'vlees' in type_lower:
        return 'vlees_filet'
    elif 'trainer' in type_lower or 'training' in name_lower:
        return 'trainers'
    elif 'zachte' in type_lower or 'softies' in name_lower:
        return 'zachte_snacks'
    elif 'stick' in type_lower or 'gedraaid' in type_lower:
        return 'sticks_gedraaid'
    elif 'assortiment' in type_lower or 'pakket' in name_lower or 'mix' in type_lower:
        return 'assortiment'
    else:
        return 'default'

def process_target_group(doelgroep):
    """Convert target group to readable text"""
    doelgroep_lower = doelgroep.lower()
    
    if 'junior' in doelgroep_lower or '1-2 jaar' in doelgroep_lower:
        return 'jonge honden en puppy\'s'
    elif 'elke levensfase' in doelgroep_lower or 'alle' in doelgroep_lower:
        return 'honden van alle leeftijden'
    elif 'senior' in doelgroep_lower:
        return 'oudere honden'
    elif 'adult' in doelgroep_lower:
        return 'volwassen honden'
    else:
        return 'alle honden'

def process_features(bijzonderheden):
    """Extract and process special features"""
    if not bijzonderheden or bijzonderheden.lower() == 'n.b.':
        return 'hoogwaardige', []
    
    features_text = bijzonderheden.lower()
    special_features = []
    
    # Map features to descriptions
    feature_mapping = {
        'natuurlijk': 'natuurlijke',
        'hypoallergeen': 'hypoallergene',
        'belgisch': 'Belgische',
        'supplement': 'voedingssupplement',
        'training': 'trainings',
        'bestseller': 'populaire',
        'himalaya': 'traditionele Himalaya',
        'premium': 'premium',
        'reviews' in features_text: 'veelgeprezen'
    }
    
    description_parts = []
    for key, desc in feature_mapping.items():
        if key in features_text:
            description_parts.append(desc)
            if key in SPECIAL_FEATURES:
                special_features.append(SPECIAL_FEATURES[key])
    
    if not description_parts:
        description_parts = ['hoogwaardige']
    
    return ', '.join(description_parts[:2]), special_features

def determine_size_text(product_name, gewicht, aantal):
    """Generate size-specific text"""
    name_lower = product_name.lower()
    
    if 'small' in name_lower or '<5 kg' in name_lower:
        return "Perfect voor kleine honden tot 5kg."
    elif 'medium' in name_lower or '5-10kg' in name_lower:
        return "Ideaal voor middelgrote honden van 5-10kg."
    elif 'large' in name_lower or '10-20kg' in name_lower:
        return "Geschikt voor grote honden van 10-20kg."
    elif 'extra large' in name_lower or '20+' in name_lower:
        return "Speciaal ontwikkeld voor zeer grote honden boven 20kg."
    elif aantal and aantal != '1' and aantal != 'n.b.':
        return f"Geleverd in een praktische verpakking van {aantal} stuks."
    elif gewicht and 'g' in gewicht:
        return f"In een handige {gewicht} verpakking."
    else:
        return "In de perfecte portiegrootte."

def generate_unique_description(product_data):
    """Generate a unique description for a product"""
    # Handle BOM in CSV column names
    name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product_data else 'Product Naam'
    
    # Extract product data
    naam = product_data[name_key]
    merk = product_data['Merk/Verkoper']
    type_snack = product_data['Type Snack']
    gewicht = product_data['Gewicht/Inhoud']
    aantal = product_data['Aantal Stuks']
    doelgroep = product_data['Doelgroep']
    bijzonderheden = product_data['Bijzonderheden']
    
    # Process data
    product_type = determine_product_type(type_snack, naam)
    doelgroep_text = process_target_group(doelgroep)
    bijzonderheden_text, special_features_list = process_features(bijzonderheden)
    size_text = determine_size_text(naam, gewicht, aantal)
    
    # Select random template
    templates = DESCRIPTION_TEMPLATES[product_type]
    template = random.choice(templates)
    
    # Combine special features
    special_features = ' '.join(special_features_list[:2])  # Max 2 features
    
    # Format the description
    description = template.format(
        naam=naam,
        merk=merk,
        type_snack=type_snack.lower(),
        gewicht=gewicht if gewicht != 'n.b.' else 'optimale portie',
        aantal=aantal if aantal != 'n.b.' else '',
        doelgroep_text=doelgroep_text,
        bijzonderheden_text=bijzonderheden_text,
        size_text=size_text,
        special_features=special_features
    )
    
    # Clean up description
    description = re.sub(r'\s+', ' ', description)  # Remove extra spaces
    description = description.strip()
    
    return description

def update_product_html(product_data, description):
    """Update the HTML file with the new description"""
    # Handle BOM in CSV column names
    name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product_data else 'Product Naam'
    
    product_name = product_data[name_key]
    slug = slugify(product_name)
    html_file = os.path.join(PRODUCTS_DIR, f"{slug}.html")
    
    if not os.path.exists(html_file):
        print(f"⚠️ HTML file not found: {slug}.html")
        return False
    
    # Read current HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_file = os.path.join(BACKUP_DIR, f"{slug}_original.html")
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Find and replace the description
    # Look for the product description section
    description_pattern = r'(<div class="product-description">)(.*?)(</div>)'
    
    if re.search(description_pattern, content, re.DOTALL):
        new_content = re.sub(
            description_pattern,
            f'\\1\n                <p>{description}</p>\n            \\3',
            content,
            flags=re.DOTALL
        )
    else:
        # If no description div found, look for a place to insert it
        # This is a fallback - we'll add it after the product title
        title_pattern = r'(<h1 class="product-title">.*?</h1>)'
        if re.search(title_pattern, content, re.DOTALL):
            new_content = re.sub(
                title_pattern,
                f'\\1\n            <div class="product-description">\n                <p>{description}</p>\n            </div>',
                content,
                flags=re.DOTALL
            )
        else:
            print(f"⚠️ Could not find suitable place to insert description in {slug}.html")
            return False
    
    # Write updated HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """Main function to generate unique descriptions"""
    print("🎨 UNIQUE DESCRIPTIONS GENERATOR")
    print("=" * 50)
    
    # Create backup directory
    create_backup_dir()
    
    # Read CSV data
    print(f"📖 Reading product data from {CSV_FILE}")
    
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            # Handle BOM
            content = f.read()
            if content.startswith('\ufeff'):
                content = content[1:]
            
            reader = csv.DictReader(content.splitlines(), delimiter=';')
            products = list(reader)
        
        print(f"✅ Loaded {len(products)} products from CSV")
        
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return
    
    # Generate descriptions
    print("\n🎨 Generating unique descriptions...")
    
    updated_count = 0
    failed_count = 0
    
    for i, product in enumerate(products, 1):
        try:
            # Handle BOM in CSV column names
            name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
            product_name = product[name_key]
            
            print(f"\n📝 [{i:2d}/67] Processing: {product_name}")
            
            # Generate unique description
            description = generate_unique_description(product)
            print(f"📄 Generated description ({len(description)} chars)")
            
            # Update HTML file
            if update_product_html(product, description):
                print(f"✅ Updated HTML file")
                updated_count += 1
            else:
                print(f"❌ Failed to update HTML file")
                failed_count += 1
                
        except Exception as e:
            name_key = '\ufeffProduct Naam' if '\ufeffProduct Naam' in product else 'Product Naam'
            product_name = product.get(name_key, 'Unknown Product')
            print(f"❌ Error processing {product_name}: {e}")
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 UNIQUE DESCRIPTIONS GENERATION RESULTS:")
    print(f"✅ Successfully updated: {updated_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"📁 Backups created in: {BACKUP_DIR}")
    
    if updated_count > 0:
        print(f"\n🎉 SUCCESS! {updated_count} product pages now have unique descriptions!")
        print("🔍 Each description is tailored to the product's specific characteristics")
        print("📈 This will improve SEO and user experience significantly")
    
    print("\n🏁 UNIQUE DESCRIPTIONS GENERATION COMPLETE")

if __name__ == "__main__":
    main()
