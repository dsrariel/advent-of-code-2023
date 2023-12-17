from typing import List
from collections import deque, namedtuple

FILE_NAME = "example.txt"

Row = namedtuple("Row", "arrangement damaged_groups unknown_springs")


def is_possible_arrangement(row: Row) -> bool:
    i, group, group_size = 0, 0, 0
    while i < len(row.arrangement):
        if row.arrangement[i] == "?":
            return True

        if row.arrangement[i] == "#" and group >= len(row.damaged_groups):
            return False

        if row.arrangement[i] == "#":
            group_size += 1

        if row.arrangement[i] == "." and group_size != 0:
            if group_size != row.damaged_groups[group]:
                return False

            group += 1
            group_size = 0

        i += 1

    if (
        i == len(row.arrangement)
        and row.arrangement[i - 1] == "#"
        and group_size == row.damaged_groups[group]
    ):
        group += 1

    return group == len(row.damaged_groups)


def get_possible_arrangements_count(row: Row) -> int:
    is_possible = is_possible_arrangement(row)

    if not row.unknown_springs:
        return int(is_possible)

    if row.unknown_springs and not is_possible:
        return 0

    count = 0
    next_unknown_spring = row.unknown_springs.popleft()
    row.arrangement[next_unknown_spring] = "."
    count += get_possible_arrangements_count(row)
    row.arrangement[next_unknown_spring] = "#"
    count += get_possible_arrangements_count(row)

    row.arrangement[next_unknown_spring] = "?"
    row.unknown_springs.appendleft(next_unknown_spring)

    return count


def load_input() -> List[Row]:
    condition_records = []

    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            arrangement_string, damaged_groups_string = line.split(" ", 1)

            arrangement, unknown_springs = [], deque()
            for i, a in enumerate(arrangement_string):
                arrangement.append(a)
                if a == "?":
                    unknown_springs.append(i)

            row = Row(
                arrangement, [int(g) for g in damaged_groups_string.split(",")], unknown_springs
            )
            condition_records.append(row)

    return condition_records


def unfold_input(condition_records: List[Row]) -> List[Row]:
    rows = []
    for row in condition_records:
        new_row = Row(list(row.arrangement), list(row.damaged_groups), deque(row.unknown_springs))
        for i in range(4):
            new_row.arrangement.append("?")
            new_row.arrangement.extend(row.arrangement)
            new_row.damaged_groups.extend(row.damaged_groups)
            shift = (len(row.arrangement) + 1) * (i + 1)
            new_row.unknown_springs.append(shift - 1)
            new_row.unknown_springs.extend([u + shift for u in row.unknown_springs])
        rows.append(new_row)

    return rows


def part_one():
    condition_records = load_input()
    count = sum([get_possible_arrangements_count(r) for r in condition_records])
    print(f"The sum of possible arrangements is {count}.")


def part_two():
    condition_records = load_input()
    condition_records = unfold_input(condition_records)
    count = sum([get_possible_arrangements_count(r) for r in condition_records])
    print(f"The sum of possible arrangements is {count}.")


if __name__ == "__main__":
    # part_one()
    part_two()
