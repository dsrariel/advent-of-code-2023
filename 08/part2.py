from collections import deque
from typing import Deque, Dict, List

from part1 import get_direction_index

FILE_NAME = "input.txt"


def load_input() -> (Deque[str], Deque[str], Dict[str, List[str]]):
    source_nodes = deque()
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
                if source.endswith("A"):
                    source_nodes.append(source)

    return source_nodes, directions, source_to_destinations


def main():
    source_nodes, directions, source_to_destination = load_input()
    has_finished, steps = False, 0
    while not has_finished:
        has_finished = True
        direction_index = get_direction_index(directions)
        for _ in range(len(source_nodes)):
            current_node = source_nodes.popleft()
            next_node = source_to_destination[current_node][direction_index]
            if not next_node.endswith("Z"):
                has_finished = False

            source_nodes.append(next_node)

        steps += 1

    print(f"{steps} steps required to be only on nodes that end with Z.")


if __name__ == "__main__":
    main()
