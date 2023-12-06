from collections import OrderedDict, namedtuple
from typing import Optional

Digit = namedtuple("Digit", "name value".split())

FILE_NAME = "input.txt"
LENGTH_TO_DIGITS = OrderedDict(
    [
        (1, [Digit(str(i), i) for i in range(1, 10)]),
        (3, [Digit("one", 1), Digit("two", 2), Digit("six", 6)]),
        (4, [Digit("four", 4), Digit("five", 5), Digit("nine", 9)]),
        (5, [Digit("three", 3), Digit("seven", 7), Digit("eight", 8)]),
    ]
)


def get_digits(line: str) -> Optional[int]:
    for start in range(len(line)):
        for length, digits in LENGTH_TO_DIGITS.items():
            if start + length > len(line):
                break

            possible_digit = line[start : start + length]

            for digit in digits:
                if not possible_digit == digit.name:
                    continue

                yield digit.value


def main():
    with open(FILE_NAME) as f:
        calibration_sum = 0
        for line in f.readlines():
            calibration_value, last_digit = None, None
            for digit in get_digits(line):
                if calibration_value == None:
                    calibration_value = 10 * digit

                last_digit = digit

            calibration_value += last_digit
            calibration_sum += calibration_value

    print(f"The calibration sum is {calibration_sum}")


if __name__ == "__main__":
    main()
