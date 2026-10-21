# Installation des agents — vérification du 21 octobre 2026

L’objectif est l’exécution des agents originaux, sans réécriture de leurs règles.
Les 66 fichiers de référence n’ont pas changé. 144 fichiers auxiliaires manquants
ont été copiés depuis les sources originales et verrouillés par commit et SHA256.
Les sources comprennent dageno-agents/internal-linking-audit,
ch040602/anti-ai-slop, rampstackco/claude-skills,
msimchowitz/writing-skills et seranking/seo-skills.

## Contrôles réellement effectués

- Identité des 66 fichiers originaux et couverture des 15 correspondances : PASS.
- Existence et SHA256 des 144 auxiliaires : PASS.
- Tous les liens Markdown locaux des SKILL actifs : résolus.
- Validateur du paquet anti-ai-slop complet : 0 critical/high/medium/low.
- Maillage original exécuté en import sur le vrai HTML de la page testée :
  1 page analysée, 3 liens déjà présents, 1 proposition contextuelle, aucun
  ajout manquant inventé. Les URLs ont été résolues selon le base du document
  par un export technique séparé ; le script original n’a pas été modifié.
- Playwright : navigateur installé via miroir de secours ; script original
  exécuté sur la page, deux captures 1440×1000 et 390×844. HTTP 200,
  pas de débordement horizontal, captures inspectées.
- Tests d’interface : PASS sur 104 couples page/viewport, 97 combinaisons du Finder, navigation clavier et survol.
- Build préservant les contenus : PASS. Contrôles des 52 pages : PASS.
- Adaptateurs de commandes de validation installés : échecs de contenu possibles
  sur les pages incomplètes, jamais présentés comme dépendances manquantes ou
  comme validation éditoriale. Aucun contenu, CSS ou état d’indexation modifié.

## Périmètre et limites

L’installation locale des dépendances ne crée pas de compte SE Ranking,
Firecrawl, Google ou générateur d’images et ne fournit aucune clé API. Les accès
externes sont requis seulement par les étapes qui les utilisent. Aucun score ou
résultat de ces services n’est simulé.

Les Actions françaises historiques de génération produits/marques/offres sont
hors du runtime des agents : leur application Python d’origine n’existe pas sur
ce site HTML et elles restent non migrées. Elles ne sont pas présentées comme
fonctionnelles. Une action commune distincte vérifie le vrai build de ce site.
L’installation d’agents et la migration de cette application restent deux travaux
différents ; copier les agents n’autorise pas à générer du contenu français ici.

Les résultats de l’audit éditorial précédent restent valables. Les blocages
maillage et navigateur ont été levés ; ils ne transforment pas LIGHT_UPDATE en
approbation de publication.
