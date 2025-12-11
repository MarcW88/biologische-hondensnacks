#!/usr/bin/env python3
"""
GENERATE UNIQUE PRODUCT DESCRIPTIONS
=====================================

Génère des descriptions de produits uniques et diversifiées
pour éviter le contenu dupliqué.

Auteur: AI Assistant
Date: December 2025
"""

import os
import re
import glob
from bs4 import BeautifulSoup
import random

# Configuration
PRODUITS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'

# Templates de descriptions par catégorie de produit
DESCRIPTION_TEMPLATES = {
    'kauwstaaf': {
        'intro': [
            "Deze kauwstaaf biedt langdurig kauwplezier en helpt bij tandreinigingsonderhoud.",
            "Een natuurlijke kauwstaaf die je hond urenlang bezig houdt en stress vermindert.",
            "Ideaal voor honden die graag kauwen - ondersteunt gezonde tanden en tandvlees.",
        ],
        'benefits': [
            ('🦷', 'Ondersteunt tandgezondheid', 'Helpt plaque en tandsteen te verwijderen tijdens het kauwen'),
            ('😌', 'Vermindert stress en verveling', 'Kauwactiviteit heeft een kalmerend effect'),
            ('💪', 'Versterkt kaakspieren', 'Natuurlijke workout voor kaakspieren'),
            ('🌱', '100% natuurlijk ingrediënt', 'Zonder kunstmatige toevoegingen of conserveermiddelen'),
            ('⏰', 'Langdurig kauwplezier', 'Houdt je hond urenlang tevreden bezig'),
        ]
    },
    'training': {
        'intro': [
            "Perfect voor effectieve training - kleine porties met grote smaak.",
            "Deze training treats zijn ideaal voor positieve bekrachtiging tijdens training.",
            "Ontwikkeld voor training: makkelijk te verdelen, sterke geur, onweerstaanbaar lekker.",
        ],
        'benefits': [
            ('🎯', 'Ideaal voor training', 'Kleine formaat perfect voor frequente beloningen'),
            ('👃', 'Sterke natuurlijke geur', 'Trekt aandacht en motiveert je hond'),
            ('✂️', 'Makkelijk te verdelen', 'Breek in kleinere stukjes voor maximale beloningen'),
            ('⚡', 'Snelle energie', 'Directe energieboost tijdens trainings-sessies'),
            ('🧠', 'Stimuleert leren', 'Positieve bekrachtiging voor effectief trainen'),
        ]
    },
    'kipfilet': {
        'intro': [
            "Puur kipfilet van hoogste kwaliteit - 100% vlees zonder toevoegingen.",
            "Deze gedroogde kipfilet is een proteïnerijke traktatie die elke hond adoreren.",
            "Natuurlijk gedroogd kipfilet: pure smaak, maximale voedingswaarde.",
        ],
        'benefits': [
            ('🍗', 'Puur kippenvlees', '100% kipfilet zonder bijproducten'),
            ('💪', 'Hoog eiwitgehalte', 'Ondersteunt spieropbouw en onderhoud'),
            ('🌡️', 'Luchtig gedroogd', 'Behoudt natuurlijke voedingsstoffen en smaak'),
            ('✅', 'Makkelijk verteerbaar', 'Zacht voor gevoelige magen'),
            ('🎁', 'Veelzijdig inzetbaar', 'Training, beloning of tussendoortje'),
        ]
    },
    'eend': {
        'intro': [
            "Eendenfilet is een hypoallergeen alternatief, perfect voor gevoelige honden.",
            "Deze eendensnack is rijk aan essentiële vetzuren voor een gezonde vacht.",
            "Natuurlijke eendensnack - lekker, voedzaam en zacht voor de maag.",
        ],
        'benefits': [
            ('🦆', 'Hypoallergeen eiwit', 'Ideaal voor honden met voedselallergie'),
            ('✨', 'Gezonde vacht', 'Rijk aan omega-3 en omega-6 vetzuren'),
            ('🌿', 'Natuurlijk product', 'Geen kunstmatige kleurstoffen of smaakversterkers'),
            ('❤️', 'Hartvriendelijk', 'Ondersteunt cardiovasculaire gezondheid'),
            ('🍽️', 'Smakelijk', 'Zelfs kieskeurige honden vinden dit onweerstaanbaar'),
        ]
    },
    'rund': {
        'intro': [
            "Rundvlees is een uitstekende bron van ijzer en essentiële aminozuren.",
            "Deze rundersnack combineert smaak met voedingswaarde voor optimale gezondheid.",
            "Natuurlijk rundvlees - rijk aan proteïnen en perfect voor actieve honden.",
        ],
        'benefits': [
            ('🥩', 'Premium rundvlees', 'Hoogwaardige eiwitbron voor je hond'),
            ('⚡', 'Extra energie', 'Ideaal voor actieve en sportieve honden'),
            ('🔴', 'IJzerrijk', 'Ondersteunt bloedaanmaak en energieniveau'),
            ('💪', 'Spieronderhoud', 'Aminozuren voor sterke spieren'),
            ('😋', 'Intense smaak', 'Natuurlijke rundersmaak waar honden gek op zijn'),
        ]
    },
    'puppy': {
        'intro': [
            "Speciaal ontwikkeld voor puppy's met delicate tandjes en gevoelige magen.",
            "Deze puppy snacks ondersteunen gezonde groei en ontwikkeling.",
            "Perfect voor jonge honden - zacht, voedzaam en makkelijk verteerbaar.",
        ],
        'benefits': [
            ('🐕', 'Puppy-vriendelijk', 'Aangepast aan de behoeften van groeiende honden'),
            ('🦷', 'Zacht voor melktandjes', 'Geschikt formaat en hardheid voor puppy\'s'),
            ('📈', 'Ondersteunt groei', 'Optimale voedingsstoffen voor ontwikkeling'),
            ('🧠', 'Hersenfunctie', 'DHA voor gezonde hersenontwikkeling'),
            ('❤️', 'Makkelijk verteerbaar', 'Zacht voor jonge spijsverteringssysteem'),
        ]
    },
    'dental': {
        'intro': [
            "Deze dental snack combineert lekker met tandreiniging voor een gezond gebit.",
            "Speciaal ontworpen textuur helpt plaque te verwijderen tijdens het kauwen.",
            "Dagelijkse tandverzorging in de vorm van een lekkere traktatie.",
        ],
        'benefits': [
            ('🦷', 'Tandreinigend effect', 'Vermindert plaque en tandsteen opbouw'),
            ('💨', 'Frisse adem', 'Natuurlijke ingrediënten voor betere mondgeur'),
            ('🔬', 'Klinisch getest', 'Bewezen effectief voor mondhygiëne'),
            ('😁', 'Gezond tandvlees', 'Ondersteunt tandvlees gezondheid'),
            ('🎯', 'Dagelijks gebruik', 'Voor optimale resultaten elke dag geven'),
        ]
    },
    'konijn': {
        'intro': [
            "Konijnenvlees is een magere, hypoallergene eiwitbron perfect voor dieetbewuste baasjes.",
            "Deze konijnensnack is zacht voor de maag en rijk aan essentiële voedingsstoffen.",
            "Natuurlijk konijn - nieuw eiwit ideaal voor eliminatiediëten.",
        ],
        'benefits': [
            ('🐰', 'Nieuw eiwit', 'Uitstekend voor eliminatiediëten en allergieën'),
            ('💚', 'Mager vlees', 'Laag in vet, ideaal voor gewichtsbeheersing'),
            ('✅', 'Hoge verteerbaarheid', 'Zacht voor gevoelige magen'),
            ('🌿', 'Natuurlijk product', '100% konijnenvlees zonder vullers'),
            ('❤️', 'Hypoallergeen', 'Minimaal risico op allergische reacties'),
        ]
    },
    'hertengewei': {
        'intro': [
            "Natuurlijk afgeworpen hertengewei - duurzaam en langdurig kauwplezier.",
            "Dit hertengewei biedt maanden kauwplezier en is volledig natuurlijk.",
            "Eén van de meest duurzame kauwsnacks - gevallen gewei, geen dieren geschaad.",
        ],
        'benefits': [
            ('🦌', 'Natuurlijk gewei', 'Afgeworpen door wilde herten, geen dieren geschaad'),
            ('⏰', 'Extreem lang houdbaar', 'Maanden kauwplezier uit één stuk'),
            ('🦴', 'Rijk aan mineralen', 'Calcium, fosfor en andere essentiële mineralen'),
            ('🌍', '100% duurzaam', 'Ecologisch verantwoorde keuze'),
            ('💪', 'Extra hard', 'Perfect voor sterke kauwen'),
        ]
    },
    'yak': {
        'intro': [
            "Yak kaas uit de Himalaya - een traditionele, langdurige kauwsnack.",
            "Deze yak kaas is gemaakt volgens eeuwenoude recepten en 100% natuurlijk.",
            "Harde kaas van yak- en koemelk, perfect voor intensieve kauwers.",
        ],
        'benefits': [
            ('🏔️', 'Himalaya traditie', 'Gemaakt volgens eeuwenoude Nepalese recepten'),
            ('🧀', 'Natuurlijke kaas', 'Van yak- en koemelk zonder toevoegingen'),
            ('⏱️', 'Langdurig', 'Houdt zelfs sterke kauwers lang bezig'),
            ('💪', 'Eiwitrijk', 'Hoogwaardige melkeiwitten voor spieronderhoud'),
            ('🌱', 'Glutenvrij', 'Geschikt voor honden met graanallergieën'),
        ]
    },
    'vissnack': {
        'intro': [
            "Vis is rijk aan omega-3 vetzuren voor een glanzende vacht en gezonde huid.",
            "Deze vissnack combineert lekker met maximale voedingswaarde.",
            "Natuurlijke vissnack - perfect voor honden die van vis houden.",
        ],
        'benefits': [
            ('🐟', 'Omega-3 rijk', 'EPA en DHA voor gezonde huid en vacht'),
            ('✨', 'Glanzende vacht', 'Zichtbaar resultaat na regelmatig gebruik'),
            ('🧠', 'Ondersteunt hersenen', 'Omega-3 voor cognitieve functie'),
            ('❤️', 'Hart gezondheid', 'Ondersteunt cardiovasculair systeem'),
            ('🌿', 'Natuurlijk product', 'Puur vis zonder kunstmatige toevoegingen'),
        ]
    },
}

def identify_product_category(product_name, brand):
    """Identifie la catégorie du produit"""
    name_lower = product_name.lower()
    
    if 'kauwstaaf' in name_lower or 'kauwstaven' in name_lower:
        return 'kauwstaaf'
    elif 'training' in name_lower or 'trainers' in name_lower:
        return 'training'
    elif 'kipfilet' in name_lower or 'kip' in name_lower and 'filet' in name_lower:
        return 'kipfilet'
    elif 'eend' in name_lower or 'duck' in name_lower:
        return 'eend'
    elif 'rund' in name_lower or 'beef' in name_lower:
        return 'rund'
    elif 'puppy' in name_lower:
        return 'puppy'
    elif 'dental' in name_lower or 'tand' in name_lower:
        return 'dental'
    elif 'konijn' in name_lower or 'rabbit' in name_lower:
        return 'konijn'
    elif 'hertengewei' in name_lower or 'gewei' in name_lower:
        return 'hertengewei'
    elif 'yak' in name_lower:
        return 'yak'
    elif 'vis' in name_lower or 'spiering' in name_lower or 'fish' in name_lower:
        return 'vissnack'
    else:
        return 'kauwstaaf'  # default

def generate_unique_description(product_name, brand, category):
    """Génère une description unique pour le produit"""
    
    template = DESCRIPTION_TEMPLATES.get(category, DESCRIPTION_TEMPLATES['kauwstaaf'])
    
    # Intro aléatoire
    intro = random.choice(template['intro'])
    
    # Sélectionner 4-5 bénéfices aléatoires
    num_benefits = random.randint(4, 5)
    selected_benefits = random.sample(template['benefits'], num_benefits)
    
    # Construire le HTML
    html = f'''                <div class="product-description">
                    <h3>Over dit product</h3>
                    <p style="margin-bottom: 1.5rem; line-height: 1.6; color: #4a5568;">
                        {intro}
                    </p>
                    
                    <h3>Voordelen</h3>
                    <ul class="benefits-list" style="list-style: none; padding: 0;">
'''
    
    for emoji, title, desc in selected_benefits:
        html += f'''                        <li style="margin-bottom: 0.75rem; padding-left: 0;">
                            <strong style="color: #2d3748;">{emoji} {title}</strong>
                            <p style="margin: 0.25rem 0 0 1.5rem; color: #6b7280; font-size: 0.9rem;">{desc}</p>
                        </li>
'''
    
    html += '''                    </ul>
                </div>'''
    
    return html

def process_product_page(html_path):
    """Traite une page produit"""
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extraire infos produit
        brand_elem = soup.find(class_='brand')
        h1_elem = soup.find('h1')
        
        if not brand_elem or not h1_elem:
            return False, "Missing brand or title"
        
        brand = brand_elem.text.strip()
        product_name = h1_elem.text.strip()
        
        # Identifier catégorie
        category = identify_product_category(product_name, brand)
        
        # Générer nouvelle description
        new_description = generate_unique_description(product_name, brand, category)
        
        # Trouver et remplacer la section description
        desc_section = soup.find(class_='product-description')
        if desc_section:
            # Backup
            backup_path = html_path + '.desc_backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Remplacer
            new_desc_soup = BeautifulSoup(new_description, 'html.parser')
            desc_section.replace_with(new_desc_soup)
            
            # Sauvegarder
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(str(soup.prettify()))
            
            return True, category
        
        return False, "Description section not found"
        
    except Exception as e:
        return False, str(e)

def main():
    """Fonction principale"""
    
    print("📝 GENERATE UNIQUE PRODUCT DESCRIPTIONS")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob(os.path.join(PRODUITS_DIR, '*.html'))
    
    print(f"📁 Found {len(html_files)} product pages\n")
    
    success_count = 0
    error_count = 0
    categories_count = {}
    
    for html_file in html_files:
        filename = os.path.basename(html_file)
        
        success, result = process_product_page(html_file)
        
        if success:
            category = result
            categories_count[category] = categories_count.get(category, 0) + 1
            print(f"✅ {filename[:50]:50} → {category}")
            success_count += 1
        else:
            print(f"❌ {filename[:50]:50} → {result}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 COMPLETE!")
    print(f"✅ Success: {success_count} files")
    print(f"❌ Errors: {error_count} files")
    print(f"\n📊 Categories breakdown:")
    for cat, count in sorted(categories_count.items(), key=lambda x: x[1], reverse=True):
        print(f"   {cat:15} : {count} products")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
