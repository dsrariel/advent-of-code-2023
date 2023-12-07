import unittest
from collections import namedtuple

from common import Hand, HandType
from part1 import ClassicDeck, get_classic_hand_type
from part2 import JokerDeck, get_joker_hand_type


class HandTestCase(unittest.TestCase):
    def test_hand_type(self):
        TestCase = namedtuple("TestCase", "cards hand_type_function hand_type")

        test_cases = [
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                get_classic_hand_type,
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A],
                get_joker_hand_type,
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.K],
                get_classic_hand_type,
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.K],
                get_joker_hand_type,
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.K, ClassicDeck.K],
                get_classic_hand_type,
                HandType.FULL_HOUSE,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.K, JokerDeck.K],
                get_joker_hand_type,
                HandType.FULL_HOUSE,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.Q, ClassicDeck.K],
                get_classic_hand_type,
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.Q, JokerDeck.K],
                get_joker_hand_type,
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.K],
                get_classic_hand_type,
                HandType.TWO_PAIRS,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.Q, JokerDeck.K, JokerDeck.K],
                get_joker_hand_type,
                HandType.TWO_PAIRS,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.J],
                get_classic_hand_type,
                HandType.ONE_PAIR,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.Q, JokerDeck.K, JokerDeck.T],
                get_joker_hand_type,
                HandType.ONE_PAIR,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.T, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.J],
                get_classic_hand_type,
                HandType.HIGH_CARD,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.T, JokerDeck.Q, JokerDeck.K, JokerDeck.NINE],
                get_joker_hand_type,
                HandType.HIGH_CARD,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.J],
                get_joker_hand_type,
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.T, JokerDeck.J],
                get_joker_hand_type,
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.T, JokerDeck.T, JokerDeck.J],
                get_joker_hand_type,
                HandType.FULL_HOUSE,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.T, JokerDeck.K, JokerDeck.J],
                get_joker_hand_type,
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.K, JokerDeck.T, JokerDeck.Q, JokerDeck.J],
                get_joker_hand_type,
                HandType.ONE_PAIR,
            ),
            TestCase(
                [JokerDeck.J, JokerDeck.J, JokerDeck.J, JokerDeck.J, JokerDeck.J],
                get_joker_hand_type,
                HandType.FIVE_OF_A_KIND,
            ),
        ]

        for tc in test_cases:
            with self.subTest(test_case=tc):
                self.assertIs(tc.hand_type, Hand(tc.cards, tc.hand_type_function).hand_type)

    def test_lower_than(self):
        TestCase = namedtuple("TestCase", "description hand_a hand_b lower_than")

        test_cases = [
            TestCase(
                "high card against five of a kind",
                Hand(
                    [ClassicDeck.A, ClassicDeck.T, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.J],
                    get_classic_hand_type,
                ),
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    get_classic_hand_type,
                ),
                True,
            ),
            TestCase(
                "five of a kind against five of a kind of the same type",
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    get_classic_hand_type,
                ),
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    get_classic_hand_type,
                ),
                False,
            ),
            TestCase(
                "five of a kind of K against five of a kind of A",
                Hand(
                    [ClassicDeck.K, ClassicDeck.K, ClassicDeck.K, ClassicDeck.K, ClassicDeck.K],
                    get_classic_hand_type,
                ),
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    get_classic_hand_type,
                ),
                True,
            ),
        ]

        for tc in test_cases:
            with self.subTest(description=tc.description):
                self.assertEqual(tc.lower_than, tc.hand_a < tc.hand_b)
