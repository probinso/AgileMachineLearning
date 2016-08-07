from __future__ import division
import numpy as np


def wrapper_for_backprop_neural_network_code(train_x, train_y, test_x, test_y):
    from sklearn.neural_network import MLPClassifier
    clf = MLPClassifier(
        algorithm="sgd", # stochastic gradient descent
        hidden_layer_sizes=(100,100),
        learning_rate='adaptive',
        random_state=6543,
        #verbose=True,
    )
    clf.fit(train_x, train_y)

    target = clf.predict(test_x)
    score = (target == test_y)
    _ = np.sum(score) / len(score) # compute hamming distance
    print(_)
    return _
