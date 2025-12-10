#!/usr/bin/env python3
"""
SCRIPT RÉÉCRITURE DESCRIPTIONS PRODUITS
Remplace les descriptions complexes par du texte continu 150-250 mots avec maillage interne
"""

import os
import re
import glob
from pathlib import Path

# Configuration
PRODUITS_DIR = "/Users/marc/Desktop/biologische-hondensnacks/produits"
BACKUP_DIR = "/Users/marc/Desktop/biologische-hondensnacks/scripts/backups"

# Templates de descriptions par catégorie avec maillage interne
DESCRIPTION_TEMPLATES = {
    'puppy': """
<div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 8px; line-height: 1.6;">
    <h2>Waarom {product_name} perfect is voor je puppy</h2>
    <p>Deze zachte puppy snacks zijn speciaal ontwikkeld voor jonge honden van 8 weken tot 12 maanden. De extra zachte textuur is ideaal voor melktanden en de gevoelige spijsvertering van puppy's. Net zoals we uitleggen in onze <a href="../hondensnacks-voor-puppy/" style="color: #E68161; text-decoration: underline;">complete gids voor puppy snacks</a>, is het belangrijk om snacks te kiezen die de hersenontwikkeling ondersteunen.</p>
    
    <p>Deze premium snacks bevatten essentiële voedingsstoffen zoals DHA voor gezonde hersenontwikkeling en zijn gemakkelijk verteerbaar. De kleine formaat maakt ze perfect voor training en beloning tijdens de cruciale socialisatiefase. Zoals beschreven in onze <a href="../blog/hondensnacks-voor-puppys-complete-gids/" style="color: #E68161; text-decoration: underline;">puppy voeding expert gids</a>, hebben jonge honden andere voedingsbehoeften dan volwassen honden.</p>
    
    <p>Voor de beste resultaten combineer je deze snacks met een gevarieerd dieet van <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke hondensnacks</a>. Ontdek meer over de voordelen van biologische voeding in ons artikel over <a href="../blog/waarom-biologische-snacks-beter-zijn/" style="color: #E68161; text-decoration: underline;">waarom biologische snacks beter zijn</a> voor je puppy's gezondheid en ontwikkeling.</p>
</div>
""",
    
    'training': """
<div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 8px; line-height: 1.6;">
    <h2>Effectieve training met {product_name}</h2>
    <p>Deze premium training snacks zijn speciaal ontwikkeld voor optimale resultaten tijdens trainingsessies. De kleine formaat en irresistible smaak maken ze perfect voor frequente beloningen zonder je hond te overvullen. Zoals we uitleggen in onze <a href="../beste-hondensnacks-2026/" style="color: #E68161; text-decoration: underline;">top 10 beste hondensnacks van 2026</a>, zijn de juiste training treats essentieel voor succesvol gedragstraining.</p>
    
    <p>De zachte textuur zorgt voor snelle consumptie, zodat de training vlot kan doorgaan zonder lange pauzes. Deze snacks bevatten natuurlijke ingrediënten die niet alleen lekker zijn, maar ook bijdragen aan de algehele gezondheid van je hond. Voor meer trainingstips en de beste snack keuzes, bekijk onze <a href="../" style="color: #E68161; text-decoration: underline;">homepage met expert aanbevelingen</a>.</p>
    
    <p>Combineer deze training treats met andere <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke hondensnacks</a> voor een gevarieerd dieet. Ontdek in ons artikel over <a href="../blog/waarom-biologische-snacks-beter-zijn/" style="color: #E68161; text-decoration: underline;">biologische voeding</a> waarom natuurlijke ingrediënten zo belangrijk zijn voor je hond's welzijn en trainingsresultaten.</p>
</div>
""",
    
    'hypoallergenic': """
<div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 8px; line-height: 1.6;">
    <h2>{product_name} voor gevoelige honden</h2>
    <p>Deze hypoallergene snacks zijn speciaal ontwikkeld voor honden met voedselallergieën en gevoelige magen. Met slechts één eiwitbron en een beperkte ingrediëntenlijst minimaliseren ze het risiko op allergische reacties. Zoals beschreven in onze <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke hondensnacks gids</a>, zijn limited ingredient formules essentieel voor honden met voedselgevoeligheden.</p>
    
    <p>De zorgvuldig geselecteerde ingrediënten zijn vrij van veelvoorkomende allergenen zoals granen, gluten en kunstmatige toevoegingen. Deze snacks zijn niet alleen veilig, maar ook voedzaam en lekker voor je gevoelige hond. Voor meer informatie over allergie-vriendelijke voeding, bekijk onze <a href="../beste-hondensnacks-2026/" style="color: #E68161; text-decoration: underline;">expert selectie van de beste snacks</a>.</p>
    
    <p>Introduceer nieuwe snacks altijd geleidelijk over 7-10 dagen om maagklachten te voorkomen. Ontdek meer over gezonde voeding voor gevoelige honden in ons artikel over <a href="../blog/waarom-biologische-snacks-beter-zijn/" style="color: #E68161; text-decoration: underline;">biologische snacks</a> en hun voordelen voor honden met allergieën en voedselgevoeligheden.</p>
</div>
""",
    
    'dental': """
<div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 8px; line-height: 1.6;">
    <h2>Tandverzorging met {product_name}</h2>
    <p>Deze dental chews combineren lekker smaak met effectieve tandverzorging. De speciale textuur helpt bij het verwijderen van tandplak en tandsteen tijdens het kauwen, terwijl natuurlijke ingrediënten zoals munt en peterselie zorgen voor frisse adem. Zoals we uitleggen in onze <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke snacks gids</a>, is dagelijkse tandverzorging essentieel voor je hond's gezondheid.</p>
    
    <p>Het regelmatig kauwen op deze dental treats versterkt de kauwspieren en ondersteunt gezond tandvlees. De natuurlijke ingrediënten helpen bij het neutraliseren van bacteriën in de mond en bevorderen een gezonde mondflora. Voor de beste tandverzorging combineer je deze treats met andere <a href="../beste-hondensnacks-2026/" style="color: #E68161; text-decoration: underline;">premium kwaliteit snacks</a>.</p>
    
    <p>Dagelijkse tandverzorging is net zo belangrijk voor honden als voor mensen. Ontdek meer over natuurlijke tandverzorging en gezonde voeding in ons artikel over <a href="../blog/waarom-biologische-snacks-beter-zijn/" style="color: #E68161; text-decoration: underline;">biologische hondensnacks</a> en hun rol in de algehele gezondheid van je hond.</p>
</div>
""",
    
    'senior': """
<div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 8px; line-height: 1.6;">
    <h2>{product_name} voor oudere honden</h2>
    <p>Deze senior snacks zijn speciaal aangepast voor honden van 7 jaar en ouder. De zachte textuur is gemakkelijk te kauwen voor oudere honden met gevoelige tanden, terwijl toegevoegde glucosamine en chondroïtine de gewrichtsgezondheid ondersteunen. Zoals beschreven in onze <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke voeding gids</a>, hebben senior honden aangepaste voedingsbehoeften.</p>
    
    <p>Deze premium snacks bevatten antioxidanten die het immuunsysteem ondersteunen en helpen bij het behouden van vitaliteit op oudere leeftijd. De aangepaste voedingsstoffen ondersteunen hart, hersenen en gewrichten. Voor meer senior voeding tips, bekijk onze <a href="../beste-hondensnacks-2026/" style="color: #E68161; text-decoration: underline;">expert aanbevelingen</a>.</p>
    
    <p>Regelmatige controles bij de dierenarts en aangepaste voeding zijn essentieel voor senior honden. Ontdek meer over gezonde veroudering bij honden in ons artikel over <a href="../blog/waarom-biologische-snacks-beter-zijn/" style="color: #E68161; text-decoration: underline;">biologische voeding</a> en de voordelen voor oudere honden.</p>
</div>
""",
    
    'default': """
<div class="product-description-extended" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 8px; line-height: 1.6;">
    <h2>Waarom kiezen voor {product_name}</h2>
    <p>Deze premium hondensnacks zijn gemaakt van hoogwaardige natuurlijke ingrediënten zonder kunstmatige toevoegingen. Elke snack wordt zorgvuldig geproduceerd volgens strenge kwaliteitsstandaarden om optimale smaak en voedingswaarde te garanderen. Zoals we uitleggen in onze <a href="../natuurlijke-hondensnacks/" style="color: #E68161; text-decoration: underline;">natuurlijke hondensnacks gids</a>, maken natuurlijke ingrediënten het verschil voor je hond's gezondheid.</p>
    
    <p>De zorgvuldig geselecteerde ingrediënten bieden niet alleen heerlijke smaak, maar ook essentiële voedingsstoffen die bijdragen aan je hond's algehele welzijn. Deze snacks zijn perfect voor dagelijkse verwenning, training of als gezonde tussendoortje. Ontdek waarom deze snacks tot onze <a href="../beste-hondensnacks-2026/" style="color: #E68161; text-decoration: underline;">top aanbevelingen van 2026</a> behoren.</p>
    
    <p>Voor de beste resultaten combineer je deze snacks met een gevarieerd dieet van natuurlijke producten. Lees meer over de voordelen van biologische en natuurlijke voeding in ons uitgebreide artikel over <a href="../blog/waarom-biologische-snacks-beter-zijn/" style="color: #E68161; text-decoration: underline;">waarom biologische snacks beter zijn</a> voor je hond's gezondheid en geluk.</p>
</div>
"""
}

def detect_product_category(filename, content):
    """Detecteer de categorie van het product"""
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

def extract_product_name(content):
    """Extraheer product naam uit de HTML content"""
    # Try to extract from title
    title_match = re.search(r'<title>([^|]+)', content)
    if title_match:
        return title_match.group(1).strip()
    
    # Try to extract from h1
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        return h1_match.group(1).strip()
    
    return "Deze premium snacks"

def rewrite_product_description(file_path):
    """Herschrijf de product beschrijving"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_path = os.path.join(BACKUP_DIR, f"desc_{os.path.basename(file_path)}.backup")
        os.makedirs(BACKUP_DIR, exist_ok=True)
        with open(backup_path, 'w', encoding='utf-8') as backup:
            backup.write(content)
        
        # Remove existing detailed description
        content = re.sub(
            r'<!-- Detailed Product Description -->.*?</section>\s*',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Extract product info
        product_name = extract_product_name(content)
        category = detect_product_category(os.path.basename(file_path), content)
        
        # Generate new description
        template = DESCRIPTION_TEMPLATES[category]
        new_description = template.format(product_name=product_name)
        
        # Insert new description before Related Products
        related_products_pattern = r'(\s*<!-- Related Products -->)'
        if re.search(related_products_pattern, content):
            new_content = re.sub(
                related_products_pattern,
                new_description + r'\n            \1',
                content
            )
        else:
            print(f"⚠️  Could not find Related Products section in {os.path.basename(file_path)}")
            return False
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Rewrote {category} description for {os.path.basename(file_path)}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(file_path)}: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 STARTING PRODUCT DESCRIPTIONS REWRITE")
    print("=" * 50)
    
    # Get all product HTML files
    product_files = glob.glob(os.path.join(PRODUITS_DIR, "*.html"))
    product_files = [f for f in product_files if not f.endswith('/index.html')]
    
    print(f"📁 Found {len(product_files)} product files")
    print("📝 New descriptions will be 150-250 words with internal linking")
    
    success_count = 0
    error_count = 0
    
    for file_path in product_files:
        if rewrite_product_description(file_path):
            success_count += 1
        else:
            error_count += 1
    
    print("\n" + "=" * 50)
    print("📊 DESCRIPTION REWRITE RESULTS:")
    print(f"✅ Successfully rewritten: {success_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📁 Total files: {len(product_files)}")
    
    if success_count > 0:
        print(f"\n🎉 Successfully rewrote {success_count} product descriptions!")
        print("📋 New descriptions include:")
        print("   • 150-250 words continuous text")
        print("   • Internal links to pillar pages")
        print("   • Links to homepage and blog articles")
        print("   • Category-specific content")
    
    print("\n🏁 DESCRIPTION REWRITE COMPLETE")

if __name__ == "__main__":
    main()
