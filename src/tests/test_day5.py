"""Test cases for day 5."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day5 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,result_hv,result_all",
    [
        [Path("day5/data/data-small.txt"), 5, 12],
        [Path("day5/data/data-large.txt"), 4655, 20500],
    ],
)
def test_day(dataset_path: Path, result_hv: int, result_all: int):
    """Test case for verifying the results of day 5."""
    data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Day 5 dataset %s loaded with %d unique points.", dataset_path.name, len(data)
    )
    count_hv = 0  # Record horizontal and vertical overlapped points
    count_all = 0  # Record all overlapped points
    for _, point in data.items():
        if point.value_hv > 1:
            count_hv += 1
        if point.value_hv + point.value_d > 1:
            count_all += 1
    log.info(
        "Found %s horizontal and vertical overlaps, and %d overall overlaps.",
        count_hv,
        count_all,
    )
    assert count_hv == result_hv
    assert count_all == result_all
