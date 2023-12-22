FILE_NAME = "input.txt"


def load_input() -> list[list[list[int]]]:
    valley = []
    with open(FILE_NAME, encoding="utf-8") as f:
        mountain = []
        for line in f.readlines():
            line = line.rstrip()
            if not line:
                valley.append(mountain)
                mountain = []
                continue

            mountain.append([int(c == "#") for c in line])

    valley.append(mountain)

    return valley


def get_minimum_distance_from_edge(mountain: list[list[int]], j: int) -> int:
    y = len(mountain[0])
    return min(j - 0, y - j)


def are_all_the_lines_symmetric(mountain: list[list[int]], j: int) -> bool:
    if mountain[0][j - 1] != mountain[0][j]:
        return False

    offset = get_minimum_distance_from_edge(mountain, j)
    for line in mountain:
        for i in range(offset):
            if line[j - 1 - i] != line[j + i]:
                return False

    return True


def transpose_mountain(mountain: list[list[int]]) -> list[list[int]]:
    x, y = len(mountain), len(mountain[0])
    transposed_mountain = [[0] * x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            transposed_mountain[j][i] = mountain[i][j]

    return transposed_mountain


def find_mirror_sum(mountain: list[list[int]]):
    def find_vertical_mirror_sum(mountain: list[list[int]]) -> int:
        y = len(mountain[0])
        for j in range(1, y):
            if are_all_the_lines_symmetric(mountain, j):
                return j

        return -1

    mirror_sum = find_vertical_mirror_sum(mountain)
    if mirror_sum != -1:
        return mirror_sum

    inverted_mountain = transpose_mountain(mountain)
    return find_vertical_mirror_sum(inverted_mountain) * 100


def part_one():
    valley = load_input()
    mirrors_sum = sum(find_mirror_sum(m) for m in valley)
    print(f"The sum of the mirrors across the valley is {mirrors_sum}.")


if __name__ == "__main__":
    part_one()
