#!/usr/bin/env python3
"""
ADD VISIBLE PAGINATION HTML
============================
Ajoute les boutons de pagination visibles dans les pages winkel
"""

import os
import re
from pathlib import Path

BASE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
WINKEL_DIR = os.path.join(BASE_DIR, 'winkel')

def create_pagination_html(current_page, total_pages):
    """Génère le HTML de pagination visible"""
    
    pagination_html = '''
    <!-- Pagination Navigation -->
    <div id="paginationContainer" style="margin: 3rem 0; padding: 2rem; background: white; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <div style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
    '''
    
    # Bouton Précédent
    if current_page > 1:
        prev_url = '/winkel/' if current_page == 2 else f'/winkel/page/{current_page - 1}/'
        pagination_html += f'''
            <a href="{prev_url}" style="padding: 0.75rem 1.25rem; background: #E68161; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.5rem;" onmouseover="this.style.background='#d4704f'" onmouseout="this.style.background='#E68161'">
                ← Vorige
            </a>
        '''
    else:
        pagination_html += f'''
            <span style="padding: 0.75rem 1.25rem; background: #e5e7eb; color: #9ca3af; border-radius: 8px; font-weight: 600; cursor: not-allowed;">
                ← Vorige
            </span>
        '''
    
    # Numéros de page
    for page_num in range(1, total_pages + 1):
        page_url = '/winkel/' if page_num == 1 else f'/winkel/page/{page_num}/'
        
        if page_num == current_page:
            # Page active
            pagination_html += f'''
                <span style="padding: 0.75rem 1.25rem; background: #E68161; color: white; border-radius: 8px; font-weight: 700; min-width: 45px; text-align: center;">
                    {page_num}
                </span>
            '''
        else:
            # Page inactive
            pagination_html += f'''
                <a href="{page_url}" style="padding: 0.75rem 1.25rem; background: white; color: #374151; text-decoration: none; border: 2px solid #e5e7eb; border-radius: 8px; font-weight: 600; transition: all 0.3s; min-width: 45px; text-align: center;" onmouseover="this.style.borderColor='#E68161'; this.style.color='#E68161'" onmouseout="this.style.borderColor='#e5e7eb'; this.style.color='#374151'">
                    {page_num}
                </a>
            '''
    
    # Bouton Suivant
    if current_page < total_pages:
        next_url = f'/winkel/page/{current_page + 1}/'
        pagination_html += f'''
            <a href="{next_url}" style="padding: 0.75rem 1.25rem; background: #E68161; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.5rem;" onmouseover="this.style.background='#d4704f'" onmouseout="this.style.background='#E68161'">
                Volgende →
            </a>
        '''
    else:
        pagination_html += f'''
            <span style="padding: 0.75rem 1.25rem; background: #e5e7eb; color: #9ca3af; border-radius: 8px; font-weight: 600; cursor: not-allowed;">
                Volgende →
            </span>
        '''
    
    pagination_html += '''
        </div>
        
        <!-- Info Page -->
        <div style="text-align: center; margin-top: 1.5rem; color: #6b7280; font-size: 0.95rem;">
            Pagina <strong style="color: #E68161;">''' + str(current_page) + '''</strong> van <strong>''' + str(total_pages) + '''</strong>
        </div>
    </div>
    '''
    
    return pagination_html

def inject_pagination(file_path, current_page, total_pages):
    """Injecte la pagination dans un fichier HTML"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Créer le HTML de pagination
    pagination_html = create_pagination_html(current_page, total_pages)
    
    # Trouver où insérer (juste avant le footer ou avant les "Gerelateerde Artikelen")
    # Chercher le marker pour "Gerelateerde Artikelen" ou le footer
    
    # Pattern pour trouver la section "Gerelateerde Artikelen"
    related_pattern = r'(<section[^>]*style="[^"]*background:\s*#f9fafb[^"]*"[^>]*>.*?<h2[^>]*>Gerelateerde Artikelen</h2>)'
    
    match = re.search(related_pattern, html_content, re.DOTALL)
    
    if match:
        # Insérer avant "Gerelateerde Artikelen"
        insertion_point = match.start()
        new_html = html_content[:insertion_point] + pagination_html + html_content[insertion_point:]
    else:
        # Fallback: insérer avant le footer
        footer_pattern = r'(<!-- Footer -->|<footer)'
        match = re.search(footer_pattern, html_content)
        if match:
            insertion_point = match.start()
            new_html = html_content[:insertion_point] + pagination_html + html_content[insertion_point:]
        else:
            # Dernier fallback: avant </body>
            new_html = html_content.replace('</body>', pagination_html + '\n</body>')
    
    # Écrire le fichier modifié
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"✅ Pagination ajoutée: {file_path}")

def main():
    print("\n🎨 AJOUT PAGINATION HTML VISIBLE")
    print("=" * 70)
    
    total_pages = 3
    
    # Page 1
    page1_path = os.path.join(WINKEL_DIR, 'index.html')
    if os.path.exists(page1_path):
        inject_pagination(page1_path, 1, total_pages)
    
    # Page 2
    page2_path = os.path.join(WINKEL_DIR, 'page', '2', 'index.html')
    if os.path.exists(page2_path):
        inject_pagination(page2_path, 2, total_pages)
    
    # Page 3
    page3_path = os.path.join(WINKEL_DIR, 'page', '3', 'index.html')
    if os.path.exists(page3_path):
        inject_pagination(page3_path, 3, total_pages)
    
    print("\n✅ PAGINATION HTML VISIBLE AJOUTÉE!")
    print("=" * 70)
    print("\nLes boutons suivants sont maintenant visibles:")
    print("  - ← Vorige (page précédente)")
    print("  - Numéros 1, 2, 3 (navigation directe)")
    print("  - Volgende → (page suivante)")
    print("  - Page active en orange (#E68161)")

if __name__ == "__main__":
    main()
