class Card:

    def __init__(self, suit, value):
        if suit not in ('spade', 'club', 'diamond', 'heart'):
            raise ValueError('This is a standart cardgame')
        self.suit = suit

        if value not in ['A', 'K', 'Q', 'J'] and value not in list(range(2, 10)):
            raise ValueError('Not a valid value')

        self.value = value

    def __add__(self, other):
        return self.value + other.value


class Deck:
    pass
