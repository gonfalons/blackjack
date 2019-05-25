from blackjack import Deck

test_deck = Deck()
test_new_deck = Deck.make_deck()

print(test_new_deck)


def test_deck_is_correct_size():
    """52 cards"""
    assert len(test_deck) == 51


def test_deck_has_all_cards():
    pass
