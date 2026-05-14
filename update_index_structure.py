#!/usr/bin/env python3
"""
Script pour mettre à jour index.html pour suivre la structure de italiaanse-percolator
"""

from pathlib import Path

def update_index_html():
    """Met à jour index.html avec la structure de italiaanse-percolator"""
    index_file = Path('index.html')
    
    if not index_file.exists():
        print(f"Erreur: {index_file} n'existe pas")
        return
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer le hero section avec la structure de italiaanse-percolator
    old_hero = '''  <!-- Hero -->
  <section>
   <div class="container">
    <div>
     <h1>
      Natuurlijke hondensnacks die je hond verdient
     </h1>
     <p>
      Biologisch en gezond verwennen
     </p>
     <div>
      <a class="btn btn-primary" href="winkel.html">Ontdek de winkel →</a>
      <a class="btn btn-outline" href="beste-hondensnacks-2026/">Bekijk onze top 10 →</a>
     </div>
    </div>
   </div>
  </section>'''
    
    new_hero = '''<!-- Hero -->
<section style="background: var(--surface-soft); padding: 4.5rem 0;">
<div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center; max-width: 1100px;">
<div>
<p style="font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1.25rem;">Onafhankelijke gids sinds 2026</p>
<h1 style="font-family: var(--font-serif); font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 400; line-height: 1.15; color: var(--text); margin-bottom: 1.5rem;">De beste biologische hondensnacks, getest en vergeleken</h1>
<p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-dim); max-width: 460px;">
Wij testen hondensnacks in ons eigen laboratorium. 500+ producten, van €2 tot €100, eerlijk vergeleken zodat jij de juiste keuze maakt.
</p>
<div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
<a class="btn btn-primary" href="winkel.html">Bekijk de winkel</a>
<a class="btn btn-secondary" href="beste-hondensnacks-2026/">Bekijk top 10</a>
</div>
<div style="display: flex; gap: 2rem; margin-top: 2.5rem; font-size: 0.8rem; color: var(--text-light);">
<span>500+ producten getest</span>
<span>Onafhankelijke selectie</span>
<span>100% biologisch</span>
</div>
</div>
<div style="position: relative;">
<img alt="Biologische hondensnacks" src="images/biologische-hondensnacks-hero.jpg" style="width: 100%; border-radius: 0.5rem; aspect-ratio: 4/3; object-fit: cover;"/>
</div>
</div>
</section>'''
    
    content = content.replace(old_hero, new_hero)
    
    # Sauvegarder
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {index_file} mis à jour")

if __name__ == '__main__':
    update_index_html()
