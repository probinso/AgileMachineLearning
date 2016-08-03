from __future__ import division

def wrapper_for_backprop_neural_network_code(train_x, train_y, test_x, test_y):
    from sklearn.neural_network import MLPClassifier
    clf = MLPClassifier(algorithm="l-bfgs", alpha=1e-5, hidden_layer_sizes=(5,2),
            random_state=6543)
    clf.fit(train_x, train_y)
    target = clf.predict(test_x)
    underscore = map(lambda (x,y): x == y, zip(target, test_y))
    score = sum(underscore) / len(underscore)

    return score
