

# Party test data pulled from: https://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html
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

from sklearn.datasets import load_digits

DIGITS_DATASET = load_digits()
