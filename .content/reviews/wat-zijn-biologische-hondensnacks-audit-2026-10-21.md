# Audit Guide — Wat zijn biologische hondensnacks?

Date : 21 octobre 2026. Mode : `AUDIT`, pas `PUBLISH_REVIEW`.
URL : https://biologische-hondensnacks.nl/gidsen/wat-zijn-biologische-hondensnacks/

## Décision

**LIGHT_UPDATE — confiance élevée sur le diagnostic éditorial.**
Conserver l’URL et la structure principale. Ajouter une explication concrète de la
production biologique, améliorer l’accessibilité de la définition et réduire les
répétitions réglementaires avec les guides voisins. Pas de justification pour une
réécriture intégrale ou une fusion à ce stade. Maintenir l’état `noindex,follow`.
Ce rapport ne donne aucune autorisation de publication ou d’indexation.

Le test fait aussi apparaître une limite d’installation : les fichiers partagés
sont identiques à Bloc-notes, mais certains fichiers auxiliaires que leurs SKILL
mentionnent n’existent pas dans le paquet source copié. Identité ne signifie donc
pas autonomie technique complète. Les blocages sont décrits ci-dessous ; aucun
script de substitution n’a été inventé.

## Entrées et traçabilité

- Workflow lu intégralement : `.agents/skills/guide-analysis-workflow/SKILL.md`.
- Instructions de rubrique, contexte, routage et brief existant lus.
- Les onze skills d’audit applicables ont été lus ; les protocoles anti-ai-slop
  présents et nécessaires ont également été lus. Les sorties réelles sont ici.
- `python scripts/sync_shared_agents.py --check` : 66 fichiers identiques à
  `MarcW88/bloc-notes-numerique@5b798c38648fdc32a9bbb0f2f6742b2dca9b7951`.
- Page en ligne lue avec recherche web et téléchargée en HTML (HTTP 200).
- Guides voisins lus : biologique/naturel, contrôle du label, lecture des
  ingrédients, quantité quotidienne. Inventaire des titres des dix guides locaux.
- L’ancien `.content/guides/wat-zijn-biologische-hondensnacks.md` contient des
  mentions PASS générales ; elles ne sont pas reprises comme preuves.
- GSC, analytics, backlinks et historique de requêtes non fournis pour cette URL.
  Aucun diagnostic de performance, volume, CTR ou cannibalisation mesurée.

## 1. seo-content-audit — exécuté, action UPDATE

Rôle actuel : expliquer la signification de biologique pour les snacks pour chien.
Valeur à conserver : seuil relatif aux ingrédients agricoles (pas au poids total),
distinction production/nutrition, distinction avec naturel, sources primaires,
absence de faux test et de classement produit. L’URL mérite une existence propre.

Problème principal : le texte explique ce que le cadre réglementaire permet de
nommer biologique sans vraiment expliquer la réalité de production derrière ce
mot. Dans le tableau « Wat verandert biologisch wél », les bénéfices explicatifs
restent proches de « conditions », « indications » et « cadre contrôlable ».
L’explication est en partie circulaire pour un lecteur débutant.

Confiance élevée ; aucune suppression, redirection ou fusion recommandée.

## 2. seo-keyword — exécuté avec données limitées

Sujet cible confirmé par le brief et le contenu : `wat zijn biologische
hondensnacks`. Intention informationnelle dominante, avec une conséquence de choix.
Variantes de travail, non issues de volumes mesurés : `wat betekent biologisch bij
hondensnacks`, `biologische hondensnacks betekenis`.

Inspection des résultats web : mélange de pages marchandes et explicatives ;
cela ne justifie pas de transformer cette URL en classement. Recherche limitée,
non équivalente à une SERP Google géolocalisée NL exhaustive. Priorité par volume,
difficulté et potentiel de trafic : NON ÉVALUABLE sans données.

## 3. search-intent — exécuté, NEEDS_WORK

Type : EXPLAINER dominant, CHOICE secondaire. Lecteur : propriétaire de chien
néerlandophone qui veut comprendre une appellation avant de choisir un produit.
Résultat attendu : expliquer en termes simples ce qui est biologique, comment le
reconnaître et ce que cela ne garantit pas pour son chien.

Réponse précoce présente, mais la formulation « petfoodproducten waarbij de
biologische aanduiding gekoppeld is aan Europese regels » est administrative.
Expliquer d’abord les ingrédients et les règles de production ; nommer ensuite
les textes qui encadrent la désignation. La section historique sur la règle petfood
peut être raccourcie, sans perdre la source ou le seuil.

## 4. content-refresh — exécuté après UPDATE

Diagnostic : thin value partielle + langage abstrait + recouvrement de sous-sujets.
Niveau : correction ciblée, pas full rewrite. Aucun intent drift temporel démontré.

- Garder : seuil, limites nutritionnelles, sources, distinction des dimensions,
  renvois utiles, URL, canonical et intention.
- Raccourcir : seconde définition et contexte juridique répété.
- Ajouter : explication de production avec exemples sourcés distinguant matières
  végétales, élevage et transformation ; ne pas faire de promesse « zéro pesticide ».
- Ajouter : exemple pédagogique explicitement fictif de lecture de composition,
  sans marque ou certification inventée, pour illustrer la différence entre
  ingrédient bio et produit vendu comme biologique.
- Vérifier avant rédaction : portée exacte des règles utilisées et formulations
  permettant d’éviter bio = local, meilleur pour chaque chien ou sans additifs.

## 5. fact-check — exécuté, pas de contradiction centrale établie

| Affirmation | Statut | Preuve / action |
|---|---|---|
| La désignation et les ingrédients biologiques des petfoods relèvent de 2023/2419 | CONFIRMED | Règlement officiel, article 3 ; garder |
| Au moins 95 % en poids des ingrédients agricoles, avec autres conditions | CONFIRMED | Article 3(1)(a), extrait officiel retrouvé ; conserver le dénominateur exact |
| Sous le seuil, références possibles aux ingrédients sous conditions | PARTIAL | Base réglementaire identifiée ; vérifier toutes les conditions et exceptions dans la version officielle lisible avant correction juridique détaillée |
| EU-biologo obligatoire pour le préemballé relevant d’art. 3(1)(a), depuis le 1 mai 2024 | CONFIRMED sur le texte identifié | Articles 4 et 6, extrait officiel ; garder la qualification, pas une règle universelle sans exception |
| Skal intervient dans le contrôle biologique aux Pays-Bas | CONFIRMED dans ce périmètre | Source Skal actuelle ; source liée surtout structurée B2B, qui renvoie le petfood consommateur vers une autre page |
| Naturel n’est pas un certificat biologique | CONFIRMED | NVWA classe naturel parmi les productbeschrijvers ; ne pas confondre avec certification biologique |
| Treats/chews généralement complémentaires, non complets | CONFIRMED | FEDIAF, section Top Tips on Treating ; conserver « doorgaans » |
| Biologique ne garantit pas faible apport calorique, mono-ingrédient ou adéquation individuelle | CONFIRMED comme limite de portée | Critères biologiques distincts des critères nutritionnels ; ne pas convertir en comparaison sanitaire chiffrée |
| Vérifié le 14 septembre 2026 | UNVERIFIED comme historique | Date affichée et ancien registre présents, mais pas de journal détaillé prouvant cette vérification passée ; ne pas remplacer automatiquement par la date du présent audit |

Accès aux variantes EUR-Lex inégal : certaines montrent une protection robot,
une variante bilingue et des extraits officiels indexés ont fourni des passages.
Cela ne constitue pas une vérification exhaustive de consolidation ou un avis
juridique. Aucune allégation de test physique ou d’expérience inventée relevée.

Sources consultées :
- https://eur-lex.europa.eu/legal-content/EN-DA/ALL/?uri=CELEX%3A32023R2419
- https://www.skal.nl/onderwerpen/import/aanduidingen/bio-checker/diervoeder
- https://www.nvwa.nl/onderwerpen/diervoeder/claims-op-diervoeders-en-petfood/wat-is-een-claim
- https://europeanpetfood.org/pet-food-facts/fact-sheets/quality-and-safety/chews-and-treats-for-dogs/
- Commission européenne, production biologique :
  https://agriculture.ec.europa.eu/farming/organic-farming/organic-production-and-products_en
  (repérage des éléments de production à approfondir avant rédaction).

## 6. evidence-based-reviews — NON APPLICABLE

Aucun jugement expérientiel produit, comparatif d’agrément ou expérience réelle
non documentée n’est nécessaire pour cette page explicative.

## 7. affiliate-value — exécuté, valeur existante à renforcer

La page reste utile sans affiliation ; pas de liens marchands dans le corps
principal téléchargé. Les limites du label et la distinction avec nutrition sont
de vraies informations indépendantes. Manque : traduire le critère de production
en compréhension concrète plutôt qu’ajouter une sélection de produits.
Aucune preuve de merchant duplication relevée ; pas d’analyse exhaustive de plagiat.

## 8. internal-linking-audit — lecture/extraction effectuées, script BLOQUÉ

Le script `scripts/internal_link_audit.py` décrit par le skill n’est présent ni
à la racine ni dans le paquet installé. Son exécution et ses exports standards
ne peuvent être déclarés réussis. `links.json` contient l’extraction HTML observée,
avec résolution selon le vrai `<base href="/">`, et non un crawl Firecrawl.

Les liens corporels vers biologique/naturel, contrôle du label et quantité
quotidienne sont déjà présents et leurs destinations directes répondent 200 :
`no_action_needed`. L’outil web avait résolu les liens relatifs sans tenir compte
du base et rapporté des 404 : ce n’est PAS retenu comme lien cassé.

Un renvoi vers la lecture des ingrédients serait pertinent près de la section
sur la composition ; sa cible a été lue. Il apparaît dans le footer, pas dans le
corps : lien contextuel OPTIONNEL, aucune obligation de quota.

## 9. anti-ai-slop — exécuté sur les protocoles présents

Contrat : expliquer clairement un terme à un propriétaire de chien, sans promesse
sanitaire ou produit inventée. But dominant : informational writing.
Risque de contenu générique : MEDIUM, pas HIGH ; aucune attribution d’origine IA.

| Preuve visible | Impact | Correction et critère de contrôle |
|---|---|---|
| Définitions successives autour d’un « cadre » et d’une « indication » | Le lecteur comprend qu’il y a des règles, peu ce qu’elles changent | Remplacer la répétition par explication de production vérifiable ; le lecteur doit pouvoir décrire un changement concret |
| Plusieurs sections aboutissent à une limite du label | La prudence prend plus de place que l’explication positive | Conserver les limites en les hiérarchisant ; ajouter les mécanismes absents |
| Seuil, logo et limites nutritionnelles répétés dans trois guides | La spécificité de chaque URL s’affaiblit | Cible = production/définition ; naturel = comparaison des termes ; label = contrôle pratique |

Faux positifs écartés : tableau utile, sources communes normales, composants
visuels partagés normaux. Les plans des dix guides ne sont pas identiques ; pas
de preuve de clonage systématique imposant une réécriture complète.

## 10. seo-onpage — huit dimensions

| Dimension | Résultat | Observation |
|---|---|---|
| Title | PASS | Conforme au sujet, sans ranking trompeur |
| Meta description | PASS | Reflète la définition, le seuil et les limites |
| Headings | PASS | Un H1, sous-questions pertinentes ; pas de quota |
| Corps | NEEDS_WORK | Compréhension de production insuffisamment concrète |
| Liens | PASS pour les destinations testées | Renvois déjà présents, option composition ci-dessus |
| Médias | PASS / pas d’image requise pour expliquer le texte actuel | Aucune raison d’exiger une image décorative |
| URL | PASS | URL descriptive ; aucun changement proposé |
| Schema | PASS pour honnêteté du type observé | BreadcrumbList visible dans le HTML, pas de faux Review ; Rich Results Test non exécuté |

## 11. seo-technical — contrôle borné à l’URL, PARTIEL

- Crawl : cible HTTP 200 ; robots.txt HTTP 404. Un robots absent ne bloque pas à
  lui seul Google. Aucune conclusion sur le crawl effectif Google sans GSC/logs.
- Indexabilité : `noindex,follow` et canonical vers elle-même dans HTML reçu.
  Conforme au statut de brouillon, donc pas un incident à corriger automatiquement.
  Tant qu’il reste, la page n’est pas destinée à performer en recherche indexée.
- Rendering : texte principal présent en HTML sans exécution JS. Rendu mobile/
  desktop NON vérifié : Chromium absent, téléchargement Playwright tenté puis
  échoué (archive invalide). Aucun PASS responsive ou accessibilité rendu.
- Architecture : destinations testées 200 ; sitemap.xml HTTP 404. À traiter avant
  une ouverture à l’indexation, pas en ajoutant les brouillons au sitemap.
- Données structurées : BreadcrumbList et canonical inspectés ; validation Google
  et inspection d’URL NON exécutées.
- Expérience/sécurité : HTTPS et en-tête HSTS observés ; CWV, INP, CLS et contrôle
  visuel NON MESURÉS. Le template technique référencé par le skill est absent.

`python validate_guide_quality.py` : PASS pour les dix guides, contrôle structurel
local. Ce résultat n’implique ni exactitude factuelle ni profondeur ni validation
visuelle et ne constitue pas un PUBLISH_REVIEW de cette page.

## 12. seo-drift — NON APPLICABLE

Aucune version réécrite ; pas de baseline avant/après utile. Pas de score inventé.

## 13. editorial-qa — exécuté, corrections requises

- Intent : réponse précoce et rôle clair, explication à renforcer.
- Original affiliate value : valeur indépendante présente, amélioration ciblée.
- Factuality : pas de contradiction centrale établie ; contrôle juridique complet
  et traçabilité de date restent limités comme indiqué.
- Natural Dutch : globalement compréhensible ; « petfoodproducten », « aanduiding »
  et « productiekader » rendent la première réponse plus administrative que nécessaire.
- SEO preservation : conserver URL, sujet, H1, liens utiles et informations justes.
- User usefulness : utile sans lien affilié ; ne permet pas encore de comprendre
  assez concrètement la production biologique.
- Image : `NOT_NEEDED` pour une image générée. Un éventuel exemple de vrai label
  doit être fidèle, sourcé et autorisé, pas produit par IA. Aucune requête créée.

Pas de PASS de publication. `PUBLISH_REVIEW` non déclenché en mode AUDIT.

## Plan de correction priorisé / handoff

1. **P1 — expliquer la production réelle** : reformuler l’entrée puis ajouter les
   mécanismes nécessaires, sur preuves de production adaptées. Ne pas transformer
   « bio » en bénéfice santé, promesse de zéro résidu, local ou absence d’additifs.
2. **P2 — rendre le seuil compréhensible** : exemple pédagogique clairement fictif,
   sans inventer un produit réel ni affirmer que le seuil suffit à lui seul.
3. **P2 — différencier les trois guides** : garder le détail de production ici,
   renvoyer aux contrôles du label et à la comparaison naturel sans les redévelopper.
4. **P2 — fiabiliser la preuve affichée** : source Skal orientée consommateur et
   preuve de vérification datée ; ne pas changer arbitrairement le 14 septembre.

Avant validation finale : relancer les faits sur le texte corrigé, le maillage,
la qualité rédactionnelle, les contrôles SEO et la lecture rendue lorsque le
navigateur est disponible, puis `guide-analysis-workflow / PUBLISH_REVIEW`.
Les aides manquantes (script maillage, template technique) doivent être restaurées
à partir de leurs vraies sources, pas remplacées silencieusement par un faux PASS.

Aucun article, agent, CSS, état d’indexation ou fichier source n’a été modifié par
cet audit. Seuls les preuves et rapports d’audit ont été ajoutés.
