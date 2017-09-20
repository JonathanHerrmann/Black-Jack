class Card:

    def __init__(self, suit):
        if suit not in ('spade', 'club', 'diamond', 'heart'):
            raise ValueError('This is a standart cardgame')
        self.suit = suit

    pass


class Deck:
    pass
