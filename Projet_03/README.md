# Projet 03 : Dessiner le Tour de France 2027

Clustering et optimisation de parcours : regrouper 120 villages en 21 étapes,
puis trouver l'ordre de passage le plus court dans chaque étape.

## Objectif
- **Mission 1** : découper 120 villages de France en 21 étapes de villages proches.
- **Mission 2** : pour chaque étape, trouver le parcours le plus court
  (problème du voyageur de commerce, en chemin ouvert).

## Données
`villages_2027.csv` : 120 villages avec département, latitude et longitude.

## Méthode
- Conversion des coordonnées GPS (degrés) en kilomètres
- Clustering non supervisé : comparaison **K-Means** et **CAH (Ward)**
  avec le score de silhouette et la taille des étapes
- Choix du K-Means : silhouettes quasi égales, mais la CAH crée une étape
  d'un seul village
- Distance à vol d'oiseau avec la **formule de haversine**
- Parcours de chaque étape : algorithme **glouton** (plus proche voisin),
  amélioré par le **2-opt**, en testant tous les villages de départ

## Résultat
Distance totale d'environ XXXX km sur 21 étapes, contre environ 46 800 km
pour un parcours dans l'ordre alphabétique du fichier.
Plusieurs étapes dépassent 200 km : le découpage et la liste de villages
sont à revoir (zones très denses d'un côté, très vides de l'autre).

## Technologies
Python, pandas, matplotlib, scikit-learn, Jupyter

## Fichiers
- `projet_03.ipynb` : notebook complet
- `utils.py` : fonctions d'affichage des cartes
- `villages_2027.csv` : données

## Pour aller plus loin
Ajouter Paris en étape finale, limiter les étapes à 200 km maximum,
utiliser de vrais temps de trajet routiers (OR-Tools).

## Crédit
Projet issu du Cahier de Vacances 2026 de [Machine Learnia](https://www.youtube.com/@MachineLearnia).
Exercices complétés par moi-même.