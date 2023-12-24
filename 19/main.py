from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from operator import lt, gt
from typing import Callable


FILE_NAME = "input.txt"


@dataclass
class Rule:
    category: str
    operator: Callable
    threshold: int
    output: str

    def evaluate(self, part: dict) -> bool:
        if self.category == "d":
            return True

        return self.operator(part[self.category], self.threshold)


def get_rules(rule_str: str) -> list[Rule]:
    rules = []

    rules_str = rule_str.split(",")
    for rule in rules_str[:-1]:
        category = rule[0]
        operator = gt if rule[1] == ">" else lt
        threshold_str, output = rule[2:].split(":", 1)
        rules.append(Rule(category, operator, int(threshold_str), output))

    rules.append(Rule("d", gt, 0, rules_str[-1]))

    return rules


def load_input() -> (dict[str, list[Rule]], list[dict[str, int]]):
    workflows, parts = {}, []
    decode_parts = False
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            line = line.rstrip()
            if not line:
                decode_parts = True
                continue

            if not decode_parts:
                workflow_name, rules = line.split("{", 1)
                workflows[workflow_name] = get_rules(rules.rstrip("}"))
                continue

            categories = line.rstrip()[1:-1].split(",")
            part = {c[0]: int(c[2:]) for c in categories}
            parts.append(part)

    return workflows, parts


def process_part(workflows: dict[str, list[Rule]], part: dict) -> str:
    workflow = "in"
    while workflow not in {"A", "R"}:
        for rule in workflows[workflow]:
            if rule.evaluate(part):
                workflow = rule.output
                break

    return workflow


def part_one():
    workflows, parts = load_input()
    accepted_rating_sum = 0
    for part in parts:
        output = process_part(workflows, part)
        if output == "A":
            accepted_rating_sum += sum(part[c] for c in "xmas")

    print(f"The accepted rating sum is {accepted_rating_sum}.")


def get_destination_to_sources_counts(workflows: dict[str, list[Rule]]) -> dict[dict[int]]:
    destination_to_sources_counts = defaultdict(dict)
    for workflow, rules in workflows.items():
        for rule in rules:
            destination_to_sources_counts[rule.output][workflow] = (
                destination_to_sources_counts[rule.output].get(workflow, 0) + 1
            )

    return destination_to_sources_counts


def get_acceptance_paths(destination_to_sources_counts: dict[dict[int]]) -> list[list[str]]:
    acceptance_paths = []
    incomplete_paths = deque([["A"]])
    while incomplete_paths:
        incomplete_path = incomplete_paths.popleft()
        last_node_sources = destination_to_sources_counts[incomplete_path[-1]].keys()
        for source in last_node_sources:
            new_path = incomplete_path + [source]
            if source == "in":
                acceptance_paths.append(new_path)
            else:
                incomplete_paths.append(new_path)

    return acceptance_paths


def merge_boundary(boundary: dict[str, list[int]], rule: Rule, union=True):
    if rule.category == "d":
        return

    threshold = rule.threshold
    if not union:
        threshold += 1 if rule.operator is gt else -1

    if rule.operator is lt and union or rule.operator is gt and not union:
        boundary[rule.category][1] = min(threshold, boundary[rule.category][1])
        return

    boundary[rule.category][0] = max(threshold, boundary[rule.category][0])


def get_acceptance_path_boundaries(
    workflows: dict[str, list[Rule]],
    destination_to_sources_counts: dict[dict[int]],
    acceptance_path: list[str],
) -> list[dict]:
    boundaries = []
    boundary = {c: [0, 4_001] for c in "xmas"}
    for i in range(len(acceptance_path) - 1, 0, -1):
        source, destination = acceptance_path[i], acceptance_path[i - 1]
        for rule in workflows[source]:
            if destination != "A":
                merge_boundary(boundary, rule, rule.output == destination)
                if rule.output == destination:
                    break
                continue

            if rule.output == "A":
                boundary_copy = deepcopy(boundary)
                merge_boundary(boundary_copy, rule, True)
                boundaries.append(boundary_copy)

            # The only destinations that appear more than once in the same source are A and R.
            is_last_boundary = len(boundaries) == destination_to_sources_counts["A"][source]
            if is_last_boundary:
                break

            merge_boundary(boundary, rule, False)

    return boundaries


def count_possibilities(boundaries: list[dict]) -> int:
    possibilities_sum = 0
    for boundary in boundaries:
        possibilities = 1
        for limits in boundary.values():
            possibilities *= limits[1] - limits[0] - 1
        possibilities_sum += possibilities

    return possibilities_sum


def part_two():
    workflows, _ = load_input()
    destination_to_sources_counts = get_destination_to_sources_counts(workflows)
    acceptance_paths = get_acceptance_paths(destination_to_sources_counts)

    accepted_boundaries = []
    for acceptance_path in acceptance_paths:
        accepted_boundaries.extend(
            get_acceptance_path_boundaries(
                workflows, destination_to_sources_counts, acceptance_path
            )
        )

    possibilities_count = count_possibilities(accepted_boundaries)

    print(f"The number of accepted combinations of the Elves' workflows is {possibilities_count}.")


if __name__ == "__main__":
    part_one()
    part_two()
