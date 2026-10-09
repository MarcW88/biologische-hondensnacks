# Behoeften — rédaction, correction et nouvelle page

Scope : uniquement `/voor-gevoelige-honden/`. Utiliser **après** `behoeften-analysis.md / AUDIT` pour une page existante ; sur une page nouvelle, commencer par intention, périmètre, cannibalisation, preuves et brief. La langue de toutes les pages est le **néerlandais naturel (NL)**.

L'orchestration suit la séparation **analyse → rédaction/correction → analyse finale**, déjà utilisée dans les dépôts de référence. Elle s'appuie sur les skills existants et non sur un nouvel agent monolithique.

## Décision d'entrée

- `KEEP` : ne pas réécrire ;
- `LIGHT_UPDATE` : corriger uniquement les faiblesses identifiées ;
- `DEEP_REWRITE` : reconstruire après avoir listé ce qu'il faut préserver ;
- `MERGE` ou `NOINDEX` : arrêter et demander décision éditoriale, ne pas produire une page concurrente.

## Skills à exécuter (ceux déjà présents dans .agents/skills/)

1. `search-intent`, `seo-keyword`, `jobs-to-be-done` selon le besoin : problème pratique, intention, sous-questions, rôle par rapport aux autres clusters.
2. `content-audit` / `content-refresh` pour une URL existante : valeur préservée, corrections nécessaires.
3. `fact-check`, éventuellement `evidence-based-reviews` : registre claim → source primaire ou vétérinaire fiable → date → certitude → formulation autorisée.
4. `affiliate-value` si achat : rendre le texte utile sans produit ou commission, expliquer les limites.
5. `content-brief-authoring` : brief spécifique à chaque page, sans structure imposée.
6. `content-and-copy`, `natural-writing`, `general-writing`, `humanizer`, `anti-ai-slop` : écrire en NL et supprimer formulations interchangeables ou artificielles.
7. `internal-linking-audit`, `seo-onpage`, `seo-technical`, `editorial-qa` : maillage, HTML, preuves, cohérence et contrôles techniques.

## Contraintes de production

- Aucun diagnostic ni promesse de traitement. Si un chien présente des réactions alimentaires suspectées ou des troubles persistants, la page doit recommander une consultation vétérinaire plutôt que des substitutions empiriques.
- « Graanvrij » ne signifie pas automatiquement hypoallergénique ; « mono-eiwit » doit se vérifier sur la composition entière ; ne pas confondre labels biologiques, marketing « naturel » et sécurité clinique.
- Éviter les recommandations absolues pour chiots, chiens âgés ou malades ; différencier snack et alimentation complète.
- Conserver structure HTML, liens et médias **lorsqu'ils sont utiles** ; ne pas écraser une page pour faire rentrer un modèle générique. Une refonte du template est une modification distincte.
- Produire un fichier de suivi dans `.content/behoeften/<slug>.md` avec intention, décision, claims/sources, liens visés, modifications, questions non résolues et statut de revue. **Ce fichier ne remplace pas les sources externes**.
- Avant correction finale, comparer la version produite à la page initiale et reprendre les défauts substantiels. Ne pas considérer un simple contrôle syntaxique comme une analyse éditoriale.

## Livraison et publication

1. Proposer les modifications HTML sur branche de travail ou PR ; limiter les chemins édités au scope.
2. Exécuter les contrôles disponibles `npm run check` et, si pertinent, `npm run build` dans un environnement de test ; examiner les diffs après le build, car la génération peut toucher d'autres clusters.
3. Exécuter `behoeften-analysis.md / PUBLISH_REVIEW` après les corrections.
4. Si échec, corriger et refaire la review. Si succès, conserver `noindex,follow` et demander validation humaine explicite avant toute indexation/merge de publication.
