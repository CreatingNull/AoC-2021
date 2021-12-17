"""Test cases for day 4."""
from pathlib import Path

import pytest

from aoc import ROOT_PATH
from day4 import Bingo


@pytest.mark.parametrize(
    "dataset_path,result_first,result_second",
    [
        [Path("day4/data/data-small.txt"), 4512, 1924],
        [Path("day4/data/data-large.txt"), 49686, 26878],
    ],
)
def test_day(dataset_path: Path, result_first: int, result_second: int):
    """Test cases fpr verifying the results for day 4."""
    data = Bingo(ROOT_PATH.joinpath(dataset_path))
    assert data.result_products[0] == result_first
    assert data.result_products[1] == result_second
