import unittest
from Models.naivebayes import wrapper_for_nb_in_sklearn
import pandas as pd


# Test data pulled from: https://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html
# Thanks, Marsland!

PARTY_DATA_HEADER = ["Deadline", "Party", "Lazy", "Activity"]
PARTY_DATA =       [["Urgent", "Yes", "Yes", "Party"],
                    ["Urgent", "No", "Yes", "Study"],
                    ["Near", "Yes", "Yes", "Party"],
                    ["None", "Yes", "No", "Party"],
                    ["None", "No", "Yes", "Pub"],
                    ["None", "Yes", "No", "Party"],
                    ["Near", "No", "No", "Study"],
                    ["Near", "No", "Yes", "TV"],
                    ["Near", "Yes", "Yes", "Party"],
                    ["Urgent", "No", "No", "Study"]]

dataframe = pd.DataFrame(PARTY_DATA, columns=PARTY_DATA_HEADER)
class TestNaiveBayes(unittest.TestCase):
    def test_party_solutions_with_pre_built_model(self):

        X = ["Near", "No", "Yes"]
        prob, predicted_class = wrapper_for_nb_in_sklearn(dataframe, X)
        print(prob, predicted_class)
        self.assertEqual(predicted_class, "TV")

