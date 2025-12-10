#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - LOGO HEADER FIXER
============================================

Script om alle logo image references te vervangen door tekst
"Biologische Hondensnacks" in alle HTML bestanden.

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import glob
from pathlib import Path

# Configuration
PROJECT_DIR = '/Users/marc/Desktop/biologische-hondensnacks'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/logo_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def fix_logo_in_file(file_path):
    """Fix logo reference in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains logo image reference
        if 'logotype-primary-2.png' not in content and '<img' not in content.split('</div>')[0]:
            return False
        
        # Create backup
        backup_name = os.path.basename(file_path).replace('.html', '_logo_backup.html')
        backup_path = os.path.join(BACKUP_DIR, backup_name)
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Pattern to match the logo div with image
        logo_pattern = r'<div class="logo">\s*<a href="[^"]*">\s*<img[^>]*>\s*</a>\s*</div>'
        
        # Replacement with text logo
        replacement = '''<div class="logo">
                    <a href="../">Biologische Hondensnacks</a>
                </div>'''
        
        # Apply replacement
        new_content = re.sub(logo_pattern, replacement, content, flags=re.DOTALL)
        
        # If no match with the full pattern, try simpler patterns
        if new_content == content:
            # Try to match just the img tag within logo div
            img_pattern = r'(<div class="logo">\s*<a href="[^"]*">)\s*<img[^>]*>\s*(</a>\s*</div>)'
            replacement_simple = r'\1Biologische Hondensnacks\2'
            new_content = re.sub(img_pattern, replacement_simple, content, flags=re.DOTALL)
        
        # If still no match, try even simpler
        if new_content == content:
            # Replace any img tag that has logotype in src
            img_logotype_pattern = r'<img[^>]*logotype[^>]*>'
            new_content = re.sub(img_logotype_pattern, 'Biologische Hondensnacks', content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def find_all_html_files():
    """Find all HTML files in the project"""
    html_files = []
    
    # Find HTML files in root and subdirectories
    for pattern in ['*.html', '*/*.html', '*/*/*.html']:
        files = glob.glob(os.path.join(PROJECT_DIR, pattern))
        html_files.extend(files)
    
    return html_files

def main():
    """Main function to fix all logo references"""
    print("🔧 LOGO HEADER FIXER")
    print("=" * 50)
    
    # Create backup directory
    create_backup_dir()
    
    # Find all HTML files
    html_files = find_all_html_files()
    print(f"📄 Found {len(html_files)} HTML files to check")
    
    fixed_count = 0
    
    for file_path in html_files:
        relative_path = os.path.relpath(file_path, PROJECT_DIR)
        
        if fix_logo_in_file(file_path):
            print(f"✅ Fixed logo in: {relative_path}")
            fixed_count += 1
        else:
            print(f"⚪ No logo fix needed: {relative_path}")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 LOGO FIX RESULTS:")
    print(f"✅ Files fixed: {fixed_count}")
    print(f"📄 Total files checked: {len(html_files)}")
    print(f"💾 Backups created in: {BACKUP_DIR}")
    
    if fixed_count > 0:
        print(f"\n🎉 SUCCESS! {fixed_count} files now show 'Biologische Hondensnacks'")
        print("🏷️ All logo images replaced with text")
        print("🎨 Consistent branding across all pages")
    else:
        print("\n⚠️ No files needed logo fixes")
    
    print("\n🏁 LOGO HEADER FIX COMPLETE")

if __name__ == "__main__":
    main()
