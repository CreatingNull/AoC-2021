"""--- Day 13: Transparent Origami ---"""
from dataclasses import dataclass
from pathlib import Path

from numpy import array
from numpy import bitwise_or
from numpy import byte
from numpy import flip
from numpy import sum as sum_
from numpy import zeros

from aoc import open_utf8


@dataclass
class Fold:
    """Class containing information on an origami fold action."""

    x: int  # set > 0 when a fold is occurring for an index on this axis.
    y: int


def __fold_grid(grid: array, fold: Fold) -> array:
    """Folds the paper in around the axis and index in Fold.

    :param grid: Numpy array showing current view of the transparent sheet.
    :param fold: The fold action to complete on the grid.
    :return: The folded numpy grid.
    """
    if fold.y > 0:  # Fold horizontal
        top = grid[0 : fold.y]
        bot = flip(grid[fold.y + 1 :], axis=0)
        return bitwise_or(bot, top)
    left = grid[:, 0 : fold.x]  # Fold vertical
    right = flip(grid[:, fold.x + 1 :], axis=1)
    grid = bitwise_or(left, right)
    return grid


def do_origami(grid: array, folds: [Fold]) -> (int, array):
    """Executes all the folds on the input numpy grid.

    :param grid: Numpy array representing the transparent sheet.
    :param folds: List of fold actions to complete on the input data.
    :return: (number of dots after the first fold, the final numpy grid).
    """
    first_fold = -1  # Tracks the dots visible on the first fold
    for fold in folds:
        grid = __fold_grid(grid, fold)
        if first_fold == -1:
            first_fold = sum_(grid)
    return first_fold, grid


def load_dataset(dataset_path: Path) -> (array, [Fold]):
    """Loads the input data grid and fold actions from file."""
    points = [[], []]  # store the [x] and [y] values of input points
    folds = []
    with open_utf8(dataset_path) as file:
        fold_trigger = False
        for index, line in enumerate(file):
            if len(line.strip()) == 0:  # start loading fold actions.
                fold_trigger = True
            elif not fold_trigger:  # load grid positions.
                points[0].append(int(line.strip().split(",")[0]))
                points[1].append(int(line.strip().split(",")[1]))
            else:  # Load fold actions
                axis, value = line.split("along ")[1].strip().split("=")
                folds.append(
                    Fold(
                        -1 if axis == "y" else int(value),
                        -1 if axis == "x" else int(value),
                    )
                )
    # Create an array of the right dimensions and populate our true bits.
    grid = zeros((max(points[1]) + 1, max(points[0]) + 1), dtype=byte)
    for index in range(len(points[0])):
        grid[points[1][index], points[0][index]] = 1
    return grid, folds
