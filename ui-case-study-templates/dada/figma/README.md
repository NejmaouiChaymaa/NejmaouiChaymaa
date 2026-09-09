# Importer le poster dans Figma

`dada-poster-figma.html` est une version du poster Mon Artisan préparée pour l'import : elle
donne des calques Figma modifiables, pas une image plate.

## La méthode (5 minutes)

1. Dans Figma, ouvrir **Ressources → Plugins** et installer **html.to.design**
   (éditeur : ‹div›RIOTS). L'import de fichiers est inclus dans l'offre gratuite.
2. Télécharger ce dossier **entier** (`dada-poster-figma.html` + `assets/`) et le
   garder tel quel : le HTML pointe vers les images du sous-dossier.
3. Lancer le plugin, onglet **File**, puis déposer `dada-poster-figma.html`.
   Si le plugin n'accepte qu'un seul fichier, déposer un **.zip** du dossier.
4. Choisir la largeur **1200 px** (Desktop) et lancer l'import.
5. Le poster arrive comme une frame de 1200 × ~10 500 px, avec ses textes,
   ses formes et ses images en calques séparés.

## Ce qui change dans cette version

Figma ne sait pas faire certaines choses du HTML ; elles ont été converties
en amont pour éviter un import cassé :

| HTML d'origine | Version Figma |
|---|---|
| — | ce poster n'utilise aucune 3D : rien à aplatir |
| Images `.webp` | `.png` — Figma n'importe pas le webp |
| `aspect-ratio`, `filter: drop-shadow` | hauteurs fixes, `box-shadow` |
| Décors en `::before` / `::after` (encoche, caméra, pupille) | vrais éléments, donc vrais calques |

Ce poster étant construit à plat, la version Figma est visuellement identique à la
version publiée.

## À vérifier juste après l'import

- **Polices** : installer *Playfair Display*, *Roboto* et *Aref Ruqaa* (gratuites,
  Google Fonts) avant l'import. Ce sont les trois polices de la charte DADA :
  aucune substitution, la typographie du poster est celle du projet.
- **Cercles** : les portraits et les photos de couverture sont des images masquées
  en rond avec une bordure jaune. Après import, vérifier que le masque a suivi ;
  sinon, appliquer un ellipse mask sur l'image.
- **Textes** : les paragraphes arrivent souvent en largeur fixe — passer en
  *Auto width* / *Auto height* si vous comptez réécrire.
- **Graphique** : les barres arrivent en rectangles ; leur largeur porte la donnée
  (90 / 85 / 78 / 72 / 68 %). Si vous les redimensionnez, corrigez la valeur écrite.
- **Zellige** : le filet sous chaque titre est l'image `motif.png` recadrée. Pour le
  rallonger, étirer la largeur sans toucher à la hauteur.

## Après l'import

`TOKENS.md` liste les couleurs, la typographie et les espacements exacts.
Les recréer en Styles (ou Variables) Figma prend 10 minutes et rend le poster
re-stylable en un clic pour le projet suivant.

## Remplacer les captures d'écran

Les fichiers de `assets/` sont extraits de la présentation du projet. Pour un autre projet :
garder les mêmes noms, ou sélectionner l'image dans Figma et remplacer le
remplissage (le cadre, l'ombre et l'encoche restent).

> Les captures viennent de la présentation PDF du projet. Si vous avez le fichier
> Figma d'origine, ré-exportez les écrans en 2× et remplacez les fichiers de
> `assets/` : le rendu sera plus net, surtout sur la page d'accueil complète.
