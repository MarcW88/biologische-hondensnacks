#!/usr/bin/env python3
"""
FIX HOMEPAGE ISSUES
===================

Corrige tous les problèmes de la homepage:
1. Hero section: améliorer visibilité titre/texte
2. Supprimer soulignement liens
3. Section Top 3: retirer "top 3", améliorer structure
4. Témoignages: remettre images Unsplash
5. Blog: corriger structure
6. FAQ: corriger structure et centrage
7. Footer: remplacer par celui du winkel

Auteur: AI Assistant
Date: December 2025
"""

from bs4 import BeautifulSoup
import re

def fix_homepage():
    """Corrige tous les problèmes de la homepage"""
    
    input_file = '/Users/marc/Desktop/biologische-hondensnacks/index.html'
    
    # Lire le fichier
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Backup
    backup_file = input_file + '.fixes_backup'
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("🔧 FIXING HOMEPAGE ISSUES")
    print("=" * 60)
    
    # 1. HERO SECTION: Améliorer visibilité titre/texte
    print("\n1. Fixing Hero Section...")
    hero_h1 = soup.find('h1')
    if hero_h1:
        # Augmenter taille et ombre
        style = hero_h1.get('style', '')
        style = re.sub(r'font-size:\s*[\d.]+rem', 'font-size: 4rem', style)
        style = re.sub(r'text-shadow:[^;]+', 'text-shadow: 0 4px 20px rgba(0,0,0,0.7), 0 2px 10px rgba(0,0,0,0.5)', style)
        style = re.sub(r'font-weight:\s*\d+', 'font-weight: 800', style)
        hero_h1['style'] = style
        print("   ✅ Hero H1: font-size 4rem, text-shadow amélioré, font-weight 800")
    
    # Améliorer le paragraphe hero
    hero_section = soup.find('section', class_='hero')
    if hero_section:
        hero_p = hero_section.find('p')
        if hero_p:
            style = hero_p.get('style', '')
            style = re.sub(r'font-size:\s*[\d.]+rem', 'font-size: 1.6rem', style)
            style = re.sub(r'text-shadow:[^;]+', 'text-shadow: 0 3px 10px rgba(0,0,0,0.6), 0 2px 5px rgba(0,0,0,0.4)', style)
            if 'font-weight' not in style:
                style += ' font-weight: 500;'
            hero_p['style'] = style
            print("   ✅ Hero paragraph: font-size 1.6rem, text-shadow amélioré")
    
    # 2. SUPPRIMER SOULIGNEMENT LIENS
    print("\n2. Removing link underlines...")
    all_links = soup.find_all('a')
    count = 0
    for link in all_links:
        style = link.get('style', '')
        if 'text-decoration' not in style:
            style += ' text-decoration: none;'
            link['style'] = style
            count += 1
    print(f"   ✅ {count} liens modifiés pour retirer soulignement")
    
    # 3. SECTION TOP 3
    print("\n3. Fixing Top 3 Section...")
    # Trouver la section top products
    top_section = soup.find('section', id='top-products')
    if top_section:
        # Modifier le titre
        h2 = top_section.find('h2')
        if h2:
            h2.string = h2.get_text().replace('- top 3', '').replace('- Top 3', '').replace('TOP 3', '').strip()
            print(f"   ✅ Titre modifié: {h2.get_text()}")
        
        # Trouver tous les produits et améliorer leur structure
        product_cards = top_section.find_all('div', class_=re.compile(r'product-card|product', re.I))
        for card in product_cards:
            # Ajouter du style pour meilleure visibilité
            card['style'] = card.get('style', '') + ' border: 1px solid #e5e7eb; border-radius: 12px; padding: 1.5rem; background: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'
            
            # Prix: le rendre plus visible
            price = card.find(class_=re.compile(r'price', re.I))
            if price:
                price['style'] = 'font-size: 1.5rem; font-weight: 700; color: #E68161; margin: 1rem 0;'
            
            # Grammage: le mettre sous le titre
            weight = card.find(string=re.compile(r'\d+\s*g|\d+\s*kg', re.I))
            if weight and weight.parent:
                weight.parent['style'] = 'font-size: 0.9rem; color: #6b7280; margin-bottom: 0.5rem;'
        
        print(f"   ✅ {len(product_cards)} product cards restructurées")
    
    # Retirer "beperkte voorraad" et "morgen in huis"
    for elem in soup.find_all(string=re.compile(r'beperkte voorraad|morgen in huis', re.I)):
        parent = elem.parent
        if parent:
            parent.decompose()
    print("   ✅ Retiré 'beperkte voorraad' et 'morgen in huis'")
    
    # 4. TÉMOIGNAGES: Remettre Unsplash
    print("\n4. Fixing testimonials images...")
    testimonial_images = [
        'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop',
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop',
        'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop'
    ]
    
    # Trouver la section qui contient "Wat Zeggen Onze Klanten"
    for section in soup.find_all('section'):
        h_tag = section.find(['h2', 'h3'])
        if h_tag and 'wat zeggen onze klanten' in h_tag.get_text().lower():
            # Chercher les divs avec class testimonial-image
            testimonial_divs = section.find_all('div', class_='testimonial-image')
            for idx, div in enumerate(testimonial_divs[:3]):
                if idx < len(testimonial_images):
                    style = div.get('style', '')
                    # Remplacer l'URL de background
                    new_style = re.sub(r'background:\s*url\([^)]+\)', f"background: url('{testimonial_images[idx]}')", style)
                    if new_style == style:
                        # Si pas de background trouvé, l'ajouter
                        new_style = style + f" background: url('{testimonial_images[idx]}') center/cover;"
                    div['style'] = new_style
            print(f"   ✅ {len(testimonial_divs[:3])} images témoignages remises à Unsplash")
            break
    
    # 5. BLOG SECTION
    print("\n5. Fixing Blog Section...")
    # Trouver la section "Laatste blog artikelen"
    for section in soup.find_all('section'):
        h_tag = section.find(['h2', 'h3'])
        if h_tag and 'laatste blog artikelen' in h_tag.get_text().lower():
            # Chercher le conteneur des articles
            blog_grid = section.find('div', class_='blog-grid')
            if not blog_grid:
                # Chercher n'importe quel div avec des articles
                blog_grid = section.find('div', style=re.compile(r'grid|flex', re.I))
            
            if blog_grid:
                # Forcer la structure grid
                blog_grid['style'] = 'display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin-top: 2rem;'
                print("   ✅ Blog grid structure corrigée")
            else:
                print("   ⚠️  Blog grid container non trouvé")
            break
    
    # 6. FAQ SECTION
    print("\n6. Fixing FAQ Section...")
    # Chercher une section avec "vraag" ou "faq" dans le titre
    faq_found = False
    for section in soup.find_all('section'):
        h_tag = section.find(['h2', 'h3'])
        if h_tag:
            title_text = h_tag.get_text().lower()
            if 'faq' in title_text or 'vraag' in title_text or 'veelgestelde' in title_text:
                # Centrer la section
                section['style'] = section.get('style', '') + ' max-width: 900px; margin: 0 auto; padding: 3rem 1rem;'
                
                # S'assurer que les items FAQ sont bien structurés
                faq_items = section.find_all('div', class_=re.compile(r'faq-item|accordion', re.I))
                if not faq_items:
                    # Chercher les details/summary (format HTML5)
                    faq_items = section.find_all('details')
                
                for item in faq_items:
                    item['style'] = item.get('style', '') + ' margin-bottom: 1.5rem; border: 1px solid #e5e7eb; border-radius: 8px; padding: 1rem; background: white;'
                
                print(f"   ✅ FAQ trouvée et centrée avec {len(faq_items)} items restructurés")
                faq_found = True
                break
    
    if not faq_found:
        print("   ⚠️  Section FAQ non trouvée sur la page")
    
    # 7. FOOTER: Remplacer par celui du winkel
    print("\n7. Replacing Footer...")
    new_footer = '''
    <!-- Footer -->
    <footer style="background: #374151; color: #e5e7eb; padding: 3rem 0 1rem 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 3rem; margin-bottom: 2rem;">
                
                <!-- About -->
                <div>
                    <h3 style="color: #E68161; margin-bottom: 1rem; font-size: 1.25rem;">Biologische Hondensnacks</h3>
                    <p style="color: #9ca3af; line-height: 1.6; margin: 0;">
                        Wij bieden de beste biologische en natuurlijke hondensnacks voor jouw trouwe viervoeter. 
                        Kwaliteit en gezondheid staan bij ons voorop.
                    </p>
                </div>
                
                <!-- Navigatie -->
                <div>
                    <h3 style="color: #E68161; margin-bottom: 1rem; font-size: 1.25rem;">Navigatie</h3>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="/" style="color: #e5e7eb; text-decoration: none;">Home</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="/winkel/" style="color: #e5e7eb; text-decoration: none;">Winkel</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="/blog/" style="color: #e5e7eb; text-decoration: none;">Blog</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="/over-ons/" style="color: #e5e7eb; text-decoration: none;">Over ons</a></li>
                    </ul>
                </div>
                
                <!-- Juridisch -->
                <div>
                    <h3 style="color: #E68161; margin-bottom: 1rem; font-size: 1.25rem;">Juridisch</h3>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="/privacy-policy/" style="color: #e5e7eb; text-decoration: none;">Privacy policy</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="/algemene-voorwaarden/" style="color: #e5e7eb; text-decoration: none;">Algemene voorwaarden</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="/disclaimer/" style="color: #e5e7eb; text-decoration: none;">Disclaimer</a></li>
                    </ul>
                </div>
                
            </div>
            
            <!-- Footer Bottom -->
            <div style="border-top: 1px solid #4b5563; padding-top: 1.5rem; text-align: center;">
                <p style="margin: 0 0 1rem 0; color: #9ca3af; font-size: 0.9rem;">
                    <strong>Disclaimer:</strong> De informatie op deze website is alleen bedoeld voor algemene doeleinden 
                    en vervangt geen professioneel veterinair advies. Raadpleeg altijd je dierenarts voor specifieke 
                    voedings- en gezondheidsadvies voor je hond.
                </p>
                <p style="margin: 0; color: #9ca3af; font-size: 0.9rem;">
                    &copy; 2026 Biologische hondensnacks. Alle rechten voorbehouden. | Gemaakt voor honden en hun baasjes
                </p>
            </div>
        </div>
    </footer>
    '''
    
    # Retirer l'ancien footer
    old_footer = soup.find('footer')
    if old_footer:
        old_footer.decompose()
    
    # Ajouter le nouveau footer avant la fermeture du body
    body = soup.find('body')
    if body:
        body.append(BeautifulSoup(new_footer, 'html.parser'))
        print("   ✅ Nouveau footer ajouté (style winkel)")
    
    # Sauvegarder
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    print(f"\n{'='*60}")
    print("🎉 TOUTES LES CORRECTIONS APPLIQUÉES!")
    print(f"💾 Backup: {backup_file}")
    print(f"{'='*60}")

if __name__ == "__main__":
    fix_homepage()
