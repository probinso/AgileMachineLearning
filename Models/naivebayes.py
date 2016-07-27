from __future__ import print_function, division
from collections import namedtuple
from collections import defaultdict
import pandas as pd



def wrapper_for_nb_in_sklearn(data, current_state_to_predict):
    """
        Import an already-built implementation, train it on the data,
    and return the class predicted given the current state.

        Note that the last column of data is assumed to be the variable
    to predict, and the order
    """

    store = defaultdict(lambda : defaultdict(dict))
    Label = data.columns[-1]
    pop = len(data)
    for choice in data[Label].unique():
        for col in data.columns[:-1]:
            for type in data[col].unique():
                _ = data[data[col]==type][data[Label]==choice]
                count = len(_)
                store[choice][col][type] = count/pop

    

    return store
