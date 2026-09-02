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
| `eyeon-case-study-infographic@2x.png` | 2400 × 16054 | Qualité maximale |
| `eyeon-case-study-infographic.jpg` | 2400 × 16054 | Behance, Dribbble, LinkedIn |
| `eyeon-case-study-infographic-1x.jpg` | 1200 × 8027 | Web léger |
| `eyeon-case-study-infographic.pdf` | 1 page continue, 12,5 × 83,6 in | Envoi, impression |

Pour régénérer après modification de `infographic.html` :

```bash
python3 tools/inline-assets.py infographic.html infographic.standalone.html
node tools/export-poster.js   # PNG 2x + PDF
```
