import unittest
from Models.naivebayes import wrapper_for_nb_in_sklearn
from tests.data import PARTY_DATA


class TestNaiveBayes(unittest.TestCase):
    def test_party_solutions_with_pre_built_model(self):
        X = ["Near", "No", "Yes"]
        predicted_class = wrapper_for_nb_in_sklearn(PARTY_DATA, X)
        self.assertEqual(predicted_class, "TV")

        #TODO: Probably should have a few other assertions in here.
