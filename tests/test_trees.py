from unittest import TestCase

from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split

from Models.trees import wrapper_for_decision_tree_in_sklearn
from Models.trees import wrapper_for_decision_tree_accuracy
from tests.data   import DIGITS_DATASET

class TestDecisionTrees(TestCase):
    def setUp(self):
        self.data   = DIGITS_DATASET['data']
        self.labels = DIGITS_DATASET['target']

    def test_digits_solutions_with_pre_built_model(self):
        arbitrary_sample_the_default_tree_will_get_right = 3
        state_predicted_from_model = wrapper_for_decision_tree_in_sklearn(
            self.data,
            self.labels,
            self.data[arbitrary_sample_the_default_tree_will_get_right]
        )

        self.assertEqual(
            self.labels[arbitrary_sample_the_default_tree_will_get_right],
            state_predicted_from_model,
            "Solve me first by writing `wrapper_for_decision_tree_in_sklearn`.")


    def test_minimum_accuracy_of_tree_model(self):
        """
            Split the data into a train and test set.
            Evaluate the accuracy of the model and assert it's above the
        supplied threshold.
            May require making a new function next to
        `wrapper_for_decision_tree_in_sklearn` to handle more than one test sample.

            Replace the assertion below with one that checks the model's accuracy
        is greater than or equal to the accuracy_target.
        """

        train, test = train_test_split(self.data, train_size = 0.8)

        accuracy_target = 0.8  # percent
        relative_test_set_size = 0.4  # percent

        score = 0.0

        self.assertGreaterEqual(score, accuracy_target,
                                "Write me second - after you get the above test working!")
