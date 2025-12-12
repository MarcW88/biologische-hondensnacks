#!/usr/bin/env python3
"""
UPDATE HERO SECTION - HOMEPAGE
==============================

Met à jour la hero section avec le nouveau positionnement
comme guide comparatif (type Sleeps/Wirecutter).

Auteur: AI Assistant
Date: December 2025
"""

import re

def update_hero_section():
    """Met à jour la hero section"""
    
    input_file = '/Users/marc/Desktop/biologische-hondensnacks/index.html'
    
    # Lire le fichier
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    backup_file = input_file + '.hero_backup'
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Nouvelle hero section
    new_hero = '''<section class="hero" style="background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80') center/cover; color: white; padding: 80px 0;">
        <div class="container">
            <div class="hero-content" style="text-align: center; max-width: 900px; margin: 0 auto;">
                
                <!-- Hero Text Block -->
                <div class="hero-text-block" style="padding: 2rem 1rem; margin-bottom: 2rem;">
                    <h1 style="font-size: 3.2rem; margin-bottom: 1.5rem; font-weight: 700; line-height: 1.2; color: #ffffff; text-shadow: 0 2px 10px rgba(0,0,0,0.3);">
                        Gezonde hondensnacks kiezen hoeft niet moeilijk te zijn
                    </h1>
                    <p style="font-size: 1.4rem; margin-bottom: 0; line-height: 1.5; color: #fef7f0; text-shadow: 0 1px 3px rgba(0,0,0,0.2);">
                        Wij testen en vergelijken biologische hondensnacks<br>
                        zodat jij met een gerust hart de beste keuze maakt.
                    </p>
                </div>
                
                <!-- Trust Elements -->
                <div class="trust-badges" style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 2.5rem; flex-wrap: wrap;">
                    <div class="trust-badge" style="background: rgba(255,255,255,0.95); color: #2d3748; padding: 0.75rem 1.25rem; border-radius: 12px; border: 2px solid #E68161; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #22c55e; font-size: 1.2rem;">✓</span>
                        <span>100% biologisch & natuurlijk</span>
                    </div>
                    <div class="trust-badge" style="background: rgba(255,255,255,0.95); color: #2d3748; padding: 0.75rem 1.25rem; border-radius: 12px; border: 2px solid #E68161; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #22c55e; font-size: 1.2rem;">✓</span>
                        <span>Graanvrij & hypoallergeen</span>
                    </div>
                    <div class="trust-badge" style="background: rgba(255,255,255,0.95); color: #2d3748; padding: 0.75rem 1.25rem; border-radius: 12px; border: 2px solid #E68161; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #22c55e; font-size: 1.2rem;">✓</span>
                        <span>Beoordeeld door 10.000+ hondenbaasjes</span>
                    </div>
                </div>
                
                <!-- CTAs -->
                <div class="hero-cta" style="text-align: center; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                    <a href="#snack-finder" class="btn btn-primary btn-large" style="background: #E68161; border: none; padding: 1.25rem 2.5rem; border-radius: 12px; text-decoration: none; color: white; font-size: 1.1rem; font-weight: 600; box-shadow: 0 4px 16px rgba(230, 129, 97, 0.4); transition: all 0.3s ease; display: inline-block;">
                        Start de snack-keuzehulp
                    </a>
                    <a href="beste-hondensnacks-2026/" class="btn btn-secondary btn-large" style="background: rgba(255,255,255,0.95); border: 2px solid white; padding: 1.25rem 2.5rem; border-radius: 12px; text-decoration: none; color: #2d3748; font-size: 1.1rem; font-weight: 600; transition: all 0.3s ease; display: inline-block;">
                        Bekijk onze top 10 →
                    </a>
                </div>
                
            </div>
        </div>
    </section>'''
    
    # Trouver et remplacer la section hero
    hero_pattern = r'<section class="hero"[^>]*>.*?</section>'
    
    if re.search(hero_pattern, content, re.DOTALL):
        updated_content = re.sub(hero_pattern, new_hero, content, count=1, flags=re.DOTALL)
        
        # Sauvegarder
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("✅ Hero section mise à jour avec succès!")
        print("\n📝 Changements appliqués:")
        print("  • Titre: 'Gezonde hondensnacks kiezen hoeft niet moeilijk te zijn'")
        print("  • Sous-titre: 'Wij testen en vergelijken...'")
        print("  • 3 trust badges: Biologisch, Graanvrij, 10.000+ avis")
        print("  • CTA principal: 'Start de snack-keuzehulp'")
        print("  • CTA secondaire: 'Bekijk onze top 10 →'")
        print("\n💾 Backup sauvegardé: index.html.hero_backup")
        
        return True
    else:
        print("❌ Hero section non trouvée")
        return False

if __name__ == "__main__":
    print("🎨 UPDATE HERO SECTION")
    print("=" * 60)
    update_hero_section()
    print("=" * 60)
