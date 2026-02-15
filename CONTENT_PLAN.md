# Content Plan: Élargissement du Champ Sémantique

## Structure Actuelle
- **Homepage** : biologische-hondensnacks.nl
- **Catégories** : Training, Puppy, Kauw, Graanvrij, Natuurlijke
- **Blog** : 3 articles (puppys gids, graanvrije vs normale, waarom biologisch)
- **Pages** : Over ons, Contact, Winkel

---

## 1. NOUVEAUX HUBS CATÉGORIES (5 pages)

### 1.1 Hypoallergene Hondensnacks
**URL** : `/hypoallergene-hondensnacks/`
**H1** : Hypoallergene Hondensnacks voor Gevoelige Honden
**Focus** : één eiwit, graanvrij, zonder kip/rund, voedselallergie
**Mots-clés** : hypoallergene hondensnacks, snacks voor honden met allergie, één-eiwit snacks

### 1.2 Hondensnacks per Leeftijd
**URL** : `/hondensnacks-per-leeftijd/`
**H1** : Hondensnacks per Leeftijd: Puppy, Adult & Senior
**Focus** : recommandations par âge, texture, taille, fréquence
**Mots-clés** : hondensnacks puppy, snacks volwassen hond, senior hondensnacks

### 1.3 Kauwsnacks voor Tandverzorging
**URL** : `/kauwsnacks-tandverzorging/`
**H1** : Natuurlijke Kauwsnacks voor Gezonde Tanden
**Focus** : tandplak, kauwbehoefte, duur van kauwen, veiligheid
**Mots-clés** : kauwsnacks tanden, hondensnacks tandverzorging, natuurlijke kauwbotten

### 1.4 Caloriearme Hondensnacks
**URL** : `/caloriearme-hondensnacks/`
**H1** : Caloriearme & Light Hondensnacks
**Focus** : surpoids, chiens castrés, faible activité, dieet
**Mots-clés** : light hondensnacks, caloriearme snacks hond, dieet hondensnacks

### 1.5 Duurzame Hondensnacks
**URL** : `/duurzame-hondensnacks/`
**H1** : Duurzame & Milieuvriendelijke Hondensnacks
**Focus** : bio, herkomst, impact environnemental, insect snacks
**Mots-clés** : duurzame hondensnacks, eco hondensnacks, insecten snacks hond

---

## 2. ARTICLES INFORMATIONNELS (10 articles)

### Santé & Nutrition
1. **Wat zijn de voordelen van biologische hondensnacks?**
   `/blog/voordelen-biologische-hondensnacks/`
   
2. **Welke hondensnacks zijn het gezondst voor dagelijks gebruik?**
   `/blog/gezondste-hondensnacks-dagelijks/`
   
3. **Hond met voedselallergie: welke snacks zijn veilig?**
   `/blog/hondensnacks-voedselallergie/`
   
4. **Natuurlijke hondensnacks voor honden met gevoelige maag**
   `/blog/hondensnacks-gevoelige-maag/`
   
5. **Hoeveel hondensnacks per dag is gezond?**
   `/blog/hoeveel-hondensnacks-per-dag/`

### Guides Pratiques
6. **Beste trainingssnacks voor puppies: waar moet je op letten?**
   `/blog/trainingssnacks-puppies-gids/`
   
7. **Top hondensnacks per vleessoort: zalm, hert, lam, kip**
   `/blog/hondensnacks-per-vleessoort/`
   
8. **Hondensnacks combineren met hoofdvoeding**
   `/blog/hondensnacks-combineren-hoofdvoeding/`

### Lifestyle & Occasions
9. **Hondensnacks voor op reis en tijdens wandelingen**
   `/blog/hondensnacks-reis-wandelingen/`
   
10. **Verjaardagscadeau voor je hond: biologische snackbox ideeën**
    `/blog/verjaardag-hond-snackbox/`

---

## 3. ENRICHISSEMENT PAGES EXISTANTES

### Pour chaque catégorie (Training, Puppy, Kauw, Graanvrij) ajouter :
- [ ] Bloc "Wat zijn [X] hondensnacks?"
- [ ] Bloc "Voordelen van [X] snacks"
- [ ] Bloc "Hoe kies je de juiste [X] snack?"
- [ ] FAQ (3-5 questions People Also Ask)

### Lexique à injecter :
hondensnoepjes, hondentraktaties, beloningssnoepjes, hondenkoekjes, kauwbotten, 
hondenkluiven, gedroogde vleessnacks, trainers, natuurlijke snacks, biologische snacks, 
hypoallergene traktaties, gezonde beloningen, eiwitrijke snacks

---

## 4. MAILLAGE INTERNE

Chaque nouveau contenu doit linker vers :
- ✓ Au moins 1 page catégorie existante
- ✓ Au moins 1 autre article informatif
- ✓ Pages produits/affiliation pertinentes

### Structure de liens :
```
Homepage
├── Catégories (Training, Puppy, Kauw, Graanvrij, Natuurlijke)
│   └── Nouveaux Hubs (Hypoallergeen, Leeftijd, Tanden, Light, Duurzaam)
├── Blog
│   ├── Articles existants
│   └── Nouveaux articles informationnels
└── Winkel (produits)
```

---

## 5. PRIORITÉS D'IMPLÉMENTATION

### Phase 1 (Cette session)
1. ✓ Créer hub "Hypoallergene Hondensnacks"
2. ✓ Créer hub "Kauwsnacks Tandverzorging"
3. ✓ Créer article "Hoeveel hondensnacks per dag"
4. ✓ Enrichir page Training existante

### Phase 2 (Prochaine session)
- Hub "Caloriearme Hondensnacks"
- Hub "Hondensnacks per Leeftijd"
- Articles santé (allergie, gevoelige maag)

### Phase 3
- Hub "Duurzame Hondensnacks"
- Articles lifestyle (reis, verjaardag)
- Enrichissement autres catégories

---

## 6. TEMPLATE STRUCTURE PAGE HUB

```html
<h1>[Titre optimisé]</h1>
<p class="intro">[Paragraphe d'intro 150-200 mots]</p>

<section id="wat-zijn">
  <h2>Wat zijn [X] hondensnacks?</h2>
  [Définition, exemples, contexte]
</section>

<section id="voordelen">
  <h2>Voordelen van [X] snacks</h2>
  [Liste des bénéfices avec explications]
</section>

<section id="beste-producten">
  <h2>Beste [X] hondensnacks [année]</h2>
  [Top 5-10 produits avec liens affiliation]
</section>

<section id="hoe-kiezen">
  <h2>Hoe kies je de juiste [X] snack?</h2>
  [Critères de sélection]
</section>

<section id="faq">
  <h2>Veelgestelde vragen</h2>
  [5-7 FAQ avec schema markup]
</section>

<section id="gerelateerd">
  <h2>Gerelateerde artikelen</h2>
  [Liens internes]
</section>
```
