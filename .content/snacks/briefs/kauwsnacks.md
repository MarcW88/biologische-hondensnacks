# Content brief — Kauwsnacks

## Cadrage
- URL : `/soorten/kauwsnacks/`
- Langue / marché : néerlandais, Pays-Bas
- Décision d’audit : `DEEP_REWRITE`
- Robots : conserver `noindex,follow`
- Intention dominante : choisir une kauwsnack concrète selon formaat, hardheid, kauwgedrag et sécurité.
- Job : trouver une option à mâcher adaptée sans présumer que plus dur ou plus long est automatiquement meilleur.

## Scope candidats

1. Yarrah Organic Chewsticks for Dogs — 33 g
2. Bandit Bio lamspezen — 100 g
3. Beeztees runderkophuid — 80 cm
4. BF Dental Rol — tailles M/L/XL, 15/23/30 cm

## Rôle des candidats
- Yarrah : option biologique plus courte et portionnable.
- Bandit lamspezen : option biologique clairement orientée mastication.
- Beeztees runderkophuid : exemple de très grand format en runderhuid, non présenté comme biologique.
- BF Dental Rol : exemple avec tailles explicites pour montrer l’importance du format.

## Critères
1. lengte / formaat ;
2. hardheid / materiaal ;
3. kauwgedrag attendu ;
4. taille du morceau vs risque d’avaler ;
5. état du gebit ;
6. composition / protéine ;
7. énergie si disponible ;
8. statut biologique séparé ;
9. claim dentaire séparée.

## Preuves
- Yarrah Chewsticks : 33 g, 3 sticks, 40% biologisch rund + 46% biologische kip, 440 kcal/100 g, peut être donné entier ou cassé.
- Bandit Bio lamspezen : biologique, séché, 100 g.
- Beeztees runderkophuid : 80 cm, 100% gedroogde runderhuid, grand format ; retailer recommande d’adapter au gabarit/kauwgedrag.
- BF Dental Rol : runderhuid, tailles 15/23/30 cm ; analyse 85-90% protéine, 1-2% graisse ; retailer rappelle que le kauwgedrag varie par chien.
- VOHC : seules certaines références disposent d’un Seal spécifique pour plaque/tartre, preuve que mastication et efficacité dentaire ne sont pas synonymes.

## Logique de recommandation
- Yarrah : meilleur choix de cette sélection pour un petit chew biologique / reward plus court.
- Bandit lamspezen : meilleur choix biologique de la sélection pour un kauwmoment plus long.
- BF Dental Rol : meilleur exemple si le critère principal est de pouvoir choisir un format explicite.
- Beeztees 80 cm : option à réserver aux chiens pour lesquels un très grand format est réellement pertinent ; ne pas présenter comme universellement meilleur.

## Architecture
1. answer-first sécurité ;
2. tableau formaat/hardheid/usage ;
3. sélection produit ;
4. stopregels ;
5. distinction kauwsnack/tandsnack ;
6. lien vers guide détaillé ;
7. sources.

## Anti-patterns
- pas de `harder = beter` ;
- pas de claim dentaire sans preuve ;
- pas de `natuurlijk = biologisch` ;
- pas de recommandation absolue par poids ;
- pas de faux hands-on ;
- pas de promesse de durée précise.
