from collections import Counter
from enum import Enum

from part1 import get_classic_hand_type
from common import Game, Hand, HandType, get_sequence

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


def get_joker_hand_type(hand: Hand) -> HandType:
    counter = Counter(hand.cards)
    j_counts = counter[JokerDeck.J]
    del counter[JokerDeck.J]

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


def main():
    with open(FILE_NAME, encoding="utf-8") as f:
        game = Game([])
        for line in f.readlines():
            game.sequences.append(get_sequence(line, get_joker_hand_type, JokerDeck))

    print(f"The game total winnings are {game.winnings}.")


if __name__ == "__main__":
    main()
