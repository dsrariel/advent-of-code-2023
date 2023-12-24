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


if __name__ == "__main__":
    part_one()
