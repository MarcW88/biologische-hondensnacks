#!/usr/bin/env python3
"""
CREATE PAGINATION - Implémente pagination SEO-friendly pour la page winkel
============================================================================

Crée de vraies pages HTML pour chaque page de pagination :
- /winkel/index.html (page 1)
- /winkel/page/2/index.html
- /winkel/page/3/index.html
- etc.

Auteur: AI Assistant
Date: Décembre 2025
"""

import json
import os
import math
import shutil
from pathlib import Path

BASE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
WINKEL_DIR = os.path.join(BASE_DIR, 'winkel')
CATALOG_JSON = os.path.join(WINKEL_DIR, 'products-catalog.json')
TEMPLATE_HTML = os.path.join(WINKEL_DIR, 'index.html')

PRODUCTS_PER_PAGE = 24

def load_products():
    """Charge les produits depuis le catalog JSON"""
    with open(CATALOG_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_template():
    """Lit le template HTML"""
    with open(TEMPLATE_HTML, 'r', encoding='utf-8') as f:
        return f.read()

def create_pagination_html(current_page, total_pages, base_url='/winkel'):
    """Génère le HTML de la pagination"""
    html = '<div class="pagination" style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; margin: 3rem 0; flex-wrap: wrap;">\n'
    
    # Bouton Précédent
    if current_page > 1:
        prev_url = f'{base_url}/' if current_page == 2 else f'{base_url}/page/{current_page - 1}/'
        html += f'  <a href="{prev_url}" class="pagination-btn" style="padding: 0.75rem 1.25rem; border: 2px solid #E68161; border-radius: 8px; color: #E68161; text-decoration: none; font-weight: 600; transition: all 0.3s;">← Vorige</a>\n'
    else:
        html += f'  <span class="pagination-btn disabled" style="padding: 0.75rem 1.25rem; border: 2px solid #e5e7eb; border-radius: 8px; color: #cbd5e0; font-weight: 600; cursor: not-allowed;">← Vorige</span>\n'
    
    # Numéros de page
    # Logique: toujours montrer 1, current-1, current, current+1, last
    pages_to_show = set()
    pages_to_show.add(1)
    pages_to_show.add(total_pages)
    
    for i in range(max(1, current_page - 1), min(total_pages + 1, current_page + 2)):
        pages_to_show.add(i)
    
    pages_list = sorted(pages_to_show)
    
    prev_page = 0
    for page in pages_list:
        # Ajouter "..." si gap
        if page > prev_page + 1:
            html += '  <span style="padding: 0.75rem 0.5rem; color: #cbd5e0;">...</span>\n'
        
        page_url = f'{base_url}/' if page == 1 else f'{base_url}/page/{page}/'
        
        if page == current_page:
            html += f'  <span class="pagination-number active" style="padding: 0.75rem 1rem; background: #E68161; color: white; border-radius: 8px; font-weight: 600; min-width: 45px; text-align: center;">{page}</span>\n'
        else:
            html += f'  <a href="{page_url}" class="pagination-number" style="padding: 0.75rem 1rem; border: 2px solid #e5e7eb; border-radius: 8px; color: #4a5568; text-decoration: none; font-weight: 600; min-width: 45px; text-align: center; transition: all 0.3s;">{page}</a>\n'
        
        prev_page = page
    
    # Bouton Suivant
    if current_page < total_pages:
        next_url = f'{base_url}/page/{current_page + 1}/'
        html += f'  <a href="{next_url}" class="pagination-btn" style="padding: 0.75rem 1.25rem; border: 2px solid #E68161; border-radius: 8px; color: #E68161; text-decoration: none; font-weight: 600; transition: all 0.3s;">Volgende →</a>\n'
    else:
        html += f'  <span class="pagination-btn disabled" style="padding: 0.75rem 1.25rem; border: 2px solid #e5e7eb; border-radius: 8px; color: #cbd5e0; font-weight: 600; cursor: not-allowed;">Volgende →</span>\n'
    
    html += '</div>\n'
    
    # Ajout du CSS pour hover
    html += '''
<style>
.pagination-number:hover:not(.active) {
  background: #f8fafc;
  border-color: #E68161 !important;
  color: #E68161 !important;
}
.pagination-btn:hover:not(.disabled) {
  background: #E68161;
  color: white !important;
}
</style>
'''
    
    return html

def create_page_html(template, current_page, total_pages, products_chunk):
    """Crée le HTML d'une page avec pagination"""
    
    # 1. Remplacer le title si ce n'est pas la page 1
    if current_page > 1:
        template = template.replace(
            '<title>Biologische Hondensnacks Winkel (2026) | Alle Natuurlijke Snacks Online</title>',
            f'<title>Biologische Hondensnacks Winkel - Pagina {current_page} | Natuurlijke Snacks</title>'
        )
    
    # 2. Mettre à jour la canonical URL
    canonical_url = 'https://biologische-hondensnacks.nl/winkel/'
    if current_page > 1:
        canonical_url = f'https://biologische-hondensnacks.nl/winkel/page/{current_page}/'
    
    template = template.replace(
        '<link rel="canonical" href="https://biologische-hondensnacks.nl/winkel/">',
        f'<link rel="canonical" href="{canonical_url}">'
    )
    
    # 3. Ajouter les balises prev/next pour SEO
    seo_links = ''
    if current_page > 1:
        prev_url = 'https://biologische-hondensnacks.nl/winkel/' if current_page == 2 else f'https://biologische-hondensnacks.nl/winkel/page/{current_page - 1}/'
        seo_links += f'<link rel="prev" href="{prev_url}">\n'
    
    if current_page < total_pages:
        next_url = f'https://biologische-hondensnacks.nl/winkel/page/{current_page + 1}/'
        seo_links += f'<link rel="next" href="{next_url}">\n'
    
    # Insérer après canonical
    template = template.replace(
        '<link rel="canonical"',
        seo_links + '<link rel="canonical"'
    )
    
    # 4. Injecter les données de pagination dans le HTML
    # Ajouter un script qui définit la page actuelle et les produits
    pagination_script = f'''
<script>
window.PAGINATION_CONFIG = {{
  currentPage: {current_page},
  totalPages: {total_pages},
  productsPerPage: {PRODUCTS_PER_PAGE},
  products: {json.dumps(products_chunk, ensure_ascii=False)}
}};
</script>
'''
    
    # Insérer avant </head>
    template = template.replace('</head>', pagination_script + '</head>')
    
    # 5. Remplacer le bouton "Load More" par la pagination
    pagination_html = create_pagination_html(current_page, total_pages)
    
    # Chercher et remplacer le conteneur loadMoreContainer
    template = template.replace(
        '<div id="loadMoreContainer"',
        f'<div id="paginationContainer" style="display: block;">{pagination_html}</div><div id="loadMoreContainer" style="display: none;"'
    )
    
    return template

def main():
    print("\n🔄 CREATE SEO-FRIENDLY PAGINATION")
    print("=" * 70)
    
    # 1. Charger les produits
    print(f"\n📦 Chargement des produits...")
    products = load_products()
    print(f"   ✅ {len(products)} produits chargés")
    
    # 2. Calculer le nombre de pages
    total_pages = math.ceil(len(products) / PRODUCTS_PER_PAGE)
    print(f"   📄 {total_pages} pages nécessaires ({PRODUCTS_PER_PAGE} produits/page)")
    
    # 3. Lire le template
    print(f"\n📄 Lecture du template HTML...")
    template = read_template()
    print(f"   ✅ Template chargé")
    
    # 4. Backup de l'original
    backup_path = os.path.join(WINKEL_DIR, 'index.html.before_pagination')
    shutil.copy2(TEMPLATE_HTML, backup_path)
    print(f"   💾 Backup: {backup_path}")
    
    # 5. Créer les pages
    print(f"\n🔨 Création des pages de pagination...")
    
    for page_num in range(1, total_pages + 1):
        # Calculer les indices de produits pour cette page
        start_idx = (page_num - 1) * PRODUCTS_PER_PAGE
        end_idx = start_idx + PRODUCTS_PER_PAGE
        products_chunk = products[start_idx:end_idx]
        
        # Créer le HTML
        page_html = create_page_html(template, page_num, total_pages, products_chunk)
        
        # Déterminer le chemin de sauvegarde
        if page_num == 1:
            output_path = TEMPLATE_HTML
        else:
            output_dir = os.path.join(WINKEL_DIR, 'page', str(page_num))
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            output_path = os.path.join(output_dir, 'index.html')
        
        # Sauvegarder
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        print(f"   ✅ Page {page_num}/{total_pages} créée: {output_path}")
    
    # 6. Mettre à jour le JavaScript pour gérer la pagination
    print(f"\n📝 Mise à jour du load-products.js...")
    js_path = os.path.join(WINKEL_DIR, 'load-products.js')
    
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Backup du JS
    js_backup = js_path + '.before_pagination'
    with open(js_backup, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    # Ajouter un code pour utiliser les produits paginés
    pagination_js = '''
// Pagination support
if (window.PAGINATION_CONFIG) {
  console.log(`📄 Page ${window.PAGINATION_CONFIG.currentPage}/${window.PAGINATION_CONFIG.totalPages}`);
  // Utiliser les produits de la page courante
  const paginatedProducts = window.PAGINATION_CONFIG.products;
  allProducts = paginatedProducts;
}
'''
    
    # Insérer après le chargement des produits
    js_content = js_content.replace(
        'console.log(`📦 ${products.length} produits chargés depuis le catalogue`);',
        'console.log(`📦 ${products.length} produits chargés depuis le catalogue`);\n' + pagination_js
    )
    
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"   ✅ JavaScript mis à jour")
    
    # 7. Résumé
    print(f"\n{'='*70}")
    print(f"✅ PAGINATION SEO-FRIENDLY CRÉÉE!")
    print(f"   Total pages: {total_pages}")
    print(f"   Produits par page: {PRODUCTS_PER_PAGE}")
    print(f"   Page 1: /winkel/")
    if total_pages > 1:
        print(f"   Pages 2-{total_pages}: /winkel/page/[2-{total_pages}]/")
    print(f"   Bouton 'Load More' remplacé par navigation pagination")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
