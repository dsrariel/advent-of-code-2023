from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

FILE_NAME = "example.txt"


@dataclass
class Row:
    arrangement: List[str]
    damaged_groups: List[int]


def get_possible_arrangements_count(row: Row, cache: defaultdict[str, Dict[str, int]]) -> int:
    arrangement = "".join(row.arrangement)
    numbers = "".join(map(str, row.damaged_groups))

    if not row.damaged_groups:
        cache[arrangement][numbers] = int(not any(a == "#" for a in row.arrangement))
        return cache[arrangement][numbers]

    group_size = 0
    for i, c in enumerate(row.arrangement):
        if c == "?":
            a = Row(list(row.arrangement), row.damaged_groups)
            b = Row(list(row.arrangement), row.damaged_groups)
            a.arrangement[i], b.arrangement[i] = "#", "."
            cache[arrangement][numbers] = get_possible_arrangements_count(
                a, cache
            ) + get_possible_arrangements_count(b, cache)
            return cache[arrangement][numbers]

        if c == "#":
            group_size += 1
            continue

        if group_size == 0:
            continue

        if group_size == row.damaged_groups[0]:
            cache[arrangement][numbers] = get_possible_arrangements_count(
                Row(row.arrangement[i:], row.damaged_groups[1:]), cache
            )
            return cache[arrangement][numbers]

        cache[arrangement][numbers] = 0
        return cache[arrangement][numbers]

    cache[arrangement][numbers] = int(
        len(row.damaged_groups) == 1 and group_size == row.damaged_groups[0]
    )
    return cache[arrangement][numbers]


def load_input() -> List[Row]:
    condition_records = []

    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            arrangement_string, damaged_groups_string = line.split(" ", 1)
            row = Row(list(arrangement_string), [int(g) for g in damaged_groups_string.split(",")])
            condition_records.append(row)

    return condition_records


def unfold_input(condition_records: List[Row]) -> List[Row]:
    rows = []
    for row in condition_records:
        new_arrangement, new_damaged_groups = list(row.arrangement), list(row.damaged_groups)
        for _ in range(4):
            new_arrangement.extend("?")
            new_arrangement.extend(row.arrangement)
            new_damaged_groups.extend(row.damaged_groups)
        rows.append(Row(new_arrangement, new_damaged_groups))

    return rows


def part_one():
    condition_records = load_input()
    count = sum(get_possible_arrangements_count(r, defaultdict(dict)) for r in condition_records)
    print(f"The sum of possible arrangements is {count}.")


def part_two():
    condition_records = load_input()
    condition_records = unfold_input(condition_records)
    count = sum(get_possible_arrangements_count(r, defaultdict(dict)) for r in condition_records)
    print(f"The sum of possible arrangements is {count}.")


if __name__ == "__main__":
    part_one()
    part_two()
