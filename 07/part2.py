from collections import Counter
from enum import Enum
from typing import List

from common import Game, HandType, get_sequence
from part1 import ClassicDeck

FILE_NAME = "input.txt"


class JokerDeck(Enum):
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

    @classmethod
    def get_hand_type(cls, cards: List[Enum]) -> HandType:
        counter = Counter(cards)
        j_counts = counter[cls.J]
        del counter[cls.J]

        highest = counter.most_common(1)
        if not highest:
            cards = [cls.J for _ in range(j_counts)]
            return ClassicDeck.get_hand_type(cards)

        counter[highest[0][0]] += j_counts
        cards = [e for e in counter.elements()]
        return ClassicDeck.get_hand_type(cards)


def main():
    with open(FILE_NAME, encoding="utf-8") as f:
        game = Game([])
        for line in f.readlines():
            game.sequences.append(get_sequence(line, JokerDeck))

    print(f"The game total winnings are {game.winnings}.")


if __name__ == "__main__":
    main()
