#!/usr/bin/env python3
"""
SCRIPT CORRECTION MAJUSCULES
Supprime les majuscules incorrectes dans tous les titres du site
"""

import os
import re
import glob
from pathlib import Path

# Configuration
SITE_DIR = "/Users/marc/Desktop/biologische-hondensnacks"
BACKUP_DIR = "/Users/marc/Desktop/biologische-hondensnacks/scripts/backups"

# Patterns de correction des majuscules
CAPITALIZATION_FIXES = [
    # Titres généraux
    (r'\bNatuurlijke Ingrediënten\b', 'Natuurlijke ingrediënten'),
    (r'\bPerfecte Snack\b', 'Perfecte snack'),
    (r'\bBeste Kwaliteit\b', 'Beste kwaliteit'),
    (r'\bGezonde Keuze\b', 'Gezonde keuze'),
    (r'\bVeilige Ingrediënten\b', 'Veilige ingrediënten'),
    (r'\bBiologische Kwaliteit\b', 'Biologische kwaliteit'),
    (r'\bNatuurlijke Voeding\b', 'Natuurlijke voeding'),
    (r'\bGraanvrije Snacks\b', 'Graanvrije snacks'),
    (r'\bPuppy Training\b', 'Puppy training'),
    (r'\bGezonde Honden\b', 'Gezonde honden'),
    (r'\bNatuurlijke Snacks\b', 'Natuurlijke snacks'),
    (r'\bBiologische Snacks\b', 'Biologische snacks'),
    (r'\bHondenvoeding Expert\b', 'Hondenvoeding expert'),
    (r'\bVoedingsdeskundige Advies\b', 'Voedingsdeskundige advies'),
    
    # Titres de sections
    (r'\bWat Ons Uniek Maakt\b', 'Wat ons uniek maakt'),
    (r'\bOnze Expertise\b', 'Onze expertise'),
    (r'\bOver Biologische Hondensnacks\b', 'Over biologische hondensnacks'),
    (r'\bPopulaire Categorieën\b', 'Populaire categorieën'),
    (r'\bBeste Hondensnacks\b', 'Beste hondensnacks'),
    (r'\bTop Producten\b', 'Top producten'),
    (r'\bAanbevolen Snacks\b', 'Aanbevolen snacks'),
    (r'\bVertrouwde Merken\b', 'Vertrouwde merken'),
    
    # Titres de quiz et CTA
    (r'\bVind de Perfecte Snack in 3 Stappen\b', 'Vind de perfecte snack in 3 stappen'),
    (r'\bVind Je Perfecte Snack\b', 'Vind je perfecte snack'),
    (r'\bOntdek De Beste Snacks\b', 'Ontdek de beste snacks'),
    (r'\bKies De Juiste Snack\b', 'Kies de juiste snack'),
    (r'\bStart Je Zoektocht\b', 'Start je zoektocht'),
    
    # Titres de produits
    (r'\bProduct Beschrijving\b', 'Product beschrijving'),
    (r'\bProduct Details\b', 'Product details'),
    (r'\bVoedingswaarden\b', 'Voedingswaarden'),
    (r'\bIngrediënten Lijst\b', 'Ingrediënten lijst'),
    (r'\bGebruiksaanwijzing\b', 'Gebruiksaanwijzing'),
    (r'\bBewaar Instructies\b', 'Bewaar instructies'),
    
    # Titres de blog
    (r'\bGerelateerde Artikelen\b', 'Gerelateerde artikelen'),
    (r'\bMeer Lezen\b', 'Meer lezen'),
    (r'\bVeelgestelde Vragen\b', 'Veelgestelde vragen'),
    (r'\bTips En Tricks\b', 'Tips en tricks'),
    (r'\bExpert Advies\b', 'Expert advies'),
    
    # Noms propres à préserver (exceptions)
    # Ces patterns seront appliqués APRÈS les corrections pour restaurer les noms propres
]

# Noms propres à préserver (ne pas toucher)
PROPER_NOUNS = [
    'Yarrah', 'Blue Buffalo', 'Kong', 'Benebone', 'Green Petfood', 
    'Lily\'s Kitchen', 'Wellness', 'Nylabone', 'Zuke\'s',
    'Nederland', 'Nederlandse', 'Europa', 'Europese',
    'SKAL', 'Bio', 'Organic', 'Natural', 'Premium',
    'DHA', 'EPA', 'Omega', 'Vitamin', 'Calcium',
    'Google', 'Facebook', 'Instagram', 'YouTube', 'Bol.com'
]

def backup_file(file_path):
    """Maak een backup van het originele bestand"""
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup_path = os.path.join(BACKUP_DIR, f"caps_{os.path.basename(file_path)}.backup")
        with open(file_path, 'r', encoding='utf-8') as original:
            content = original.read()
        with open(backup_path, 'w', encoding='utf-8') as backup:
            backup.write(content)
        return True
    except Exception as e:
        print(f"❌ Error creating backup for {os.path.basename(file_path)}: {str(e)}")
        return False

def fix_capitalization_in_file(file_path):
    """Corrige les majuscules dans un fichier"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # Apply capitalization fixes
        for pattern, replacement in CAPITALIZATION_FIXES:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes_made += 1
        
        # Only write if changes were made
        if content != original_content:
            # Create backup first
            if not backup_file(file_path):
                return False, 0
            
            # Write corrected content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Fixed {changes_made} capitalization issues in {os.path.basename(file_path)}")
            return True, changes_made
        else:
            print(f"⚪ No capitalization issues found in {os.path.basename(file_path)}")
            return True, 0
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(file_path)}: {str(e)}")
        return False, 0

def main():
    """Main function"""
    print("🚀 STARTING CAPITALIZATION FIXES")
    print("=" * 50)
    
    # Get all HTML files in the site
    html_files = []
    
    # Root directory files
    html_files.extend(glob.glob(os.path.join(SITE_DIR, "*.html")))
    
    # Subdirectory files
    for subdir in ['over-ons', 'winkel', 'blog', 'natuurlijke-hondensnacks', 
                   'beste-hondensnacks-2026', 'hondensnacks-voor-puppy', 'produits']:
        subdir_path = os.path.join(SITE_DIR, subdir)
        if os.path.exists(subdir_path):
            html_files.extend(glob.glob(os.path.join(subdir_path, "*.html")))
    
    # Blog subdirectories
    blog_dir = os.path.join(SITE_DIR, "blog")
    if os.path.exists(blog_dir):
        for item in os.listdir(blog_dir):
            item_path = os.path.join(blog_dir, item)
            if os.path.isdir(item_path):
                html_files.extend(glob.glob(os.path.join(item_path, "*.html")))
    
    print(f"📁 Found {len(html_files)} HTML files to process")
    
    success_count = 0
    error_count = 0
    total_changes = 0
    
    for file_path in html_files:
        success, changes = fix_capitalization_in_file(file_path)
        if success:
            success_count += 1
            total_changes += changes
        else:
            error_count += 1
    
    print("\n" + "=" * 50)
    print("📊 CAPITALIZATION FIX RESULTS:")
    print(f"✅ Successfully processed: {success_count}")
    print(f"❌ Errors: {error_count}")
    print(f"🔧 Total changes made: {total_changes}")
    print(f"📁 Total files: {len(html_files)}")
    
    if total_changes > 0:
        print(f"\n🎉 Successfully fixed {total_changes} capitalization issues!")
        print("📋 Fixed patterns include:")
        print("   • 'Natuurlijke Ingrediënten' → 'Natuurlijke ingrediënten'")
        print("   • 'Perfecte Snack' → 'Perfecte snack'")
        print("   • 'Vind de Perfecte Snack' → 'Vind de perfecte snack'")
        print("   • And many more...")
    
    print("\n🏁 CAPITALIZATION FIXES COMPLETE")

if __name__ == "__main__":
    main()
