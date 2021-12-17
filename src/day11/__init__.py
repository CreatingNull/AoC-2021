"""--- Day 11: Dumbo Octopus ---"""
from pathlib import Path

from numpy import all as all_
from numpy import array
from numpy import byte
from numpy import where

from aoc import open_utf8


def __execute_step(data: array, bounds: [[]]) -> int:
    """Recursive function to simulate a single step in time for the input
    state.

    :param data: Numpy array of all octopi energy states.
    :param bounds: Limit the data to consider, [[y_lo, y_hi],[x_lo,x_hi]]
    :return: Total number of flashes occurring in the simulated time-step.
    """
    count_flashes = 0
    bounded_view = data[bounds[0][0] : bounds[0][1], bounds[1][0] : bounds[1][1]]
    # All octopi energy increase by 1, -1 only used to exclude already flashed.
    bounded_view[bounded_view != -1] = bounded_view[bounded_view != -1] + 1
    # Locate all the pending 10's for executing a flash
    flashes = where(bounded_view == 10)
    for index in range(len(flashes[0])):
        # Only flash if recursion hasn't already flashed this point.
        if bounded_view[flashes[0][index], flashes[1][index]] != -1:
            count_flashes += 1
            bounded_view[flashes[0][index], flashes[1][index]] = -1
            # Recuse pending flash on bounded array (sub-array)
            count_flashes += __execute_step(
                data,
                [  # values adjusted by origin change of bounded view
                    [
                        bounds[0][0] + flashes[0][index] - 1
                        if bounds[0][0] + flashes[0][index] > 0
                        else bounds[0][0] + flashes[0][index],
                        bounds[0][0] + flashes[0][index] + 2
                        if bounds[0][0] + flashes[0][index] < data.shape[1]
                        else bounds[0][0] + flashes[0][index] + 1,
                    ],
                    [
                        bounds[1][0] + flashes[1][index] - 1
                        if bounds[1][0] + flashes[1][index] > 0
                        else bounds[1][0] + flashes[1][index],
                        bounds[1][0] + flashes[1][index] + 2
                        if bounds[1][0] + flashes[1][index] < data.shape[1]
                        else bounds[1][0] + flashes[1][index] + 1,
                    ],
                ],
            )
    return count_flashes


def execute_steps(data: array) -> (int, int):
    """Simulates the final octopi array after num_steps and counts the flashes.

    :param data: Numpy array of octopi energy states.
    :return: The summation of flashes, the step at which all octopi flashed.
    """
    flashes = 0
    all_flashed = -1
    i = 1  # AoC counts loading data as step 0.
    while all_flashed == -1:
        new_flashes = __execute_step(data, [[0, data.shape[0]], [0, data.shape[1]]])
        data[data == -1] = 0  # reset all flashes to 0 energy
        if i <= 100:  # part one is up to 99 only
            flashes += new_flashes
        if all_(data == 0):
            all_flashed = i
        i += 1
    return flashes, all_flashed


def load_dataset(dataset_path: Path) -> array:
    """Loads in the dataset as a numpy array of signed bytes."""
    with open_utf8(dataset_path) as file:
        return array(
            [
                [byte(cell) for cell in row.strip()]
                for row in file
                if len(row.strip()) > 0
            ],
            dtype=byte,
        )
