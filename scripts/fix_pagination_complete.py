#!/usr/bin/env python3
"""
FIX PAGINATION COMPLETE
=======================
Recrée TOUTES les pages de pagination correctement:
- Page 1: supprime "laad meer", ajoute pagination
- Pages 2-3: copie structure complète + pagination
"""

import os
import json
import re
from pathlib import Path

BASE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
WINKEL_DIR = os.path.join(BASE_DIR, 'winkel')
PRODUCTS_PER_PAGE = 24

def load_products():
    """Charge tous les produits"""
    with open(os.path.join(WINKEL_DIR, 'products-catalog.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def read_original_template():
    """Lit le template original (backup)"""
    template_path = os.path.join(WINKEL_DIR, 'index.html.before_pagination')
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def create_pagination_html(current_page, total_pages):
    """Génère le HTML de pagination"""
    html = '\n    <!-- Pagination Navigation -->\n    <div id="paginationContainer" style="margin: 3rem 0; padding: 2rem; background: white; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\n        <div style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; flex-wrap: wrap;">\n    '
    
    # Bouton Précédent
    if current_page > 1:
        prev_url = '../' if current_page == 2 else f'../' if current_page == 3 else '../'
        prev_url = '' if current_page == 2 else '../' if current_page > 2 else ''
        prev_href = '../' if current_page == 2 else f'../../{current_page-1}/' if current_page > 2 else ''
        
        # Simplification
        if current_page == 2:
            prev_href = '../'
        elif current_page == 3:
            prev_href = '../2/'
        
        html += f'''
            <a href="{prev_href}" style="padding: 0.75rem 1.25rem; background: #E68161; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.5rem;" onmouseover="this.style.background='#d4704f'" onmouseout="this.style.background='#E68161'">
                ← Vorige
            </a>
        '''
    else:
        html += '''
            <span style="padding: 0.75rem 1.25rem; background: #e5e7eb; color: #9ca3af; border-radius: 8px; font-weight: 600; cursor: not-allowed;">
                ← Vorige
            </span>
        '''
    
    # Numéros de page
    for page_num in range(1, total_pages + 1):
        if current_page == 1:
            page_href = '' if page_num == 1 else f'page/{page_num}/'
        elif current_page == 2:
            page_href = '../' if page_num == 1 else f'../{page_num}/' if page_num > 1 else ''
            if page_num == 2:
                page_href = ''
            elif page_num > 2:
                page_href = f'../{page_num}/'
        else:  # page 3
            page_href = '../../' if page_num == 1 else f'../../page/{page_num}/' if page_num > 1 else ''
            if page_num == 2:
                page_href = '../2/'
            elif page_num == 3:
                page_href = ''
        
        # Simplification finale
        if page_num == 1:
            if current_page == 1:
                page_href = ''
            else:
                page_href = '../../' if current_page > 2 else '../'
        elif page_num == current_page:
            page_href = ''
        else:
            # Relatif depuis current_page
            if current_page == 1:
                page_href = f'page/{page_num}/'
            else:
                # Retour à winkel puis aller à page N
                page_href = f'../../page/{page_num}/' if page_num > 1 else '../../'
        
        if page_num == current_page:
            html += f'''
                <span style="padding: 0.75rem 1.25rem; background: #E68161; color: white; border-radius: 8px; font-weight: 700; min-width: 45px; text-align: center;">
                    {page_num}
                </span>
            '''
        else:
            html += f'''
                <a href="{page_href}" style="padding: 0.75rem 1.25rem; background: white; color: #374151; text-decoration: none; border: 2px solid #e5e7eb; border-radius: 8px; font-weight: 600; transition: all 0.3s; min-width: 45px; text-align: center;" onmouseover="this.style.borderColor='#E68161'; this.style.color='#E68161'" onmouseout="this.style.borderColor='#e5e7eb'; this.style.color='#374151'">
                    {page_num}
                </a>
            '''
    
    # Bouton Suivant
    if current_page < total_pages:
        if current_page == 1:
            next_href = 'page/2/'
        elif current_page == 2:
            next_href = '../3/'
        else:
            next_href = ''
        
        html += f'''
            <a href="{next_href}" style="padding: 0.75rem 1.25rem; background: #E68161; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.5rem;" onmouseover="this.style.background='#d4704f'" onmouseout="this.style.background='#E68161'">
                Volgende →
            </a>
        '''
    else:
        html += '''
            <span style="padding: 0.75rem 1.25rem; background: #e5e7eb; color: #9ca3af; border-radius: 8px; font-weight: 600; cursor: not-allowed;">
                Volgende →
            </span>
        '''
    
    html += f'''
        </div>
        
        <!-- Info Page -->
        <div style="text-align: center; margin-top: 1.5rem; color: #6b7280; font-size: 0.95rem;">
            Pagina <strong style="color: #E68161;">{current_page}</strong> van <strong>{total_pages}</strong>
        </div>
    </div>
    '''
    
    return html

def create_pagination_config(current_page, total_pages, all_products):
    """Crée le script PAGINATION_CONFIG"""
    start_idx = (current_page - 1) * PRODUCTS_PER_PAGE
    end_idx = start_idx + PRODUCTS_PER_PAGE
    page_products = all_products[start_idx:end_idx]
    
    config = {
        'currentPage': current_page,
        'totalPages': total_pages,
        'productsPerPage': PRODUCTS_PER_PAGE,
        'products': page_products
    }
    
    return f'''<script>
window.PAGINATION_CONFIG = {json.dumps(config, ensure_ascii=False, indent=2)};
</script>'''

def update_page_1(template, all_products, total_pages):
    """Met à jour la page 1: supprime laad meer, ajoute pagination"""
    
    # 1. Remplacer le bouton "laad meer" par la pagination
    load_more_pattern = r'<!-- Load More -->.*?</div>\s*<!-- Empty State -->'
    pagination_html = create_pagination_html(1, total_pages)
    
    template = re.sub(load_more_pattern, pagination_html + '\n    <!-- Empty State -->', template, flags=re.DOTALL)
    
    # 2. Ajouter window.PAGINATION_CONFIG avant </head>
    config_script = create_pagination_config(1, total_pages, all_products)
    template = template.replace('</head>', config_script + '\n</head>')
    
    # 3. Mettre à jour les balises SEO
    # Ajouter rel="next"
    if '<link rel="next"' not in template:
        canonical_pattern = r'(<link rel="canonical"[^>]*>)'
        template = re.sub(canonical_pattern, r'\1\n<link rel="next" href="https://biologische-hondensnacks.nl/winkel/page/2/">', template)
    
    return template

def create_page_n(template, page_num, all_products, total_pages):
    """Crée une page N (2 ou 3) avec le contenu complet"""
    
    # 1. Mettre à jour le title
    template = re.sub(
        r'<title>([^<]*)</title>',
        f'<title>Biologische Hondensnacks Winkel - Pagina {page_num} | Natuurlijke Snacks</title>',
        template
    )
    
    # 2. Mettre à jour canonical + prev/next
    # Supprimer l'ancien canonical et next
    template = re.sub(r'<link rel="canonical"[^>]*>', '', template)
    template = re.sub(r'<link rel="next"[^>]*>', '', template)
    template = re.sub(r'<link rel="prev"[^>]*>', '', template)
    
    # Ajouter les nouveaux
    seo_links = f'''<link rel="canonical" href="https://biologische-hondensnacks.nl/winkel/page/{page_num}/">
'''
    
    if page_num > 1:
        prev_url = 'https://biologische-hondensnacks.nl/winkel/' if page_num == 2 else f'https://biologische-hondensnacks.nl/winkel/page/{page_num-1}/'
        seo_links += f'<link rel="prev" href="{prev_url}">\n'
    
    if page_num < total_pages:
        seo_links += f'<link rel="next" href="https://biologische-hondensnacks.nl/winkel/page/{page_num+1}/">\n'
    
    template = template.replace('<!-- Favicon -->', seo_links + '<!-- Favicon -->')
    
    # 3. Remplacer le bouton "laad meer" par la pagination
    load_more_pattern = r'<!-- Load More -->.*?</div>\s*<!-- Empty State -->'
    pagination_html = create_pagination_html(page_num, total_pages)
    template = re.sub(load_more_pattern, pagination_html + '\n    <!-- Empty State -->', template, flags=re.DOTALL)
    
    # 4. Ajouter window.PAGINATION_CONFIG
    config_script = create_pagination_config(page_num, total_pages, all_products)
    template = template.replace('</head>', config_script + '\n</head>')
    
    # 5. Fixer les chemins CSS/JS (ajouter ../ ou ../../)
    depth = 1 if page_num > 1 else 0  # pages 2+ sont dans /winkel/page/N/
    prefix = '../../' if depth else '../'
    
    template = re.sub(r'href="\.\./', f'href="{prefix}', template)
    template = re.sub(r'src="\.\./', f'src="{prefix}', template)
    
    return template

def main():
    print("\n🔧 FIX PAGINATION COMPLÈTE")
    print("=" * 70)
    
    # 1. Charger les produits
    print("\n📦 Chargement des produits...")
    all_products = load_products()
    total_pages = 3  # 67 produits / 24 = 2.79 → 3 pages
    print(f"   ✅ {len(all_products)} produits chargés")
    print(f"   📄 {total_pages} pages nécessaires")
    
    # 2. Lire le template original
    print("\n📄 Lecture du template original...")
    template = read_original_template()
    print(f"   ✅ Template chargé ({len(template)} caractères)")
    
    # 3. Créer page 1 (supprime laad meer, ajoute pagination)
    print("\n🔨 Création Page 1...")
    page1_html = update_page_1(template, all_products, total_pages)
    page1_path = os.path.join(WINKEL_DIR, 'index.html')
    with open(page1_path, 'w', encoding='utf-8') as f:
        f.write(page1_html)
    print(f"   ✅ Page 1 créée: {page1_path}")
    print(f"      - Bouton 'laad meer' supprimé")
    print(f"      - Pagination ajoutée")
    print(f"      - {PRODUCTS_PER_PAGE} premiers produits")
    
    # 4. Créer page 2
    print("\n🔨 Création Page 2...")
    page2_html = create_page_n(template, 2, all_products, total_pages)
    page2_dir = os.path.join(WINKEL_DIR, 'page', '2')
    Path(page2_dir).mkdir(parents=True, exist_ok=True)
    page2_path = os.path.join(page2_dir, 'index.html')
    with open(page2_path, 'w', encoding='utf-8') as f:
        f.write(page2_html)
    print(f"   ✅ Page 2 créée: {page2_path}")
    print(f"      - Contenu complet (filtres + produits)")
    print(f"      - Produits 25-48")
    
    # 5. Créer page 3
    print("\n🔨 Création Page 3...")
    page3_html = create_page_n(template, 3, all_products, total_pages)
    page3_dir = os.path.join(WINKEL_DIR, 'page', '3')
    Path(page3_dir).mkdir(parents=True, exist_ok=True)
    page3_path = os.path.join(page3_dir, 'index.html')
    with open(page3_path, 'w', encoding='utf-8') as f:
        f.write(page3_html)
    print(f"   ✅ Page 3 créée: {page3_path}")
    print(f"      - Contenu complet (filtres + produits)")
    print(f"      - Produits 49-67")
    
    print("\n" + "=" * 70)
    print("✅ PAGINATION COMPLÈTE FIXÉE!")
    print("=" * 70)
    print("\n📋 Résumé:")
    print(f"   - Page 1: /winkel/ ({PRODUCTS_PER_PAGE} produits)")
    print(f"   - Page 2: /winkel/page/2/ ({PRODUCTS_PER_PAGE} produits)")
    print(f"   - Page 3: /winkel/page/3/ ({len(all_products) - 2*PRODUCTS_PER_PAGE} produits)")
    print("\n🎯 Changements:")
    print("   ✅ Bouton 'laad meer' supprimé")
    print("   ✅ Pagination visible ajoutée")
    print("   ✅ Toutes les pages ont le contenu complet")
    print("   ✅ Produits réels du CSV")
    print("   ✅ SEO tags (rel=prev/next)")

if __name__ == "__main__":
    main()
