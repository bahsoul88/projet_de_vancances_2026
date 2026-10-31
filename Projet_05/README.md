# Projet 05 : Encadrer et nommer les poissons d'un aquarium (Deep Learning & Vision)

Détection d'objets : localiser chaque poisson sur une photo et identifier son espèce,
avec un Faster R-CNN fine-tuné.

## Objectif
Pouvoir photographier un aquarium et obtenir, pour chaque poisson,
une boîte englobante et le nom de son espèce (13 espèces).

## Données
Dataset Kaggle [fish-dataset](https://www.kaggle.com/datasets/mahmoodyousaf/fish-dataset) :
plus de 8 200 photos, format YOLO. Non inclus dans ce dépôt :
il se télécharge automatiquement avec `kagglehub` en exécutant le notebook.

## Méthode
- Test d'un détecteur pré-entraîné sur COCO : il prend les poissons pour des oiseaux
  (COCO ne contient aucune catégorie poisson), mais localise correctement la zone
- Dataset PyTorch personnalisé : boîtes `BoundingBoxes`, labels décalés de +1
  (la classe 0 est réservée au fond)
- Modèle : `fasterrcnn_mobilenet_v3_large_320_fpn` (léger, utilisable sur CPU)
- **Fine-tuning** : backbone gelé, nouvelle tête de classification (14 sorties :
  13 espèces + fond)
- Entraînement sur 1 000 photos, 3 epochs, SGD (lr 0,005), suivi des 4 losses
  du détecteur

## Résultats
Loss totale : 1.277 -> 0.762 en 3 epochs.
Le détecteur fine-tuné encadre et nomme correctement les poissons de test
(ClownFish, GoldFish...).

## Limites
Pas de data augmentation, dataset déséquilibré (un Gourami a presque 10 fois plus
de photos qu'un YellowCichlid), entraînement sur un sous-ensemble,
aucune espèce ne peut être signalée comme « inconnue ».

## Technologies
Python, PyTorch, torchvision, torchmetrics, kagglehub, Jupyter

## Fichiers
- `projet_05.ipynb` : notebook complet
- `utils.py` : lecture des annotations et affichages

## Pour aller plus loin
Entraîner sur les 6 800 photos complètes (Google Colab + GPU), comparer à
`fasterrcnn_resnet50_fpn` ou à YOLO (ultralytics), ajouter de la data augmentation.

## Crédit
Projet issu du Cahier de Vacances 2026 de [Machine Learnia](https://www.youtube.com/@MachineLearnia).
Exercices complétés par moi-même.