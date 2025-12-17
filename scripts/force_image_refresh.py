#!/usr/bin/env python3
"""
BIOLOGISCHE HONDENSNACKS - FORCE IMAGE REFRESH
==============================================

Script om browser cache te forceren door timestamps toe te voegen aan image URLs
en ervoor te zorgen dat de nieuwe images geladen worden.

Auteur: AI Assistant
Datum: December 2025
"""

import os
import re
import time

# Configuration
SHOP_JS_FILE = '/Users/marc/Desktop/biologische-hondensnacks/winkel/shop.js'
BACKUP_DIR = '/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/cache_fix'

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📁 Backup directory created: {BACKUP_DIR}")

def force_image_refresh():
    """Add timestamp to image URLs to force browser refresh"""
    try:
        # Create backup
        create_backup_dir()
        backup_file = os.path.join(BACKUP_DIR, 'shop_js_before_cache_fix.js')
        
        with open(SHOP_JS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Save backup
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"💾 Backup created: {backup_file}")
        
        # Generate timestamp
        timestamp = str(int(time.time()))
        
        # Replace image URLs to add cache busting
        # Pattern: image: "../images/filename.jpg"
        pattern = r'(image:\s*"\.\.\/images\/[^"]+\.jpg)"'
        replacement = rf'\1?v={timestamp}"'
        
        new_content = re.sub(pattern, replacement, content)
        
        # Count replacements
        old_count = len(re.findall(pattern, content))
        new_count = len(re.findall(r'image:\s*"\.\.\/images\/[^"]+\.jpg\?v=\d+"', new_content))
        
        if new_count > 0:
            # Write updated content
            with open(SHOP_JS_FILE, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated {new_count} image URLs with cache busting")
            print(f"🔄 Cache busting parameter: ?v={timestamp}")
            return True
        else:
            print("⚠️ No image URLs found to update")
            return False
            
    except Exception as e:
        print(f"❌ Error updating shop.js: {e}")
        return False

def main():
    """Main function"""
    print("🔄 FORCE IMAGE REFRESH - CACHE BUSTING")
    print("=" * 50)
    
    success = force_image_refresh()
    
    if success:
        print("\n🎉 SUCCESS! Images will now refresh in browser")
        print("📱 Users should see new images after page refresh")
        print("🔍 Cache busting parameters added to all image URLs")
    else:
        print("\n❌ Failed to update image URLs")
    
    print("\n🏁 CACHE BUSTING COMPLETE")

if __name__ == "__main__":
    main()
