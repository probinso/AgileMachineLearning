from __future__ import print_function, division
from collections import namedtuple
from collections import defaultdict
import pandas as pd

from scipy.stats import norm
from math import sqrt, exp, pi

def wrapper_for_nb_in_sklearn(data, current_state_to_predict, normal_columns={}):
    """
        Import an already-built implementation, train it on the data,
    and return the class predicted given the current state.

        Note that the last column of data is assumed to be the variable
    to predict, and the order
    """

    store = defaultdict(lambda : defaultdict(dict))
    Label = data.columns[-1]
    maxstore = []


    for choice in data[Label].unique():
        for col in data.columns[:-1]:
            for type in data[col].unique(): 
                if type in normal_columns:
                    continue
                subgraph = data[data[Label]==choice]
                pop   = len(subgraph)
                count = len(subgraph[subgraph[col]==type])

                store[choice][col][type] = count/pop

        store[choice].update({col : norm.fit(data[col]) for col in normal_columns})


    for choice in store:
        prob = len(data[data[Label]==choice])/len(data)
        for index, col in enumerate(data.columns[:-1]):
            state = current_state_to_predict[index]
            if col in normal_columns:
                mu, si = store[choice][col][state]
                P = lambda x : 1/sqrt(2 * pi * si ** 2) * exp(-1/2 * ((x - mu)/si)**2)
                state_probability = P(state)
            else:
                state_probability = store[choice][col][state]

            prob *= state_probability

        maxstore.append((prob, choice))

    return max(maxstore)
