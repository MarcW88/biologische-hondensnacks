#!/usr/bin/env python3
"""
Script pour nettoyer tout inline CSS et mettre à jour les classes CSS
pour correspondre au template de italiaanse-percolator
"""

import re
from pathlib import Path

def clean_inline_css(file_path):
    """Nettoie tout inline CSS et remplace avec des classes CSS"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remplacer les couleurs hex par des variables CSS
    color_replacements = {
        '#E68161': 'var(--primary)',
        '#f4a582': 'var(--primary-light)',
        '#d67347': 'var(--primary-dark)',
        '#2d3748': 'var(--text)',
        '#4a5568': 'var(--text-dim)',
        '#64748b': 'var(--text-light)',
        '#22c55e': 'var(--success)',
        '#f59e0b': 'var(--warning)',
        '#dc3545': 'var(--error)',
        '#FFA726': 'var(--rating)',
        '#ffffff': 'white',
        '#f8fafc': 'var(--surface-soft)',
        '#e5e7eb': 'var(--border)',
    }
    
    # Remplacer les couleurs dans les styles inline
    for hex_color, css_var in color_replacements.items():
        content = re.sub(hex_color, css_var, content)
    
    # Remplacer les tailles de police inline avec des variables
    font_replacements = {
        r'font-size:\s*3\.5rem': 'font-size: var(--fs-5xl)',
        r'font-size:\s*2\.2rem': 'font-size: var(--fs-4xl)',
        r'font-size:\s*1\.5rem': 'font-size: var(--fs-xl)',
        r'font-size:\s*1\.1rem': 'font-size: var(--fs-lg)',
        r'font-size:\s*0\.9rem': 'font-size: var(--fs-sm)',
    }
    
    for pattern, replacement in font_replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # Remplacer les padding/margin inline avec des variables
    spacing_replacements = {
        r'padding:\s*3rem\s*0': 'padding: var(--sp-12) 0',
        r'padding:\s*2rem\s*1rem': 'padding: var(--sp-8) var(--sp-4)',
        r'padding:\s*1\.5rem': 'padding: var(--sp-6)',
        r'padding:\s*1\.25rem\s*2\.5rem': 'padding: var(--sp-5) var(--sp-10)',
        r'padding:\s*0\.75rem\s*1\.5rem': 'padding: var(--sp-3) var(--sp-6)',
        r'padding:\s*0\.5rem\s*1rem': 'padding: var(--sp-2) var(--sp-4)',
        r'margin:\s*1\.5rem': 'margin: var(--sp-6)',
        r'margin:\s*1rem': 'margin: var(--sp-4)',
        r'margin:\s*0\.5rem': 'margin: var(--sp-2)',
        r'margin-bottom:\s*1\.5rem': 'margin-bottom: var(--sp-6)',
        r'margin-bottom:\s*1rem': 'margin-bottom: var(--sp-4)',
        r'margin-bottom:\s*0\.5rem': 'margin-bottom: var(--sp-2)',
    }
    
    for pattern, replacement in spacing_replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # Remplacer les border-radius inline avec des variables
    radius_replacements = {
        r'border-radius:\s*12px': 'border-radius: var(--r-xl)',
        r'border-radius:\s*8px': 'border-radius: var(--r-lg)',
        r'border-radius:\s*20px': 'border-radius: var(--r-2xl)',
    }
    
    for pattern, replacement in radius_replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # Remplacer les box-shadow inline avec des variables
    shadow_replacements = {
        r'box-shadow:\s*0\s*2px\s*8px\s*rgba\(0,0,0,0\.1\)': 'box-shadow: var(--shadow-md)',
        r'box-shadow:\s*0\s*4px\s*16px\s*rgba\(0,0,0,0\.12\)': 'box-shadow: var(--shadow-lg)',
    }
    
    for pattern, replacement in shadow_replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # Mettre à jour les liens CSS pour utiliser css/styles.css
    content = re.sub(r'<link href="style\.css"', '<link href="css/styles.css"', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path.name} - Nettoyé")
        return True
    else:
        print(f"✗ {file_path.name} - Pas de changements")
        return False

def main():
    """Fonction principale"""
    directory = Path('.')
    
    # Trouver tous les fichiers HTML
    html_files = list(directory.rglob('*.html'))
    
    # Exclure les fichiers de backup
    html_files = [f for f in html_files if 'backup' not in str(f)]
    
    print(f"Nettoyage de {len(html_files)} fichiers HTML...\n")
    
    updated_count = 0
    for html_file in html_files:
        if clean_inline_css(html_file):
            updated_count += 1
    
    print(f"\nTerminé! {updated_count} fichiers mis à jour.")

if __name__ == '__main__':
    main()
