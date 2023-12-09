from typing import List

FILE_NAME = "example.txt"


class History:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def _calculate_differences(self) -> List[List[int]]:
        previous_series = self.numbers
        finished = False
        differences = [[self.numbers[0], self.numbers[-1]]]
        while not finished:
            finished = True
            current_series = []
            for i in range(1, len(previous_series)):
                next_element = previous_series[i] - previous_series[i - 1]
                current_series.append(next_element)
                if next_element != 0:
                    finished = False

            differences.append([current_series[0], current_series[-1]])
            previous_series = current_series

        return differences

    def extrapolates_previous_value(self) -> int:
        differences = self._calculate_differences()
        previous = 0
        for i in range(len(differences) - 2, -1, -1):
            previous = differences[i][0] - previous

        return previous

    def extrapolate_next_value(self) -> int:
        differences = self._calculate_differences()
        previous = 0
        for i in range(len(differences) - 2, -1, -1):
            previous = differences[i][-1] + previous

        return previous


def part2():
    previous_values = []
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            history = History([int(n) for n in line.split(" ")])
            previous_values.append(history.extrapolates_previous_value())

    print(f"The sum of the extrapolated values is {sum(previous_values)}.")


def part1():
    next_values = []
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            history = History([int(n) for n in line.split(" ")])
            next_values.append(history.extrapolate_next_value())

    print(f"The sum of the extrapolated values is {sum(next_values)}.")


if __name__ == "__main__":
    part1()
    part2()
