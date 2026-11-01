# Projet 06 : Combien de glaces préparer demain ? (Séries temporelles)

Prévision des ventes quotidiennes d'un marchand de glaces avec des modèles
MA et ARMA (statsmodels).

## Objectif
Aider un vendeur à décider chaque matin combien de bacs sortir du congélateur,
en prévoyant le nombre de glaces vendues le lendemain, puis la semaine suivante.

## Données
`data/ventes_glaces.csv` : ventes quotidiennes du 1er juin au 30 septembre,
étés 2022 à 2025 (488 jours). Une seule colonne de ventes : pas de météo.

## Méthode
- Découpage temporel : les 22 derniers jours en test, jamais de mélange aléatoire
- Baselines : « toujours la moyenne » et « comme hier »
- **Autocorrélation** codée à la main, validée contre `statsmodels`,
  lecture de l'ACF et de la PACF
- **MA(q)** : simulation d'une série MA à la main, puis MA(3) ajusté
  sur la saison 2025 (122 jours)
- Avec 488 jours, la mémoire décroît lentement : passage à l'**ARMA(1,1)**
- Comparaison par **AIC** et par le test de **Ljung-Box** sur les résidus
- Prévision du lendemain (réévaluée chaque jour) et à 7 jours

## Résultats

| Modèle | Erreur moyenne (MAE) |
|---|---|
| **ARMA(1,1), 4 étés** | **14,80 glaces/jour** |
| MA(3), 4 étés | 16,27 |
| MA(3), saison 2025 seule | 16,48 |
| Comme hier | 19,00 |
| Toujours la moyenne | 30,38 |

- L'ARMA(1,1) divise par deux l'erreur de la moyenne et améliore de 22 % le réflexe
  « comme hier », avec seulement 2 coefficients (φ = 0,675 ; θ = 0,632).
- **AIC** : 3920,1 pour l'ARMA(1,1) contre 3945,3 pour le MA(3) (plus bas = mieux).
- **Ljung-Box** : p = 0,590 pour l'ARMA (résidus = bruit pur),
  p ≈ 0 pour le MA(3) (il reste de la structure non captée).
- **Prévision à 7 jours** : le MA(3) devient plat dès J+4 à 198,3 (la moyenne,
  sa mémoire est de 3 jours), l'ARMA(1,1) revient progressivement vers cette
  moyenne (192,7 à J+1, 197,8 à J+7). Prévoir le lendemain fonctionne ;
  à une semaine, mieux vaut se fier à la moyenne.

## Limites
Pas de saisonnalité hebdomadaire, pas de météo, un seul vendeur,
22 jours de test seulement.

## Technologies
Python, pandas, numpy, statsmodels, Jupyter

## Fichiers
- `Projet_06.ipynb` : notebook complet
- `utils.py` : fonctions d'affichage et métriques
- `data/ventes_glaces.csv` : données

## Pour aller plus loin
SARIMA (saisonnalité hebdomadaire), SARIMAX avec la température,
comparaison avec un modèle de Machine Learning à variables de retard.

## Crédit
Projet issu du Cahier de Vacances 2026 de [Machine Learnia](https://www.youtube.com/@MachineLearnia).
Exercices complétés par moi-même.