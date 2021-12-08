"""--- Day 6: Lanternfish ---"""
from pathlib import Path

from aoc import open_utf8


def simulate_population(fish: {}, days: int) -> {}:
    """Step through the days adding additional '8' keyed fish from the '0'
    keyed parents.

    :param fish: Dictionary containing day counter keys to number of fish values.
    :param days: Number of days to simulate.
    :return: Dictionary containing the updated state of the fish.
    """
    for _ in range(days):
        daily_fish = fish[0]
        for index in range(0, 8):
            if index in fish:  # shift the fish 8 -> 1 down
                fish[index] = fish[index + 1]
        fish[8] = daily_fish  # add new fish
        fish[6] += daily_fish  # reset parent fish
    return fish


def load_dataset(dataset_path: Path) -> {}:
    """Loads the fishy fish from file.

    :param dataset_path: Path object to load the data from.
    :return: Dictionary containing day counter keys to number of fish values.
    """
    data = {i: 0 for i in range(9)}  # The possible counter states for the fish
    with open_utf8(dataset_path) as file:
        for line in file:
            for digit in line.split(","):
                data[int(digit)] += 1
    return data
