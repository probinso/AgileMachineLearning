import unittest
from Models.naivebayes import wrapper_for_nb_in_sklearn, wrapper_for_nb_in_sklearn_using_bernoulli_nb
from tests.data import PARTY_DATA, BERNOULLI_PARTY_DATA


class TestNaiveBayes(unittest.TestCase):
    def test_party_solutions_with_pre_built_model(self):
        X = ["Near", "No", "Yes"]
        predicted_class = wrapper_for_nb_in_sklearn(PARTY_DATA, X)
        self.assertEqual(predicted_class, "TV")

    def test_party_solutions_with_pre_built_bernoulli_model(self):
        X = ["No", "Yes", "No", "No", "Yes"]
        predicted_class = wrapper_for_nb_in_sklearn_using_bernoulli_nb(BERNOULLI_PARTY_DATA, X)
        self.assertEqual(predicted_class, "TV")
