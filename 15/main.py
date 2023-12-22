from collections import namedtuple

FILE_NAME = "input.txt"

Lens = namedtuple("Lens", "label operation focal_length")


def load_input() -> list[str]:
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            return line.split(",")


def get_lens(operations: list[str]) -> list[Lens]:
    lens = []
    for operation in operations:
        if operation[-2] == "=":
            lens.append(Lens(operation[:-2], operation[-2], int(operation[-1])))
            continue
        lens.append(Lens(operation[:-1], operation[-1], ""))

    return lens


def hashing(string: str) -> int:
    result = 0
    for c in string:
        result += ord(c)
        result *= 17
        result %= 256

    return result


def insert_lens(hash_map: list[list[Lens]], lens: Lens):
    box_number = hashing(lens.label)
    box = hash_map[box_number]

    for i, item in enumerate(box):
        if item.label == lens.label:
            box[i] = lens
            return

    box.append(lens)


def remove_lens(hash_map: list[list[Lens]], lens: Lens):
    box_number = hashing(lens.label)
    box = hash_map[box_number]

    for i, item in enumerate(box):
        if item.label == lens.label:
            del box[i]
            return


def get_sum_of_focus_power(boxes: list[list[Lens]]) -> int:
    focus_power = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focus_power += (i + 1) * (j + 1) * lens.focal_length

    return focus_power


def part_one():
    sequences = load_input()
    print(f"The sum of the hashes is {sum(map(hashing, sequences))}.")


def part_two():
    hash_map = [[] for _ in range(256)]

    sequences = load_input()
    steps = get_lens(sequences)
    for lens in steps:
        if lens.operation == "=":
            insert_lens(hash_map, lens)
            continue

        remove_lens(hash_map, lens)

    print(f"The sum of the focus powers is {get_sum_of_focus_power(hash_map)}.")


if __name__ == "__main__":
    part_one()
    part_two()
