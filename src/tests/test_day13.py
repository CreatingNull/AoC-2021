"""Test cases for day 13."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day13 import do_origami
from day13 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,first_fold_limit,string_limit",
    [
        [
            Path("day13/data/data-small.txt"),
            17,
            [
                "OOOOO",
                "O...O",
                "O...O",
                "O...O",
                "OOOOO",
                ".....",
                ".....",
            ],
        ],
        [
            Path("day13/data/data-large.txt"),
            765,
            [
                "OOO..OOOO.O..O.OOOO.O....OOO...OO..O..O.",
                "O..O....O.O.O.....O.O....O..O.O..O.O..O.",
                "O..O...O..OO.....O..O....O..O.O....OOOO.",
                "OOO...O...O.O...O...O....OOO..O.OO.O..O.",
                "O.O..O....O.O..O....O....O....O..O.O..O.",
                "O..O.OOOO.O..O.OOOO.OOOO.O.....OOO.O..O.",
            ],
        ],
    ],
)
def test_day(dataset_path: Path, first_fold_limit: int, string_limit: [str]):
    """Test case for verifying the results of day 13."""
    grid, folds = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 13 dataset %s with %s grid and %d fold actions",
        dataset_path.name,
        grid.shape,
        len(folds),
    )
    first_fold, grid = do_origami(grid, folds)
    log.info("After the first fold there are %d dots showing.", first_fold)
    result_string = []
    for row in grid:
        result_string.append("".join("O" if element == 1 else "." for element in row))
    assert first_fold == first_fold_limit
    assert len(result_string) == len(string_limit)
    for index, row in enumerate(result_string):
        log.info(row)
        assert row == string_limit[index]
