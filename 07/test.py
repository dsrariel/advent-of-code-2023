import unittest
from collections import namedtuple

from part1 import Card as Part1Card, Hand as Part1Hand, HandType
from part2 import Card as Part2Card, Hand as Part2Hand


class Part1HandTestCase(unittest.TestCase):
    def test_hand_type(self):
        TestCase = namedtuple("TestCase", "hand hand_type")

        test_cases = [
            TestCase(
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A]),
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.K]),
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.K, Part1Card.K]),
                HandType.FULL_HOUSE,
            ),
            TestCase(
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.Q, Part1Card.K]),
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.Q, Part1Card.K, Part1Card.K]),
                HandType.TWO_PAIRS,
            ),
            TestCase(
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.Q, Part1Card.K, Part1Card.J]),
                HandType.ONE_PAIR,
            ),
            TestCase(
                Part1Hand([Part1Card.A, Part1Card.T, Part1Card.Q, Part1Card.K, Part1Card.J]),
                HandType.HIGH_CARD,
            ),
        ]

        for tc in test_cases:
            self.assertIs(tc.hand_type, tc.hand.hand_type)

    def test_lower_than(self):
        TestCase = namedtuple("TestCase", "description hand_a hand_b lower_than")

        test_cases = [
            TestCase(
                "high card against five of a kind",
                Part1Hand([Part1Card.A, Part1Card.T, Part1Card.Q, Part1Card.K, Part1Card.J]),
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A]),
                True,
            ),
            TestCase(
                "five of a kind against five of a kind of the same type",
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A]),
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A]),
                False,
            ),
            TestCase(
                "five of a kind of K against five of a kind of A",
                Part1Hand([Part1Card.K, Part1Card.K, Part1Card.K, Part1Card.K, Part1Card.K]),
                Part1Hand([Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A, Part1Card.A]),
                True,
            ),
        ]

        for tc in test_cases:
            with self.subTest(description=tc.description):
                self.assertEqual(tc.lower_than, tc.hand_a < tc.hand_b)


class Part2HandTestCase(unittest.TestCase):
    def test_hand_type(self):
        TestCase = namedtuple("TestCase", "hand hand_type")

        test_cases = [
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.A]),
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.K]),
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.K, Part2Card.K]),
                HandType.FULL_HOUSE,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.Q, Part2Card.K]),
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.Q, Part2Card.K, Part2Card.K]),
                HandType.TWO_PAIRS,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.Q, Part2Card.K, Part2Card.T]),
                HandType.ONE_PAIR,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.T, Part2Card.Q, Part2Card.K, Part2Card.NINE]),
                HandType.HIGH_CARD,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.J]),
                HandType.FIVE_OF_A_KIND,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.A, Part2Card.T, Part2Card.J]),
                HandType.FOUR_OF_A_KIND,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.T, Part2Card.T, Part2Card.J]),
                HandType.FULL_HOUSE,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.A, Part2Card.T, Part2Card.K, Part2Card.J]),
                HandType.THREE_OF_A_KIND,
            ),
            TestCase(
                Part2Hand([Part2Card.A, Part2Card.K, Part2Card.T, Part2Card.Q, Part2Card.J]),
                HandType.ONE_PAIR,
            ),
            TestCase(
                Part2Hand([Part2Card.J, Part2Card.J, Part2Card.J, Part2Card.J, Part2Card.J]),
                HandType.FIVE_OF_A_KIND,
            ),
        ]

        for tc in test_cases:
            self.assertIs(tc.hand_type, tc.hand.hand_type)


if __name__ == "__main__":
    unittest.main()
