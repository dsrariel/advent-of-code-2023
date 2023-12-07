import unittest
from collections import namedtuple

from common import Hand, HandType
from part1 import ClassicDeck
from part2 import JokerDeck


class HandTestCase(unittest.TestCase):
    def test_hand_type(self):
        TestCase = namedtuple("TestCase", "cards deck_type hand_type")

        test_cases = [
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                ClassicDeck,
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A],
                JokerDeck,
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.K],
                ClassicDeck,
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.K],
                JokerDeck,
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.K, ClassicDeck.K],
                ClassicDeck,
                HandType.FULL_HOUSE,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.K, JokerDeck.K],
                JokerDeck,
                HandType.FULL_HOUSE,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.Q, ClassicDeck.K],
                ClassicDeck,
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.Q, JokerDeck.K],
                JokerDeck,
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.K],
                ClassicDeck,
                HandType.TWO_PAIRS,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.Q, JokerDeck.K, JokerDeck.K],
                JokerDeck,
                HandType.TWO_PAIRS,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.A, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.J],
                ClassicDeck,
                HandType.ONE_PAIR,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.Q, JokerDeck.K, JokerDeck.T],
                JokerDeck,
                HandType.ONE_PAIR,
            ),
            TestCase(
                [ClassicDeck.A, ClassicDeck.T, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.J],
                ClassicDeck,
                HandType.HIGH_CARD,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.T, JokerDeck.Q, JokerDeck.K, JokerDeck.NINE],
                JokerDeck,
                HandType.HIGH_CARD,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.J],
                JokerDeck,
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.A, JokerDeck.T, JokerDeck.J],
                JokerDeck,
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.T, JokerDeck.T, JokerDeck.J],
                JokerDeck,
                HandType.FULL_HOUSE,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.A, JokerDeck.T, JokerDeck.K, JokerDeck.J],
                JokerDeck,
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                [JokerDeck.A, JokerDeck.K, JokerDeck.T, JokerDeck.Q, JokerDeck.J],
                JokerDeck,
                HandType.ONE_PAIR,
            ),
            TestCase(
                [JokerDeck.J, JokerDeck.J, JokerDeck.J, JokerDeck.J, JokerDeck.J],
                JokerDeck,
                HandType.FIVE_OF_A_KIND,
            ),
        ]

        for tc in test_cases:
            with self.subTest(test_case=tc):
                self.assertIs(tc.hand_type, Hand(tc.cards, tc.deck_type).hand_type)

    def test_lower_than(self):
        TestCase = namedtuple("TestCase", "description hand_a hand_b lower_than")

        test_cases = [
            TestCase(
                "high card against five of a kind",
                Hand(
                    [ClassicDeck.A, ClassicDeck.T, ClassicDeck.Q, ClassicDeck.K, ClassicDeck.J],
                    ClassicDeck,
                ),
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    ClassicDeck,
                ),
                True,
            ),
            TestCase(
                "five of a kind against five of a kind of the same type",
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    ClassicDeck,
                ),
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    ClassicDeck,
                ),
                False,
            ),
            TestCase(
                "five of a kind of K against five of a kind of A",
                Hand(
                    [ClassicDeck.K, ClassicDeck.K, ClassicDeck.K, ClassicDeck.K, ClassicDeck.K],
                    ClassicDeck,
                ),
                Hand(
                    [ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A, ClassicDeck.A],
                    ClassicDeck,
                ),
                True,
            ),
        ]

        for tc in test_cases:
            with self.subTest(description=tc.description):
                self.assertEqual(tc.lower_than, tc.hand_a < tc.hand_b)
