#!/usr/bin/env python3
"""
FIX UI ISSUES - 4 CORRECTIONS
==============================

Corrige 4 problèmes UI identifiés:
1. Page Top 10: Supprime image placeholder vide à droite
2. Homepage: Supprime fond blanc sur badges (bestseller, klantenfavoriet, top rated)
3. Homepage: Répare structure articles/FAQ cassée
4. Page Puppy Snacks: Remplace fond orange par fond blanc + bord orange

Auteur: AI Assistant
Date: Décembre 2025
"""

import os
import re
from bs4 import BeautifulSoup

# Configuration
BASE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
BACKUP_DIR = os.path.join(BASE_DIR, 'scripts/backups/ui_fixes')

os.makedirs(BACKUP_DIR, exist_ok=True)

def fix_top10_page():
    """Problème 1: Supprime images placeholder vides sur page Top 10"""
    file_path = os.path.join(BASE_DIR, 'beste-hondensnacks-2026/index.html')
    
    print("\n1️⃣  Fixing Top 10 page (image placeholders)...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    backup_path = os.path.join(BACKUP_DIR, 'top10-index.html.backup')
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Trouver toutes les divs avec placeholder images
    placeholders_removed = 0
    
    # Chercher les images via.placeholder
    for img in soup.find_all('img', src=re.compile(r'placeholder')):
        # Supprimer la div parente si elle ne contient que cette image
        parent_div = img.find_parent('div')
        if parent_div and len(parent_div.find_all()) == 1:  # Seulement 1 élément (l'image)
            parent_div.decompose()
            placeholders_removed += 1
    
    # Sauvegarder
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    print(f"   ✅ Removed {placeholders_removed} placeholder images")
    return placeholders_removed > 0

def fix_homepage_badges():
    """Problème 2: Supprime fond blanc sur badges homepage"""
    file_path = os.path.join(BASE_DIR, 'index.html')
    
    print("\n2️⃣  Fixing Homepage badges (white background)...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    backup_path = os.path.join(BACKUP_DIR, 'homepage-index.html.backup')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Problème: du CSS inline répété qui contient plusieurs "; background: white;"
    # Pattern à chercher: style="...background: #17a2b8...background: white..."
    
    # Regex pour nettoyer les répétitions de styles inline cassés
    # Chercher les patterns qui ont plusieurs répétitions de border/padding/background
    pattern = r'(style="[^"]*background:\s*#[0-9a-fA-F]{6}[^"]*?)(;\s*border:\s*1px solid #e5e7eb;\s*border-radius:\s*12px;\s*padding:\s*1\.5rem;\s*background:\s*white;\s*box-shadow:[^"]*?)+(")'
    
    # Remplacer en gardant seulement la première partie
    content_fixed = re.sub(pattern, r'\1\3', content)
    
    # Si pas de changements, essayer un autre pattern plus spécifique
    if content_fixed == content:
        # Chercher spécifiquement les badges avec background répété
        pattern2 = r'(class="product-badge"[^>]*style="[^"]*background:\s*#[0-9a-fA-F]{6};[^"]*?)(;\s*border:\s*1px[^"]*?background:\s*white[^"]*?)(")'
        content_fixed = re.sub(pattern2, r'\1\3', content_fixed)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content_fixed)
    
    changes = len(re.findall(pattern, content)) + len(re.findall(pattern2, content))
    print(f"   ✅ Fixed {changes} badge styling issues")
    return changes > 0

def fix_homepage_blog_faq():
    """Problème 3: Répare section blog/FAQ cassée"""
    file_path = os.path.join(BASE_DIR, 'index.html')
    
    print("\n3️⃣  Fixing Homepage blog/FAQ section...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Trouver la section blog avec le HTML cassé
    # Chercher la balise img cassée
    broken_imgs = soup.find_all('img', src=re.compile(r'biologische-hondensnacks\.png'))
    
    fixed_count = 0
    for img in broken_imgs:
        # L'image a des attributs cassés comme #666;""
        # Recréer proprement
        new_img = soup.new_tag('img', 
                                src='images/puppy-snacks-blog.jpg',
                                alt='Hondensnacks voor puppys',
                                style='width: 100%; height: 200px; object-fit: cover; border-radius: 8px 8px 0 0;',
                                loading='lazy')
        
        # Trouver le parent card
        card = img.find_parent('div', class_='card')
        if card:
            # Vider le contenu cassé et reconstruire
            card.clear()
            
            # Ajouter image
            card.append(new_img)
            
            # Ajouter badge temps lecture
            badge = soup.new_tag('div', style='position: absolute; top: 15px; right: 15px; background: rgba(0,0,0,0.7); color: white; padding: 0.4rem 0.8rem; border-radius: 4px;')
            badge.string = '7 min lezen'
            card.append(badge)
            
            # Ajouter contenu texte dans une div
            content_div = soup.new_tag('div', style='padding: 1.5rem;')
            
            h3 = soup.new_tag('h3', style='margin-bottom: 0.5rem;')
            h3.string = "Hondensnacks voor puppy's: complete gids"
            content_div.append(h3)
            
            p = soup.new_tag('p', style='margin-bottom: 1rem; color: #666;')
            p.string = "Alles wat je moet weten over het kiezen van de juiste snacks voor je puppy. Van leeftijd tot ingrediënten."
            content_div.append(p)
            
            meta_div = soup.new_tag('div', style='display: flex; justify-content: space-between; margin-bottom: 1rem;')
            date_span = soup.new_tag('span', style='color: #666;')
            date_span.string = '22 november 2025'
            author_span = soup.new_tag('span', style='color: #666;')
            author_span.string = 'Door Mark, Hondenexpert'
            meta_div.append(date_span)
            meta_div.append(author_span)
            content_div.append(meta_div)
            
            link = soup.new_tag('a', href='/blog/puppy-snacks-gids/', 
                               style='color: #E68161; text-decoration: none; font-weight: 600;')
            link.string = 'Lees de Gids →'
            content_div.append(link)
            
            card.append(content_div)
            
            # Ajouter position relative au card
            if 'style' in card.attrs:
                card['style'] += '; position: relative;'
            else:
                card['style'] = 'position: relative; border-radius: 15px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);'
            
            fixed_count += 1
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    print(f"   ✅ Fixed {fixed_count} broken blog cards")
    return fixed_count > 0

def fix_puppy_page_backgrounds():
    """Problème 4: Remplace fond orange par blanc + bord orange sur page puppy snacks"""
    file_path = os.path.join(BASE_DIR, 'hondensnacks-voor-puppy/index.html')
    
    print("\n4️⃣  Fixing Puppy Snacks page (orange backgrounds)...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    backup_path = os.path.join(BACKUP_DIR, 'puppy-index.html.backup')
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Remplacer background: #E68161 par background: white dans les guide-cards
    # Mais s'assurer qu'il y a un bord orange visible
    
    pattern = r'(<div class="guide-card"[^>]*style="[^"]*)(background:\s*#E68161;)'
    
    def replacer(match):
        before = match.group(1)
        # Vérifier s'il y a déjà un border
        if 'border:' not in before:
            # Ajouter border orange
            return before + 'background: white; border: 3px solid #E68161;'
        else:
            # Remplacer juste le background et renforcer le border
            result = before + 'background: white;'
            # Changer border 2px en 3px pour plus de visibilité
            result = result.replace('border: 2px solid', 'border: 3px solid')
            return result
    
    content_fixed = re.sub(pattern, replacer, content)
    
    # Compter les changements
    changes = len(re.findall(pattern, content))
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content_fixed)
    
    print(f"   ✅ Fixed {changes} orange background cards")
    return changes > 0

def main():
    """Fonction principale"""
    print("\n🔧 UI FIXES - 4 CORRECTIONS")
    print("=" * 70)
    
    results = {
        'top10': False,
        'badges': False,
        'blog_faq': False,
        'puppy': False
    }
    
    try:
        results['top10'] = fix_top10_page()
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    try:
        results['badges'] = fix_homepage_badges()
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    try:
        results['blog_faq'] = fix_homepage_blog_faq()
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    try:
        results['puppy'] = fix_puppy_page_backgrounds()
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print(f"\n{'='*70}")
    print(f"✅ FIXES COMPLETE!")
    print(f"\nRésultats:")
    print(f"  1. Top 10 placeholders: {'✅' if results['top10'] else '⚠️  Aucun changement'}")
    print(f"  2. Homepage badges: {'✅' if results['badges'] else '⚠️  Aucun changement'}")
    print(f"  3. Blog/FAQ section: {'✅' if results['blog_faq'] else '⚠️  Aucun changement'}")
    print(f"  4. Puppy backgrounds: {'✅' if results['puppy'] else '⚠️  Aucun changement'}")
    print(f"\n💾 Backups saved in: {BACKUP_DIR}")
    print(f"={'='*70}")

if __name__ == "__main__":
    main()
