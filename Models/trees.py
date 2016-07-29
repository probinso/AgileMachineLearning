from __future__ import print_function, division

import numpy as np
from sklearn.tree.tree import DecisionTreeClassifier

def wrapper_for_decision_tree_in_sklearn(X, y, current_state_to_predict):
    dtc = DecisionTreeClassifier()
    dtc.fit(X, y)
    predicted_state = dtc.predict(current_state_to_predict.reshape(1, -1))
    return predicted_state

def wrapper_for_decision_tree_accuracy(train, test):
    dtc = DecisionTreeClassifier()
    dtc.fit(train, test)
    
