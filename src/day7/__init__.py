"""--- Day 7: The Treachery of Whales ---"""
from pathlib import Path

from aoc import open_utf8


def find_minima(crabs: [int], flat_fuel_cost: bool) -> []:
    """Iterates through the range of crabs and locates the.

    :param crabs: The list of individual crab positions.
    :param flat_fuel_cost: `True` for flat fuel cost, `False` for triangular.
    :return: List containing 0 - min position, 1 - min fuel cost.
    """
    min_value = -1  # track the minimum cost of the fuel thus far
    min_index = -1  # track the index that provided that minimum
    for position in range(min(crabs), max(crabs) + 1):
        fuel = 0  # fuel consumption for horizontal location
        for crab in crabs:
            fuel += (
                abs(position - crab)
                if flat_fuel_cost
                else nth_triangular_number(abs(position - crab))
            )
        if fuel < min_value or min_value < 0:  # We found a new minima
            min_value = fuel
            min_index = position
    return min_index, min_value


def nth_triangular_number(number: int) -> int:
    """Function to compute the triangular number for a positive integer.

    :param number: The integer n to compute the triangular number.
    :return: The resulting integer triangular number.
    """
    return number * (number + 1) // 2  # I like to call this the 'addition-factorial'


def load_dataset(dataset_path: Path) -> [int]:
    """Loads the dataset from file as a list of integer crab positions.

    :param dataset_path: Path object to load the data from.
    :return: List of integers representing positions of individual crabs.
    """
    with open_utf8(dataset_path) as file:
        return [
            int(number)
            for line in file
            for number in line.split(",")
            if len(number.strip()) > 0
        ]
