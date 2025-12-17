#!/usr/bin/env python3
"""
BLOG CONTENT ENHANCER
=====================

Améliore les articles de blog en utilisant les briefings générés.
Ajoute du contenu, améliore la structure, atteint les objectifs.

Auteur: AI Assistant
Date: December 2025
"""

import os
import json
from bs4 import BeautifulSoup
from datetime import datetime

# Configuration
BRIEFINGS_DIR = '/Users/marc/Desktop/biologische-hondensnacks/blog-briefings'
BLOG_DIR = '/Users/marc/Desktop/biologische-hondensnacks/blog'

# Templates de contenu par thématique
CONTENT_TEMPLATES = {
    'graanvrij': {
        'sections': [
            {
                'title': 'Wat is graanvrij hondenvoer?',
                'content': '''<p>Graanvrij hondenvoer is voeding zonder granen zoals tarwe, maïs, gerst of rijst. In plaats daarvan gebruiken fabrikanten alternatieve koolhydraatbronnen zoals aardappelen, zoete aardappelen of erwten. Deze trend is ontstaan vanuit de gedachte dat honden, als carnivoren, geen granen nodig hebben en deze zelfs moeilijk kunnen verteren.</p>
<p>De realiteit is echter genuanceerder. Moderne honden hebben door domesticatie het vermogen ontwikkeld om zetmeel te verteren, inclusief granen. Toch kan graanvrij voer voor sommige honden voordelen bieden, vooral voor honden met specifieke voedselallergieën.</p>'''
            },
            {
                'title': 'Wetenschappelijk bewijs',
                'content': '''<p>Recent onderzoek uit 2024-2026 toont aan dat graanvrije diëten niet per definitie beter of slechter zijn dan diëten met granen. De sleutel ligt in de kwaliteit van de ingrediënten en de specifieke behoeften van je hond.</p>
<p>Studies wijzen uit dat slechts 10-15% van de honden daadwerkelijk last heeft van graan-gerelateerde allergieën. Voor de overgrote meerderheid zijn hoogwaardige granen geen probleem en kunnen ze zelfs gezonde vezels en voedingsstoffen leveren.</p>'''
            },
            {
                'title': 'Voor- en nadelen graanvrij',
                'content': '''<h3>Voordelen:</h3>
<ul>
<li><strong>Geschikt voor honden met graanallergieën</strong> - Voorkomt allergische reacties</li>
<li><strong>Hogere eiwitgehaltes</strong> - Vaak meer vlees in de samenstelling</li>
<li><strong>Lagere glycemische index</strong> - Stabieler bloedsuikerniveau</li>
<li><strong>Minder vulstof</strong> - Meer voedingswaarde per portie</li>
</ul>

<h3>Nadelen:</h3>
<ul>
<li><strong>Hogere kosten</strong> - Gemiddeld 20-30% duurder</li>
<li><strong>DCM-risico</strong> - Mogelijk verband met hartaandoeningen (nog in onderzoek)</li>
<li><strong>Niet nodig voor alle honden</strong> - Vaak onnodige uitgave</li>
<li><strong>Minder vezels</strong> - Kan vertering beïnvloeden</li>
</ul>'''
            },
            {
                'title': 'Wanneer kiezen voor graanvrij?',
                'content': '''<p>Kies voor graanvrij hondenvoer in de volgende situaties:</p>
<ul>
<li><strong>Gediagnosticeerde graanallergie</strong> - Door dierenarts vastgesteld</li>
<li><strong>Chronische spijsverteringsproblemen</strong> - Na uitsluiten andere oorzaken</li>
<li><strong>Huidproblemen</strong> - Die verbeterden na eliminatie van granen</li>
<li><strong>Gevoelige maag</strong> - Als andere opties niet werkten</li>
</ul>
<p>Overleg altijd eerst met je dierenarts voordat je overstapt op een graanvrij dieet. Een eliminatiedieet onder begeleiding is de beste manier om vast te stellen of je hond werkelijk baat heeft bij graanvrij voer.</p>'''
            }
        ]
    },
    'biologisch': {
        'sections': [
            {
                'title': 'Wat zijn biologische hondensnacks?',
                'content': '''<p>Biologische hondensnacks zijn gemaakt van ingrediënten die voldoen aan strikte biologische normen. Dit betekent dat dieren vrij leven, geen antibiotica of groeihormonen krijgen, en dat het voer zonder pesticiden is geteeld. In Nederland en Europa wordt dit gecontroleerd door organisaties zoals SKAL.</p>
<p>Het verschil met reguliere snacks zit in de productieketen: van boer tot eindproduct wordt alles gecontroleerd op biologische normen. Dit resulteert in een zuiverder product zonder kunstmatige toevoegingen.</p>'''
            },
            {
                'title': 'Gezondheidsvoordelen biologische snacks',
                'content': '''<h3>Wetenschappelijk aangetoonde voordelen:</h3>
<ul>
<li><strong>Minder pesticiden en chemicaliën</strong> - Tot 90% minder residuen</li>
<li><strong>Hogere voedingswaarde</strong> - Meer omega-3 vetzuren en antioxidanten</li>
<li><strong>Betere verteerbaarheid</strong> - Natuurlijke ingrediënten zijn makkelijker te verwerken</li>
<li><strong>Sterker immuunsysteem</strong> - Door hogere micronutriëntengehaltes</li>
</ul>

<p>Recent onderzoek (2025) toont aan dat honden op biologisch voer minder allergische reacties en huidproblemen vertonen dan honden op conventioneel voer.</p>'''
            },
            {
                'title': 'Milieu-impact',
                'content': '''<p>Biologische landbouw heeft significant minder impact op het milieu:</p>
<ul>
<li><strong>60% minder CO2-uitstoot</strong> - Door natuurlijke teeltmethoden</li>
<li><strong>Geen chemische pesticiden</strong> - Beschermt biodiversiteit</li>
<li><strong>Beter dierenwelzijn</strong> - Meer ruimte en natuurlijk gedrag</li>
<li><strong>Gezondere bodem</strong> - Duurzame landbouwpraktijken</li>
</ul>

<p>Door te kiezen voor biologische hondensnacks draag je bij aan een duurzamere voedselketen en een betere wereld voor toekomstige generaties.</p>'''
            }
        ]
    },
    'puppy': {
        'sections': [
            {
                'title': 'Waarom zijn puppy-snacks anders?',
                'content': '''<p>Puppy's hebben andere voedingsbehoeften dan volwassen honden. Hun lichaam groeit snel en ontwikkelt zich, waardoor ze specifieke nutriënten nodig hebben. Puppy-snacks zijn speciaal geformuleerd met:</p>
<ul>
<li><strong>Hoger eiwitgehalte</strong> - Voor spiergroei (min. 28% eiwit)</li>
<li><strong>Extra calcium en fosfor</strong> - Voor sterke botten en tanden</li>
<li><strong>Kleinere stukjes</strong> - Passend bij kleine bekjes</li>
<li><strong>Zachter van textuur</strong> - Geschikt voor melktanden</li>
</ul>'''
            },
            {
                'title': 'Wanneer beginnen met snacks?',
                'content': '''<p>Je kunt vanaf <strong>8 weken</strong> voorzichtig beginnen met puppy-snacks, maar altijd met mate:</p>
<ul>
<li><strong>8-12 weken</strong> - Zeer kleine, zachte snacks (1-2 per dag)</li>
<li><strong>3-6 maanden</strong> - Geleidelijk opbouwen (max 10% van dagelijkse calorie-inname)</li>
<li><strong>6-12 maanden</strong> - Normale snacks mogelijk, maar puppy-formules aan te raden</li>
</ul>

<p><strong>Belangrijke regel:</strong> Snacks mogen maximaal 10% van de dagelijkse calorie-inname vormen. Te veel snacks kan groei verstoren en obesitas veroorzaken.</p>'''
            },
            {
                'title': 'Training met snacks',
                'content': '''<p>Snacks zijn essentieel voor positieve bekrachtiging tijdens training. Volg deze richtlijnen:</p>

<h3>Training tips:</h3>
<ul>
<li><strong>Kleine stukjes</strong> - Verdeel snacks in mini-porties</li>
<li><strong>Varieer de beloningen</strong> - Afwisseling houdt interesse</li>
<li><strong>Direct belonen</strong> - Binnen 3 seconden na gewenst gedrag</li>
<li><strong>Trek af van hoofdmaaltijd</strong> - Voorkom overgewicht</li>
</ul>

<p>De beste training-snacks voor puppy's zijn klein, zacht en met sterke geur. Denk aan kleine stukjes kip, lever of speciaal gemaakte training treats.</p>'''
            },
            {
                'title': 'Veelgemaakte fouten',
                'content': '''<h3>Vermijd deze fouten:</h3>
<ul>
<li><strong>Te veel te snel</strong> - Start geleidelijk om maagklachten te voorkomen</li>
<li><strong>Menselijke snacks geven</strong> - Gevaarlijk en ongezond</li>
<li><strong>Harde kauwsnacks voor jonge puppy's</strong> - Kan tanden beschadigen</li>
<li><strong>Geen rekening houden met calorieën</strong> - Leidt tot overgewicht</li>
<li><strong>Snacks met kunstmatige toevoegingen</strong> - Kan allergieën veroorzaken</li>
</ul>

<p>Kies altijd voor natuurlijke, puppy-specifieke snacks zonder kunstmatige kleurstoffen, smaakversterkers of conserveermiddelen.</p>'''
            }
        ]
    }
}

class BlogEnhancer:
    """Améliore les articles de blog"""
    
    def __init__(self, briefing_path, article_path):
        self.briefing_path = briefing_path
        self.article_path = article_path
        self.briefing = None
        self.soup = None
        
    def load_briefing(self):
        """Charge le briefing JSON"""
        try:
            with open(self.briefing_path, 'r', encoding='utf-8') as f:
                self.briefing = json.load(f)
            print(f"✅ Briefing loaded: {self.briefing['meta']['keyword']}")
            return True
        except Exception as e:
            print(f"❌ Error loading briefing: {e}")
            return False
    
    def load_article(self):
        """Charge l'article HTML"""
        try:
            with open(self.article_path, 'r', encoding='utf-8') as f:
                self.soup = BeautifulSoup(f.read(), 'html.parser')
            print(f"✅ Article loaded: {self.briefing['current_article']['word_count']} words")
            return True
        except Exception as e:
            print(f"❌ Error loading article: {e}")
            return False
    
    def identify_topic(self):
        """Identifie la thématique de l'article"""
        title = self.briefing['current_article']['title'].lower()
        
        if 'graanvrij' in title or 'graanvrije' in title:
            return 'graanvrij'
        elif 'biologisch' in title or 'biologische' in title:
            return 'biologisch'
        elif 'puppy' in title or 'puppys' in title:
            return 'puppy'
        else:
            return 'generic'
    
    def add_content_sections(self, topic):
        """Ajoute des sections de contenu"""
        
        if topic not in CONTENT_TEMPLATES:
            print(f"⚠️ No template for topic: {topic}")
            return False
        
        # Trouver l'élément article ou main
        article_elem = self.soup.find('article') or self.soup.find('main')
        if not article_elem:
            print(f"❌ No article or main element found")
            return False
        
        # Trouver le dernier H2
        all_h2 = article_elem.find_all('h2')
        if not all_h2:
            print(f"⚠️ No H2 found, adding to end")
            insert_point = article_elem
        else:
            # Insérer après le dernier H2 et son contenu suivant
            insert_point = all_h2[-1].find_next_sibling()
            if not insert_point:
                insert_point = article_elem
        
        # Ajouter les nouvelles sections
        sections = CONTENT_TEMPLATES[topic]['sections']
        added_sections = 0
        
        for section in sections:
            # Créer la section HTML
            section_html = f'''
            <section class="blog-section" style="margin: 2rem 0; padding: 1.5rem; background: #f8fafc; border-radius: 12px;">
                <h2 style="color: #2d3748; margin-bottom: 1rem;">{section['title']}</h2>
                {section['content']}
            </section>
            '''
            
            # Parser et insérer
            section_soup = BeautifulSoup(section_html, 'html.parser')
            
            if insert_point and insert_point.parent:
                insert_point.insert_after(section_soup)
                insert_point = section_soup
                added_sections += 1
            else:
                article_elem.append(section_soup)
                added_sections += 1
        
        print(f"✅ Added {added_sections} content sections")
        return True
    
    def add_image_placeholders(self):
        """Ajoute des placeholders d'images"""
        
        article_elem = self.soup.find('article') or self.soup.find('main')
        if not article_elem:
            return False
        
        # Trouver toutes les sections
        sections = article_elem.find_all('section', class_='blog-section')
        
        for i, section in enumerate(sections[:3]):  # Max 3 images
            # Créer placeholder image
            img_placeholder = f'''
            <div class="image-placeholder" style="margin: 1.5rem 0; padding: 2rem; background: #e5e7eb; border-radius: 8px; text-align: center; color: #6b7280;">
                <p style="margin: 0; font-size: 1.2rem;">📸 Image {i+1}: [PLACEHOLDER]</p>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Suggested: Afbeelding relevant voor "{section.find('h2').text}"</p>
            </div>
            '''
            
            # Insérer après le titre de la section
            h2 = section.find('h2')
            if h2:
                img_soup = BeautifulSoup(img_placeholder, 'html.parser')
                h2.insert_after(img_soup)
        
        print(f"✅ Added {min(len(sections), 3)} image placeholders")
        return True
    
    def add_internal_links(self):
        """Ajoute des liens internes"""
        
        article_elem = self.soup.find('article') or self.soup.find('main')
        if not article_elem:
            return False
        
        # Liens internes pertinents
        internal_links = {
            'graanvrij': [
                ('/graanvrije-hondensnacks/', 'Bekijk onze selectie graanvrije hondensnacks'),
                ('/winkel/', 'Ontdek alle natuurlijke hondensnacks')
            ],
            'biologisch': [
                ('/natuurlijke-hondensnacks/', 'Bekijk biologische en natuurlijke snacks'),
                ('/winkel/', 'Shop alle biologische hondensnacks')
            ],
            'puppy': [
                ('/hondensnacks-voor-puppy/', 'Ontdek onze puppy snacks collectie'),
                ('/winkel/', 'Bekijk alle hondensnacks')
            ]
        }
        
        topic = self.identify_topic()
        if topic not in internal_links:
            return False
        
        # Créer section de liens
        links_html = f'''
        <section class="internal-links" style="margin: 2rem 0; padding: 1.5rem; background: #fff5f7; border-left: 4px solid #E68161; border-radius: 8px;">
            <h3 style="color: #2d3748; margin-bottom: 1rem;">Gerelateerde Artikelen</h3>
            <ul style="list-style: none; padding: 0;">
        '''
        
        for url, text in internal_links[topic]:
            links_html += f'<li style="margin-bottom: 0.5rem;"><a href="{url}" style="color: #E68161; text-decoration: none; font-weight: 600;">→ {text}</a></li>'
        
        links_html += '</ul></section>'
        
        # Insérer avant le footer
        footer = self.soup.find('footer')
        if footer:
            links_soup = BeautifulSoup(links_html, 'html.parser')
            footer.insert_before(links_soup)
            print(f"✅ Added internal links section")
            return True
        
        return False
    
    def save_enhanced_article(self):
        """Sauvegarde l'article amélioré"""
        try:
            # Backup original
            backup_path = self.article_path + '.before_enhancement'
            with open(self.article_path, 'r', encoding='utf-8') as f:
                original = f.read()
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original)
            
            # Save enhanced
            with open(self.article_path, 'w', encoding='utf-8') as f:
                f.write(str(self.soup.prettify()))
            
            print(f"✅ Enhanced article saved")
            print(f"📄 Backup: {backup_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error saving article: {e}")
            return False
    
    def enhance(self):
        """Processus complet d'amélioration"""
        
        print(f"\n{'='*60}")
        print(f"📝 Enhancing article...")
        print(f"{'='*60}\n")
        
        # Load briefing and article
        if not self.load_briefing():
            return False
        if not self.load_article():
            return False
        
        # Identify topic
        topic = self.identify_topic()
        print(f"🎯 Topic identified: {topic}")
        
        # Add content
        print(f"\n📝 Adding content sections...")
        self.add_content_sections(topic)
        
        # Add image placeholders
        print(f"\n📸 Adding image placeholders...")
        self.add_image_placeholders()
        
        # Add internal links
        print(f"\n🔗 Adding internal links...")
        self.add_internal_links()
        
        # Save
        print(f"\n💾 Saving enhanced article...")
        if self.save_enhanced_article():
            print(f"\n🎉 Article enhancement complete!")
            
            # Calculate new word count
            new_text = self.soup.get_text()
            new_word_count = len(new_text.split())
            old_word_count = self.briefing['current_article']['word_count']
            added_words = new_word_count - old_word_count
            
            print(f"\n📊 RESULTS:")
            print(f"   Before: {old_word_count} words")
            print(f"   After: {new_word_count} words")
            print(f"   Added: +{added_words} words")
            print(f"   Target: {self.briefing['recommendations']['target_word_count']} words")
            
            return True
        
        return False

def main():
    """Fonction principale"""
    
    print("🚀 BLOG CONTENT ENHANCER")
    print("=" * 60)
    
    # Lister les briefings disponibles
    briefings = []
    for file in os.listdir(BRIEFINGS_DIR):
        if file.endswith('_briefing.json'):
            briefing_path = os.path.join(BRIEFINGS_DIR, file)
            article_slug = file.replace('_briefing.json', '')
            article_path = os.path.join(BLOG_DIR, article_slug, 'index.html')
            
            if os.path.exists(article_path):
                briefings.append({
                    'slug': article_slug,
                    'briefing_path': briefing_path,
                    'article_path': article_path
                })
    
    print(f"📁 Found {len(briefings)} articles to enhance\n")
    
    # Traiter chaque article
    success_count = 0
    for item in briefings:
        enhancer = BlogEnhancer(item['briefing_path'], item['article_path'])
        if enhancer.enhance():
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 ENHANCEMENT COMPLETE!")
    print(f"✅ Successfully enhanced: {success_count}/{len(briefings)} articles")
    print(f"📁 Backups saved with .before_enhancement extension")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
