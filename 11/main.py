from collections import OrderedDict
from typing import Dict, List

FILE_NAME = "input.txt"


def expand_vertically(columns: List[int], start: int, j: int) -> int:
    """expands all values in the columns that are positioned after start and that have a value lower
    than j.

    Args:
        columns (List[int]): ints to be modified.
        start (int): where to start searching.
        j (int): bound for comparison.

    Returns:
        int: first position modified in columns.
    """
    end = len(columns) - 1
    while start <= end:
        mid = (end - start) // 2 + start

        if columns[mid] <= j:
            start = mid + 1
            continue

        end = mid - 1

    for i in range(start, len(columns)):
        columns[i] += 1

    return start


def load_galaxies() -> Dict[int, List[int]]:
    galaxies = OrderedDict()

    columns_with_galaxies, galaxy_x, observation_y_len = set(), 0, None
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            line = line.rstrip()
            if observation_y_len is None:
                observation_y_len = len(line)

            for j, c in enumerate(line):
                if c != "#":
                    continue

                columns_with_galaxies.add(j)
                if galaxy_x not in galaxies:
                    galaxies[galaxy_x] = []
                galaxies[galaxy_x].append(j)

            if galaxy_x not in galaxies:
                galaxy_x += 1
            galaxy_x += 1

    for columns in galaxies.values():
        start, expansions = 0, 0
        for j in range(observation_y_len):
            if j in columns_with_galaxies:
                continue

            start = expand_vertically(columns, start, j + expansions)
            expansions += 1

    return galaxies


def main():
    galaxies = load_galaxies()

    distance_sum = 0
    for i, columns in galaxies.items():
        for j in columns:
            for m, m_columns in galaxies.items():
                for n in m_columns:
                    if m < i or i == m and n <= j:
                        continue
                    distance_sum += (m - i) + abs(n - j)

    print(f"The sum of the lengths between the paths is {distance_sum}.")


if __name__ == "__main__":
    main()
