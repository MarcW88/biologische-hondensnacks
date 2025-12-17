#!/usr/bin/env python3
"""
SCRIPT UNIFICATION FOOTERS
Applique le footer exact de la homepage sur TOUTES les pages du site
"""

import os
import re
import glob
from pathlib import Path

# Configuration
SITE_DIR = "/Users/marc/Desktop/biologische-hondensnacks"
BACKUP_DIR = "/Users/marc/Desktop/biologische-hondensnacks/scripts/backups"

# Footer exact de la homepage (avec liens relatifs adaptés)
def get_unified_footer(is_root=True, is_product=False, is_blog_subdir=False):
    """Retourne le footer unifié avec les bons liens relatifs"""
    
    if is_root:
        prefix = ""
    elif is_product:
        prefix = "../"
    elif is_blog_subdir:
        prefix = "../../"
    else:
        prefix = "../"
    
    return f'''    <!-- Footer -->
    <footer class="footer" style="background: #1f2937; color: white;">
        <div class="container">
            <div class="footer-content" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; padding: 3rem 0;">
                <div>
                    <h3 style="color: #e2e8f0; margin-bottom: 1rem;">Biologische hondensnacks</h3>
                    <p style="margin-bottom: 1.5rem; color: #d1d5db;">De beste natuurlijke en biologische snacks voor jouw hond. Graanvrij, gezond en heerlijk.</p>
                    
                    <!-- Newsletter Signup -->
                    <div style="background: #374151; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                        <h4 style="margin-bottom: 1rem; font-size: 1rem;">Wekelijkse tips & aanbiedingen</h4>
                        <form style="display: flex; gap: 0.5rem; margin-bottom: 0.5rem;">
                            <input type="email" placeholder="je@email.nl" required style="flex: 1; padding: 0.8rem; border: none; border-radius: 4px; background: white; color: #333;">
                            <button type="submit" style="background: #2d3748; color: white; border: none; padding: 0.8rem 1.2rem; border-radius: 4px; cursor: pointer; font-weight: 600; white-space: nowrap;">Aanmelden</button>
                        </form>
                        <p style="font-size: 0.7rem; color: #9ca3af; margin: 0;">Geen spam, uitschrijven altijd mogelijk</p>
                    </div>
                    
                    <!-- Social Media -->
                    <div>
                        <h4 style="margin-bottom: 1rem; font-size: 1rem;">Volg ons</h4>
                        <div style="display: flex; gap: 1rem;">
                            <a href="#" style="background: #4a5568; color: white; padding: 0.8rem; border-radius: 4px; text-decoration: none; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; font-size: 1.2rem;">f</a>
                            <a href="#" style="background: #718096; color: white; padding: 0.8rem; border-radius: 4px; text-decoration: none; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; font-size: 1.2rem;">ig</a>
                            <a href="#" style="background: #a0aec0; color: white; padding: 0.8rem; border-radius: 4px; text-decoration: none; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; font-size: 1.2rem;">yt</a>
                        </div>
                    </div>
                </div>
                
                <div>
                    <h3 style="margin-bottom: 1rem;">Populaire categorieën</h3>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}natuurlijke-hondensnacks/" style="color: #d1d5db; text-decoration: none;">Natuurlijke snacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}hondensnacks-voor-puppy/" style="color: #d1d5db; text-decoration: none;">Puppy snacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}hondensnacks-voor-training/" style="color: #d1d5db; text-decoration: none;">Training snacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}gezonde-kauwsnacks/" style="color: #d1d5db; text-decoration: none;">Kauwsnacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}graanvrije-hondensnacks/" style="color: #d1d5db; text-decoration: none;">Graanvrije snacks</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 style="margin-bottom: 1rem;">Support & info</h3>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}over-ons/" style="color: #d1d5db; text-decoration: none;">Over ons</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}blog/" style="color: #d1d5db; text-decoration: none;">Blog & tips</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}contact/" style="color: #d1d5db; text-decoration: none;">Contact</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}veelgestelde-vragen/" style="color: #d1d5db; text-decoration: none;">FAQ</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="{prefix}beste-hondensnacks-2026/" style="color: #d1d5db; text-decoration: none;">Top 10 beste</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 style="margin-bottom: 1rem;">Vertrouwen & veiligheid</h3>
                    
                    <!-- Trust Badges -->
                    <div style="margin-bottom: 1.5rem;">
                        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
                            <span style="background: #4a5568; color: white; padding: 0.3rem 0.8rem; border-radius: 4px; font-size: 0.8rem;">Bol.com partner</span>
                            <span style="background: #718096; color: white; padding: 0.3rem 0.8rem; border-radius: 4px; font-size: 0.8rem;">veilig betalen</span>
                        </div>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                            <span style="background: #a0aec0; color: white; padding: 0.3rem 0.8rem; border-radius: 4px; font-size: 0.8rem;">SKAL bio</span>
                            <span style="background: #2d3748; color: white; padding: 0.3rem 0.8rem; border-radius: 4px; font-size: 0.8rem;">4.8/5 reviews</span>
                        </div>
                    </div>
                    
                    <!-- Legal Links -->
                    <div>
                        <h4 style="margin-bottom: 0.5rem; font-size: 0.9rem; color: #9ca3af;">Juridisch</h4>
                        <ul style="list-style: none; padding: 0;">
                            <li style="margin-bottom: 0.3rem;"><a href="{prefix}privacy-policy/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Privacy policy</a></li>
                            <li style="margin-bottom: 0.3rem;"><a href="{prefix}algemene-voorwaarden/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Algemene voorwaarden</a></li>
                            <li style="margin-bottom: 0.3rem;"><a href="{prefix}disclaimer/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Disclaimer</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom" style="border-top: 1px solid #374151; padding: 1.5rem 0; text-align: center;">
                <p style="margin: 0 0 1rem 0; color: #9ca3af; font-size: 0.8rem;">
                    <strong>Disclaimer:</strong> De informatie op deze website is alleen bedoeld voor algemene doeleinden en vervangt geen professioneel veterinair advies. 
                    Raadpleeg altijd je dierenarts voor specifieke voedings- en gezondheidsadvies voor je hond.
                </p>
                <p style="margin: 0; color: #9ca3af; font-size: 0.9rem;">&copy; 2026 Biologische hondensnacks. Alle rechten voorbehouden. | Gemaakt voor honden en hun baasjes</p>
            </div>
        </div>
    </footer>'''

def backup_file(file_path):
    """Maak een backup van het originele bestand"""
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup_path = os.path.join(BACKUP_DIR, f"footer_{os.path.basename(file_path)}.backup")
        with open(file_path, 'r', encoding='utf-8') as original:
            content = original.read()
        with open(backup_path, 'w', encoding='utf-8') as backup:
            backup.write(content)
        return True
    except Exception as e:
        print(f"❌ Error creating backup for {os.path.basename(file_path)}: {str(e)}")
        return False

def determine_file_type(file_path):
    """Détermine le type de fichier pour les liens relatifs"""
    if file_path.endswith('/index.html') and '/blog/' in file_path and file_path.count('/') > 3:
        return 'blog_subdir'
    elif '/produits/' in file_path:
        return 'product'
    elif file_path.endswith('/index.html'):
        return 'root'
    else:
        return 'subdir'

def unify_footer_in_file(file_path):
    """Unifie le footer dans un fichier"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip homepage
        if file_path.endswith('/index.html') and file_path.count('/') <= 4:
            print(f"⚪ Skipping homepage: {os.path.basename(file_path)}")
            return True
        
        # Create backup first
        if not backup_file(file_path):
            return False
        
        # Determine file type
        file_type = determine_file_type(file_path)
        
        # Get appropriate footer
        if file_type == 'root':
            footer = get_unified_footer(is_root=True)
        elif file_type == 'product':
            footer = get_unified_footer(is_product=True)
        elif file_type == 'blog_subdir':
            footer = get_unified_footer(is_blog_subdir=True)
        else:
            footer = get_unified_footer(is_root=False)
        
        # Find and replace footer - multiple patterns
        footer_patterns = [
            r'(\s*)<!-- Footer -->\s*<footer.*?</footer>',
            r'(\s*)<footer class="footer".*?</footer>',
            r'(\s*)<footer.*?</footer>'
        ]
        
        footer_found = False
        new_content = content
        
        for pattern in footer_patterns:
            if re.search(pattern, content, re.DOTALL):
                new_content = re.sub(
                    pattern,
                    r'\1' + footer,
                    content,
                    flags=re.DOTALL
                )
                footer_found = True
                break
        
        if not footer_found:
            print(f"⚠️  Could not find footer section in {os.path.basename(file_path)}")
            return False
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Unified footer in {os.path.basename(file_path)} ({file_type})")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(file_path)}: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 STARTING FOOTER UNIFICATION")
    print("=" * 50)
    
    # Get all HTML files in the site
    html_files = []
    
    # Root directory files (skip index.html)
    root_files = glob.glob(os.path.join(SITE_DIR, "*.html"))
    html_files.extend([f for f in root_files if not f.endswith('/index.html')])
    
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
    print("🏠 Homepage footer will be used as template")
    
    success_count = 0
    error_count = 0
    skip_count = 0
    
    for file_path in html_files:
        result = unify_footer_in_file(file_path)
        if result is True:
            success_count += 1
        elif result is None:
            skip_count += 1
        else:
            error_count += 1
    
    print("\n" + "=" * 50)
    print("📊 FOOTER UNIFICATION RESULTS:")
    print(f"✅ Successfully unified: {success_count}")
    print(f"⚪ Skipped: {skip_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📁 Total files: {len(html_files)}")
    
    if success_count > 0:
        print(f"\n🎉 Successfully unified {success_count} footers!")
        print("📋 All pages now have:")
        print("   • Newsletter signup")
        print("   • Social media links")
        print("   • Trust badges")
        print("   • Complete navigation")
        print("   • Legal disclaimer")
        print("   • Correct relative links")
    
    print("\n🏁 FOOTER UNIFICATION COMPLETE")

if __name__ == "__main__":
    main()
