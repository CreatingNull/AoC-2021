"""Test cases for day 18."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day18 import add_all_numbers
from day18 import find_greatest_magnitude
from day18 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,mag_all_limit,mag_max_limit",
    [
        [Path("day18/data/data-small.txt"), 4140, 3993],
        [Path("day18/data/data-large.txt"), 2501, 4935],
    ],
)
def test_day(dataset_path: Path, mag_all_limit: int, mag_max_limit: int):
    """Test case for verifying the results of day 18."""
    numbers = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 18 dataset %s with numbers to add",
        dataset_path.name,
    )
    mag_max = find_greatest_magnitude(numbers)
    mag_all = add_all_numbers(numbers)
    log.info(
        "Final magnitude summing all numbers = %s and the highest summing 2 = %d",
        mag_all,
        mag_max,
    )
    assert mag_all == mag_all_limit
    assert mag_max == mag_max_limit
