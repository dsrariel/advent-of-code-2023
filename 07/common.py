from collections import namedtuple
from enum import Enum
from typing import List


HandType = Enum(
    "HandType",
    "HIGH_CARD ONE_PAIR TWO_PAIRS THREE_OF_A_KIND FULL_HOUSE FOUR_OF_A_KIND FIVE_OF_A_KIND",
)


class Hand:
    def __init__(self, cards: List[Enum], hand_type_function: callable):
        self.cards = cards
        self.hand_type_function = hand_type_function

    @property
    def hand_type(self):
        return self.hand_type_function(self)

    def __lt__(self, other: "Hand"):
        if not self.hand_type is other.hand_type:
            return self.hand_type.value < other.hand_type.value

        for self_card, other_card in zip(self.cards, other.cards):
            if self_card.value == other_card.value:
                continue
            return self_card.value < other_card.value

        return False


Sequence = namedtuple("Sequence", "hand bid")


def get_sequence(line: str, hand_type_func: callable, deck_type: Enum) -> Sequence:
    cards_and_bid = line.split(" ")
    bid = int(cards_and_bid[1])
    cards = [get_card(c, deck_type) for c in cards_and_bid[0]]
    return Sequence(Hand(cards, hand_type_func), bid)


class Game:
    def __init__(self, sequences: List[Sequence]):
        self.sequences = sequences

    @property
    def winnings(self) -> int:
        sequences = sorted(self.sequences, reverse=True)
        ranks = len(sequences)
        return sum([(ranks - i) * sequence.bid for i, sequence in enumerate(sequences)])


def get_card(char: str, deck_type: Enum) -> Enum:
    try:
        return deck_type[char]
    except KeyError:
        return deck_type(int(char))
