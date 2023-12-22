FILE_NAME = "input.txt"


def load_input() -> list[list[str]]:
    with open(FILE_NAME, encoding="utf-8") as f:
        return [list(line.rstrip()) for line in f.readlines()]


def tilt_vertical(dish: list[list[str]], north: bool):
    x, y = len(dish), len(dish[0])

    if north:
        step, initial_rock_index, x_range = 1, 0, range(0, x, 1)
    else:
        step, initial_rock_index, x_range = -1, x - 1, range(x - 1, -1, -1)

    for j in range(y):
        rock_index = initial_rock_index

        for i in x_range:
            if dish[i][j] == ".":
                continue

            if dish[i][j] == "#":
                rock_index = i + step
                continue

            dish[rock_index][j], dish[i][j] = dish[i][j], dish[rock_index][j]
            rock_index += step


def tilt_horizontal(dish: list[list[str]], west: bool):
    x, y = len(dish), len(dish[0])

    if west:
        step, initial_rock_index, y_range = 1, 0, range(0, y, 1)
    else:
        step, initial_rock_index, y_range = -1, y - 1, range(y - 1, -1, -1)

    for i in range(x):
        rock_index = initial_rock_index

        for j in y_range:
            if dish[i][j] == ".":
                continue

            if dish[i][j] == "#":
                rock_index = j + step
                continue

            dish[i][rock_index], dish[i][j] = dish[i][j], dish[i][rock_index]
            rock_index += step


def tilt_lever_north(dish: list[list[str]]):
    tilt_vertical(dish, True)


def tilt_lever_south(dish: list[list[str]]):
    tilt_vertical(dish, False)


def tilt_lever_west(dish: list[list[str]]):
    tilt_horizontal(dish, True)


def tilt_lever_east(dish: list[list[str]]):
    tilt_horizontal(dish, False)


def cycle(dish):
    tilt_lever_north(dish)
    tilt_lever_west(dish)
    tilt_lever_south(dish)
    tilt_lever_east(dish)


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


def part_two():
    dish = load_input()
    for _ in range(1_000):
        cycle(dish)
    print(f"The total load on the north support beams is {get_load_sum(dish)}.")


if __name__ == "__main__":
    part_one()
    part_two()
