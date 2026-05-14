#!/usr/bin/env python3
"""
Script pour mettre à jour toutes les pages HTML pour utiliser les nouvelles classes CSS
"""

import re
from pathlib import Path

def update_html_classes(file_path):
    """Met à jour les classes CSS dans un fichier HTML"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remplacer les anciennes classes CSS par les nouvelles
    class_replacements = {
        'class="header"': 'class="navbar"',
        'class="nav"': 'class="nav-menu"',
        'class="logo"': 'class="nav-brand"',
        'class="nav-shop"': 'class="nav-link active"',
    }
    
    for old_class, new_class in class_replacements.items():
        content = content.replace(old_class, new_class)
    
    # Mettre à jour les liens CSS pour utiliser css/styles.css
    content = re.sub(r'href="style\.css"', 'href="css/styles.css"', content)
    content = re.sub(r'href="css/styles\.css"', 'href="css/styles.css"', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Fonction principale"""
    directory = Path('.')
    
    # Trouver tous les fichiers HTML sauf ceux dans produits/ (déjà mis à jour)
    html_files = list(directory.rglob('*.html'))
    html_files = [f for f in html_files if 'produits' not in str(f)]
    
    print(f"Mise à jour de {len(html_files)} fichiers HTML...\n")
    
    updated_count = 0
    for html_file in html_files:
        try:
            if update_html_classes(html_file):
                updated_count += 1
                print(f"✓ {html_file.relative_to(directory)}")
        except Exception as e:
            print(f"✗ {html_file.relative_to(directory)} - Erreur: {e}")
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
