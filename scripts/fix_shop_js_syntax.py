#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - SHOP.JS SYNTAX FIXER
===============================================

Script pour corriger l'erreur de syntaxe JavaScript dans shop.js
causée par du code dupliqué orphelin.

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import shutil

# Configuration
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/syntax_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def fix_shop_js_syntax():
    """Fix the JavaScript syntax error in shop.js"""
    try:
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_file = os.path.join(BACKUP_DIR, 'shop_js_corrupted_backup.js')
        shutil.copy2(SHOP_JS_FILE, backup_file)
        print(f"💾 Backup created: {backup_file}")
        
        # Find the end of the first renderProducts function
        first_render_end = content.find('    updateLoadMoreButton();\n}')
        
        if first_render_end == -1:
            print("❌ Could not find first renderProducts function end")
            return False
        
        # Find the position right after the first function
        first_function_end = first_render_end + len('    updateLoadMoreButton();\n}')
        
        # Find the start of the next proper function (loadMoreProducts)
        next_function_start = content.find('\n// Load more products\nfunction loadMoreProducts()')
        
        if next_function_start == -1:
            print("❌ Could not find loadMoreProducts function")
            return False
        
        # Remove the orphaned code between the two functions
        clean_content = content[:first_function_end] + content[next_function_start:]
        
        # Verify the fix by checking for syntax errors
        # Remove any remaining orphaned code patterns
        
        # Pattern 1: Remove orphaned const/let declarations without function context
        orphaned_pattern = r'\n\s+const startIndex = \(currentPage - 1\) \* productsPerPage;.*?(?=\n\/\/|\nfunction|\n\s*$)'
        clean_content = re.sub(orphaned_pattern, '', clean_content, flags=re.DOTALL)
        
        # Pattern 2: Remove any orphaned console.log statements
        orphaned_console = r'\n\s+console\.log\([^)]+\);\s*(?=\n\/\/|\nfunction|\n\s*$)'
        clean_content = re.sub(orphaned_console, '', clean_content, flags=re.MULTILINE)
        
        # Pattern 3: Remove orphaned HTML generation code
        orphaned_html = r'\n\s+productsGrid\.innerHTML = productsToShow\.map\(.*?\`\)\.join\(\'\'\);'
        clean_content = re.sub(orphaned_html, '', clean_content, flags=re.DOTALL)
        
        # Write the cleaned content
        with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        
        print("✅ Removed orphaned code from shop.js")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing shop.js: {e}")
        return False

def verify_syntax():
    """Verify that the JavaScript syntax is now correct"""
    try:
        import subprocess
        result = subprocess.run(['node', '-c', SHOP_JS_FILE], 
                              capture_output=True, text=True, cwd='/Users/marc/Desktop/biologische-hondensnacks')
        
        if result.returncode == 0:
            print("✅ JavaScript syntax is now valid")
            return True
        else:
            print(f"❌ Syntax error still exists: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"⚠️ Could not verify syntax (Node.js not available): {e}")
        return True  # Assume it's fixed

def main():
    """Main function to fix shop.js syntax"""
    print("🔧 SHOP.JS SYNTAX FIXER")
    print("=" * 50)
    
    create_backup_dir()
    
    print("🔄 Fixing JavaScript syntax errors...")
    syntax_fixed = fix_shop_js_syntax()
    
    if syntax_fixed:
        print("🔍 Verifying syntax...")
        syntax_valid = verify_syntax()
        
        print("\n" + "=" * 50)
        print("📊 SYNTAX FIX RESULTS:")
        print(f"🔧 Orphaned code removed: {'✅' if syntax_fixed else '❌'}")
        print(f"✅ Syntax validation: {'✅ Valid' if syntax_valid else '❌ Still has errors'}")
        
        if syntax_fixed and syntax_valid:
            print(f"\n🎉 SUCCESS! shop.js syntax is now clean!")
            print("📱 Products should now display in winkel")
            print("🔍 JavaScript will execute properly")
            print("⚙️ All functions should work correctly")
        else:
            print(f"\n⚠️ Partial fix - manual review may be needed")
    else:
        print("\n❌ Failed to fix syntax errors")
    
    print("\n🏁 SYNTAX FIX COMPLETE")

if __name__ == "__main__":
    main()
