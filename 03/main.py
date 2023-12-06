from typing import List

FILE_NAME = "input.txt"


def get_schematic() -> List[List[str]]:
    with open(FILE_NAME, encoding="utf-8") as f:
        return [[char for char in line.rstrip()] for line in f.readlines()]


def has_adjacent_symbol(schematic: List[List[str]], i: int, j: int) -> bool:
    for x in range(i - 1, i + 2):
        if x < 0 or x >= len(schematic):
            continue

        for y in range(j - 1, j + 2):
            if x == i and j == i:
                continue
            if y < 0 or y >= len(schematic[i]):
                continue

            is_symbol = not schematic[x][y].isdigit() and schematic[x][y] != "."
            if is_symbol:
                return True

    return False


def get_number_start_and_end(line: List[str], i: int) -> (int, int):
    start = i
    while start >= 0 and line[start].isdigit():
        start -= 1
    start += 1

    end = i
    while end < len(line) and line[end].isdigit():
        end += 1

    return start, end


def main():
    part_numbers_sum = 0
    schematic = get_schematic()
    for i, line in enumerate(schematic):
        j, line = 0, schematic[i]
        while j < len(line):
            char = line[j]
            if char.isdigit() and has_adjacent_symbol(schematic, i, j):
                start, end = get_number_start_and_end(line, j)
                number = int("".join(line[start:end]))
                part_numbers_sum += number
                j = end - 1

            j += 1

    print(
        f"The sum of all of the part numbers is the engine schematic is {part_numbers_sum}"
    )


if __name__ == "__main__":
    main()
