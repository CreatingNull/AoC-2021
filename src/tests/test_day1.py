"""Test cases for day 1."""
from pathlib import Path

import pytest
from aoc import DatasetType
from aoc import load_dataset
from aoc import log
from aoc import ROOT_PATH
from day1 import count_increases


@pytest.mark.parametrize(
    "dataset_path,window,result",
    [
        [Path("day1/data/small.txt"), 1, 7],
        [Path("day1/data/large.txt"), 1, 1752],
        [Path("day1/data/small.txt"), 3, 5],
        [Path("day1/data/large.txt"), 3, 1781],
    ],
)
def test_day(dataset_path, window, result):
    """Test case for verifying the results of day 1."""
    small_data = load_dataset(
        DatasetType.ROW_LIST_NUMERIC, ROOT_PATH.joinpath(dataset_path)
    )
    log.debug("Loaded dataset of length %s", len(small_data))
    increases = count_increases(scan=small_data, window=window)
    log.info(
        "Found %d increases in %s dataset scan with window %d.",
        increases,
        dataset_path.name,
        window,
    )
    assert increases == result
