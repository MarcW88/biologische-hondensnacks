#!/usr/bin/env python3
"""
GENERATE "WAAROM KIEZEN VOOR" WITH CHATGPT API
==============================================

Génère des descriptions uniques et naturelles pour chaque produit
en utilisant l'API ChatGPT.

Auteur: AI Assistant
Date: December 2025
"""

import os
import glob
from bs4 import BeautifulSoup
from openai import OpenAI
import time

# Configuration
PRODUITS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/produits'

def create_openai_client(api_key):
    """Crée un client OpenAI avec la nouvelle API"""
    return OpenAI(api_key=api_key)

def extract_product_data(soup):
    """Extrait les données du produit"""
    try:
        brand = soup.find(class_='brand').text.strip()
        product_name = soup.find('h1').text.strip()
        
        # Extraire des specs
        specs = {}
        spec_rows = soup.find_all(class_='spec-row')
        for row in spec_rows:
            label = row.find(class_='spec-label')
            value = row.find(class_='spec-value')
            if label and value:
                specs[label.text.strip()] = value.text.strip()
        
        weight = specs.get('Gewicht', 'n.b.')
        aantal = specs.get('Aantal stuks', 'n.b.')
        type_snack = specs.get('Type snack', 'snack')
        bijzonderheden = specs.get('Bijzonderheden', '')
        doelgroep = specs.get('Doelgroep', 'alle honden')
        
        # Extraire les bénéfices de la section "Voordelen"
        benefits = []
        benefits_list = soup.find(class_='benefits-list')
        if benefits_list:
            benefit_items = benefits_list.find_all('li')
            for item in benefit_items:
                strong = item.find('strong')
                if strong:
                    benefit_text = strong.text.strip()
                    # Nettoyer emojis/symboles
                    benefit_text = ''.join(char for char in benefit_text if char.isalnum() or char.isspace() or char in ['-', ',', '.'])
                    if benefit_text:
                        benefits.append(benefit_text.strip())
        
        return {
            'brand': brand,
            'product_name': product_name,
            'weight': weight,
            'aantal': aantal,
            'type_snack': type_snack,
            'bijzonderheden': bijzonderheden,
            'doelgroep': doelgroep,
            'benefits': benefits[:3]  # Max 3 bénéfices
        }
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def generate_text_with_chatgpt(client, product_data):
    """Génère le texte avec ChatGPT API (nouvelle version OpenAI >= 1.0.0)"""
    
    # Construire le prompt
    benefits_text = ", ".join(product_data['benefits']) if product_data['benefits'] else "natuurlijke kwaliteit"
    
    prompt = f"""Je bent een professionele copywriter voor een webshop van hondensnacks in België.

Schrijf een natuurlijke, informatieve en overtuigende paragraaf van ongeveer 50-70 woorden voor de sectie "Waarom kiezen voor [product]?" op een productpagina.

PRODUCTGEGEVENS:
- Merk: {product_data['brand']}
- Productnaam: {product_data['product_name']}
- Type: {product_data['type_snack']}
- Gewicht: {product_data['weight']}
- Aantal stuks: {product_data['aantal']}
- Doelgroep: {product_data['doelgroep']}
- Bijzonderheden: {product_data['bijzonderheden']}
- Belangrijkste voordelen: {benefits_text}

INSTRUCTIES:
- Schrijf in het Nederlands (Belgisch)
- Gebruik een natuurlijke, vloeiende stijl (GEEN templated tekst)
- Focus op de USP's van dit specifieke product
- Vermeld concreet het merk, type snack, en relevante eigenschappen
- Maak het persoonlijk en authentiek
- GEEN emojis
- GEEN clichés zoals "verwén je hond"
- GEEN generieke zinnen die op elk product passen
- Spreek de lezer direct aan met "je" en "jouw hond"

Schrijf ALLEEN de paragraaf, zonder titel of introductie."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Plus rapide et moins cher
            messages=[
                {"role": "system", "content": "Je bent een expert copywriter voor huisdierproducten in België. Je schrijft natuurlijke, authentieke productteksten zonder clichés."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.8,  # Plus de créativité
            n=1
        )
        
        generated_text = response.choices[0].message.content.strip()
        
        # Nettoyer le texte (retirer guillemets si présents)
        generated_text = generated_text.strip('"').strip("'")
        
        return generated_text
        
    except Exception as e:
        print(f"Error calling ChatGPT API: {e}")
        return None

def process_product_page(client, html_path, delay=1):
    """Traite une page produit avec ChatGPT"""
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extraire données produit
        data = extract_product_data(soup)
        if not data:
            return False, "Could not extract product data"
        
        # Générer texte avec ChatGPT
        print(f"   🤖 Generating with ChatGPT for: {data['product_name'][:40]}...")
        new_text = generate_text_with_chatgpt(client, data)
        
        if not new_text:
            return False, "ChatGPT generation failed"
        
        # Trouver la section "Waarom kiezen voor"
        extended_desc = soup.find(class_='product-description-extended')
        if not extended_desc:
            return False, "Section not found"
        
        # Trouver le premier paragraphe
        first_p = extended_desc.find('p')
        if first_p:
            # Backup
            backup_path = html_path + '.chatgpt_backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Remplacer le texte
            first_p.string = new_text
            
            # Sauvegarder
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(str(soup.prettify()))
            
            # Delay pour respecter rate limits API
            time.sleep(delay)
            
            return True, new_text[:60]
        
        return False, "Paragraph not found"
        
    except Exception as e:
        return False, str(e)

def main(api_key, batch_size=None):
    """Fonction principale"""
    
    if not api_key:
        print("❌ ERREUR: Clé API OpenAI requise")
        print("\nUsage:")
        print("  python3 generate_waarom_with_chatgpt.py")
        print("\nOu dans le code, définir OPENAI_API_KEY")
        return
    
    # Créer le client OpenAI
    try:
        client = create_openai_client(api_key)
        print("✅ Client OpenAI créé avec succès")
    except Exception as e:
        print(f"❌ Erreur création client OpenAI: {e}")
        return
    
    print("🤖 GENERATE 'WAAROM KIEZEN VOOR' WITH CHATGPT API")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob(os.path.join(PRODUITS_DIR, '*.html'))
    html_files = [f for f in html_files if not f.endswith('index.html')]
    
    total_files = len(html_files)
    
    # Limiter si batch_size spécifié (pour tester)
    if batch_size:
        html_files = html_files[:batch_size]
        print(f"📁 Processing {len(html_files)} files (batch mode, total: {total_files})\n")
    else:
        print(f"📁 Found {total_files} product pages\n")
    
    success_count = 0
    error_count = 0
    
    for idx, html_file in enumerate(html_files, 1):
        filename = os.path.basename(html_file)
        print(f"[{idx}/{len(html_files)}] Processing: {filename[:45]}...")
        
        success, result = process_product_page(client, html_file, delay=1.5)
        
        if success:
            print(f"   ✅ Generated: {result}...\n")
            success_count += 1
        else:
            print(f"   ❌ Error: {result}\n")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 COMPLETE!")
    print(f"✅ Success: {success_count} files")
    print(f"❌ Errors: {error_count} files")
    print(f"💾 Backups saved with .chatgpt_backup extension")
    print(f"{'='*60}")
    
    if batch_size:
        remaining = total_files - batch_size
        print(f"\n⚠️  BATCH MODE: {remaining} files remaining")
        print(f"Run again without batch_size to process all files")

if __name__ == "__main__":
    # DÉFINIR TA CLÉ API ICI
    API_KEY = None  # ⚠️ Remplacer par ta clé API OpenAI (ne jamais commiter la vraie clé !)
    
    if not API_KEY:
        print("\n⚠️  ATTENTION: Définis ta clé API OpenAI dans le script")
        print("Ligne 238: API_KEY = 'sk-...'")
        print("\nOu passe-la comme argument:")
        import sys
        if len(sys.argv) > 1:
            API_KEY = sys.argv[1]
    
    if API_KEY:
        # Traiter TOUS les produits
        print("🚀 FULL MODE: Processing ALL products")
        print("=" * 60)
        main(API_KEY)  # Sans batch_size = tous les produits
    else:
        print("\n❌ Clé API OpenAI requise pour continuer")
