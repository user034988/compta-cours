# Comptabilité · saisie et amortissements

Site pour les cours de comptabilité :

- **Bordereaux de saisie** : saisie des écritures au clavier (Tab), équilibre débit/crédit automatique, plan comptable avec création rapide de comptes, calculs dans les montants, colonne Note, exports Excel, PDF et copier-coller vers un tableur.
- **Exports Excel** : mise en page identique au PDF, formules conservées, feuille « PCG » avec tout le plan comptable. Dans le fichier, l'intitulé du compte est une formule : corriger un numéro de compte met l'intitulé à jour.
- **Tableaux d'amortissement** : plan économique linéaire, plan fiscal dégressif ou linéaire, amortissement dérogatoire, étalement d'une subvention d'investissement, commentaires par cellule et export Excel avec formules et commentaires.

Adresse du site : https://user034988.github.io/compta-cours/

## Fonctionnement

- `src/app.html` : la page elle-même. C'est aussi la version publiée comme artifact sur claude.ai.
- `tools/build.py` : produit `index.html`, la page complète servie par GitHub Pages. Il y ajoute la connexion au projet Supabase `compta-cours`.
- Données : table `documents` du projet Supabase `compta-cours`. Des règles de sécurité au niveau des lignes (RLS) limitent chaque compte à ses propres documents.

Après une modification de `src/app.html` :

```bash
python3 tools/build.py
```

## Sources

- Plan comptable général 2026 de l'Autorité des normes comptables, d'après le jeu de données [arrhes/PCG](https://github.com/arrhes/PCG) (licence CC0). Quelques subdivisions usuelles en cours (530, 580, 6097…) sont ajoutées et signalées comme telles.
- Bibliothèques chargées depuis cdnjs : ExcelJS (export Excel), jsPDF et jsPDF-AutoTable (export PDF), supabase-js depuis jsDelivr.

## Réglage Supabase à faire une fois

Dans le tableau de bord Supabase du projet `compta-cours`, ouvrez **Authentication → URL Configuration** :

- **Site URL** : `https://user034988.github.io/compta-cours/`
- **Redirect URLs** : ajoutez `https://user034988.github.io/compta-cours/`

Sans ce réglage, les liens de confirmation et de réinitialisation du mot de passe envoyés par e-mail pointent vers `localhost`.
