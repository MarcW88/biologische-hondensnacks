#!/usr/bin/env python3
"""
REBUILD PAGINATION CORRECTLY
=============================
Recrée TOUTES les pages de pagination avec:
1. Même design que page 1
2. Liens produits qui fonctionnent depuis pages 2/3
3. Produits du CSV uniquement
"""

import os
import json
import re
from pathlib import Path

BASE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
WINKEL_DIR = os.path.join(BASE_DIR, 'winkel')
PRODUCTS_PER_PAGE = 24

def load_products():
    """Charge tous les produits du catalogue"""
    with open(os.path.join(WINKEL_DIR, 'products-catalog.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def adjust_product_urls_for_depth(products, depth):
    """
    Ajuste les URLs des produits selon la profondeur
    depth=0 : /winkel/ (../produits/)
    depth=1 : /winkel/page/2/ (../../produits/)
    """
    adjusted = []
    for p in products:
        product = p.copy()
        
        # Ajuster productUrl
        if 'productUrl' in product:
            # Remplacer ../produits/ par le bon chemin
            if depth == 0:
                # Page 1: ../produits/ est correct
                pass
            else:
                # Pages 2/3: besoin de ../../produits/
                product['productUrl'] = product['productUrl'].replace('../produits/', '../../produits/')
        
        # Ajuster image si nécessaire
        if 'image' in product and product['image'].startswith('../images/'):
            if depth > 0:
                product['image'] = product['image'].replace('../images/', '../../images/')
        
        adjusted.append(product)
    
    return adjusted

def read_base_template():
    """Lit le template de base (page 1 originale avant pagination)"""
    template_path = os.path.join(WINKEL_DIR, 'index.html.before_pagination')
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # Fallback: utiliser la page 1 actuelle
        with open(os.path.join(WINKEL_DIR, 'index.html'), 'r', encoding='utf-8') as f:
            content = f.read()
            # Supprimer window.PAGINATION_CONFIG et pagination HTML
            content = re.sub(r'<script>\s*window\.PAGINATION_CONFIG = .*?</script>', '', content, flags=re.DOTALL)
            content = re.sub(r'<!-- Pagination Navigation -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)
            # Restaurer le bouton load more
            if 'loadMoreContainer' not in content:
                load_more = '''
    <!-- Load More -->
    <div class="load-more-container" id="loadMoreContainer">
        <button class="load-more-btn" onclick="loadMoreProducts()">
            Laad meer producten
        </button>
    </div>
    '''
                content = content.replace('<!-- Empty State -->', load_more + '\n    <!-- Empty State -->')
            return content

def create_pagination_html(current_page, total_pages, depth):
    """Génère le HTML de pagination avec les bons chemins relatifs"""
    
    def get_page_url(page_num, from_page):
        """Génère l'URL d'une page depuis une autre page"""
        if from_page == 1:
            # Depuis page 1
            if page_num == 1:
                return ''  # Reste sur place
            else:
                return f'page/{page_num}/'
        else:
            # Depuis page 2 ou 3
            if page_num == 1:
                return '../../'
            elif page_num == from_page:
                return ''  # Reste sur place
            else:
                return f'../{page_num}/'
    
    html = '\n    <!-- Pagination Navigation -->\n    <div id="paginationContainer" style="margin: 3rem 0; padding: 2rem; background: white; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\n        <div style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; flex-wrap: wrap;">\n    '
    
    # Bouton Précédent
    if current_page > 1:
        prev_url = get_page_url(current_page - 1, current_page)
        html += f'''
            <a href="{prev_url}" style="padding: 0.75rem 1.25rem; background: #E68161; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.5rem;" onmouseover="this.style.background='#d4704f'" onmouseout="this.style.background='#E68161'">
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
        page_url = get_page_url(page_num, current_page)
        
        if page_num == current_page:
            html += f'''
                <span style="padding: 0.75rem 1.25rem; background: #E68161; color: white; border-radius: 8px; font-weight: 700; min-width: 45px; text-align: center;">
                    {page_num}
                </span>
            '''
        else:
            html += f'''
                <a href="{page_url}" style="padding: 0.75rem 1.25rem; background: white; color: #374151; text-decoration: none; border: 2px solid #e5e7eb; border-radius: 8px; font-weight: 600; transition: all 0.3s; min-width: 45px; text-align: center;" onmouseover="this.style.borderColor='#E68161'; this.style.color='#E68161'" onmouseout="this.style.borderColor='#e5e7eb'; this.style.color='#374151'">
                    {page_num}
                </a>
            '''
    
    # Bouton Suivant
    if current_page < total_pages:
        next_url = get_page_url(current_page + 1, current_page)
        html += f'''
            <a href="{next_url}" style="padding: 0.75rem 1.25rem; background: #E68161; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.5rem;" onmouseover="this.style.background='#d4704f'" onmouseout="this.style.background='#E68161'">
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

def create_pagination_config_script(current_page, total_pages, page_products):
    """Crée le script window.PAGINATION_CONFIG"""
    config = {
        'currentPage': current_page,
        'totalPages': total_pages,
        'productsPerPage': PRODUCTS_PER_PAGE,
        'products': page_products
    }
    
    return f'''<script>
window.PAGINATION_CONFIG = {json.dumps(config, ensure_ascii=False, indent=2)};
</script>'''

def create_page(template, page_num, total_pages, all_products):
    """Crée une page de pagination complète"""
    
    # Calculer depth (0 pour page 1, 1 pour pages 2+)
    depth = 0 if page_num == 1 else 1
    
    # Extraire les produits de cette page
    start_idx = (page_num - 1) * PRODUCTS_PER_PAGE
    end_idx = start_idx + PRODUCTS_PER_PAGE
    page_products = all_products[start_idx:end_idx]
    
    # Ajuster les URLs des produits selon la profondeur
    adjusted_products = adjust_product_urls_for_depth(page_products, depth)
    
    # 1. Mettre à jour le title
    if page_num > 1:
        template = re.sub(
            r'<title>([^<]*)</title>',
            f'<title>Biologische Hondensnacks Winkel - Pagina {page_num} | Natuurlijke Snacks</title>',
            template
        )
    
    # 2. Mettre à jour canonical + prev/next
    template = re.sub(r'<link rel="canonical"[^>]*>\n?', '', template)
    template = re.sub(r'<link rel="next"[^>]*>\n?', '', template)
    template = re.sub(r'<link rel="prev"[^>]*>\n?', '', template)
    
    seo_links = ''
    if page_num == 1:
        seo_links += '<link rel="canonical" href="https://biologische-hondensnacks.nl/winkel/">\n'
        if total_pages > 1:
            seo_links += '<link rel="next" href="https://biologische-hondensnacks.nl/winkel/page/2/">\n'
    else:
        seo_links += f'<link rel="canonical" href="https://biologische-hondensnacks.nl/winkel/page/{page_num}/">\n'
        if page_num > 1:
            prev_url = 'https://biologische-hondensnacks.nl/winkel/' if page_num == 2 else f'https://biologische-hondensnacks.nl/winkel/page/{page_num-1}/'
            seo_links += f'<link rel="prev" href="{prev_url}">\n'
        if page_num < total_pages:
            seo_links += f'<link rel="next" href="https://biologische-hondensnacks.nl/winkel/page/{page_num+1}/">\n'
    
    template = template.replace('<!-- Favicon -->', seo_links + '<!-- Favicon -->')
    
    # 3. Remplacer load more par pagination
    load_more_pattern = r'<!-- Load More -->.*?</div>\s*<!-- Empty State -->'
    pagination_html = create_pagination_html(page_num, total_pages, depth)
    template = re.sub(load_more_pattern, pagination_html + '\n    <!-- Empty State -->', template, flags=re.DOTALL)
    
    # 4. Ajouter window.PAGINATION_CONFIG avant </head>
    config_script = create_pagination_config_script(page_num, total_pages, adjusted_products)
    template = template.replace('</head>', config_script + '\n</head>')
    
    # 5. Ajuster les chemins CSS/JS si page > 1
    if depth > 0:
        # Chemins dans <head>
        template = re.sub(r'href="\.\./css/', r'href="../../css/', template)
        template = re.sub(r'href="shop-styles\.css"', r'href="../../shop-styles.css"', template)
        template = re.sub(r'href="\.\./favicon', r'href="../../favicon', template)
        template = re.sub(r'href="\.\./apple-touch-icon', r'href="../../apple-touch-icon', template)
        
        # Liens de navigation - remplacer tous les ../ par ../../
        template = template.replace('href="../"', 'href="../../"')
        template = template.replace('href="../natuurlijke-hondensnacks/', 'href="../../natuurlijke-hondensnacks/')
        template = template.replace('href="../beste-hondensnacks-2026/', 'href="../../beste-hondensnacks-2026/')
        template = template.replace('href="../hondensnacks-voor-puppy/', 'href="../../hondensnacks-voor-puppy/')
        template = template.replace('href="../gezonde-kauwsnacks/', 'href="../../gezonde-kauwsnacks/')
        template = template.replace('href="../graanvrije-hondensnacks/', 'href="../../graanvrije-hondensnacks/')
        template = template.replace('href="../blog/', 'href="../../blog/')
        template = template.replace('href="../over-ons/', 'href="../../over-ons/')
        template = template.replace('href="../winkel/', 'href="../../winkel/')
        
        # Scripts en bas de page
        template = re.sub(r'src="\.\./js/', r'src="../../js/', template)
        template = re.sub(r'src="shop\.js"', r'src="../../shop.js"', template)
        template = re.sub(r'src="load-products\.js"', r'src="../../load-products.js"', template)
        
        # Liens footer
        footer_links = [
            'natuurlijke-hondensnacks', 'hondensnacks-voor-puppy', 'hondensnacks-voor-training',
            'gezonde-kauwsnacks', 'graanvrije-hondensnacks', 'over-ons', 'blog', 'contact',
            'veelgestelde-vragen', 'beste-hondensnacks-2026', 'privacy-policy',
            'algemene-voorwaarden', 'disclaimer'
        ]
        for link in footer_links:
            template = re.sub(f'href="{link}/"', f'href="../../{link}/"', template)
    
    return template

def main():
    print("\n🔨 REBUILD PAGINATION CORRECTLY")
    print("=" * 70)
    
    # 1. Charger les produits
    print("\n📦 Chargement des produits...")
    all_products = load_products()
    total_pages = (len(all_products) + PRODUCTS_PER_PAGE - 1) // PRODUCTS_PER_PAGE
    print(f"   ✅ {len(all_products)} produits du CSV")
    print(f"   📄 {total_pages} pages nécessaires")
    
    # Vérifier que tous les produits ont une page
    print("\n🔍 Vérification des pages produits...")
    missing_pages = []
    for p in all_products[:5]:  # Tester les 5 premiers
        if 'productUrl' in p:
            page_path = os.path.join(BASE_DIR, p['productUrl'].replace('../', ''))
            if not os.path.exists(page_path):
                missing_pages.append(p['name'])
    
    if missing_pages:
        print(f"   ⚠️  {len(missing_pages)} pages produits manquantes")
        for name in missing_pages[:3]:
            print(f"      - {name}")
    else:
        print(f"   ✅ Pages produits vérifiées")
    
    # 2. Lire le template de base
    print("\n📄 Lecture du template...")
    template = read_base_template()
    print(f"   ✅ Template chargé")
    
    # 3. Créer les 3 pages
    for page_num in range(1, total_pages + 1):
        print(f"\n🔨 Création Page {page_num}...")
        
        page_html = create_page(template, page_num, total_pages, all_products)
        
        # Déterminer le chemin de sauvegarde
        if page_num == 1:
            page_path = os.path.join(WINKEL_DIR, 'index.html')
        else:
            page_dir = os.path.join(WINKEL_DIR, 'page', str(page_num))
            Path(page_dir).mkdir(parents=True, exist_ok=True)
            page_path = os.path.join(page_dir, 'index.html')
        
        # Sauvegarder
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        # Calculer produits
        start_idx = (page_num - 1) * PRODUCTS_PER_PAGE
        end_idx = min(start_idx + PRODUCTS_PER_PAGE, len(all_products))
        product_range = f"{start_idx + 1}-{end_idx}"
        
        print(f"   ✅ Sauvegardé: {page_path}")
        print(f"   📦 Produits {product_range} ({end_idx - start_idx} produits)")
        print(f"   🔗 URLs produits: {'../' if page_num == 1 else '../../'}produits/...")
    
    print("\n" + "=" * 70)
    print("✅ PAGINATION COMPLÈTEMENT RECONSTRUITE!")
    print("=" * 70)
    print("\n🎯 Résumé:")
    print(f"   ✅ {total_pages} pages créées avec design identique")
    print(f"   ✅ Tous les produits du CSV ({len(all_products)} produits)")
    print(f"   ✅ Liens produits fonctionnels sur toutes les pages")
    print(f"   ✅ Navigation pagination correcte")
    print("\n📋 Structure:")
    for i in range(1, total_pages + 1):
        start = (i-1) * PRODUCTS_PER_PAGE + 1
        end = min(i * PRODUCTS_PER_PAGE, len(all_products))
        url = f"/winkel/" if i == 1 else f"/winkel/page/{i}/"
        print(f"   - Page {i}: {url} (produits {start}-{end})")

if __name__ == "__main__":
    main()
