from typing import List

FILE_NAME = "input.txt"


class History:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def _calculate_differences(self) -> List[List[int]]:
        finished = False
        differences = [self.numbers]
        while not finished:
            finished = True
            differences.append([])
            for i in range(1, len(differences[-2])):
                difference = differences[-2][i] - differences[-2][i - 1]
                differences[-1].append(difference)
                if difference != 0:
                    finished = False

        return differences

    def _extrapolate(self) -> None:
        differences = self._calculate_differences()
        for i in range(len(differences) - 1, 0, -1):
            new_number = differences[i - 1][-1] + differences[i][-1]
            differences[i - 1].append(new_number)

    def extrapolate_next_value(self) -> int:
        self._extrapolate()
        return self.numbers[-1]


def main():
    next_values = []
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            history = History([int(n) for n in line.split(" ")])
            next_values.append(history.extrapolate_next_value())

    print(f"The sum of the extrapolated values is {sum(next_values)}.")


if __name__ == "__main__":
    main()
