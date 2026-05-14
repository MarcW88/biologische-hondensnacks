#!/usr/bin/env python3
"""
Script pour générer les pages produits de snacks biologiques pour chien
Basé sur le template de italiaanse-percolator
"""

import json
import re
import html as html_mod
from pathlib import Path

ROOT = Path(__file__).parent
PRODUCTS = json.load(open(ROOT / 'filtered_dog_snacks.json', encoding='utf-8'))
OUT_DIR = ROOT / 'produits'
OUT_DIR.mkdir(exist_ok=True)

def h(text):
    return html_mod.escape(str(text))

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def generate_page(product):
    """Génère une page produit HTML avec la structure de italiaanse-percolator"""
    title = h(product.get('title', ''))
    ean = product.get('ean', '')
    product_id = product.get('product_id', '')
    price = product.get('price_nl', '')
    image_url = product.get('image_url', '')
    product_url = product.get('product_url_nl', '')
    brand = h(product.get('brand', ''))
    description = h(product.get('description', ''))
    
    # Créer un slug à partir du titre
    slug = slugify(title)
    
    # Formater le prix
    if price:
        try:
            price_float = float(price)
            price_display = f"ca. €{price_float:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        except:
            price_display = f"ca. €{price}"
    else:
        price_display = "Prijs niet beschikbaar"
    
    # HTML template basé sur italiaanse-percolator
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} | Biologische Hondensnacks</title>
<meta content="{description[:150]}" name="description"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Outfit:wght@400;600;700&amp;family=DM+Serif+Display:ital,wght@0,400&amp;display=swap" rel="stylesheet"/>
<link href="../css/styles.css" rel="stylesheet"/>
<link href="../favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="../favicon-simple.svg" rel="icon" sizes="16x16" type="image/svg+xml"/>
<link href="../favicon.svg" rel="apple-touch-icon" sizes="180x180"/>
<meta content="var(--primary)" name="theme-color"/>
</head>
<body>
<nav class="navbar">
<div class="container">
<div class="nav-container">
<a class="nav-brand" href="../index.html">Biologische Hondensnacks</a>
<button class="mobile-menu-toggle" aria-label="Menu">
<span></span>
<span></span>
<span></span>
</button>
<ul class="nav-menu">
<li><a class="nav-link" href="../index.html">Home</a></li>
<li><a class="nav-link" href="../natuurlijke-hondensnacks/">Natuurlijke snacks</a></li>
<li><a class="nav-link" href="../beste-hondensnacks-2026/">Top 10</a></li>
<li><a class="nav-link" href="../winkel.html">Winkel</a></li>
</ul>
</div>
</div>
</nav>
<div class="mobile-menu-overlay"></div>

<!-- Hero -->
<section class="section" style="background: var(--surface-soft);">
<div class="container">
<div class="grid grid-2" style="gap: var(--sp-14); align-items: center;">
<div>
<p class="kicker">Biologisch hondensnack</p>
<h1 style="font-family: var(--font-serif); font-size: var(--fs-3xl); font-weight: 400; line-height: 1.15; color: var(--text); margin-bottom: var(--sp-6);">{title}</h1>
<p class="text-dim" style="max-width: 460px;">
{description[:200]}...
</p>
<div style="display: flex; gap: var(--sp-3); flex-wrap: wrap; margin-top: var(--sp-6);">
<a class="btn btn-primary" href="{product_url}" rel="nofollow noopener" target="_blank">Bekijk op Bol.com</a>
<a class="btn btn-secondary" href="../winkel.html">Terug naar winkel</a>
</div>
<div style="display: flex; gap: var(--sp-8); margin-top: var(--sp-10); font-size: var(--fs-sm); color: var(--text-light);">
<span>Biologisch</span>
<span>Natuurlijk</span>
<span>Gezond</span>
</div>
</div>
<div style="position: relative;">
<img alt="{title}" src="{image_url}" style="width: 100%; border-radius: var(--r-lg); aspect-ratio: 4/3; object-fit: cover;"/>
</div>
</div>
</div>
</section>

<!-- Product Details -->
<section class="section">
<div class="container">
<h2 style="font-family: var(--font-display); margin-bottom: var(--sp-2);">Productdetails</h2>
<p class="text-dim" style="margin-bottom: var(--sp-10); max-width: 560px;">Alles wat je moet weten over dit biologische hondensnack.</p>
<div class="grid grid-3" style="gap: var(--sp-8);">
<div>
<h4 style="font-size: var(--fs-sm); font-weight: 600; margin-bottom: var(--sp-2);">Merk</h4>
<p class="text-sm text-dim">{brand}</p>
</div>
<div>
<h4 style="font-size: var(--fs-sm); font-weight: 600; margin-bottom: var(--sp-2);">Prijs</h4>
<p class="text-sm text-dim">{price_display}</p>
</div>
<div>
<h4 style="font-size: var(--fs-sm); font-weight: 600; margin-bottom: var(--sp-2);">Biologisch</h4>
<p class="text-sm text-dim">Ja, 100% natuurlijk</p>
</div>
</div>
</div>
</section>

<!-- Description -->
<section class="section-sm" style="border-top: 1px solid var(--border);">
<div class="container" style="max-width: 780px;">
<h2 style="font-family: var(--font-display); margin-bottom: var(--sp-6);">Beschrijving</h2>
<p class="text-dim" style="margin-bottom: var(--sp-6); line-height: 1.7;">
{description}
</p>
</div>
</section>

<!-- FAQ -->
<section class="section-sm faq-section">
<div class="container faq-container">
<h2 class="faq-title">Veelgestelde vragen</h2>
<div class="faq-list">
<details class="faq-item">
<summary>Is dit hondensnack biologisch?</summary>
<p class="text-dim">Ja, dit product is gemaakt van 100% natuurlijke ingrediënten zonder kunstmatige toevoegingen.</p>
</details>
<details class="faq-item">
<summary>Voor welke honden is dit snack geschikt?</summary>
<p class="text-dim">Dit snack is geschikt voor alle hondenrassen en leeftijden. Raadpleeg altijd de verpakking voor specifieke informatie.</p>
</details>
<details class="faq-item">
<summary>Hoe bewaar ik dit hondensnack?</summary>
<p class="text-dim">Bewaar op een koele, droge plaats en sluit de verpakking goed af na gebruik.</p>
</details>
</div>
</div>
</section>

<!-- Footer -->
<footer class="footer">
<div class="container">
<div class="grid" style="grid-template-columns: 2fr repeat(3, 1fr); gap: var(--sp-12);">
<div>
<p style="font-family: var(--font-serif); font-size: var(--fs-xl); color: white; margin-bottom: var(--sp-4);">Biologische Hondensnacks</p>
<p style="color: #999; font-size: var(--fs-sm); line-height: 1.7; margin-bottom: 0;">
De beste biologische en natuurlijke hondensnacks voor jouw trouwe viervoeter.
</p>
</div>
<div>
<h4 style="color: white; font-size: var(--fs-xs); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: var(--sp-4);">Gidsen</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin-bottom: var(--sp-2);"><a href="../beste-hondensnacks-2026/" style="color: #aaa; font-size: var(--fs-sm);">Top 10 hondensnacks</a></li>
<li style="margin-bottom: var(--sp-2);"><a href="../natuurlijke-hondensnacks/" style="color: #aaa; font-size: var(--fs-sm);">Natuurlijke snacks</a></li>
<li style="margin-bottom: var(--sp-2);"><a href="../hondensnacks-voor-puppy/" style="color: #aaa; font-size: var(--fs-sm);">Puppy snacks</a></li>
</ul>
</div>
<div>
<h4 style="color: white; font-size: var(--fs-xs); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: var(--sp-4);">Winkel</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin-bottom: var(--sp-2);"><a href="../winkel.html" style="color: #aaa; font-size: var(--fs-sm);">Alle producten</a></li>
<li style="margin-bottom: var(--sp-2);"><a href="../kauwsnacks-tandverzorging/" style="color: #aaa; font-size: var(--fs-sm);">Kauwsnacks</a></li>
<li style="margin-bottom: var(--sp-2);"><a href="../hypoallergene-hondensnacks/" style="color: #aaa; font-size: var(--fs-sm);">Hypoallergeen</a></li>
</ul>
</div>
<div>
<h4 style="color: white; font-size: var(--fs-xs); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: var(--sp-4);">Info</h4>
<ul style="list-style: none; padding: 0;">
<li style="margin-bottom: var(--sp-2);"><a href="../over-ons/" style="color: #aaa; font-size: var(--fs-sm);">Over ons</a></li>
<li style="margin-bottom: var(--sp-2);"><a href="../blog/" style="color: #aaa; font-size: var(--fs-sm);">Blog</a></li>
</ul>
</div>
</div>
<div style="border-top: 1px solid #333; padding-top: var(--sp-6); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: var(--sp-4);">
<p style="color: #666; font-size: var(--fs-xs); margin: 0;">© 2026 Biologische hondensnacks. Alle rechten voorbehouden.</p>
<p style="color: #666; font-size: var(--fs-xs); margin: 0;">Deze site bevat partnerlinks. Bij aankoop ontvangen wij een commissie, zonder extra kosten voor jou.</p>
</div>
</div>
</footer>

<script>
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuToggle) {{
    mobileMenuToggle.addEventListener('click', () => {{
        mobileMenuToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        mobileMenuOverlay.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    }});
}}

if (mobileMenuOverlay) {{
    mobileMenuOverlay.addEventListener('click', () => {{
        mobileMenuToggle.classList.remove('active');
        navMenu.classList.remove('active');
        mobileMenuOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }});
}}
</script>

</body>
</html>'''
    
    return slug, html

def main():
    """Fonction principale"""
    print(f"Génération de {len(PRODUCTS)} pages produits...")
    
    for i, product in enumerate(PRODUCTS):
        try:
            slug, html = generate_page(product)
            
            # Sauvegarder la page
            output_file = OUT_DIR / f"{slug}.html"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
            
            if (i + 1) % 50 == 0:
                print(f"Progression: {i + 1}/{len(PRODUCTS)} pages générées...")
        
        except Exception as e:
            print(f"Erreur génération page {i}: {e}")
            continue
    
    print(f"\nTerminé! {len(PRODUCTS)} pages générées dans {OUT_DIR}")

if __name__ == '__main__':
    main()
