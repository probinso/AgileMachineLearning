import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder


def wrapper_for_nb_in_sklearn(data, current_state_to_predict):
    """
        Import an already-built implementation, train it on the data,
    and return the class predicted given the current state.

        Note that the last column of data is assumed to be the variable
    to predict, and the order
    """

    # Convert inputs to arrays to leverage numpy's reshaping and indexing
    data = np.array(data)
    state_to_predict = np.array(current_state_to_predict).reshape((1, -1))

    # Convert strs to ints for all Inputs:
    le = LabelEncoder()
    all_states = data.flatten()
    le.fit(all_states)

    intified_data = le.transform(data)
    intified_state_to_predict = le.transform(state_to_predict)

    # Pick out X and y from data:
    X = intified_data[:, :-1]
    y = data[:, -1]

    # Create and train model:
    clf = MultinomialNB(alpha=1., fit_prior=True,)
    clf.fit(X, y)

    # Predict for sample, and convert back to string:
    predicted_state_as_str = clf.predict(intified_state_to_predict)[0]

    return predicted_state_as_str
