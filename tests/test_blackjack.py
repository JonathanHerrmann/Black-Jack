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


def test_init_deck():
    deck = Deck()
    assert len(deck.cards) == 52


def test_shuffle_deck():
    deck_a = Deck()
    deck_b = Deck()

    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        assert c_a.value == c_b.value

        # checks that the decks are identical

    deck_b.shuffle()
    randomness = []
    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        randomness.append(c_a.value != c_b.value)

    assert any(randomness)


def test_len_deck():
    deck = Deck()

    assert len(deck) == 52


def test_iter_deck():
    deck = Deck()

    assert next(deck) == Card('spade', 2)

    next(deck)
    next(deck)

    assert next(deck) == Card('spade', 5)


def test_deal_hand():
    deck = Deck()

    assert isinstance(deck.deal_card(), Card)

    card1, card2 = deck.deal_hand()

    assert isinstance(card1, Card)
    assert isinstance(card2, Card)

    assert card1 != card2

    deck = Deck()
    deck.shuffle()
    card1, card2 = deck.deal_hand()

    assert card1 != card2

    card1, card2 = deck.deal_card(), deck.deal_card()
    
    assert card1 != card2


def test_proper_repr():
    assert "<A of spades>" == repr(Card("spade", "A"))
