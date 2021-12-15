"""--- Day 14: Extended Polymerization ---"""
from pathlib import Path

from aoc import open_utf8

# Still have to figure out a solution to part 2.
# Not going to spend time linting until I have a design.
# pylint: disable=C0116,R0913


def polymerisation(template: str, rules: {}, steps: int, frequency: {}) -> {}:
    for char in template:
        frequency[char] += 1
    for char_index in range(1, len(template)):
        __find_polymer(
            template[char_index - 1], template[char_index], 0, steps, rules, frequency
        )
    return sorted(
        frequency.items(), key=lambda x: x[1], reverse=True
    )  # sort by desc value


def __find_polymer(
    element_a: str, element_b: str, depth: int, limit: int, rules: {}, frequency: {}
):
    # Computes the next element and adds it to frequency then  recuses on self and a / b
    if depth < limit:
        new_char = rules[element_a + element_b]
        frequency[new_char] += 1
        __find_polymer(element_a, new_char, depth + 1, limit, rules, frequency)
        __find_polymer(new_char, element_b, depth + 1, limit, rules, frequency)


def load_dataset(dataset_path: Path) -> (str, {}, {}):
    loading_rules = False  # Trigger to start loading rules
    template = ""
    rules = {}
    with open_utf8(dataset_path) as file:
        for line in file:
            if not loading_rules:
                template = line.strip()
                loading_rules = True
            elif len(line.strip()) > 0:
                rule_split = line.strip().split(" -> ")
                rules[rule_split[0]] = rule_split[1]
    frequency = {char: 0 for char in rules.values()}
    return template, rules, frequency


def compute_polymer_length(num_initial: int, steps: int) -> int:
    accumulate = num_initial
    for _ in range(steps):
        accumulate += accumulate - 1
    return accumulate
