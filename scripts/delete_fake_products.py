#!/usr/bin/env python3
"""
SCRIPT SUPPRESSION PRODUITS INVENTÉS
Supprime tous les 48 produits inventés pour les remplacer par les vrais
"""

import os
import glob
import shutil
from pathlib import Path

# Configuration
PRODUITS_DIR = "/Users/marc/Desktop/biologische-hondensnacks/produits"
BACKUP_DIR = "/Users/marc/Desktop/biologische-hondensnacks/scripts/backups/fake_products"

# Liste des produits inventés à supprimer
FAKE_PRODUCTS = [
    "benebone-freezedried-treats-eend.html",
    "benebone-grainfree-bites-lam.html", 
    "benebone-hypoallergenic-snacks-kip.html",
    "benebone-large-breed-chews-eend.html",
    "benebone-puppy-soft-bites-kip.html",
    "benebone-puppy-soft-bites-mix.html",
    "benebone-puppy-soft-bites-vis.html",
    "benebone-wishbone-bacon-flavor.html",
    "blue-buffalo-freezedried-treats-kalkoen.html",
    "blue-buffalo-grainfree-bites-zalm.html",
    "blue-buffalo-organic-training-rewards-mix.html",
    "blue-buffalo-puppy-soft-bites-eend.html",
    "blue-buffalo-wilderness-zalm-bites.html",
    "green-petfood-freezedried-treats-zalm.html",
    "green-petfood-hypoallergenic-snacks-rund.html",
    "green-petfood-insectdog-hypoallergeen-snacks.html",
    "green-petfood-large-breed-chews-zalm.html",
    "green-petfood-premium-training-treats-mix.html",
    "green-petfood-puppy-soft-bites-rund.html",
    "green-petfood-senior-care-treats-kip.html",
    "kong-freezedried-treats-zalm.html",
    "kong-natural-dental-chews-kip.html",
    "kong-puppy-soft-bites-vis.html",
    "lilys-kitchen-dental-chews-mint-parsley.html",
    "lilys-kitchen-freezedried-treats-mix.html",
    "lilys-kitchen-large-breed-chews-vis.html",
    "lilys-kitchen-puppy-soft-bites-lam.html",
    "lilys-kitchen-puppy-training-treats.html",
    "nylabone-grainfree-bites-lam.html",
    "nylabone-grainfree-bites-vis.html",
    "nylabone-premium-training-treats-rund.html",
    "nylabone-puppy-soft-bites-kalkoen.html",
    "wellness-core-pure-rewards-kip-freezedried.html",
    "wellness-organic-training-rewards-kalkoen.html",
    "wellness-premium-training-treats-eend.html",
    "yarrah-biologische-kip-rund-trainingssnacks.html",
    "yarrah-biologische-vis-trainingssnacks.html",
    "yarrah-freezedried-treats-vis.html",
    "yarrah-hypoallergenic-snacks-eend.html",
    "yarrah-hypoallergenic-snacks-zalm.html",
    "yarrah-organic-training-rewards-lam.html",
    "yarrah-premium-training-treats-rund.html",
    "zukes-grainfree-bites-zalm.html",
    "zukes-hypoallergenic-snacks-rund.html",
    "zukes-hypoallergenic-snacks-zalm.html",
    "zukes-mini-naturals-zalm-training-treats.html",
    "zukes-organic-training-rewards-kip.html",
    "zukes-puppy-naturals-kalkoen-zoete-aardappel.html"
]

def backup_fake_products():
    """Sauvegarde les produits inventés avant suppression"""
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        
        for product in FAKE_PRODUCTS:
            source_path = os.path.join(PRODUITS_DIR, product)
            if os.path.exists(source_path):
                backup_path = os.path.join(BACKUP_DIR, product)
                shutil.copy2(source_path, backup_path)
                print(f"📦 Backed up: {product}")
        
        print(f"✅ All fake products backed up to: {BACKUP_DIR}")
        return True
        
    except Exception as e:
        print(f"❌ Error backing up fake products: {str(e)}")
        return False

def delete_fake_products():
    """Supprime tous les produits inventés"""
    try:
        deleted_count = 0
        
        for product in FAKE_PRODUCTS:
            file_path = os.path.join(PRODUITS_DIR, product)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"🗑️ Deleted: {product}")
                deleted_count += 1
            else:
                print(f"⚠️ Not found: {product}")
        
        print(f"✅ Successfully deleted {deleted_count} fake products")
        return deleted_count
        
    except Exception as e:
        print(f"❌ Error deleting fake products: {str(e)}")
        return 0

def main():
    """Main function"""
    print("🚨 STARTING FAKE PRODUCTS DELETION")
    print("=" * 50)
    print(f"📁 Target directory: {PRODUITS_DIR}")
    print(f"🗑️ Products to delete: {len(FAKE_PRODUCTS)}")
    
    # Backup first
    print("\n📦 BACKING UP FAKE PRODUCTS...")
    if not backup_fake_products():
        print("❌ Backup failed! Aborting deletion.")
        return
    
    # Delete fake products
    print("\n🗑️ DELETING FAKE PRODUCTS...")
    deleted_count = delete_fake_products()
    
    print("\n" + "=" * 50)
    print("📊 DELETION RESULTS:")
    print(f"🗑️ Deleted: {deleted_count}")
    print(f"📦 Backed up to: {BACKUP_DIR}")
    print(f"📁 Remaining files in produits/:")
    
    # Show remaining files
    remaining_files = [f for f in os.listdir(PRODUITS_DIR) if f.endswith('.html')]
    for file in remaining_files:
        print(f"   • {file}")
    
    print(f"\n✅ Ready for real products creation!")
    print("🏁 FAKE PRODUCTS DELETION COMPLETE")

if __name__ == "__main__":
    main()
