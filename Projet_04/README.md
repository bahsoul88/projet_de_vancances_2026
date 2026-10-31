# Projet 04 : Un assistant virtuel pour l'Hôtel Le Belvédère (RAG & LLM)

Construction d'un assistant qui répond aux questions des clients d'un hôtel
à partir de sa documentation PDF, sans inventer de réponses.

## Objectif
Un LLM générique ne connaît pas l'hôtel et invente (hallucinations).
Le but : le faire répondre uniquement à partir de la vraie documentation,
et lui faire dire « je ne sais pas » quand l'information n'y figure pas.

## Démarche en trois actes
1. **LLM seul** : il invente (hôtel à Paris, 5 étoiles...) : réponses inutilisables.
2. **Toute la documentation dans le prompt** : meilleur, mais lent
   (~1 400 mots relus à chaque question), et le modèle se perd parfois.
3. **RAG** : seules les rubriques pertinentes sont envoyées au modèle.
   Réponses plus justes, environ 5 fois plus rapides, sources citées.

## Méthode
- Extraction du texte de 5 PDF avec `pypdf`, nettoyage (titres, pieds de page)
  et mise en forme Markdown (15 rubriques)
- Modèle de génération : `Qwen/Qwen2.5-0.5B-Instruct` (Hugging Face)
- Embeddings multilingues : `paraphrase-multilingual-MiniLM-L12-v2`
  (vecteurs de dimension 384)
- Recherche par similarité cosinus (produit scalaire de vecteurs normalisés)
  des `top_k` rubriques les plus proches de la question
- Visualisation des rubriques en 2D avec **t-SNE**
- Prompt avec rôle, contexte, question et consigne anti-invention

## Résultats
- Le check-in (15h), le wifi gratuit et le tarif des chambres sont enfin
  retrouvés correctement
- La question piège (paiement en Bitcoin) reçoit bien « je ne sais pas »
- Contexte envoyé au LLM : ~1 400 mots en partie 2, ~200 mots avec le RAG

## Limites
Petit modèle de 500 millions de paramètres (parfois maladroit), 15 rubriques
seulement, pas d'évaluation systématique (recall@k).

## Technologies
Python, transformers, sentence-transformers, pypdf, pandas, numpy,
scikit-learn, matplotlib, Jupyter

## Fichiers
- `projet_04.ipynb` : notebook complet
- `utils.py` : fonction d'affichage des conversations
- `data/` : les 5 PDF de documentation de l'hôtel

## Pour aller plus loin
Base vectorielle (FAISS, Chroma), modèle de génération plus grand,
chunking de documents longs, jeu de questions d'évaluation.

## Crédit
Projet issu du Cahier de Vacances 2026 de [Machine Learnia](https://www.youtube.com/@MachineLearnia).
Exercices complétés par moi-même.