from random import choice


class WordChain:

    def __init__(self, word):
        self.word = word
        self.nexts = []
        self.values = {}

    def add_next(self, next):
        self.nexts.append(next)

    def compute_next(self):
        return choice(self.nexts)
