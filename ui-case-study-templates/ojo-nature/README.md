# OJO Nature — étude de cas en infographie

Poster vertical dérivé de la présentation **OJO Nature** (Asmaa Nejmaoui, encadrée
par M. Ounssy, ISAG OFPPT 2025) : plateforme de photographie de nature.

## Une direction volontairement différente

Les deux autres posters du dépôt sont construits autour d'appareils en perspective
et de cartes. Celui-ci suit une direction éditoriale et photographique, adaptée au
sujet :

- **Couverture pleine image** avec le titre en serif, plutôt qu'un collage d'écrans
- **Instrument Serif + Karla** au lieu de Poppins ou Archivo Black
- **Colonne de repère à gauche** (numéro, libellé, filet) répétée à chaque section
- **Aucun arrondi, aucune ombre** : filets 1 px, aplats, bandes pleine largeur
- **Écrans sans cadre d'appareil**, présentés comme des tirages
- **Plus court** : 7 sections, ~6 400 px de haut contre ~11 000 pour les autres

## Fichiers

| Fichier | Rôle |
|---|---|
| `infographic.html` | source éditable |
| `infographic.standalone.html` | copie autonome — images et polices embarquées |
| `export/…​.html` · `@2x.png` · `.jpg` · `-1x.jpg` · `.pdf` | livrables |
| `export/ojo-nature-poster-figma.zip` | paquet prêt pour html.to.design |
| `figma/` | version import-Figma, assets PNG, tokens, guide |

Régénérer : mêmes commandes que `../mon-artisan/README.md`, avec
`figma-overrides.css` de ce dossier.

## Sources et chiffres

Les quatre pourcentages du graphique (78 % inspiration visuelle, 70 % mobile,
65 % progression technique, 54 % interaction communautaire) sont **les résultats du
questionnaire mené dans le projet** — ce sont les seuls chiffres du poster, et ils
sont présentés comme des réponses au questionnaire, pas comme des résultats produit.
La section « La suite » liste ce qui reste à mesurer après les tests utilisateurs.
