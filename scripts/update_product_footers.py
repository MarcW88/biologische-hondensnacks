#!/usr/bin/env python3
"""
SCRIPT AUTOMATISATION FOOTERS PRODUITS
Remplace tous les footers produits par le footer unifié de la homepage
"""

import os
import re
import glob
from pathlib import Path

# Configuration
PRODUITS_DIR = "/Users/marc/Desktop/biologische-hondensnacks/produits"
BACKUP_DIR = "/Users/marc/Desktop/biologische-hondensnacks/scripts/backups"

# Footer unifié (identique à la homepage)
UNIFIED_FOOTER = '''    <!-- Footer -->
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
                        <li style="margin-bottom: 0.5rem;"><a href="../natuurlijke-hondensnacks/" style="color: #d1d5db; text-decoration: none;">Natuurlijke snacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../hondensnacks-voor-puppy/" style="color: #d1d5db; text-decoration: none;">Puppy snacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../hondensnacks-voor-training/" style="color: #d1d5db; text-decoration: none;">Training snacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../gezonde-kauwsnacks/" style="color: #d1d5db; text-decoration: none;">Kauwsnacks</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../graanvrije-hondensnacks/" style="color: #d1d5db; text-decoration: none;">Graanvrije snacks</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 style="margin-bottom: 1rem;">Support & info</h3>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 0.5rem;"><a href="../over-ons/" style="color: #d1d5db; text-decoration: none;">Over ons</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../blog/" style="color: #d1d5db; text-decoration: none;">Blog & tips</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../contact/" style="color: #d1d5db; text-decoration: none;">Contact</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../veelgestelde-vragen/" style="color: #d1d5db; text-decoration: none;">FAQ</a></li>
                        <li style="margin-bottom: 0.5rem;"><a href="../beste-hondensnacks-2026/" style="color: #d1d5db; text-decoration: none;">Top 10 beste</a></li>
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
                            <li style="margin-bottom: 0.3rem;"><a href="../privacy-policy/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Privacy policy</a></li>
                            <li style="margin-bottom: 0.3rem;"><a href="../algemene-voorwaarden/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Algemene voorwaarden</a></li>
                            <li style="margin-bottom: 0.3rem;"><a href="../disclaimer/" style="color: #9ca3af; text-decoration: none; font-size: 0.8rem;">Disclaimer</a></li>
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
        backup_path = os.path.join(BACKUP_DIR, os.path.basename(file_path) + '.backup')
        with open(file_path, 'r', encoding='utf-8') as original:
            content = original.read()
        with open(backup_path, 'w', encoding='utf-8') as backup:
            backup.write(content)
        return True
    except Exception as e:
        print(f"❌ Error creating backup for {os.path.basename(file_path)}: {str(e)}")
        return False

def update_footer_in_product(file_path):
    """Update footer in een product bestand"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup first
        if not backup_file(file_path):
            return False
        
        # Find footer section - more flexible pattern
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
                    r'\1' + UNIFIED_FOOTER,
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
        
        print(f"✅ Updated footer in {os.path.basename(file_path)}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(file_path)}: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 STARTING PRODUCT FOOTERS AUTOMATION")
    print("=" * 50)
    
    # Create backup directory
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    # Get all product HTML files
    product_files = glob.glob(os.path.join(PRODUITS_DIR, "*.html"))
    product_files = [f for f in product_files if not f.endswith('/index.html')]
    
    print(f"📁 Found {len(product_files)} product files")
    print(f"💾 Backups will be saved to: {BACKUP_DIR}")
    
    success_count = 0
    error_count = 0
    
    for file_path in product_files:
        result = update_footer_in_product(file_path)
        if result:
            success_count += 1
        else:
            error_count += 1
    
    print("\n" + "=" * 50)
    print("📊 AUTOMATION RESULTS:")
    print(f"✅ Successfully updated: {success_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📁 Total files: {len(product_files)}")
    
    if success_count > 0:
        print(f"\n🎉 Successfully updated footers in {success_count} products!")
        print("📋 All products now have:")
        print("   • Newsletter signup")
        print("   • Social media links")
        print("   • Trust badges")
        print("   • Complete navigation")
        print("   • Legal disclaimer")
    
    print("\n🏁 FOOTER AUTOMATION COMPLETE")

if __name__ == "__main__":
    main()
