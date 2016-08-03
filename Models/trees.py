import numpy as np
from sklearn.tree.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split


def wrapper_for_decision_tree_in_sklearn(X, y, current_state_to_predict):
	clf = DecisionTreeClassifier()
	clf.fit(X, y)
	current_state_to_predict = np.array(current_state_to_predict).reshape(1,-1)
	predicted_state = clf.predict(current_state_to_predict)
	return predicted_state


def wrapper_for_decision_tree_accuracy(X, y, relative_test_size):
	X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=relative_test_size, random_state=42)


	clf = DecisionTreeClassifier()
	clf.fit(X_train, y_train)
	pred = clf.predict(X_test)
	score = accuracy_score(pred,y_test)

	return score
