"""--- Day 1: Sonar Sweep ---"""
from pathlib import Path

from aoc import open_utf8


def count_increases(scan: list, window: int) -> int:
    """Count the number of gradient increases in scan data for a window length.

    :param scan: List containing the numeric scan data to evaluate.
    :param window: The integer length of the window to include in the gradient sum.
    :return: Number of increases in gradient for the input data.
    """
    increases = 0
    for index in range(len(scan) - window):
        # Iterate through the window transitions and compute the sums
        if (
            sum(scan[index + 1 : index + window + 1])
            - sum(scan[index : index + window])
            > 0
        ):
            increases += 1
    return increases


def load_dataset(dataset_path: Path):
    """Processes the input file and returns a list of numeric data."""
    with open_utf8(dataset_path) as file:
        return [int(line.rstrip()) for line in file]
