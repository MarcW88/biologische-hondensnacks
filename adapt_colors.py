#!/usr/bin/env python3
"""
Script pour adapter les couleurs du CSS pour biologische-hondensnacks
Remplace les couleurs marron de italiaanse-percolator par orange
"""

from pathlib import Path

def adapt_css_colors(css_file):
    """Adapte les couleurs CSS pour biologische-hondensnacks"""
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remplacer les couleurs de italiaanse-percolator par celles de biologische-hondensnacks
    color_replacements = {
        # Couleurs principales (marron → orange)
        '#7B5A43': '#E68161',  # primary coffee → primary orange
        '#8B6B54': '#F4A582',  # primary light
        '#6B4A32': '#D67347',  # primary dark
        
        # Couleurs secondaires
        '#A67C52': '#E68161',
        '#C4A882': '#F4A582',
        '#D4C4A8': '#F4A582',
        
        # Couleurs de fond
        '#f5f0ea': '#FFF5F0',  # fond beige → fond très léger orange
        '#f0ebe5': '#FFF0EB',
        
        # Couleurs de texte (garder les mêmes)
        # '#2d2d2d': '#2d2d2d',
        # '#666666': '#666666',
        # '#999999': '#999999',
    }
    
    for old_color, new_color in color_replacements.items():
        content = content.replace(old_color, new_color)
    
    # Remplacer les variables CSS si elles existent
    var_replacements = {
        '--coffee': '--primary',
        '--coffee-light': '--primary-light',
        '--coffee-dark': '--primary-dark',
    }
    
    for old_var, new_var in var_replacements.items():
        content = content.replace(old_var, new_var)
    
    if content != original_content:
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Fonction principale"""
    css_file = Path('css/styles.css')
    
    if not css_file.exists():
        print(f"Erreur: {css_file} n'existe pas")
        return
    
    if adapt_css_colors(css_file):
        print(f"✓ Couleurs adaptées dans {css_file}")
    else:
        print(f"✗ Aucun changement nécessaire dans {css_file}")

if __name__ == '__main__':
    main()
