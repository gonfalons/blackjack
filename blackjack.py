"""
As a portfolio project, develop a basic blackjack program.
Using test-driven development, build a readable program
that functions as expected as a simulation.

Build a solid foundation, using git.
Testing incrementally, to form a  project that can be expanded upon
for greater depth if desired.

Demonstrate proficiency in object-oriented programming, write
readable and intuitive, well documented code using Python 3.6+
"""

import logging
from random import shuffle  # random is insecure! Not for production...
#  see REFS in README for more information. (Ref #0)
logging.basicConfig(filename='blackjack.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Deck:
    """
    Build a simulated classic French Deck to use for blackjack

    This is the standard 52 card playing card decks used in casinos
    and with most card games. 
    """

    def __init__(self):
        self.deck = self.make_deck()
        shuffle(self.deck)

    @staticmethod
    def make_deck():
        """
        Build deck with idiomatic syntax: clubs, diamonds, hearts, spades:
        represented as 'c', 'd', 'h', 's' respectively. i.e.
        '5 of clubs' --> '5c'
        """

        _card_ranks = [
            str(n) for n in range(2, 10)
        ] + list('TJQKA')

        _card_suits = 'c h d s'.split()  # clubs hearts diamonds spades

        new_deck = [
            (f'{rank}{suit}')
            for rank in _card_ranks
            for suit in _card_suits
        ]

        logging.debug(f'New deck: {new_deck}')

        return new_deck

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return f'''
        {len(self)} cards: in deck \n\t {self.deck[:26]}\n\t{self.deck[26:]}
        '''


my_test_deck = Deck()
