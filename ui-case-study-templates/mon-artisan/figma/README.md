# Importer le poster dans Figma

`mon-artisan-poster-figma.html` est une version du poster Mon Artisan préparée pour l'import : elle
donne des calques Figma modifiables, pas une image plate.

## La méthode (5 minutes)

1. Dans Figma, ouvrir **Ressources → Plugins** et installer **html.to.design**
   (éditeur : ‹div›RIOTS). L'import de fichiers est inclus dans l'offre gratuite.
2. Télécharger ce dossier **entier** (`mon-artisan-poster-figma.html` + `assets/`) et le
   garder tel quel : le HTML pointe vers les images du sous-dossier.
3. Lancer le plugin, onglet **File**, puis déposer `mon-artisan-poster-figma.html`.
   Si le plugin n'accepte qu'un seul fichier, déposer un **.zip** du dossier.
4. Choisir la largeur **1200 px** (Desktop) et lancer l'import.
5. Le poster arrive comme une frame de 1200 × ~10 500 px, avec ses textes,
   ses formes et ses images en calques séparés.

## Ce qui change dans cette version

Figma ne sait pas faire certaines choses du HTML ; elles ont été converties
en amont pour éviter un import cassé :

| HTML d'origine | Version Figma |
|---|---|
| Perspective 3D du hero (`rotateY` / `rotateX`) | rotation 2D simple — Figma ne gère pas la 3D |
| Images `.webp` | `.png` — Figma n'importe pas le webp |
| `aspect-ratio`, `filter: drop-shadow` | hauteurs fixes, `box-shadow` |
| Décors en `::before` / `::after` (encoche, caméra, pupille) | vrais éléments, donc vrais calques |

Le hero est donc légèrement différent de la version publiée : les appareils sont
posés à plat au lieu d'être en perspective. C'est le prix d'un hero modifiable.

## À vérifier juste après l'import

- **Polices** : installer *Archivo* et *Archivo Black* (gratuites, Google Fonts) avant
  l'import, sinon Figma substitue et les blocs de texte se décalent. La police d'origine
  du projet, *Intro Rust*, est commerciale : si vous la possédez, remplacez le style
  display après l'import.
- **Groupes d'appareils** : regrouper chaque téléphone avec son écran, et le
  portable avec le sien, avant de les déplacer.
- **Textes** : les paragraphes arrivent souvent en largeur fixe — passer en
  *Auto width* / *Auto height* si vous comptez réécrire.
- **Hero de secours** : si la composition du hero arrive abîmée, supprimez-la et
  posez `hero-band@2x.png` à la place, puis retravaillez par-dessus.

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
