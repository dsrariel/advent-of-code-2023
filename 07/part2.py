from collections import Counter, namedtuple
from enum import Enum
from typing import List

from part1 import HandType, Sequence, Game

FILE_NAME = "input.txt"


class Card(Enum):
    J = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    T = 10
    Q = 12
    K = 13
    A = 14


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    @property
    def hand_type(self):
        counter = Counter(self.cards)
        j_counts = counter[Card.J]
        del counter[Card.J]

        highest = counter.most_common(2)
        if not highest:
            return HandType.FIVE_OF_A_KIND

        first_count = highest[0][1]
        first_count += j_counts

        if first_count == 5:
            return HandType.FIVE_OF_A_KIND
        if first_count == 4:
            return HandType.FOUR_OF_A_KIND

        second_count = highest[1][1]

        if first_count == 3 and second_count == 2:
            return HandType.FULL_HOUSE
        if first_count == 3:
            return HandType.THREE_OF_A_KIND
        if first_count == 2 and second_count == 2:
            return HandType.TWO_PAIRS
        if first_count == 2:
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
