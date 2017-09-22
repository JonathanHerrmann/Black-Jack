import random


class Card:

    def __init__(self, suit, value):
        if suit not in ['spade', 'club', 'diamond', 'heart']:
            raise ValueError('Unexpected suit. This is a standard Deck')
        self.suit = suit

        if value not in ['A', 'K', 'Q', 'J'] and value not in list(range(2, 11)):
            raise ValueError('Not a valid value')

        self.value = value

        if value in ['J', 'Q', 'K']:
            self.numeric_value = 10
        elif value == 'A':
            self.numeric_value = 11
        else:
            self.numeric_value = self.value

    def __add__(self, other):
        return self.numeric_value + other.numeric_value

    def __gt__(self, other):
        return self.numeric_value > other.numeric_value

    def __eq__(self, other):
        return self.numeric_value == other.numeric_value

    def __repr__(self):
        return "<{} of {}s>".format(self.value, self.suit)

    def __str__(self):
        return repr(self)


class Deck:

    """A Standard deck class with 52 cards, 13 cards in each suit"""

    def __init__(self):
        self.cards = []  #same as list()

        for suit in ['spade', 'club', 'diamond', 'heart']:
            for value in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

