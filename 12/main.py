from collections import defaultdict, namedtuple
from itertools import repeat
from multiprocessing import Pool, cpu_count
from typing import Dict, List

FILE_NAME = "example.txt"
POOL_SIZE = cpu_count() - 2

Row = namedtuple("Row", "arrangement damaged_groups")


def get_possible_arrangements_count(
    row: Row, cache: defaultdict[str, Dict[str, int]], i=0, group_size=0
) -> int:
    arrangement = "".join(row.arrangement)
    groups = "".join(map(str, row.damaged_groups))

    if cache.get(arrangement, {}).get(groups, None) is not None:
        return cache[arrangement][groups]

    if not row.damaged_groups:
        cache[arrangement][groups] = int(not any(a == "#" for a in row.arrangement))
        return cache[arrangement][groups]

    while i < len(row.arrangement):
        if row.arrangement[i] == "?":
            a = Row(row.arrangement[i:], row.damaged_groups)
            b = Row(row.arrangement[i:], row.damaged_groups)
            a.arrangement[0], b.arrangement[0] = "#", "."
            cache[arrangement][groups] = get_possible_arrangements_count(
                a, cache, 0, group_size
            ) + get_possible_arrangements_count(b, cache, 0, group_size)
            return cache[arrangement][groups]

        if row.arrangement[i] == "#":
            group_size += 1
            i += 1
            continue

        if group_size == 0:
            i += 1
            continue

        if group_size == row.damaged_groups[0]:
            cache[arrangement][groups] = get_possible_arrangements_count(
                Row(row.arrangement[i:], row.damaged_groups[1:]),
                cache,
            )
            return cache[arrangement][groups]

        cache[arrangement][groups] = 0
        return cache[arrangement][groups]

    cache[arrangement][groups] = int(
        len(row.damaged_groups) == 1 and group_size == row.damaged_groups[0]
    )
    return cache[arrangement][groups]


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
    with Pool(POOL_SIZE) as p:
        count = sum(
            p.starmap(
                get_possible_arrangements_count, zip(condition_records, repeat(defaultdict(dict)))
            )
        )
    print(f"The sum of possible arrangements is {count}.")


if __name__ == "__main__":
    part_one()
    part_two()
