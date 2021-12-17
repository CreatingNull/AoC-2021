"""Test cases for day 16."""
from logging import DEBUG
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day16 import load_dataset
from day16 import Packet


log.setLevel(DEBUG)


@pytest.mark.parametrize(
    "dataset_path,version_sum_limit,equation_limit",
    [
        [Path("day16/data/data-small.txt"), 20, 1],
        [Path("day16/data/data-large.txt"), 955, 158135423448],
    ],
)
def test_day(dataset_path: Path, version_sum_limit, equation_limit):
    """Test case for verifying the results of day 16."""
    binary_data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 16 dataset %s with %d bits",
        dataset_path.name,
        len(binary_data),
    )
    version_sum, equation_result = Packet(binary_data).compute_equation()
    log.info(
        "Computed version_sum %d and final equation result %d",
        version_sum,
        equation_result,
    )
    assert version_sum == version_sum_limit
    assert equation_result == equation_limit
