from blackjack import Deck

test_deck = Deck()
test_new_deck = Deck.make_deck()

print(test_new_deck)


def test_deck_is_correct_size():
    assert len(test_deck) == 51
