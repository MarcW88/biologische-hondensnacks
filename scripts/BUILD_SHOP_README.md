# 🏗️ BUILD COMPLETE SHOP - Mode d'emploi

## Description
Ce script génère un shop complet avec:
- ✅ 67 pages produit individuelles avec descriptions uniques via ChatGPT
- ✅ Pages de listing avec pagination (12 produits par page = 6 pages)
- ✅ Images matchées automatiquement depuis `/images/`
- ✅ Liens internes corrects entre pages
- ✅ CSS et JavaScript inclus
- ✅ 100% en néerlandais

## Prérequis

1. **Clé API OpenAI**
   - Nécessaire pour générer des descriptions uniques
   - Se trouve normalement dans un de tes autres scripts Python
   - Format: `sk-proj-...`

2. **Fichiers requis**
   - `Hondensnacks Catalogus (1).csv` (67 produits)
   - Images dans `/images/` (37 images trouvées)

## Utilisation

### Option 1: Définir la clé dans le script

1. Ouvre `/Users/marc/Desktop/biologische-hondensnacks/scripts/build_complete_shop.py`
2. Ligne 972, remplace:
   ```python
   API_KEY = None
   ```
   par:
   ```python
   API_KEY = "sk-proj-..."  # Ta vraie clé API
   ```
3. Lance le script:
   ```bash
   cd /Users/marc/Desktop/biologische-hondensnacks
   python3 scripts/build_complete_shop.py
   ```

### Option 2: Passer la clé en argument

```bash
cd /Users/marc/Desktop/biologische-hondensnacks
python3 scripts/build_complete_shop.py "sk-proj-..."
```

### Option 3: Sans clé API (descriptions fallback)

```bash
cd /Users/marc/Desktop/biologische-hondensnacks
python3 scripts/build_complete_shop.py
# Réponds "o" quand demandé
```

## Ce qui sera créé

### Structure des fichiers

```
/winkel/
  ├── index.html              (Page 1 - produits 1-12)
  ├── shop-styles.css
  └── page/
      ├── 2/index.html        (Page 2 - produits 13-24)
      ├── 3/index.html        (Page 3 - produits 25-36)
      ├── 4/index.html        (Page 4 - produits 37-48)
      ├── 5/index.html        (Page 5 - produits 49-60)
      └── 6/index.html        (Page 6 - produits 61-67)

/produits/
  ├── chewpi-kauwstaaf-20-kg-extra-large.html
  ├── chewpi-kauwstaaf-5-kg-small-4-pack.html
  └── ... (65 autres pages produit)

/css/
  └── product-page.css
```

### Fonctionnalités

✅ **Pages produit individuelles**
- Description unique générée par ChatGPT (120-150 mots)
- Image matchée automatiquement
- Prix avec réduction si applicable
- Lien vers bol.com
- Breadcrumb navigation
- Schema.org markup

✅ **Pages de listing**
- 12 produits par page (grille 3 colonnes)
- Pagination fonctionnelle
- Liens vers pages produit
- Hero section avec statistiques
- Responsive design

✅ **SEO-friendly**
- URLs slugifiées (ex: `chewpi-kauwstaaf-20-kg-extra-large.html`)
- Meta descriptions
- Canonical URLs
- Schema markup

## Temps d'exécution

Avec ChatGPT API:
- ~67 appels API (1 par produit)
- ~10-15 minutes (selon débit API)

Sans ChatGPT API:
- ~30 secondes

## Après l'exécution

1. **Vérifier localement**
   ```bash
   open /Users/marc/Desktop/biologische-hondensnacks/winkel/index.html
   ```

2. **Commit & Deploy**
   ```bash
   git add winkel/ produits/ css/
   git commit -m "🏗️ Nouveau shop complet avec 67 produits et pagination"
   git push origin main
   ```

3. **Tester en production**
   - `https://biologische-hondensnacks.nl/winkel/`
   - `https://biologische-hondensnacks.nl/winkel/page/2/`
   - `https://biologische-hondensnacks.nl/produits/chewpi-kauwstaaf-20-kg-extra-large.html`

## Notes importantes

⚠️ **Ne JAMAIS commiter la clé API**
- Toujours mettre `API_KEY = None` avant de commit
- Ou utiliser `.env` + `.gitignore`

⚠️ **Images**
- 37 images disponibles
- 67 produits
- ~30 produits utiliseront des images réutilisées (matching par nom)
- Les autres auront `images/placeholder.jpg` (à créer si nécessaire)

⚠️ **ChatGPT**
- Coût estimé: ~$0.50-1.00 pour 67 descriptions
- Modèle: GPT-4
- Température: 0.8 (pour variété)

## Troubleshooting

**Erreur: "OpenAIError: The api_key client option must be set"**
→ Définis ta clé API (voir "Utilisation")

**Erreur: "FileNotFoundError: Hondensnacks Catalogus (1).csv"**
→ Vérifie que le CSV est bien dans `/Users/marc/Desktop/biologische-hondensnacks/`

**Erreur: "No module named 'openai'"**
→ Installe: `pip3 install openai`

**Les images ne s'affichent pas**
→ Vérifie que les images sont dans `/images/` et crée un `placeholder.jpg` si nécessaire
