from blackjack import Card, Deck
import pytest


def test_card_has_suit():
    card = Card('diamond', 2)
    assert hasattr(card, 'suit')


def test_card_has_valid_suit():
    with pytest.raises(ValueError):
        Card('somestupidsuit', 2)

    c = Card('spade', 2)
    assert c.suit == 'spade'


def test_card_has_value():
    king_of_spades = Card('spade', 'K')
    queen_of_clubs = Card('club', 'Q')

    assert king_of_spades.value == 'K'
    assert king_of_spades.value != 'Q'


def test_add_cards():
    assert 5 == Card('spade', 2) + Card('club', 3)


def test_compare():
    assert True == (Card('spade', 'Q') == Card('club', 'J'))


def test_greater_than():
    assert True == (Card('spade', 'A') > Card('club', 4))


def test_deck():
    pass
