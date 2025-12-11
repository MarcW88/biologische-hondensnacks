#!/usr/bin/env python3
"""
BLOG ANALYZER & BRIEFING GENERATOR
===================================

Analyse les articles existants, scrape les SERPs, 
et génère un briefing optimisé pour améliorer le contenu.

Étape 1: Analyse + Briefing (ce script)
Étape 2: Génération/Adaptation (futur script)

Auteur: AI Assistant
Date: December 2025
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import json
from datetime import datetime

# Configuration
BLOG_DIR = '/Users/marc/Desktop/biologische-hondensnacks/blog'
OUTPUT_DIR = '/Users/marc/Desktop/biologische-hondensnacks/blog-briefings'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

class BlogAnalyzer:
    """Analyse les articles de blog existants"""
    
    def __init__(self, blog_path):
        self.blog_path = blog_path
        self.analysis = {}
    
    def extract_article_info(self):
        """Extrait les infos de l'article existant"""
        try:
            html_file = os.path.join(self.blog_path, 'index.html')
            if not os.path.exists(html_file):
                return None
            
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Extraire titre
            h1 = soup.find('h1')
            title = h1.text.strip() if h1 else "Sans titre"
            
            # Extraire meta description
            meta_desc = soup.find('meta', {'name': 'description'})
            description = meta_desc['content'] if meta_desc else ""
            
            # Extraire contenu principal
            article = soup.find('article') or soup.find('main') or soup.find('body')
            
            # Compter mots
            text_content = article.get_text() if article else ""
            word_count = len(text_content.split())
            
            # Extraire structure H2-H6
            headings = []
            for level in range(2, 7):
                for heading in soup.find_all(f'h{level}'):
                    headings.append({
                        'level': level,
                        'text': heading.get_text().strip()
                    })
            
            # Compter images
            images = len(soup.find_all('img'))
            
            # Compter liens
            links = len(soup.find_all('a'))
            
            return {
                'title': title,
                'description': description,
                'word_count': word_count,
                'headings': headings,
                'images_count': images,
                'links_count': links,
                'html_path': html_file
            }
            
        except Exception as e:
            print(f"❌ Error analyzing article: {e}")
            return None

class SERPScraper:
    """Scrape les SERPs Google"""
    
    def __init__(self, keyword):
        self.keyword = keyword
        self.results = []
    
    def search_google(self, num_results=5):
        """Recherche Google et extrait top résultats"""
        try:
            # Requête Google
            query = self.keyword.replace(' ', '+')
            url = f"https://www.google.com/search?q={query}&num={num_results}"
            
            headers = {'User-Agent': USER_AGENT}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code != 200:
                print(f"⚠️ Google returned status {response.status_code}")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extraire résultats organiques
            search_results = soup.find_all('div', class_='g')
            
            results = []
            for result in search_results[:num_results]:
                try:
                    # Titre
                    title_elem = result.find('h3')
                    title = title_elem.text if title_elem else ""
                    
                    # URL
                    link_elem = result.find('a')
                    url = link_elem['href'] if link_elem else ""
                    
                    # Description
                    desc_elem = result.find('div', class_='VwiC3b')
                    description = desc_elem.text if desc_elem else ""
                    
                    if title and url:
                        results.append({
                            'title': title,
                            'url': url,
                            'description': description
                        })
                        
                except Exception as e:
                    continue
            
            self.results = results
            print(f"✅ Found {len(results)} SERP results for '{self.keyword}'")
            return results
            
        except Exception as e:
            print(f"❌ Error scraping Google: {e}")
            return []
    
    def analyze_competitor_content(self, url):
        """Analyse le contenu d'un concurrent"""
        try:
            headers = {'User-Agent': USER_AGENT}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code != 200:
                return None
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extraire contenu principal
            article = soup.find('article') or soup.find('main')
            if not article:
                # Fallback: chercher le plus gros conteneur de texte
                article = max(soup.find_all(['div', 'section']), 
                            key=lambda x: len(x.get_text()))
            
            text_content = article.get_text() if article else ""
            word_count = len(text_content.split())
            
            # Structure H2-H6
            headings = []
            for level in range(2, 7):
                for heading in soup.find_all(f'h{level}'):
                    headings.append({
                        'level': level,
                        'text': heading.get_text().strip()
                    })
            
            # Images
            images_count = len(soup.find_all('img'))
            
            return {
                'url': url,
                'word_count': word_count,
                'headings': headings,
                'images_count': images_count
            }
            
        except Exception as e:
            print(f"⚠️ Could not analyze {url}: {e}")
            return None

class BriefingGenerator:
    """Génère un briefing optimisé"""
    
    def __init__(self, article_analysis, serp_analysis):
        self.article = article_analysis
        self.serp = serp_analysis
        self.briefing = {}
    
    def analyze_gaps(self):
        """Identifie les lacunes de contenu"""
        
        # Analyser la longueur
        competitor_word_counts = [c.get('word_count', 0) 
                                 for c in self.serp.get('competitors', []) 
                                 if c]
        avg_competitor_words = sum(competitor_word_counts) / len(competitor_word_counts) if competitor_word_counts else 1000
        
        current_words = self.article.get('word_count', 0)
        word_gap = max(0, int(avg_competitor_words - current_words))
        
        # Analyser les sujets couverts par les concurrents
        competitor_headings = []
        for comp in self.serp.get('competitors', []):
            if comp and 'headings' in comp:
                competitor_headings.extend([h['text'] for h in comp['headings']])
        
        # Sujets fréquents chez les concurrents
        from collections import Counter
        heading_words = []
        for heading in competitor_headings:
            words = heading.lower().split()
            heading_words.extend(words)
        
        common_topics = Counter(heading_words).most_common(10)
        
        return {
            'word_gap': word_gap,
            'target_word_count': int(avg_competitor_words),
            'common_topics': [topic[0] for topic in common_topics if len(topic[0]) > 3],
            'competitor_avg_headings': sum([len(c.get('headings', [])) for c in self.serp.get('competitors', []) if c]) / max(len(self.serp.get('competitors', [])), 1)
        }
    
    def generate_briefing(self):
        """Génère le briefing complet"""
        
        gaps = self.analyze_gaps()
        
        briefing = {
            'meta': {
                'generated_at': datetime.now().isoformat(),
                'article_path': self.article.get('html_path', ''),
                'keyword': self.serp.get('keyword', '')
            },
            'current_article': {
                'title': self.article.get('title', ''),
                'word_count': self.article.get('word_count', 0),
                'headings_count': len(self.article.get('headings', [])),
                'images_count': self.article.get('images_count', 0)
            },
            'serp_analysis': {
                'top_5_titles': [r['title'] for r in self.serp.get('results', [])],
                'avg_competitor_words': gaps['target_word_count'],
                'common_topics': gaps['common_topics']
            },
            'recommendations': {
                'target_word_count': gaps['target_word_count'],
                'word_count_to_add': gaps['word_gap'],
                'recommended_headings_count': int(gaps['competitor_avg_headings']),
                'topics_to_cover': gaps['common_topics'][:5],
                'content_structure': self._suggest_structure()
            },
            'competitors': self.serp.get('competitors', [])
        }
        
        self.briefing = briefing
        return briefing
    
    def _suggest_structure(self):
        """Suggère une structure d'article"""
        
        # Analyser la structure des concurrents
        common_sections = []
        for comp in self.serp.get('competitors', []):
            if comp and 'headings' in comp:
                for h in comp['headings']:
                    if h['level'] == 2:
                        common_sections.append(h['text'].lower())
        
        from collections import Counter
        section_counts = Counter(common_sections)
        
        # Sections communes
        suggested_sections = []
        for section, count in section_counts.most_common(8):
            suggested_sections.append({
                'title': section.title(),
                'frequency': count,
                'priority': 'high' if count >= 3 else 'medium'
            })
        
        return suggested_sections

def main():
    """Fonction principale"""
    
    print("📊 BLOG ANALYZER & BRIEFING GENERATOR")
    print("=" * 60)
    
    # Créer dossier output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Scanner les articles de blog
    blog_articles = []
    for item in os.listdir(BLOG_DIR):
        item_path = os.path.join(BLOG_DIR, item)
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, 'index.html')):
            blog_articles.append({
                'slug': item,
                'path': item_path
            })
    
    print(f"📁 Found {len(blog_articles)} blog articles\n")
    
    # Analyser chaque article
    for article in blog_articles:
        print(f"\n{'='*60}")
        print(f"📝 Analyzing: {article['slug']}")
        print(f"{'='*60}")
        
        # Analyser l'article existant
        analyzer = BlogAnalyzer(article['path'])
        article_analysis = analyzer.extract_article_info()
        
        if not article_analysis:
            print(f"⚠️ Could not analyze article")
            continue
        
        print(f"📄 Current article: {article_analysis['word_count']} words, "
              f"{len(article_analysis['headings'])} headings")
        
        # Extraire le mot-clé du titre ou slug
        keyword = article_analysis['title']
        
        # Scraper les SERPs
        print(f"🔍 Searching Google for: '{keyword}'")
        scraper = SERPScraper(keyword)
        serp_results = scraper.search_google(num_results=5)
        
        # Analyser les concurrents
        competitors_analysis = []
        print(f"📊 Analyzing top {len(serp_results)} competitors...")
        for i, result in enumerate(serp_results[:5], 1):
            print(f"   {i}. {result['title'][:60]}...")
            comp_analysis = scraper.analyze_competitor_content(result['url'])
            if comp_analysis:
                competitors_analysis.append(comp_analysis)
        
        # Générer le briefing
        print(f"\n✍️ Generating briefing...")
        generator = BriefingGenerator(
            article_analysis,
            {
                'keyword': keyword,
                'results': serp_results,
                'competitors': competitors_analysis
            }
        )
        briefing = generator.generate_briefing()
        
        # Sauvegarder le briefing
        output_file = os.path.join(OUTPUT_DIR, f"{article['slug']}_briefing.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(briefing, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Briefing saved: {output_file}")
        
        # Afficher résumé
        print(f"\n📋 BRIEFING SUMMARY:")
        print(f"   Current words: {briefing['current_article']['word_count']}")
        print(f"   Target words: {briefing['recommendations']['target_word_count']}")
        print(f"   Gap: +{briefing['recommendations']['word_count_to_add']} words")
        print(f"   Topics to cover: {', '.join(briefing['recommendations']['topics_to_cover'][:3])}")
    
    print(f"\n{'='*60}")
    print(f"🎉 ANALYSIS COMPLETE!")
    print(f"📁 Briefings saved in: {OUTPUT_DIR}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
