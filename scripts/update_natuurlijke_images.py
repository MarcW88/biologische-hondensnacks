#!/usr/bin/env python3
"""
UPDATE NATUURLIJKE-HONDENSNACKS IMAGES
======================================

Remplace les images placeholder par les vraies images locales.

Auteur: AI Assistant
Date: December 2025
"""

import re

def update_images():
    """Met à jour les images dans la page"""
    
    input_file = '/Users/marc/Desktop/biologische-hondensnacks/natuurlijke-hondensnacks/index.html'
    
    # Lire le fichier
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    backup_file = input_file + '.images_backup'
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Mapping des produits aux images
    replacements = [
        # (nom produit dans le code, nom fichier image)
        ("Zachte Puppy Koekjes", "Zachte Puppy Koekjes .jpg"),
        ("Natuurlijke Zalm Bites", "Natuurlijke Zalm Bites.jpg"),
        ("Biologische Hertenvlees Strips", "Biologische Hertenvlees Strips .jpg"),
        ("Natuurlijke Kauwbotten Mix", "Natuurlijke Kauwsticks .jpg"),  # Mapping corrigé
        ("Zachte Puppy Kauwsticks", "Gedroogde Eend Bites .jpg"),  # Mapping corrigé
        ("Zachte Kip & Rijst Koekjes", "Mini Training Treats .jpg"),  # Mapping corrigé
    ]
    
    updates_count = 0
    
    for product_name, image_file in replacements:
        # Pattern pour trouver l'image placeholder pour ce produit
        # Cherche le bloc qui contient le nom du produit et son image placeholder
        pattern = rf"(name: '{re.escape(product_name)}',.*?image: ')(https://via\.placeholder\.com/[^']+)(')"
        
        replacement = rf"\1../images/{image_file}\3"
        
        new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
        
        if count > 0:
            content = new_content
            updates_count += count
            print(f"✅ {product_name:40} → {image_file}")
        else:
            print(f"⚠️  {product_name:40} → Non trouvé")
    
    # Sauvegarder
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*60}")
    print(f"🎉 IMAGES MISES À JOUR!")
    print(f"✅ {updates_count} images remplacées")
    print(f"💾 Backup sauvegardé: {backup_file}")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("🖼️  UPDATE NATUURLIJKE-HONDENSNACKS IMAGES")
    print("=" * 60)
    update_images()
