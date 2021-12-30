"""--- Day 25: Sea Cucumber ---"""
from pathlib import Path

from numpy import array
from numpy import byte
from numpy import roll
from numpy import sum as sum_

from aoc import open_utf8


# Used to quickly map dataset values to integer representations and vice versa
CHAR_MAP = {".": 0, ">": 1, "v": 2}


def __make_moves(cu_map: array, east: bool = True):
    """Function shifts all the cucumbers in one dimension, and recurses if
    east.

    :param cu_map: Numpy array of the current position of all the sea-cucumbers.
    :param east: Boolean used for recusing on south direction.
    :return: Integer counting the number of total movements made during the call.
    """
    cu_heard = CHAR_MAP[">"] if east else CHAR_MAP["v"]
    cu_movements = roll(  # isolate cucumber of directional heard only
        (cu_map == cu_heard),
        axis=(1 if east else 0),  # shift by 1 row or column based on direction
        shift=1,
    ) & ~(
        cu_map != CHAR_MAP["."]
    )  # check no collision on movement
    # move the unblocked sea-cucumbers
    cu_map[cu_movements] = cu_heard
    # zero old the old positions of the now moved sea-cucumbers
    cu_movements = roll(
        cu_movements, axis=(1 if east else 0), shift=-1  # roll cols or rows back one.
    )
    cu_map[cu_movements] = CHAR_MAP["."]
    movements = sum_(cu_movements)
    if east:  # recuse on the south direction
        movements += __make_moves(cu_map, False)
    return movements


def find_idle(cu_map: array) -> int:
    """Iterates through sea-floor states until no-movements are made.

    :param cu_map: Numpy array of the current position of all the sea-cucumbers.
    :return: Integer counting how many time-steps (base 1) to reach steady-state.
    """
    steps = 1  # Record the number of steps taken
    while __make_moves(cu_map) != 0:
        steps += 1
    return steps


def load_dataset(dataset_path: Path):
    """Returns a numpy array describing the sea-floor dataset."""
    with open_utf8(dataset_path) as file:
        return array(
            [
                [CHAR_MAP[char] for char in line.strip()]
                for line in file
                if len(line.strip()) > 0
            ],
            dtype=byte,
        )
