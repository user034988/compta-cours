# Comptabilité · saisie et amortissements

Site pour les cours de comptabilité :

- **Bordereaux de saisie** : saisie des écritures au clavier (Tab), équilibre débit/crédit automatique, plan comptable avec création rapide de comptes, calculs dans les montants, colonne Note, exports Excel, PDF et copier-coller vers un tableur.
- **Exports Excel** : mise en page identique au PDF, formules conservées, feuille « PCG » avec tout le plan comptable. Dans le fichier, l'intitulé du compte est une formule : corriger un numéro de compte met l'intitulé à jour.
- **Tableaux d'amortissement** : plan économique linéaire, plan fiscal dégressif ou linéaire, amortissement dérogatoire, étalement d'une subvention d'investissement, commentaires par cellule et export Excel avec formules et commentaires.

Adresse du site : https://user034988.github.io/compta-cours/

## Fonctionnement

- `src/app.html` : la page elle-même. C'est aussi la version publiée comme artifact sur claude.ai.
- `tools/build.py` : produit `index.html`, la page complète servie par GitHub Pages. Il y ajoute la connexion au projet Firebase `compta-cours`.
- Données : Firebase (Authentication par e-mail et mot de passe, base Firestore). Chaque document est rangé sous `users/{uid}/documents/{id}`.
- `firestore.rules` : règles de sécurité à coller dans la console Firebase (Firestore Database → Règles). Chaque compte ne lit et n'écrit que ses propres documents.
- Sauvegarde : le menu « ⋯ » permet d'exporter tous ses documents dans un fichier `.json` et de les restaurer, ici ou sur une autre version du site.

Après une modification de `src/app.html` :

```bash
python3 tools/build.py
```

## Sources

- Plan comptable général 2026 de l'Autorité des normes comptables, d'après le jeu de données [arrhes/PCG](https://github.com/arrhes/PCG) (licence CC0). Quelques subdivisions usuelles en cours (530, 580, 6097…) sont ajoutées et signalées comme telles.
- Bibliothèques chargées depuis cdnjs : ExcelJS (export Excel), jsPDF et jsPDF-AutoTable (export PDF), Firebase (SDK compat) depuis jsDelivr.

## Réglages Firebase à faire une fois

Dans la console Firebase du projet `compta-cours` :

- **Authentication → Méthodes de connexion** : activer « Adresse e-mail/Mot de passe ».
- **Authentication → Paramètres → Domaines autorisés** : ajouter `user034988.github.io`.
- **Firestore Database → Règles** : coller le contenu de `firestore.rules`, puis Publier.
