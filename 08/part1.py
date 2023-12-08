from collections import deque
from typing import Deque, Dict, List

FILE_NAME = "input.txt"


def load_input() -> (Deque[str], Dict[str, List[str]]):
    directions = deque()
    source_to_destinations = {}
    with open(FILE_NAME, encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            line = line.rstrip()

            if i == 0:
                directions = deque(c for c in line)
                continue

            if i > 1:
                source, destinations_string = line.split(" = ", 1)
                destinations = destinations_string[1:-1].split(", ")
                source_to_destinations[source] = destinations

    return directions, source_to_destinations


def get_direction_index(directions: Deque[str]) -> int:
    direction = directions.popleft()
    directions.append(direction)
    return 0 if direction == "L" else 1


def main():
    directions, source_to_destination = load_input()
    current_node, steps = "AAA", 0
    while current_node != "ZZZ":
        current_node = source_to_destination[current_node][get_direction_index(directions)]
        steps += 1

    print(f"{steps} steps are required to reach ZZZ.")


if __name__ == "__main__":
    main()
