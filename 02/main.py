from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

FILE_NAME = "input.txt"


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Game:
    BAG = {
        Color.RED: 12,
        Color.GREEN: 13,
        Color.BLUE: 14,
    }

    def __init__(self, index: int, cube_sets: List[Dict[Color, int]]) -> None:
        self.index = index
        self.cube_sets = cube_sets

    def is_possible(self) -> bool:
        for cube_set in self.cube_sets:
            for color, number in self.BAG.items():
                if cube_set.get(color, 0) > number:
                    return False
        return True


def get_cube_set(set_string: str) -> Dict[Color, int]:
    cube_count_strings = set_string.split(", ")
    cube_set = dict()
    for cube_count in cube_count_strings:
        count_and_color = cube_count.split()
        count = int(count_and_color[0])
        color = Color(count_and_color[1])
        cube_set[color] = count

    return cube_set


def get_game(line: str) -> Game:
    line = line[len("Game ") :]
    index_and_sets = line.split(": ", 1)

    index = int(index_and_sets[0])

    set_strings = index_and_sets[1].split("; ")
    cube_sets = [get_cube_set(set_string) for set_string in set_strings]

    return Game(index, cube_sets)


def part1():
    id_sum = 0
    with open(FILE_NAME) as f:
        for line in f.readlines():
            game = get_game(line)
            if game.is_possible():
                id_sum += game.index

    print(f"The sum of the IDs of the possible games is {id_sum}")


if __name__ == "__main__":
    part1()
