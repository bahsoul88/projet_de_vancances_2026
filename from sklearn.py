from sklearn.model_selection import KFold
from sklearn.model_selection import RepeatedKFold
import numpy as np

X = np.array([[1,2], [3,4], [1,2], [3,4]])
y = np.array([0,0,1,1])

folds = KFold(n_splits = 2, shuffle = True, random_state = 42)

for i , (train_index, test_index) in enumerate (folds.split(X,y)) :
    print("Pli", i)
    print("Index d'entrainement", train_index)
    print("Index de test",test_index)

    X_train = X[train_index]
    y_train = y[train_index]
    X_test = X[test_index]
    y_test = y[test_index]

folds = RepeatedKFold(n_splits = 2, n_repeats= 1, random_state = 42)

for i , (train_index, test_index) in enumerate (folds.split(X,y)) :
    print("Pli", i)
    print("Index d'entrainement", train_index)
    print("Index de test",test_index)