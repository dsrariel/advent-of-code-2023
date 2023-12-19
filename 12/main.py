from dataclasses import dataclass
from typing import List

FILE_NAME = "example.txt"


@dataclass
class Row:
    arrangement: List[str]
    damaged_groups: List[int]


def get_possible_arrangements_count(row: Row) -> int:
    return 0


def load_input() -> List[Row]:
    condition_records = []

    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            arrangement_string, damaged_groups_string = line.split(" ", 1)
            row = Row(arrangement_string, [int(g) for g in damaged_groups_string.split(",")])
            condition_records.append(row)

    return condition_records


def unfold_input(condition_records: List[Row]) -> List[Row]:
    rows = []
    for row in condition_records:
        new_arrangement, new_damaged_groups = [row.arrangement], list(row.damaged_groups)
        for _ in range(4):
            new_arrangement.append("?")
            new_arrangement.append(row.arrangement)
            new_damaged_groups.extend(row.damaged_groups)
        rows.append(Row("".join(new_arrangement), new_damaged_groups))

    return rows


def part_one():
    condition_records = load_input()
    count = sum(get_possible_arrangements_count(r) for r in condition_records)
    print(f"The sum of possible arrangements is {count}.")


def part_two():
    condition_records = load_input()
    condition_records = unfold_input(condition_records)
    count = sum(get_possible_arrangements_count(r) for r in condition_records)
    print(f"The sum of possible arrangements is {count}.")


if __name__ == "__main__":
    part_one()
    part_two()
