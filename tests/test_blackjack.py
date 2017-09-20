from blackjack import Card, Deck
import pytest


def test_card_has_suit():
    card = Card('diamond')
    assert hasattr(card, 'suit')


def test_card_has_valid_suit():
    with pytest.raises(ValueError):
        Card('somestupidsuit')

        c = Card('spade')

        assert c.suit == 'spade'


def test_deck():
    pass

