# Mon Artisan — étude de cas en infographie

Poster vertical dérivé de la présentation du projet **Mon Artisan** (Asmaa Nejmaoui,
encadrée par M. Ounssy) : plateforme de mise en relation entre particuliers et artisans.

Même structure et mêmes outils que le poster eyeon du dossier parent.

## Fichiers

| Fichier | Rôle |
|---|---|
| `infographic.html` | source éditable (images en liens relatifs vers `assets/`) |
| `infographic.standalone.html` | copie autonome — images et polices embarquées |
| `export/…​.html` | le fichier HTML final à envoyer ou publier |
| `export/…​@2x.png` · `.jpg` · `-1x.jpg` | 2400 × 22510, et versions allégées |
| `export/…​.pdf` | une seule page continue |
| `export/mon-artisan-poster-figma.zip` | paquet prêt pour le plugin html.to.design |
| `figma/` | version import-Figma + assets PNG + tokens + guide |
| `export-poster.js` | régénère PNG et PDF |

## Régénérer après modification

```bash
python3 ../tools/inline-assets.py infographic.html /tmp/ma.html
python3 ../tools/inline-fonts.py  /tmp/ma.html infographic.standalone.html
cp infographic.standalone.html export/mon-artisan-case-study-infographic.html
NODE_PATH=$(npm root -g) node export-poster.js
python3 ../tools/build-figma.py infographic.html figma/mon-artisan-poster-figma.html figma-overrides.css
```

## Sources et honnêteté des chiffres

Tout le contenu vient de la présentation : brief, planning des sept semaines,
benchmark des quatre plateformes, personas Sara El Idrissi et Ahmed Bennani,
empathy maps, parcours, architecture, user flow, sketchs, wireframes et maquettes.

Les chiffres visibles **dans les maquettes** (500+ artisans, 4,8/5, 234 interventions…)
sont du contenu d'exemple de la maquette, pas des résultats mesurés : le poster ne les
présente jamais comme tels. La section « Mesure » est un plan d'indicateurs à remplir.
