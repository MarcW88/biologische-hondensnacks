#!/usr/bin/env python3
"""
Script complet pour restructurer le HTML pour correspondre au template de italiaanse-percolator
- Supprime TOUT inline CSS
- Remplace les classes CSS par celles du template
- Restructure le HTML pour correspondre
"""

import re
from pathlib import Path

def remove_all_inline_styles(file_path):
    """Supprime tous les attributs style inline"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Supprimer tous les attributs style
    content = re.sub(r'\s+style="[^"]*"', '', content)
    content = re.sub(r'\s+style=\'[^\']*\'', '', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def replace_classes(file_path):
    """Remplace les anciennes classes par les nouvelles du template"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remplacer les anciennes classes par les nouvelles
    class_replacements = {
        'product-card': 'card',
        'product-badge': 'rating-badge',
        'badge-winner': '',
        'badge-favorite': '',
        'product-specs': '',
        'price-container': '',
        'price': '',
        'price-context': '',
        'cta-group': '',
        'btn-ghost': 'btn-outline',
        'btn-large': '',
        'hero-text-block': '',
        'hero-cta': '',
        'section-title': '',
        'rating': '',
        'stars': '',
        'review-count': '',
        'check': '',
    }
    
    for old_class, new_class in class_replacements.items():
        if new_class:
            content = re.sub(rf'\b{old_class}\b', new_class, content)
        else:
            content = re.sub(rf'\s+class="[^"]*{old_class}[^"]*"', 
                           lambda m: m.group(0).replace(f' {old_class}', '').replace(f'{old_class} ', '').replace(old_class, ''), 
                           content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def restructure_html(file_path):
    """Restructure le HTML pour correspondre au template"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Nettoyer les classes vides
    content = re.sub(r'\s+class=""', '', content)
    content = re.sub(r'\s+class=\'\'', '', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def process_file(file_path):
    """Traite un fichier HTML"""
    changes = False
    
    if remove_all_inline_styles(file_path):
        changes = True
    
    if replace_classes(file_path):
        changes = True
    
    if restructure_html(file_path):
        changes = True
    
    return changes

def main():
    """Fonction principale"""
    directory = Path('.')
    
    # Trouver tous les fichiers HTML
    html_files = list(directory.rglob('*.html'))
    
    # Exclure les fichiers de backup
    html_files = [f for f in html_files if 'backup' not in str(f)]
    
    print(f"Restructuration de {len(html_files)} fichiers HTML...\n")
    
    updated_count = 0
    for html_file in html_files:
        if process_file(html_file):
            updated_count += 1
            print(f"✓ {html_file.relative_to(directory)}")
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
