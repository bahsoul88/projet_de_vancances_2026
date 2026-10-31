# Projet 02 : Qui gagnera la Coupe du Monde 2026 ?

Prédiction du vainqueur d'un match de football avec du Machine Learning,
puis simulation d'une Coupe du Monde complète (bonus).

## Objectif
Entraîner un modèle capable de prédire le vainqueur d'un match à partir
de la forme récente des deux équipes.

## Données
Résultats de matchs internationaux de 1994 à 2026 (environ 30 000 matchs),
source : [martj42/international_results](https://github.com/martj42/international_results) (licence CC0).

## Méthode
- Exploration des données (avantage du terrain, meilleures équipes, buts par match)
- Création de features : écart de forme sur les 10 derniers matchs
- Encodage, standardisation, découpage train/test (80 % / 20 %)
- Modèle : Random Forest (200 arbres) avec scikit-learn

## Résultat
Accuracy : XX % (baseline « victoire à domicile » : ~63 %)

## Technologies
Python, pandas, matplotlib, scikit-learn, Jupyter

## Fichiers
- `projet_02.ipynb` : notebook complet
- `utils.py` : fonctions utilitaires
- `data/results.csv` : données

## Crédit
Projet issu du Cahier de Vacances 2026 de [Machine Learnia](https://www.youtube.com/@MachineLearnia).
Exercices complétés par moi-même.