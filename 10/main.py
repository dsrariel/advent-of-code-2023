from collections import deque
from typing import List, Tuple

FILE_NAME = "input.txt"

TILE_TO_DIRECTIONS = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    ".": [],
    "S": [[1, 0], [0, 1], [-1, 0], [0, -1]],
}


def load_input() -> (Tuple[int, int], List[str]):
    start_position = None
    grid = []
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            line = line.rstrip()
            grid.append(line.rstrip())
            for i, c in enumerate(line):
                if c == "S":
                    start_position = (len(grid) - 1, i)

    return start_position, grid


def is_within_range(tile: Tuple[int, int], x: int, y: int) -> bool:
    return tile[0] >= 0 and tile[0] < x and tile[1] >= 0 and tile[1] < y


def get_next_tiles(
    tile: Tuple[int, int], grid: List[str], visited: List[List[int]]
) -> List[Tuple[int, int]]:
    next_tiles = []

    tile_letter = grid[tile[0]][tile[1]]
    if tile_letter == "S":
        return _get_tiles_connected_to_start(tile, grid)

    directions = TILE_TO_DIRECTIONS[tile_letter]
    for direction in directions:
        next_tile = (tile[0] + direction[0], tile[1] + direction[1])
        if not is_within_range(next_tile, len(visited), len(visited[1])):
            continue

        if visited[next_tile[0]][next_tile[1]]:
            continue

        next_tiles.append(next_tile)

    return next_tiles


def _get_tiles_connected_to_start(start: Tuple[int, int], grid: List[str]) -> List[Tuple[int, int]]:
    next_tiles = []
    directions = TILE_TO_DIRECTIONS["S"]

    for direction in directions:
        next_tile = (start[0] + direction[0], start[1] + direction[1])
        if not is_within_range(next_tile, len(grid), len(grid[1])):
            continue

        next_tile_letter = grid[next_tile[0]][next_tile[1]]
        if [-direction[0], -direction[1]] in TILE_TO_DIRECTIONS[next_tile_letter]:
            next_tiles.append(next_tile)

    return next_tiles


def main():
    initial_position, tiles_grid = load_input()
    visited = [[0] * len(tiles_grid[0]) for _ in range(len(tiles_grid))]

    step = 0
    tiles_to_visit = deque([initial_position])
    while tiles_to_visit:
        for _ in range(len(tiles_to_visit)):
            tile = tiles_to_visit.popleft()
            visited[tile[0]][tile[1]] = 1
            next_tiles = get_next_tiles(tile, tiles_grid, visited)
            tiles_to_visit.extend(next_tiles)
        step += 1

    print(
        f"It takes {step - 1} steps along the loop to get to the point farthest from"
        + " the starting position."
    )


if __name__ == "__main__":
    main()
