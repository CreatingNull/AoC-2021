"""Test cases for day 2."""
from pathlib import Path

import pytest
from aoc import DatasetType
from aoc import load_dataset
from aoc import log
from aoc import ROOT_PATH
from day2 import compute_xy_product


@pytest.mark.parametrize(
    "dataset_path,aimed,result",
    [
        [Path("day2/data/data-small.txt"), False, 150],
        [Path("day2/data/data-large.txt"), False, 2027977],
        [Path("day2/data/data-small.txt"), True, 900],
        [Path("day2/data/data-large.txt"), True, 1903644897],
    ],
)
def test_day(dataset_path, aimed, result):
    """Test case for verifying the results of day 2."""
    data_set = load_dataset(DatasetType.SPACE_DELIM, ROOT_PATH.joinpath(dataset_path))
    log.info("Loaded %s data with %d instructions", dataset_path.name, len(data_set))
    assert result == compute_xy_product(data_set, aimed)
