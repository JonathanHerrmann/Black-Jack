class Card:

    def __init__(self, suit, value):
        if suit not in ('spade', 'club', 'diamond', 'heart'):
            raise ValueError('Unexpected suit. This is a standard Deck')
        self.suit = suit

        if value not in ['A', 'K', 'Q', 'J'] and value not in list(range(2, 10)):
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


class Deck:
    pass
