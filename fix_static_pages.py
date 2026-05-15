#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_favicon(content):
    """Fix favicon to use the same structure as homepage"""
    # Remove old favicon lines
    old_favicon_pattern = r'<!-- Favicon -->.*?<!--'
    new_favicon = '''<!-- Favicon -->
 <link href="../favicon.svg" rel="icon" type="image/svg+xml"/>
 <link href="../favicon-simple.svg" rel="icon" sizes="16x16" type="image/svg+xml"/>
 <link href="../favicon.svg" rel="apple-touch-icon" sizes="180x180"/>
 <meta content="var(--primary)" name="theme-color"/>
 <!--'''
    
    content = re.sub(old_favicon_pattern, new_favicon, content, flags=re.DOTALL)
    return content

def fix_menu(content):
    """Fix menu to match homepage structure"""
    # Replace old menu structure with new one
    old_menu_pattern = r'<!-- Header -->.*?<div class="mobile-menu-overlay"></div>'
    
    new_menu = '''<!-- Navigation -->
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
  <li class="nav-item dropdown">
  <a class="nav-link dropdown-toggle" href="../beste-hondensnacks-2026/">Gidsen</a>
  <ul class="dropdown-menu">
  <li><a class="dropdown-link" href="../beste-hondensnacks-2026/">Top 10</a></li>
  <li><a class="dropdown-link" href="../natuurlijke-hondensnacks/">Natuurlijke snacks</a></li>
  <li><a class="dropdown-link" href="../blog/">Blog</a></li>
  </ul>
  </li>
  <li><a class="nav-link" href="../hondensnacks-voor-puppy/">Puppy Snacks</a></li>
  <li class="nav-item dropdown">
  <a class="nav-link dropdown-toggle" href="../winkel.html">Winkel</a>
  <ul class="dropdown-menu">
  <li><a class="dropdown-link" href="../winkel.html">Alle producten</a></li>
  <li><a class="dropdown-link" href="../kauwsnacks-tandverzorging/">Kauwsnacks</a></li>
  <li><a class="dropdown-link" href="../hypoallergene-hondensnacks/">Hypoallergeen</a></li>
  </ul>
  </li>
  </ul>
  </div>
  </div>
  </nav>
  <div class="mobile-menu-overlay"></div>
'''
    
    content = re.sub(old_menu_pattern, new_menu, content, flags=re.DOTALL)
    return content

def add_mobile_script(content):
    """Add mobile dropdown toggle script if not present"""
    if 'mobile dropdown toggle' not in content:
        # Find the closing </script> tag and add the mobile script after it
        script_pattern = r'(</script>)'
        mobile_script = r'''\1

<script>
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        mobileMenuToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        mobileMenuOverlay.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });
}

if (mobileMenuOverlay) {
    mobileMenuOverlay.addEventListener('click', () => {
        mobileMenuToggle.classList.remove('active');
        navMenu.classList.remove('active');
        mobileMenuOverlay.classList.remove('active');
        document.body.style.overflow = '';
    });
}

// Mobile dropdown toggle
const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
            e.preventDefault();
            const dropdownItem = toggle.closest('.nav-item.dropdown');
            dropdownItem.classList.toggle('active');
            const dropdownMenu = dropdownItem.querySelector('.dropdown-menu');
            dropdownMenu.classList.toggle('active');
        }
    });
});
</script>'''
        content = re.sub(script_pattern, mobile_script, content, count=1)
    return content

def main():
    """Main function to fix all static pages"""
    base_dir = Path('/Users/marc/Desktop/biologische-hondensnacks')
    
    # Find all HTML files in subdirectories (static pages)
    static_pages = []
    for subdir in ['natuurlijke-hondensnacks', 'hondensnacks-voor-puppy', 'kauwsnacks-tandverzorging', 
                    'hypoallergene-hondensnacks', 'graanvrije-hondensnacks', 'gezonde-kauwsnacks',
                    'caloriearme-hondensnacks', 'beste-hondensnacks-2026', 'contact', 'over-ons']:
        subdir_path = base_dir / subdir
        if subdir_path.exists():
            html_files = list(subdir_path.glob('*.html'))
            static_pages.extend(html_files)
    
    print(f"Found {len(static_pages)} static pages to process")
    
    fixed_count = 0
    for file_path in static_pages:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix favicon
            content = fix_favicon(content)
            
            # Fix menu
            content = fix_menu(content)
            
            # Add mobile script
            content = add_mobile_script(content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Fixed: {file_path.name}")
                fixed_count += 1
            else:
                print(f"  ⊘ Skipped: {file_path.name} (no changes needed)")
                
        except Exception as e:
            print(f"  ✗ Error processing {file_path.name}: {e}")
    
    print(f"\n✓ Fixed {fixed_count} files")

if __name__ == '__main__':
    main()
