from collections import Counter, namedtuple
from enum import Enum
from typing import List

FILE_NAME = "input.txt"


class Card(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


HandType = Enum(
    "HandType",
    "HIGH_CARD ONE_PAIR TWO_PAIRS THREE_OF_A_KIND FULL_HOUSE FOUR_OF_A_KIND FIVE_OF_A_KIND",
)
Sequence = namedtuple("Sequence", "hand bid")


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    @property
    def hand_type(self):
        counter = Counter(self.cards)
        previous = None
        for _, count in counter.most_common():
            if count == 5:
                return HandType.FIVE_OF_A_KIND
            if count == 4:
                return HandType.FOUR_OF_A_KIND
            if count == 3:
                previous = 3
                continue
            if count == 2 and previous == 3:
                return HandType.FULL_HOUSE
            if previous == 3:
                return HandType.THREE_OF_A_KIND
            if count == 2 and previous == 2:
                return HandType.TWO_PAIRS
            if count == 2:
                previous = 2
                continue
            if previous == 2:
                return HandType.ONE_PAIR
            return HandType.HIGH_CARD

    def __lt__(self, other: "Hand"):
        if not self.hand_type is other.hand_type:
            return self.hand_type.value < other.hand_type.value

        for self_card, other_card in zip(self.cards, other.cards):
            if self_card.value == other_card.value:
                continue
            return self_card.value < other_card.value

        return False


class Game:
    def __init__(self, sequences: List[Sequence]):
        self.sequences = sequences

    @property
    def winnings(self) -> int:
        sequences = sorted(self.sequences, reverse=True)
        ranks = len(sequences)
        return sum([(ranks - i) * sequence.bid for i, sequence in enumerate(sequences)])


def get_card(char: str) -> Card:
    try:
        return Card[char]
    except KeyError:
        return Card(int(char))


def get_sequence(line: str) -> Sequence:
    cards_and_bid = line.split(" ")
    bid = int(cards_and_bid[1])
    cards = [get_card(c) for c in cards_and_bid[0]]
    return Sequence(Hand(cards), bid)


def main():
    with open(FILE_NAME, encoding="utf-8") as f:
        game = Game([])
        for line in f.readlines():
            game.sequences.append(get_sequence(line))

    print(f"The game total winnings are {game.winnings}.")


if __name__ == "__main__":
    main()
