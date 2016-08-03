from unittest import TestCase
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from Models.trees import wrapper_for_decision_tree_in_sklearn
from Models.trees import wrapper_for_decision_tree_accuracy
from tests.data import DIGITS_DATASET



class TestDecisionTrees(TestCase):
    def test_digits_solutions_with_pre_built_model(self):

        data = DIGITS_DATASET['data']
        labels = DIGITS_DATASET['target']

        arbitrary_sample_the_default_tree_will_get_right = 3

        state_predicted_from_model = wrapper_for_decision_tree_in_sklearn(
            data, labels, np.array(data[arbitrary_sample_the_default_tree_will_get_right]).reshape(1,-1))

        self.assertEqual(
            labels[arbitrary_sample_the_default_tree_will_get_right],
            state_predicted_from_model,
            "Solve me first by writing `wrapper_for_decision_tree_in_sklearn`.")


    def test_minimum_accuracy_of_tree_model(self):
        accuracy_target = 0.8  # percent
        relative_test_set_size = 0.4  # percent
        data = DIGITS_DATASET['data']
        labels = DIGITS_DATASET['target']

        score = wrapper_for_decision_tree_accuracy(
            data, labels, relative_test_set_size)

        self.assertGreaterEqual(score, accuracy_target,
                                "Write me second - after you get the above test working!")
