"""Retrieve random french word"""
import random
import pandas as pd

class RandomWord():
    def __init__(self):
        self.words = []
        self.load_words()

    def load_words(self) -> None:
        """Retrieve words from csv file on ./data/french_words.csv with pandas"""
        try:
            df = pd.read_csv("./data/words_to_learn.csv")
        except FileNotFoundError:
            original_df = pd.read_csv("./data/french_words.csv")
            self.words = original_df.to_dict(orient="records")
        else:
            self.words = df.to_dict(orient="records")
        return

    def get_word(self) -> object:
        """Retrieve random word from list of words"""
        return random.choice(self.words)
    
    def known_word(self, word) -> None:
        """Remove word from list of words and save them in new CSV"""
        self.words.remove(word)
        pd.DataFrame(self.words).to_csv("./data/words_to_learn.csv", index=False)
        return