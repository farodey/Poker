import random
from Card import  Card

class Deck:
    def __init__(self):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
        suits = ['s', 'c', 'h', 'd']
        self.cards = []

        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        a = len(self.cards)
        b = a - 1
        for d in range(b, 0, -1):
            e = random.randint(0, d)
            if e == d:
                continue
            self.cards[d], self.cards[e] = self.cards[e], self.cards[d]
        return self.cards