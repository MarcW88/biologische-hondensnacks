#!/usr/bin/env python3
"""
UNIFICATION TYPOGRAPHIE SITE
============================

Script pour supprimer tous les styles inline de typographie
et s'assurer qu'une seule famille de police est utilisée sur tout le site.

Auteur: AI Assistant
Date: December 2025
"""

import os
import re
import glob

# Configuration
SITE_ROOT = '/Users/marc/Desktop/biologische-hondensnacks'
FONT_FAMILY = "'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"

def backup_file(file_path):
    """Create backup of file"""
    backup_path = file_path + '.typography_backup'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ Error creating backup for {file_path}: {e}")
        return False

def clean_inline_typography(content):
    """Remove inline typography styles"""
    
    # Patterns to remove
    patterns = [
        # Font-family inline styles
        r'font-family:\s*[^;]+;?',
        # Font-size inline styles (keep only specific sizes we want to preserve)
        r'font-size:\s*[^;]+;?',
        # Font-weight inline styles (keep only specific weights)
        r'font-weight:\s*[^;]+;?',
        # Line-height inline styles
        r'line-height:\s*[^;]+;?',
    ]
    
    original_content = content
    
    for pattern in patterns:
        # Remove the pattern but preserve the rest of the style attribute
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
    
    # Clean up empty style attributes and double semicolons
    content = re.sub(r'style="\s*;*\s*"', '', content)
    content = re.sub(r'style="\s*"', '', content)
    content = re.sub(r';\s*;+', ';', content)
    content = re.sub(r'style="([^"]*);*\s*"', r'style="\1"', content)
    
    changes = len(original_content) - len(content)
    return content, changes

def update_css_typography():
    """Update CSS to ensure consistent typography"""
    
    css_file = os.path.join(SITE_ROOT, 'css/styles.css')
    
    if not os.path.exists(css_file):
        print(f"❌ CSS file not found: {css_file}")
        return False
    
    # Backup CSS
    if not backup_file(css_file):
        return False
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add comprehensive typography rules
        typography_rules = f"""

/* ==============================================
   TYPOGRAPHIE UNIFIÉE - FORCE OVERRIDE
   ============================================== */

/* Force typography on all elements */
* {{
    font-family: {FONT_FAMILY} !important;
}}

/* Consistent heading sizes */
h1, .h1 {{
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
    font-family: {FONT_FAMILY} !important;
}}

h2, .h2 {{
    font-size: 2rem !important;
    font-weight: 600 !important;
    line-height: 1.3 !important;
    font-family: {FONT_FAMILY} !important;
}}

h3, .h3 {{
    font-size: 1.5rem !important;
    font-weight: 600 !important;
    line-height: 1.4 !important;
    font-family: {FONT_FAMILY} !important;
}}

h4, .h4 {{
    font-size: 1.25rem !important;
    font-weight: 600 !important;
    line-height: 1.4 !important;
    font-family: {FONT_FAMILY} !important;
}}

h5, .h5 {{
    font-size: 1.125rem !important;
    font-weight: 600 !important;
    line-height: 1.4 !important;
    font-family: {FONT_FAMILY} !important;
}}

h6, .h6 {{
    font-size: 1rem !important;
    font-weight: 600 !important;
    line-height: 1.4 !important;
    font-family: {FONT_FAMILY} !important;
}}

/* Body text */
p, div, span, a, li, td, th {{
    font-family: {FONT_FAMILY} !important;
    font-size: 1rem !important;
    line-height: 1.6 !important;
}}

/* Small text */
.text-sm, small {{
    font-size: 0.875rem !important;
    font-family: {FONT_FAMILY} !important;
}}

/* Extra small text */
.text-xs {{
    font-size: 0.75rem !important;
    font-family: {FONT_FAMILY} !important;
}}

/* Large text */
.text-lg {{
    font-size: 1.125rem !important;
    font-family: {FONT_FAMILY} !important;
}}

/* Extra large text */
.text-xl {{
    font-size: 1.25rem !important;
    font-family: {FONT_FAMILY} !important;
}}

/* Buttons */
button, .btn, input[type="submit"], input[type="button"] {{
    font-family: {FONT_FAMILY} !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
}}

/* Forms */
input, textarea, select {{
    font-family: {FONT_FAMILY} !important;
    font-size: 1rem !important;
}}

/* Navigation */
nav, .nav, .navigation {{
    font-family: {FONT_FAMILY} !important;
}}

nav a, .nav a, .navigation a {{
    font-family: {FONT_FAMILY} !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
}}

/* Footer */
footer, .footer {{
    font-family: {FONT_FAMILY} !important;
}}

footer * {{
    font-family: {FONT_FAMILY} !important;
}}

/* Cards and components */
.card, .product-card, .category-card {{
    font-family: {FONT_FAMILY} !important;
}}

.card *, .product-card *, .category-card * {{
    font-family: {FONT_FAMILY} !important;
}}

/* Override any remaining inline styles */
[style*="font-family"] {{
    font-family: {FONT_FAMILY} !important;
}}

/* Ensure consistent font loading */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Fallback for SF Pro Text */
body {{
    font-family: {FONT_FAMILY} !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}}
"""
        
        # Add typography rules at the end of CSS
        content += typography_rules
        
        # Write updated CSS
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ CSS typography rules added to {css_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating CSS: {e}")
        return False

def process_html_files():
    """Process all HTML files to remove inline typography"""
    
    html_files = []
    
    # Find all HTML files (excluding backups)
    for root, dirs, files in os.walk(SITE_ROOT):
        # Skip backup directories
        if 'backups' in root or '.git' in root:
            continue
            
        for file in files:
            if file.endswith('.html') and not file.endswith('_backup.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"📄 Found {len(html_files)} HTML files to process")
    
    total_changes = 0
    processed_files = 0
    
    for file_path in html_files:
        try:
            # Create backup
            if not backup_file(file_path):
                continue
            
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Clean typography
            cleaned_content, changes = clean_inline_typography(content)
            
            if changes > 0:
                # Write cleaned content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                print(f"✅ Cleaned {file_path} ({changes} characters removed)")
                total_changes += changes
                processed_files += 1
            else:
                # Remove backup if no changes
                backup_path = file_path + '.typography_backup'
                if os.path.exists(backup_path):
                    os.remove(backup_path)
        
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
    
    print(f"📊 Processed {processed_files} files, removed {total_changes} characters of inline typography")
    return processed_files > 0

def main():
    """Main function"""
    print("🎨 UNIFICATION TYPOGRAPHIE SITE")
    print("=" * 50)
    
    print("\\n1️⃣ MISE À JOUR CSS...")
    css_success = update_css_typography()
    
    print("\\n2️⃣ NETTOYAGE FICHIERS HTML...")
    html_success = process_html_files()
    
    print("\\n" + "=" * 50)
    if css_success and html_success:
        print("🎉 SUCCÈS! Typographie unifiée sur tout le site")
        print(f"📝 Police utilisée: {FONT_FAMILY}")
        print("✅ Tous les styles inline de typographie supprimés")
        print("✅ CSS mis à jour avec règles !important")
        print("\\n🔄 Redémarrez le serveur pour voir les changements")
    else:
        print("❌ Certaines opérations ont échoué")
        print("🔍 Vérifiez les messages d'erreur ci-dessus")
    
    print("\\n🏁 UNIFICATION TYPOGRAPHIE TERMINÉE")

if __name__ == "__main__":
    main()
