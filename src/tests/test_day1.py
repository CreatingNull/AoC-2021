"""Test cases for day 1."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day1 import count_increases
from day1 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,window,result",
    [
        [Path("day1/data/small.txt"), 1, 7],
        [Path("day1/data/large.txt"), 1, 1752],
        [Path("day1/data/small.txt"), 3, 5],
        [Path("day1/data/large.txt"), 3, 1781],
    ],
)
def test_day(dataset_path: Path, window: int, result: int):
    """Test case for verifying the results of day 1."""
    small_data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.debug("Loaded %s dataset of length %s", dataset_path.name, len(small_data))
    increases = count_increases(scan=small_data, window=window)
    log.info(
        "Found %d increases in %s dataset scan with window %d.",
        increases,
        dataset_path.name,
        window,
    )
    assert increases == result
