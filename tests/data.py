

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

# The above party data converted to binary-valued input variables:

BERNOULLI_PARTY_DATA_HEADER = [
    "D-None", "D-Near", "D-Urgent", "Party", "Lazy", "Activity"
]
BERNOULLI_PARTY_DATA = [
    ["No", "No", "Yes", "Yes", "Yes", "Party"],
    ["No", "No", "Yes", "No", "Yes", "Study"],
    ["No", "Yes", "No", "Yes", "Yes", "Party"],
    ["Yes", "No", "No", "Yes", "No", "Party"],
    ["Yes", "No", "No", "No", "Yes", "Pub"],
    ["Yes", "No", "No", "Yes", "No", "Party"],
    ["No", "Yes", "No", "No", "No", "Study"],
    ["No", "Yes", "No", "No", "Yes", "TV"],
    ["No", "Yes", "No", "Yes", "Yes", "Party"],
    ["No", "No", "Yes", "No", "No", "Study"]
]


from sklearn.datasets import load_digits

DIGITS_DATASET = load_digits()
