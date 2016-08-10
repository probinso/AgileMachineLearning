from __future__ import division
from sknn.mlp import Convolution, Classifier, Layer
import numpy as np
from sklearn.metrics import accuracy_score

def wrapper_for_backprop_neural_network_code(train_x, train_y, test_x, test_y):

    neural_net = Classifier(
        layers=[
            Convolution(
                'Sigmoid',
                kernel_shape=(3,3),
                channels=1,
            ),
            Layer('Softmax')
            ],
        learning_rate = 0.001,
        n_iter = 25,
        learning_rule='sgd',
        dropout_rate=0.1,
    )
    neural_net.fit(train_x, train_y)
    target = neural_net.predict(test_x)
    return accuracy_score(target, test_y)
