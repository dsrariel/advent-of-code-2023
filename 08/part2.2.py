from typing import Dict, List

FILE_NAME = "input.txt"


class Path:
    def __init__(self, start_node: str):
        self.node = start_node
        self.steps = 0
        self.steps_to_end = None
        self.steps_to_end_cycle = None

    def register_end_node(self, directions: List[str]) -> None:
        if self.steps_to_end is None:
            self.steps_to_end = self.steps
            return

        if self.steps_to_end_cycle is None:
            self.steps_to_end_cycle = self.steps - self.steps_to_end

    def walk(self, directions: List[str], source_to_destination: Dict[str, List[str]]) -> None:
        direction = directions[self.steps % len(directions)]
        direction_index = 0 if direction == "L" else 1
        self.node = source_to_destination[self.node][direction_index]
        self.steps += 1


def load_input() -> (List[Path], List[str], Dict[str, List[str]]):
    paths, directions = list(), list()
    source_to_destinations = {}
    with open(FILE_NAME, encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            line = line.rstrip()

            if i == 0:
                directions = [c for c in line]
                continue

            if i > 1:
                source, destinations_string = line.split(" = ", 1)
                destinations = destinations_string[1:-1].split(", ")
                source_to_destinations[source] = destinations
                if source.endswith("A"):
                    paths.append(Path(source))

    return paths, directions, source_to_destinations


def find_path_cycles(
    paths: List[Path], directions: List[str], source_to_destination: Dict[str, List[str]]
):
    for path in paths:
        while path.steps_to_end_cycle is None:
            if path.node.endswith("Z"):
                path.register_end_node(directions)
            path.walk(directions, source_to_destination)


def get_greatest_common_divisor(a: int, b: int):
    if b == 0:
        return a

    return get_greatest_common_divisor(b, a % b)


def get_lowest_common_multiple(a: int, b: int):
    return int((a * b) / get_greatest_common_divisor(a, b))


# path.steps_to_end is equal to path.steps_to_end_cycle, so we only need to find the LCM.
def get_steps_to_end(paths: List[Path]) -> int:
    lcm = 1
    for path in paths:
        lcm = get_lowest_common_multiple(lcm, path.steps_to_end)

    return lcm


def main():
    paths, directions, source_to_destination = load_input()

    find_path_cycles(paths, directions, source_to_destination)
    for i, path in enumerate(paths):
        print(f"#{i}\t{path.steps_to_end}\t{path.steps_to_end_cycle}")

    steps_to_end = get_steps_to_end(paths)
    print(f"The number of steps to reach the end is {steps_to_end}.")


if __name__ == "__main__":
    main()
