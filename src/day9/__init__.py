"""--- Day 9: Smoke Basin ---"""
from dataclasses import dataclass
from pathlib import Path

from numpy import array
from numpy import byte
from numpy import product
from numpy import sort

from aoc import log
from aoc import open_utf8


@dataclass
class Location:
    """Class to store a checked x,y location and it's inspected type."""

    row: int
    col: int
    type: int = 0  # 0 - Nothing, 1 - Low Point, 2 - Basin Node.

    def __hash__(self):
        """Over-ride the hash to be dependant on row and col only."""
        return hash((self.row, self.col))

    def __eq__(self, other):
        """Define object equality to be dependant on hash only."""
        return self.__hash__() == other.__hash__()


def find_low_points(data: array) -> (set, int):
    """Sweeps the array and finds the low points.

    :param data: Numpy array of the input data.
    :return: (A set of the low points Locations found, integer sum of the risk)
    """
    low_points = set()
    risk_sum = 0
    for row_index, _ in enumerate(data):
        for column_index, cell_value in enumerate(data[row_index]):
            if cell_value != 9:  # 9 cant be a low point
                if __check_point_low(data, row_index, column_index):
                    low_points.add(Location(row_index, column_index, 1))
                    risk_sum += cell_value + 1
    return low_points, risk_sum


def __check_point_low(data: array, row_index, column_index) -> bool:
    """Checks if the point has all higher surrounding points.

    :param data: Numpy array of the input data.
    :param row_index: Integer row index for the point to evaluate.
    :param column_index: Integer column index for the point to evaluate.
    :return: Boolean true if the point is low.
    """
    cell_value = data[row_index][column_index]
    left = cell_value < data[row_index][column_index - 1] if column_index > 0 else True
    right = (
        cell_value < data[row_index][column_index + 1]
        if column_index < data.shape[1] - 1
        else True
    )
    up = cell_value < data[row_index - 1][column_index] if row_index > 0 else True
    down = (
        cell_value < data[row_index + 1][column_index]
        if row_index < data.shape[0] - 1
        else True
    )
    return all((left, right, up, down))


def size_basins(data: array, low_points: {}):
    """Starts at the low-point and computes the size of the surrounding basins.

    :param data: Numpy 2d array of floor height.
    :param low_points: List of (x,y) locations for the low points in data.
    :return: The product of basin sizes.
    """
    # For low point
    basins = []
    for low_point in low_points:
        searched = {low_point}
        # Recurse quadrants
        recurse_quadrant(data, low_point, searched)
        basin = {location for location in searched if location.type > 0}
        log.debug(
            "Found %d basin locations in a search space of %d starting at low-point %s",
            len(basin),
            len(searched),
            low_point,
        )
        basins.append(len(basin))
    return product(sort(basins)[-3:])


def recurse_quadrant(data: array, low_point: [], searched: {}):
    """Takes a low point and recursively evaluates the type of adjacent points.

    :param data: Numpy array of floor height.
    :param low_point: The Location object for the node being evaluated.
    :param searched: The set of Location objects already evaluated.
    :return: Inplace update on searched data.
    """
    # go left if columns available
    right = Location(low_point.row, low_point.col + 1)
    if right.col < data.shape[1] and right not in searched:
        searched.add(right)
        if data[right.row][right.col] != 9:
            right.type = 2
            recurse_quadrant(data, right, searched)
    # go left if columns available
    left = Location(low_point.row, low_point.col - 1)
    if left.col >= 0 and left not in searched:
        searched.add(left)
        if data[left.row][left.col] != 9:
            left.type = 2
            recurse_quadrant(data, left, searched)
    # go down if rows available
    down = Location(low_point.row + 1, low_point.col)
    if down.row < data.shape[0] and down not in searched:
        searched.add(down)
        if data[down.row][down.col] != 9:
            down.type = 2
            recurse_quadrant(data, down, searched)
    # go up if rows available
    up = Location(low_point.row - 1, low_point.col)
    if up.row >= 0 and up not in searched:
        searched.add(up)
        if data[up.row][up.col] != 9:
            up.type = 2
            recurse_quadrant(data, up, searched)


def load_dataset(dataset_path: Path) -> array:
    """Loads the days data into a 2D numpy array."""
    with open_utf8(dataset_path) as file:
        return array(
            [
                [byte(digit) for digit in line.strip()]
                for line in file
                if len(line.strip()) > 0
            ],
            dtype=byte,
        )
