import unittest
from collections import namedtuple

from part1 import Card, Hand, HandType


class HandTestCase(unittest.TestCase):
    def test_hand_type(self):
        TestCase = namedtuple("TestCase", "hand hand_type")

        test_cases = [
            TestCase(Hand([Card.A, Card.A, Card.A, Card.A, Card.A]), HandType.FIVE_OF_A_KIND),
            TestCase(Hand([Card.A, Card.A, Card.A, Card.A, Card.K]), HandType.FOUR_OF_A_KIND),
            TestCase(Hand([Card.A, Card.A, Card.A, Card.K, Card.K]), HandType.FULL_HOUSE),
            TestCase(Hand([Card.A, Card.A, Card.A, Card.Q, Card.K]), HandType.THREE_OF_A_KIND),
            TestCase(Hand([Card.A, Card.A, Card.Q, Card.K, Card.K]), HandType.TWO_PAIRS),
            TestCase(Hand([Card.A, Card.A, Card.Q, Card.K, Card.J]), HandType.ONE_PAIR),
            TestCase(Hand([Card.A, Card.T, Card.Q, Card.K, Card.J]), HandType.HIGH_CARD),
        ]

        for tc in test_cases:
            self.assertIs(tc.hand_type, tc.hand.hand_type)

    def test_lower_than(self):
        TestCase = namedtuple("TestCase", "description hand_a hand_b lower_than")

        test_cases = [
            TestCase(
                "high card against five of a kind",
                Hand([Card.A, Card.T, Card.Q, Card.K, Card.J]),
                Hand([Card.A, Card.A, Card.A, Card.A, Card.A]),
                True,
            ),
            TestCase(
                "five of a kind against five of a kind of the same type",
                Hand([Card.A, Card.A, Card.A, Card.A, Card.A]),
                Hand([Card.A, Card.A, Card.A, Card.A, Card.A]),
                False,
            ),
            TestCase(
                "five of a kind of K against five of a kind of A",
                Hand([Card.K, Card.K, Card.K, Card.K, Card.K]),
                Hand([Card.A, Card.A, Card.A, Card.A, Card.A]),
                True,
            ),
        ]

        for tc in test_cases:
            with self.subTest(description=tc.description):
                self.assertEqual(tc.lower_than, tc.hand_a < tc.hand_b)


if __name__ == "__main__":
    unittest.main()
