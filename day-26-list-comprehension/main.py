import pandas
NATO_ALPHABET = pandas.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
def create_nato():
    # Loop through rows of a data frame
    # Access index and row
    # Access row.student or row.score
    new_dict = {row.letter: row.code for (
        index, row) in NATO_ALPHABET.iterrows()}

    return new_dict


def apply_nato(word, nato_alphabet_dict):
    nato_applied = [nato_alphabet_dict[word] for word in word]
    print(nato_applied)


if __name__ == '__main__':
    # TODO 1. Create a dictionary in this format:
    # {"A": "Alfa", "B": "Bravo"}
    nato_alphabet_dict = create_nato()

    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    word = input("Please enter any word: \n").upper()
    apply_nato(word, nato_alphabet_dict)
