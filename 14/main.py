FILE_NAME = "input.txt"


def load_input() -> list[list[str]]:
    with open(FILE_NAME, encoding="utf-8") as f:
        return [list(line.rstrip()) for line in f.readlines()]


def tilt_lever_north(dish: list[list[str]]):
    x, y = len(dish), len(dish[0])
    for j in range(y):
        rock_index = 0

        for i in range(x):
            if dish[i][j] == ".":
                continue

            if dish[i][j] == "#":
                rock_index = i + 1
                continue

            dish[rock_index][j], dish[i][j] = dish[i][j], dish[rock_index][j]
            rock_index += 1


def get_load_sum(dish: list[list[str]]):
    x = len(dish)
    load_sum = 0
    for i, line in enumerate(dish):
        for field in line:
            if field == "O":
                load_sum += x - i

    return load_sum


def part_one():
    dish = load_input()
    tilt_lever_north(dish)
    print(f"The total load on the north support beams is {get_load_sum(dish)}.")


if __name__ == "__main__":
    part_one()
