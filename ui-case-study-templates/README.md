# eyeon — modèles d'étude de cas UI

Onze modèles réutilisables pour présenter un projet UI/UX, remplis avec le projet
**eyeon** (Design Thinking) comme exemple de rédaction.

## Fichiers

| Fichier | Usage |
|---|---|
| `eyeon-case-study.html` | Le modèle à éditer. Charge les images depuis `assets/`. |
| `eyeon-case-study.standalone.html` | Copie autonome (images en base64) — à publier, envoyer ou imprimer telle quelle. |
| `assets/` | Captures d'écran et identité extraites de la présentation du projet. |
| `tools/inline-assets.py` | Régénère la copie autonome après une modification. |

## Utiliser

Ouvrez `eyeon-case-study.html` dans un navigateur. Trois boutons en haut de page :

- **Modèle vierge** — vide tous les textes et affiche les consignes de rédaction à leur place.
  C'est le point de départ pour un autre projet.
- **Guide de rédaction** — affiche ou masque les encadrés jaunes.
- **Imprimer / PDF** — impression propre (barre d'outils et encadrés masqués).

Pour l'adapter à un autre projet : remplacez les textes dans le HTML, déposez vos
captures dans `assets/`, puis régénérez la version autonome :

```bash
python3 tools/inline-assets.py eyeon-case-study.html eyeon-case-study.standalone.html
```

## Les onze modèles

1. Couverture · 2. Résumé en quatre blocs · 3. Cadrage & hors périmètre ·
4. Recherche & irritants · 5. Problème → besoin → opportunité (persona, point de vue, CPN) ·
6. Solutions retenues · 7. Galerie d'écrans (écran → job à faire → décision) ·
8. Fondations UI · 9. Plan de mesure · 10. Apprentissages · 11. Une page

## Note sur les chiffres

Le tableau du plan de mesure est volontairement vide : le projet n'a pas encore de
résultats mesurés. Les colonnes « base de départ » et « cible » sont à remplir avec
des données réelles — aucun chiffre n'a été inventé.

---

Projet eyeon — encadrement : Formateur Ghazi. Équipe : Abdellah, Hamza, Aya, Asmaa, Yassine.

## Format infographie (poster)

`infographic.html` est la même étude de cas en **une seule image verticale**, dans le
format des case studies Behance/Dribbble : hero, rôle, timeline, personas,
problème/solution, identité visuelle, écrans, décisions, plan de mesure.

Exports dans `export/` :

| Fichier | Dimensions | Usage |
|---|---|---|
| `eyeon-case-study-infographic.html` | — | **Fichier HTML final**, autonome |
| `eyeon-case-study-infographic@2x.png` | 2400 × 20948 | Qualité maximale |
| `eyeon-case-study-infographic.jpg` | 2400 × 20948 | Behance, Dribbble, LinkedIn |
| `eyeon-case-study-infographic-1x.jpg` | 1200 × 10474 | Web léger |
| `eyeon-case-study-infographic.pdf` | 1 page continue, 12,5 × 87 in | Envoi, impression |

`export/eyeon-case-study-infographic.html` est le **fichier HTML final** : un seul
fichier, images et police embarquées, aucune dépendance réseau. Il s'ouvre par
double-clic dans n'importe quel navigateur, y compris hors ligne.

Pour régénérer après modification de `infographic.html` :

```bash
python3 tools/inline-assets.py infographic.html /tmp/step1.html
python3 tools/inline-fonts.py  /tmp/step1.html  infographic.standalone.html
cp infographic.standalone.html export/eyeon-case-study-infographic.html
NODE_PATH=$(npm root -g) node tools/export-poster.js   # PNG 2x + PDF
```

L'ordre compte : `inline-fonts.py` embarque la police Poppins en base64. Sans
cette étape, le poster s'affiche en Arial partout où Google Fonts est
inaccessible — et les exports PNG/PDF sont générés depuis ce fichier, donc ils
hériteraient de la mauvaise police.

## Éditer le poster dans Figma

Le dossier `figma/` contient une version préparée pour l'import Figma via le
plugin **html.to.design** (onglet *File*, offre gratuite) :

| Fichier | Rôle |
|---|---|
| `figma/eyeon-poster-figma.html` | poster en calques modifiables — 3D aplatie en 2D, images PNG |
| `figma/assets/*.png` | toutes les captures et déclinaisons de logo (Figma n'importe pas le webp) |
| `figma/hero-band@2x.png` | le hero en image, si l'import de la composition échoue |
| `figma/TOKENS.md` | couleurs, typographie, espacements à recréer en Styles Figma |
| `figma/README.md` | la marche à suivre, et ce qu'il faut vérifier après l'import |
| `export/eyeon-poster-figma.zip` | le tout, prêt à déposer dans le plugin |

Régénérer après modification de `infographic.html` :

```bash
python3 tools/build-figma.py infographic.html figma/eyeon-poster-figma.html
```

## Modèle packaging

`packaging/` contient un modèle d'étude de cas pour un projet de **packaging**
(ni app, ni site) : brief et contraintes industrielles, rayon et concurrence,
positionnement, **structure et plan à plat**, hiérarchie de face avant, système
graphique en Pantone/CMJN, **mentions obligatoires**, déclinaisons de gamme,
**fabrication et impression**, éco-conception, rendus et mesure.

Deux schémas SVG modifiables sont fournis : un plan à plat d'étui à rabats
(coupe, pliage, zone de sécurité) et un gabarit de hiérarchie de face avant.
