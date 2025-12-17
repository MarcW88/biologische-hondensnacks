#!/usr/bin/env python3
"""
GENERATE BLOG ARTICLES WITH CHATGPT
====================================
Génère des articles de blog professionnels optimisés SEO de 1500 mots
pour les pages blog spécifiées.

Auteur: AI Assistant
Date: December 2025
"""

import os
from pathlib import Path
from bs4 import BeautifulSoup
from openai import OpenAI
import time

# Configuration
BASE_DIR = Path('/Users/marc/Desktop/biologische-hondensnacks')
BLOG_DIR = BASE_DIR / 'blog'

# Initialisation du client OpenAI
client = None

def init_openai_client(api_key):
    """Initialise le client OpenAI"""
    global client
    client = OpenAI(api_key=api_key)
    print("✅ OpenAI API initialisé")

def generate_blog_article_chatgpt(title, topic, current_content_sample=""):
    """Génère un article de blog de 1500 mots via ChatGPT"""
    
    if not client:
        return None
    
    prompt = f"""Je hebt een blog over biologische hondensnacks in het Nederlands.

Schrijf een ZEER UITGEBREID, professioneel en SEO-geoptimaliseerd blogartikel van EXACT 1500-2000 woorden over:

TITEL: {title}
ONDERWERP: {topic}

⚠️ BELANGRIJK: Het artikel moet ABSOLUUT 1500-2000 woorden bevatten. Schrijf zeer gedetailleerd en uitgebreid.

Het artikel moet:
- EXACT 1500-2000 woorden bevatten (niet korter!)
- Zeer professioneel en diepgaand informatief zijn
- In het Nederlands geschreven zijn
- SEO-vriendelijk met natuurlijke keyword integratie
- Gestructureerd met duidelijke secties
- Vele praktische tips, voorbeelden en advies bevatten
- Wetenschappelijk onderbouwd waar mogelijk
- Engaging, leesbaar en waardevol voor de lezer

VERPLICHTE STRUCTUUR (elk deel moet uitgebreid zijn):

## Introductie (200-250 woorden)
- Hook: Persoonlijk verhaal of interessant feit
- Probleem identificatie
- Waarom dit onderwerp belangrijk is
- Preview van wat de lezer zal leren

## Hoofdstuk 1: Basis Uitleg & Achtergrond (400-500 woorden)
- Diepgaande uitleg van het onderwerp
- Historische context of wetenschappelijke basis
- Belangrijke concepten en terminologie
- Waarom dit relevant is voor hondenvoeding

## Hoofdstuk 2: Voordelen & Gezondheidsaspecten (400-500 woorden)
- Specifieke voordelen met voorbeelden
- Wetenschappelijke onderbouwing
- Impact op verschillende aspecten van hondengezondheid
- Vergelijkingen en case studies

## Hoofdstuk 3: Praktische Gids & Tips (400-500 woorden)
- Stap-voor-stap advies
- Wat te vermijden (veelvoorkomende fouten)
- Specifieke aanbevelingen per situatie
- Praktische voorbeelden en scenario's

## Conclusie & Actie (200-250 woorden)
- Samenvatting kernpunten
- Laatste belangrijke tips
- Call-to-action
- Motiverende afsluiting

SCHRIJFSTIJL:
- Gebruik uitgebreide paragrafen (4-6 zinnen per paragraaf)
- Geef veel concrete voorbeelden
- Gebruik H2 (##) voor hoofdstukken, H3 (###) voor subsecties
- Voeg bulletpoints toe waar relevant
- Schrijf vriendelijk maar professioneel
- Vermijd filler content - alleen waardevolle informatie

⚠️ NOGMAALS: Het artikel moet MINIMAAL 1500 woorden zijn. Wees uitgebreid en gedetailleerd in elk hoofdstuk.

Geef ALLEEN de artikel content in Markdown formaat. Geen meta-tekst."""

    try:
        print(f"  🤖 Generating 1500-word article via ChatGPT...")
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Je bent een expert content writer voor hondenvoeding en gezondheid in het Nederlands. Je schrijft ZEER LANGE, UITGEBREIDE en gedetailleerde artikelen van minimaal 1500-2000 woorden. Je geeft altijd volledige, diepgaande content zonder af te kappen."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4096  # Maximum pour GPT-4 pour permettre des articles très longs
        )
        
        article_content = response.choices[0].message.content.strip()
        
        # Compter les mots
        word_count = len(article_content.split())
        print(f"  ✅ Article generated: {word_count} words")
        
        return article_content
        
    except Exception as e:
        print(f"  ❌ ChatGPT error: {e}")
        return None

def markdown_to_html(markdown_text):
    """Convertit Markdown en HTML simple"""
    html = markdown_text
    
    # Convertir les headers
    html = html.replace('\n### ', '\n<h3>')
    html = html.replace('\n## ', '\n<h2>')
    html = html.replace('\n# ', '\n<h1>')
    
    # Fermer les headers (trouver fin de ligne)
    lines = html.split('\n')
    new_lines = []
    for line in lines:
        if line.startswith('<h1>'):
            line = line + '</h1>'
        elif line.startswith('<h2>'):
            line = line + '</h2>'
        elif line.startswith('<h3>'):
            line = line + '</h3>'
        elif line.startswith('- '):
            line = '<li>' + line[2:] + '</li>'
        elif line.startswith('* '):
            line = '<li>' + line[2:] + '</li>'
        elif line and not line.startswith('<'):
            line = '<p>' + line + '</p>'
        new_lines.append(line)
    
    html = '\n'.join(new_lines)
    
    # Envelopper les listes
    html = html.replace('</li>\n<li>', '</li><li>')
    
    # Convertir **bold**
    import re
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)
    
    return html

def create_simple_blog_html(title, article_html, meta_description):
    """Crée un HTML de blog simple avec l'article"""
    
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Biologische Hondensnacks</title>
    <meta name="description" content="{meta_description}">
    
    <link rel="canonical" href="https://biologische-hondensnacks.nl/blog/{title.lower().replace(' ', '-')}/">
    <link rel="icon" type="image/x-icon" href="../../favicon.ico">
    <link rel="stylesheet" href="../../css/styles.css">
    
    <style>
        .blog-article {{
            max-width: 800px;
            margin: 0 auto;
            padding: 3rem 2rem;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.8;
            color: #2d3748;
        }}
        
        .blog-article h1 {{
            font-size: 2.5rem;
            color: #2d3748;
            margin-bottom: 1rem;
            line-height: 1.2;
        }}
        
        .blog-article h2 {{
            font-size: 2rem;
            color: #2d3748;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            line-height: 1.3;
        }}
        
        .blog-article h3 {{
            font-size: 1.5rem;
            color: #4a5568;
            margin-top: 2rem;
            margin-bottom: 0.75rem;
        }}
        
        .blog-article p {{
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }}
        
        .blog-article ul, .blog-article ol {{
            margin-bottom: 1.5rem;
            padding-left: 2rem;
        }}
        
        .blog-article li {{
            margin-bottom: 0.5rem;
            font-size: 1.05rem;
        }}
        
        .blog-article strong {{
            color: #E68161;
            font-weight: 600;
        }}
        
        .blog-meta {{
            color: #6b7280;
            font-size: 0.95rem;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid #e2e8f0;
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <a href="../../" class="logo">
                    <span class="logo-icon">🐕</span>
                    <span class="logo-text">Biologische Hondensnacks</span>
                </a>
                <nav class="nav">
                    <a href="../../">Home</a>
                    <a href="../../winkel/">Shop</a>
                    <a href="../../blog/">Blog</a>
                    <a href="../../over-ons/">Over Ons</a>
                    <a href="../../contact/">Contact</a>
                </nav>
            </div>
        </div>
    </header>

    <article class="blog-article">
        <h1>{title}</h1>
        
        <div class="blog-meta">
            📅 Gepubliceerd: December 2025 | 📚 Leestijd: ~8 minuten
        </div>
        
        {article_html}
        
        <div style="margin-top: 3rem; padding: 2rem; background: #f7fafc; border-radius: 12px; border-left: 4px solid #E68161;">
            <h3 style="margin-top: 0;">💡 Op zoek naar hoogwaardige hondensnacks?</h3>
            <p>Bekijk onze collectie van <a href="../../winkel/" style="color: #E68161; text-decoration: underline;">67 biologische en natuurlijke hondensnacks</a> - allemaal zorgvuldig geselecteerd voor de gezondheid van je hond.</p>
        </div>
    </article>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 Biologische Hondensnacks. Alle rechten voorbehouden.</p>
        </div>
    </footer>
</body>
</html>'''
    
    return html

def process_blog_page(blog_slug, api_key):
    """Traite une page blog spécifique"""
    
    print(f"\n{'='*60}")
    print(f"Processing: {blog_slug}")
    print(f"{'='*60}")
    
    # Initialiser le client si nécessaire
    if not client:
        init_openai_client(api_key)
    
    # Définir le titre et topic basés sur le slug
    topics = {
        'hondensnacks-voor-puppys-complete-gids': {
            'title': 'Hondensnacks voor Puppy\'s: Complete Gids',
            'topic': 'Complete gids over hondensnacks voor puppy\'s, welke snacks geschikt zijn, hoe vaak, portiegroottes, gezondheidsvoordelen, wat te vermijden, beste trainingssnacks voor puppy\'s',
            'meta': 'Complete gids over hondensnacks voor puppy\'s. Ontdek welke snacks geschikt zijn, hoe vaak je moet geven, en de beste keuzes voor training en gezondheid.'
        },
        'graanvrije-vs-normale-hondensnacks': {
            'title': 'Graanvrije vs Normale Hondensnacks: Wat is Beter?',
            'topic': 'Vergelijking tussen graanvrije en normale hondensnacks, voordelen en nadelen, wanneer graanvrij kiezen, allergieën, spijsvertering, wetenschappelijke inzichten',
            'meta': 'Graanvrije vs normale hondensnacks: ontdek de verschillen, voordelen en wanneer je voor graanvrij moet kiezen voor je hond.'
        },
        'waarom-biologische-snacks-beter-zijn': {
            'title': 'Waarom Biologische Snacks Beter Zijn voor Je Hond',
            'topic': 'Uitgebreide uitleg waarom biologische hondensnacks beter zijn, voordelen voor gezondheid, geen pesticiden, hogere voedingswaarde, milieu impact, certificeringen',
            'meta': 'Ontdek waarom biologische hondensnacks beter zijn voor je hond. Lees over gezondheidsvoordelen, geen pesticiden en hogere voedingswaarde.'
        }
    }
    
    if blog_slug not in topics:
        print(f"❌ Unknown blog slug: {blog_slug}")
        return False
    
    topic_info = topics[blog_slug]
    
    # Générer l'article via ChatGPT
    print(f"\n📝 Generating article: {topic_info['title']}")
    article_markdown = generate_blog_article_chatgpt(
        topic_info['title'],
        topic_info['topic']
    )
    
    if not article_markdown:
        print("❌ Failed to generate article")
        return False
    
    # Convertir Markdown en HTML
    print("  🔄 Converting Markdown to HTML...")
    article_html = markdown_to_html(article_markdown)
    
    # Créer le HTML complet
    print("  📄 Creating HTML page...")
    full_html = create_simple_blog_html(
        topic_info['title'],
        article_html,
        topic_info['meta']
    )
    
    # Sauvegarder
    blog_path = BLOG_DIR / blog_slug / 'index.html'
    blog_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Backup de l'ancien fichier
    if blog_path.exists():
        backup_path = blog_path.parent / 'index.html.backup'
        import shutil
        shutil.copy(blog_path, backup_path)
        print(f"  💾 Backup saved: {backup_path.name}")
    
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"  ✅ Article saved: {blog_path}")
    
    # Pause entre les articles pour éviter rate limiting
    time.sleep(2)
    
    return True

def main(api_key, blog_slugs=None):
    """Fonction principale"""
    
    print("🤖 GENERATE PROFESSIONAL BLOG ARTICLES")
    print("=" * 60)
    
    if not api_key:
        print("❌ API Key required")
        return
    
    # Liste des blogs à traiter
    if not blog_slugs:
        blog_slugs = [
            'hondensnacks-voor-puppys-complete-gids',
            'graanvrije-vs-normale-hondensnacks'
        ]
    
    success_count = 0
    error_count = 0
    
    for slug in blog_slugs:
        try:
            if process_blog_page(slug, api_key):
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            print(f"❌ Error processing {slug}: {e}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print("🎉 COMPLETE!")
    print(f"✅ Success: {success_count} articles")
    print(f"❌ Errors: {error_count} articles")
    print(f"💾 Backups saved with .backup extension")
    print(f"{'='*60}")

if __name__ == "__main__":
    # DÉFINIR TA CLÉ API ICI
    API_KEY = None  # ⚠️ Remplacer par ta clé API OpenAI
    
    if not API_KEY:
        print("\n⚠️  ATTENTION: Définis ta clé API OpenAI dans le script")
        print("Ligne ~360: API_KEY = 'sk-...'")
        print("\nOu passe-la comme argument:")
        import sys
        if len(sys.argv) > 1:
            API_KEY = sys.argv[1]
    
    if API_KEY:
        # Articles à générer
        blog_slugs = [
            'hondensnacks-voor-puppys-complete-gids',
            'graanvrije-vs-normale-hondensnacks'
        ]
        main(API_KEY, blog_slugs)
    else:
        print("\n❌ Clé API OpenAI requise pour continuer")
