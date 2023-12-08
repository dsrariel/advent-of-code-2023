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
    seen_nodes_per_source = [{} for _ in range(len(source_nodes))]
    z_nodes_per_source = [set() for _ in range(len(source_nodes))]
    has_finished_per_source = [False] * len(source_nodes)
    steps = 0
    while sum([bool(hf) for hf in has_finished_per_source]) != len(source_nodes):
        direction_index = get_direction_index(directions)
        for i in range(len(source_nodes)):
            current_node = source_nodes.popleft()

            if current_node in seen_nodes_per_source[i]:
                is_cycle = (steps - seen_nodes_per_source[i][current_node]) % len(directions) == 0
                if is_cycle:
                    has_finished_per_source[i] = True
            else:
                seen_nodes_per_source[i][current_node] = steps

            next_node = source_to_destination[current_node][direction_index]
            if next_node.endswith("Z"):
                z_nodes_per_source[i].add(next_node)

            source_nodes.append(next_node)

        steps += 1

    for i, z_nodes in enumerate(z_nodes_per_source):
        print(f"#{i}: {z_nodes}.")


if __name__ == "__main__":
    main()
