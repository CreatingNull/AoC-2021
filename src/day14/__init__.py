"""--- Day 14: Extended Polymerization ---"""
from pathlib import Path

from aoc import open_utf8


def polymerisation(rules: {}, steps: int, frequency: {}) -> ():
    """Iterates through the time-steps and computes state based on pair
    translation.

    :param rules: Dictionary of the pairs mapping to new char.
    :param steps: Number of steps to execute over.
    :param frequency: Enumerated pairs and how many times they occur.
    :return: Ordered tuple of dict item tuples, in descending order.
    """
    for _ in range(steps):
        frequency_future = {key: 0 for key in frequency}
        for pair in frequency:
            if frequency[pair] != 0:  # each pair maps to 2 future pairs
                frequency_future[pair[0] + rules[pair]] += frequency[pair]
                frequency_future[rules[pair] + pair[-1]] += frequency[pair]
        frequency = frequency_future
    return sorted(count_chars(frequency).items(), key=lambda x: x[1], reverse=True)


def count_chars(frequency: {}) -> {}:
    """Converts a dictionary of pair occurrences to char occurrences.

    :param frequency: Dictionary of pair types to number of occurrences.
    :return: Dictionary of char values to number of occurrences.
    """
    char_frequency = {}
    for pair in frequency:
        for char in pair:  # char in pair
            if char in char_frequency:
                char_frequency[char] += frequency[pair]
            else:
                char_frequency[char] = frequency[pair]
    # most pairs are con-joined so take the ceil of half the value.
    return {char: -(value // -2) for char, value in char_frequency.items()}


def load_dataset(dataset_path: Path) -> ({}, {}):
    """Loads the template and rules from file."""
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
    frequency = {pair: 0 for pair in rules}
    for pair_index in range(1, len(template)):  # Add the template to frequency
        frequency[template[pair_index - 1 : pair_index + 1]] += 1
    return rules, frequency
