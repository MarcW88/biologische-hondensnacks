#!/usr/bin/env python3
"""
SCRIPT CORRECTION COULEURS ET HEADERS
- Restaure couleur orange pour logo
- Unifie couleurs: orange + vert seulement
- Supprime toutes les couleurs bleues
- Corrige headers produits (supprime emoji)
"""

import os
import re
import glob
from pathlib import Path

# Configuration
SITE_DIR = "/Users/marc/Desktop/biologische-hondensnacks"
BACKUP_DIR = "/Users/marc/Desktop/biologische-hondensnacks/scripts/backups"

# Corrections couleurs
COLOR_FIXES = [
    # Remplacer toutes les couleurs bleues par orange ou vert
    (r'#1e40af', '#E68161'),  # Bleu foncé -> Orange
    (r'#1e3a8a', '#d67347'),  # Bleu très foncé -> Orange foncé
    (r'#3b82f6', '#E68161'),  # Bleu -> Orange
    (r'#2563eb', '#E68161'),  # Bleu moyen -> Orange
    (r'#1d4ed8', '#E68161'),  # Bleu -> Orange
    (r'#eff6ff', '#fef7f0'),  # Bleu clair -> Orange clair
    (r'#dbeafe', '#fef7f0'),  # Bleu très clair -> Orange très clair
    (r'#93c5fd', '#E68161'),  # Bleu moyen clair -> Orange
    (r'#60a5fa', '#E68161'),  # Bleu clair -> Orange
    (r'#06b6d4', '#22c55e'),  # Cyan -> Vert
    (r'#0891b2', '#16a34a'),  # Cyan foncé -> Vert foncé
    (r'#8b5cf6', '#E68161'),  # Violet -> Orange
    (r'#7c3aed', '#d67347'),  # Violet foncé -> Orange foncé
    
    # Variables CSS bleues
    (r'--primary-blue', '--primary-orange'),
    (r'--blue-', '--orange-'),
    (r'var\(--blue-[^)]+\)', 'var(--primary-orange)'),
    
    # Classes CSS bleues
    (r'bg-blue-', 'bg-orange-'),
    (r'text-blue-', 'text-orange-'),
    (r'border-blue-', 'border-orange-'),
]

# Corrections headers
HEADER_FIXES = [
    # Supprimer emoji du logo dans headers
    (r'<a href="[^"]*">🐕 Biologische Hondensnacks</a>', '<a href="../" style="color: #E68161; font-weight: bold;">Biologische Hondensnacks</a>'),
    (r'<a href="/">🐕 Biologische Hondensnacks</a>', '<a href="/" style="color: #E68161; font-weight: bold;">Biologische Hondensnacks</a>'),
    (r'🐕 Biologische Hondensnacks', '<span style="color: #E68161; font-weight: bold;">Biologische Hondensnacks</span>'),
    
    # Assurer couleur orange pour logo
    (r'<div class="logo">\s*<a href="[^"]*">([^<]*)</a>', r'<div class="logo"><a href="../" style="color: #E68161; font-weight: bold; text-decoration: none;">\1</a>'),
]

def backup_file(file_path):
    """Maak een backup van het originele bestand"""
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup_path = os.path.join(BACKUP_DIR, f"colors_{os.path.basename(file_path)}.backup")
        with open(file_path, 'r', encoding='utf-8') as original:
            content = original.read()
        with open(backup_path, 'w', encoding='utf-8') as backup:
            backup.write(content)
        return True
    except Exception as e:
        print(f"❌ Error creating backup for {os.path.basename(file_path)}: {str(e)}")
        return False

def fix_colors_and_headers(file_path):
    """Corrige les couleurs et headers dans un fichier"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # Apply color fixes
        for pattern, replacement in COLOR_FIXES:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes_made += 1
        
        # Apply header fixes
        for pattern, replacement in HEADER_FIXES:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes_made += 1
        
        # Only write if changes were made
        if content != original_content:
            # Create backup first
            if not backup_file(file_path):
                return False, 0
            
            # Write corrected content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Fixed {changes_made} color/header issues in {os.path.basename(file_path)}")
            return True, changes_made
        else:
            print(f"⚪ No color/header issues found in {os.path.basename(file_path)}")
            return True, 0
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(file_path)}: {str(e)}")
        return False, 0

def fix_css_colors():
    """Corrige les couleurs dans le fichier CSS principal"""
    css_file = os.path.join(SITE_DIR, "css", "styles.css")
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup CSS
        backup_path = os.path.join(BACKUP_DIR, "styles.css.backup")
        os.makedirs(BACKUP_DIR, exist_ok=True)
        with open(backup_path, 'w', encoding='utf-8') as backup:
            backup.write(content)
        
        # Fix logo color in CSS
        content = re.sub(
            r'\.logo \{[^}]*\}',
            '''.logo {
  font-size: 24px;
  font-weight: var(--font-weight-bold);
  color: var(--primary-orange);
}

.logo a {
  color: var(--primary-orange) !important;
  text-decoration: none;
  font-weight: bold;
}

.logo a:hover {
  color: var(--primary-orange-dark) !important;
}''',
            content
        )
        
        # Apply color fixes to CSS
        for pattern, replacement in COLOR_FIXES:
            content = re.sub(pattern, replacement, content)
        
        # Write back CSS
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fixed colors in main CSS file")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing CSS colors: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 STARTING COLOR AND HEADER FIXES")
    print("=" * 50)
    
    # Fix CSS first
    print("🎨 Fixing main CSS colors...")
    fix_css_colors()
    
    # Get all HTML files
    html_files = []
    
    # Root directory files
    html_files.extend(glob.glob(os.path.join(SITE_DIR, "*.html")))
    
    # Subdirectory files
    for subdir in ['over-ons', 'winkel', 'blog', 'natuurlijke-hondensnacks', 
                   'beste-hondensnacks-2026', 'hondensnacks-voor-puppy', 'produits']:
        subdir_path = os.path.join(SITE_DIR, subdir)
        if os.path.exists(subdir_path):
            html_files.extend(glob.glob(os.path.join(subdir_path, "*.html")))
    
    # Blog subdirectories
    blog_dir = os.path.join(SITE_DIR, "blog")
    if os.path.exists(blog_dir):
        for item in os.listdir(blog_dir):
            item_path = os.path.join(blog_dir, item)
            if os.path.isdir(item_path):
                html_files.extend(glob.glob(os.path.join(item_path, "*.html")))
    
    print(f"📁 Found {len(html_files)} HTML files to process")
    
    success_count = 0
    error_count = 0
    total_changes = 0
    
    for file_path in html_files:
        success, changes = fix_colors_and_headers(file_path)
        if success:
            success_count += 1
            total_changes += changes
        else:
            error_count += 1
    
    print("\n" + "=" * 50)
    print("📊 COLOR AND HEADER FIX RESULTS:")
    print(f"✅ Successfully processed: {success_count}")
    print(f"❌ Errors: {error_count}")
    print(f"🎨 Total changes made: {total_changes}")
    print(f"📁 Total files: {len(html_files)}")
    
    if total_changes > 0:
        print(f"\n🎉 Successfully fixed {total_changes} color and header issues!")
        print("🎨 Color scheme now unified:")
        print("   • Primary: Orange (#E68161)")
        print("   • Secondary: Green (#22c55e)")
        print("   • All blue colors removed")
        print("   • Logo now has orange color")
        print("   • Headers cleaned (no emojis)")
    
    print("\n🏁 COLOR AND HEADER FIXES COMPLETE")

if __name__ == "__main__":
    main()
