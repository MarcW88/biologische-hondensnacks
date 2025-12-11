#!/usr/bin/env python3
"""
REMOVE ALL EMOJIS FROM WEBSITE
===============================

Supprime tous les emojis des pages HTML pour un look plus professionnel.

Auteur: AI Assistant
Date: December 2025
"""

import os
import re
import glob

# Configuration
SITE_DIR = '/Users/marc/Desktop/biologische-hondensnacks'

# Patterns d'emojis à supprimer
EMOJI_PATTERNS = [
    # Emojis courants utilisés sur le site
    r'🎯\s*',
    r'❤️\s*',
    r'🛡️\s*',
    r'⚡\s*',
    r'😋\s*',
    r'🏃\s*',
    r'🌱\s*',
    r'🚫\s*',
    r'🦷\s*',
    r'😌\s*',
    r'💪\s*',
    r'⏰\s*',
    r'👃\s*',
    r'✂️\s*',
    r'🧠\s*',
    r'🍗\s*',
    r'🌡️\s*',
    r'✅\s*',
    r'🎁\s*',
    r'🦆\s*',
    r'✨\s*',
    r'🌿\s*',
    r'🍽️\s*',
    r'🥩\s*',
    r'🔴\s*',
    r'🐕\s*',
    r'📈\s*',
    r'💨\s*',
    r'🔬\s*',
    r'😁\s*',
    r'🐰\s*',
    r'💚\s*',
    r'🦌\s*',
    r'🦴\s*',
    r'🌍\s*',
    r'🏔️\s*',
    r'🧀\s*',
    r'⏱️\s*',
    r'🐟\s*',
    r'📊\s*',
    r'💎\s*',
    r'🌟\s*',
    r'👨‍⚕️\s*',
    r'🛒\s*',
    r'👁️\s*',
    r'📸\s*',
    r'📝\s*',
    r'🔍\s*',
    r'✓\s*',
    r'⭐\s*',
    # Pattern générique pour capturer tous les emojis Unicode
    r'[\U0001F300-\U0001F9FF]\s*',  # Emojis et symboles
    r'[\U00002600-\U000027BF]\s*',  # Symboles divers
    r'[\U0001F600-\U0001F64F]\s*',  # Emoticones
    r'[\U0001F680-\U0001F6FF]\s*',  # Transport et symboles
]

def remove_emojis_from_text(text):
    """Supprime tous les emojis du texte"""
    
    # Appliquer tous les patterns
    for pattern in EMOJI_PATTERNS:
        text = re.sub(pattern, '', text)
    
    # Nettoyer les espaces multiples
    text = re.sub(r'\s+', ' ', text)
    
    # Nettoyer les espaces avant la ponctuation
    text = re.sub(r'\s+([,.:;!?])', r'\1', text)
    
    return text

def process_html_file(file_path):
    """Traite un fichier HTML"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Supprimer les emojis
        cleaned_content = remove_emojis_from_text(content)
        
        # Vérifier si des changements ont été faits
        if cleaned_content != original_content:
            # Backup
            backup_path = file_path + '.emoji_backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Sauvegarder le fichier nettoyé
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            # Compter les emojis supprimés
            emoji_count = len(original_content) - len(cleaned_content)
            
            return True, emoji_count
        
        return False, 0
        
    except Exception as e:
        return False, f"Error: {e}"

def find_all_html_files():
    """Trouve tous les fichiers HTML du site"""
    
    html_files = []
    
    # Racine
    html_files.extend(glob.glob(os.path.join(SITE_DIR, '*.html')))
    
    # Sous-dossiers importants
    folders = [
        'blog',
        'blog/*',
        'produits',
        'winkel',
        'contact',
        'over-ons',
        'natuurlijke-hondensnacks',
        'graanvrije-hondensnacks',
        'hondensnacks-voor-puppy',
        'hondensnacks-voor-training',
        'gezonde-kauwsnacks',
        'beste-hondensnacks-2026',
    ]
    
    for folder in folders:
        pattern = os.path.join(SITE_DIR, folder, '*.html')
        html_files.extend(glob.glob(pattern))
    
    return html_files

def main():
    """Fonction principale"""
    
    print("🧹 REMOVE ALL EMOJIS FROM WEBSITE")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML
    html_files = find_all_html_files()
    
    print(f"📁 Found {len(html_files)} HTML files\n")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    total_chars_removed = 0
    
    for html_file in html_files:
        filename = os.path.relpath(html_file, SITE_DIR)
        
        success, result = process_html_file(html_file)
        
        if success:
            if isinstance(result, int):
                chars_removed = result
                total_chars_removed += chars_removed
                print(f"✅ {filename[:60]:60} → {chars_removed} chars removed")
                success_count += 1
        elif result == 0:
            skip_count += 1
        else:
            print(f"❌ {filename[:60]:60} → {result}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 COMPLETE!")
    print(f"✅ Cleaned: {success_count} files")
    print(f"⏭️  Skipped: {skip_count} files (no emojis)")
    print(f"❌ Errors: {error_count} files")
    print(f"📊 Total characters removed: {total_chars_removed}")
    print(f"💾 Backups saved with .emoji_backup extension")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
