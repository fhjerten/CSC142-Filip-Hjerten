import random
from Card import *

class Deck:

    # all suits in a deck of cards
    suits = ('Diamonds', 'Clubs', 'Hearts', 'Spades')

    values = {
        'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10
    }

    def __init__(self, window):
        self.cards = []

        # make all 52 cards.
        for suits in Deck.suits:
            for rank, value in Deck.values.items():
                card = Card(window, rank, suits, value)
                self.cards.append(card)

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards) #shuffling cards.

        # hide cards to be face down.
        for c in self.cards:
            c.conceal()

    def getCard(self):
        return self.cards.pop()  # remove, and return to the top card.