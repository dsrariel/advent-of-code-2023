from collections import defaultdict, deque
from enum import Enum, auto

FILE_NAME = "input.txt"


class Direction(Enum):
    UP = auto()
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()

    def get_next_position(self, position: tuple[int, int]) -> tuple[int, int]:
        if self is Direction.UP:
            return (position[0] - 1, position[1])
        if self is Direction.LEFT:
            return (position[0], position[1] - 1)
        if self is Direction.DOWN:
            return (position[0] + 1, position[1])
        if self is Direction.RIGHT:
            return (position[0], position[1] + 1)

        return None


class Beam:
    TILE_TO_DIRECTION_CHANGE = {
        "\\": {
            Direction.RIGHT: [Direction.DOWN],
            Direction.UP: [Direction.LEFT],
            Direction.DOWN: [Direction.RIGHT],
            Direction.LEFT: [Direction.UP],
        },
        "/": {
            Direction.RIGHT: [Direction.UP],
            Direction.UP: [Direction.RIGHT],
            Direction.DOWN: [Direction.LEFT],
            Direction.LEFT: [Direction.DOWN],
        },
        "-": {
            Direction.UP: [Direction.LEFT, Direction.RIGHT],
            Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
        },
        "|": {
            Direction.RIGHT: [Direction.UP, Direction.DOWN],
            Direction.LEFT: [Direction.UP, Direction.DOWN],
        },
    }
    VISITED_TILES = defaultdict(set)

    def __init__(
        self,
        position: tuple[int, int],
        direction: Direction = Direction.RIGHT,
    ):
        self.position = position
        self.direction = direction

    def move(self, grid: list[str]):
        beams = []

        self.VISITED_TILES[self.position].add(self.direction)

        tile = grid[self.position[0]][self.position[1]]
        next_directions = self.TILE_TO_DIRECTION_CHANGE.get(tile, {}).get(
            self.direction, [self.direction]
        )
        for direction in next_directions:
            position = direction.get_next_position(self.position)
            if (
                position[0] < 0
                or position[0] >= len(grid)
                or position[1] < 0
                or position[1] >= len(grid[0])
            ):
                continue

            if direction in self.VISITED_TILES.get(position, {}):
                continue

            beams.append(Beam(position, direction))

        return beams


def load_input() -> list[str]:
    with open(FILE_NAME, encoding="utf-8") as f:
        return [line.rstrip() for line in f.readlines()]


def get_energized_tiles(grid: list[str], start_beam: Beam) -> int:
    Beam.VISITED_TILES = defaultdict(set)
    beams = deque([start_beam])
    while beams:
        beam = beams.popleft()
        next_beams = beam.move(grid)
        for beam in next_beams:
            beams.appendleft(beam)

    return len(Beam.VISITED_TILES)


def part_one():
    grid = load_input()
    start = Beam((0, 0))
    print(f"The number of energized tiles is {get_energized_tiles(grid, start)}.")


def part_two():
    grid = load_input()
    x, y = len(grid), len(grid[0])
    max_energized_tiles = 0
    for i, direction in [(0, Direction.DOWN), (x - 1, Direction.UP)]:
        for j in range(y):
            beam = Beam((i, j), direction)
            max_energized_tiles = max(max_energized_tiles, get_energized_tiles(grid, beam))

    for i in range(x):
        for j, direction in [(0, Direction.RIGHT), (y - 1, Direction.LEFT)]:
            beam = Beam((i, j), direction)
            max_energized_tiles = max(max_energized_tiles, get_energized_tiles(grid, beam))

    print(f"The number of energized tiles is {max_energized_tiles}.")


if __name__ == "__main__":
    part_one()
    part_two()
