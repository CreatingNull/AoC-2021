"""Test cases for day 11."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day11 import execute_steps
from day11 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,flash_limit,all_limit",
    [
        [Path("day11/data/data-small.txt"), 1656, 195],
        # `data large` is the same size here :(
        [Path("day11/data/data-large.txt"), 1669, 351],
    ],
)
def test_day(dataset_path: Path, flash_limit, all_limit):
    """Test case for verifying the results of day 11."""
    data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 11 dataset %s with array shape %s",
        dataset_path.name,
        data.shape,
    )
    flash_result, all_flashed = execute_steps(data)
    log.info(
        "After 100 time-steps %d flashes occurred, all octopi flashed at %d.",
        flash_result,
        all_flashed,
    )
    assert flash_result == flash_limit
    assert all_flashed == all_limit
