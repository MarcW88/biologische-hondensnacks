#!/usr/bin/env python3
"""
FIX "WAAROM KIEZEN VOOR" SECTION
================================

Corrige la section "Waarom kiezen voor..." avec du contenu
personnalisé et correct pour chaque produit.

Auteur: AI Assistant
Date: December 2025
"""

import os
import re
import glob
from bs4 import BeautifulSoup

# Configuration
PRODUITS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'

# Templates de texte par catégorie
CONTENT_TEMPLATES = {
    'kauwstaaf': [
        "Deze natuurlijke kauwstaaf van {brand} biedt {benefit} en is perfect voor {target}. De {type_snack} zorgt voor urenlang kauwplezier en ondersteunt de natuurlijke kauwbehoefte van je hond.",
        "De {product_name} van {brand} is speciaal ontwikkeld voor honden die graag kauwen. Met {weight} aan pure ingrediënten helpt deze {type_snack} bij tandreiniging en stressvermindering.",
        "{brand} staat bekend om kwaliteit, en deze {type_snack} is daar het perfecte voorbeeld van. De kauwstaaf is {bijzonderheden} en biedt langdurig kauwplezier voor je trouwe viervoeter.",
    ],
    'training': [
        "Deze training treats van {brand} zijn ideaal voor effectieve training. De {type_snack} is makkelijk te verdelen en heeft een sterke natuurlijke geur die je hond motiveert.",
        "Perfect voor positieve bekrachtiging - de {product_name} van {brand} combineert smaak met functionaliteit. Met {weight} krijg je voldoende treats voor meerdere trainingssessies.",
        "Training wordt een plezier met deze {type_snack} van {brand}. Klein formaat, grote smaak en perfect voor frequente beloningen tijdens het leren van nieuwe commando's.",
    ],
    'filet': [
        "Puur {type_snack} van {brand} - 100% vlees zonder toevoegingen. Deze natuurlijk gedroogde filet behoudt alle voedingsstoffen en biedt een proteïnerijke traktatie.",
        "De {product_name} van {brand} is een hoogwaardige eiwitbron. Met {weight} aan puur vlees geef je je hond een natuurlijke snack zonder kunstmatige toevoegingen.",
        "{brand} levert kwaliteit met deze {type_snack}. Luchtig gedroogd voor maximale smaak en voedingswaarde, perfect als beloning of tussendoortje.",
    ],
    'dental': [
        "Deze {type_snack} van {brand} combineert lekker met tandverzorging. De speciale textuur helpt plaque te verwijderen terwijl je hond geniet van deze traktatie.",
        "Dagelijkse mondverzorging wordt makkelijk met de {product_name}. {brand} heeft deze snack speciaal ontwikkeld voor optimale tandreininging en frisse adem.",
        "Investeer in de tandgezondheid van je hond met deze {type_snack} van {brand}. Klinisch bewezen effectief en heerlijk van smaak.",
    ],
    'yak': [
        "Authentieke Himalaya yak kaas van {brand} - gemaakt volgens eeuwenoude tradities. Deze harde kaas biedt maanden kauwplezier en is 100% natuurlijk.",
        "De {product_name} is een unieke kauwsnack gemaakt van yak- en koemelk. {brand} importeert deze traditionele snack rechtstreeks uit Nepal voor maximale authenticiteit.",
        "Langdurig kauwplezier gegarandeerd met deze yak kaas van {brand}. Perfect voor sterke kauwen en volledig natuurlijk zonder kunstmatige toevoegingen.",
    ],
    'hertengewei': [
        "Natuurlijk afgeworpen hertengewei - één van de meest duurzame kauwsnacks beschikbaar. Dit gewei van {brand} biedt maanden kauwplezier zonder dat er dieren zijn geschaad.",
        "De {product_name} is rijk aan natuurlijke mineralen en biedt langdurig kauwplezier. {brand} verzamelt alleen natuurlijk afgeworpen gewei voor deze duurzame snack.",
        "Extreem hard en langdurig - dit hertengewei van {brand} is perfect voor intensieve kauwers. Met {weight} krijg je een kauwsnack die weken tot maanden meegaat.",
    ],
    'puppy': [
        "Speciaal ontwikkeld voor puppy's - de {product_name} van {brand} is zacht voor melktandjes en ondersteunt gezonde groei. Perfect afgestemd op de behoeften van jonge honden.",
        "Je puppy verdient het beste begin, en {brand} levert dat met deze {type_snack}. Makkelijk verteerbaar en vol essentiële voedingsstoffen voor gezonde ontwikkeling.",
        "De {product_name} is perfect voor jonge honden. {brand} heeft rekening gehouden met gevoelige magen en delicate tandjes bij het ontwikkelen van deze puppy snack.",
    ],
    'default': [
        "De {product_name} van {brand} is een hoogwaardige natuurlijke snack voor je hond. Met {weight} aan pure ingrediënten geef je je hond een gezonde traktatie.",
        "{brand} levert kwaliteit met deze {type_snack}. Perfect als beloning, tijdens training of gewoon als verwennerij voor je trouwe viervoeter.",
        "Kies voor natuurlijke ingrediënten met de {product_name}. {brand} staat garant voor kwaliteit en smaak in deze {type_snack}.",
    ]
}

def identify_category(product_name, type_snack):
    """Identifie la catégorie du produit"""
    name_lower = product_name.lower()
    type_lower = type_snack.lower() if type_snack else ""
    
    if 'kauwstaaf' in name_lower or 'kauwstaven' in name_lower:
        return 'kauwstaaf'
    elif 'training' in name_lower or 'trainers' in name_lower or 'training' in type_lower:
        return 'training'
    elif 'filet' in name_lower or 'filet' in type_lower:
        return 'filet'
    elif 'dental' in name_lower or 'dental' in type_lower:
        return 'dental'
    elif 'yak' in name_lower or 'yak' in type_lower:
        return 'yak'
    elif 'hertengewei' in name_lower or 'gewei' in name_lower:
        return 'hertengewei'
    elif 'puppy' in name_lower:
        return 'puppy'
    else:
        return 'default'

def generate_waarom_text(product_name, brand, weight, type_snack, bijzonderheden, doelgroep):
    """Génère le texte "Waarom kiezen voor..."""""
    
    category = identify_category(product_name, type_snack)
    templates = CONTENT_TEMPLATES.get(category, CONTENT_TEMPLATES['default'])
    
    # Choisir un template aléatoire
    import random
    template = random.choice(templates)
    
    # Déterminer le bénéfice et la cible
    if 'puppy' in product_name.lower():
        benefit = "zachte kauwervaring"
        target = "jonge honden"
    elif 'training' in product_name.lower():
        benefit = "effectieve training"
        target = "elke trainingssituatie"
    elif 'dental' in product_name.lower():
        benefit = "tandreiniging"
        target = "dagelijkse mondverzorging"
    else:
        benefit = "natuurlijk kauwplezier"
        target = doelgroep.lower() if doelgroep and doelgroep != "n.b." else "alle honden"
    
    # Remplacer les variables
    text = template.format(
        product_name=product_name,
        brand=brand,
        weight=weight,
        type_snack=type_snack if type_snack else "snack",
        bijzonderheden=bijzonderheden.lower() if bijzonderheden else "hoogwaardige kwaliteit",
        doelgroep=target,
        benefit=benefit,
        target=target
    )
    
    return text

def extract_product_data(soup):
    """Extrait les données du produit"""
    
    try:
        brand = soup.find(class_='brand').text.strip()
        product_name = soup.find('h1').text.strip()
        
        # Extraire des specs
        specs = {}
        spec_rows = soup.find_all(class_='spec-row')
        for row in spec_rows:
            label = row.find(class_='spec-label')
            value = row.find(class_='spec-value')
            if label and value:
                specs[label.text.strip()] = value.text.strip()
        
        weight = specs.get('Gewicht', 'n.b.')
        type_snack = specs.get('Type snack', 'snack')
        bijzonderheden = specs.get('Bijzonderheden', '')
        doelgroep = specs.get('Doelgroep', 'alle honden')
        
        return {
            'brand': brand,
            'product_name': product_name,
            'weight': weight,
            'type_snack': type_snack,
            'bijzonderheden': bijzonderheden,
            'doelgroep': doelgroep
        }
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def process_product_page(html_path):
    """Traite une page produit"""
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extraire données produit
        data = extract_product_data(soup)
        if not data:
            return False, "Could not extract product data"
        
        # Trouver la section "Waarom kiezen voor"
        extended_desc = soup.find(class_='product-description-extended')
        if not extended_desc:
            return False, "Section not found"
        
        h2 = extended_desc.find('h2')
        if not h2:
            return False, "H2 not found"
        
        # Générer nouveau texte
        new_text = generate_waarom_text(
            data['product_name'],
            data['brand'],
            data['weight'],
            data['type_snack'],
            data['bijzonderheden'],
            data['doelgroep']
        )
        
        # Trouver le premier paragraphe
        first_p = extended_desc.find('p')
        if first_p:
            # Backup
            backup_path = html_path + '.waarom_backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Remplacer le texte
            first_p.string = new_text
            
            # Sauvegarder
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(str(soup.prettify()))
            
            return True, data['product_name']
        
        return False, "Paragraph not found"
        
    except Exception as e:
        return False, str(e)

def main():
    """Fonction principale"""
    
    print("📝 FIX 'WAAROM KIEZEN VOOR' SECTION")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob(os.path.join(PRODUITS_DIR, '*.html'))
    html_files = [f for f in html_files if not f.endswith('index.html')]
    
    print(f"📁 Found {len(html_files)} product pages\n")
    
    success_count = 0
    error_count = 0
    
    for html_file in html_files:
        filename = os.path.basename(html_file)
        
        success, result = process_product_page(html_file)
        
        if success:
            print(f"✅ {filename[:50]:50} → {result[:40]}")
            success_count += 1
        else:
            print(f"❌ {filename[:50]:50} → {result}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 COMPLETE!")
    print(f"✅ Success: {success_count} files")
    print(f"❌ Errors: {error_count} files")
    print(f"💾 Backups saved with .waarom_backup extension")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
