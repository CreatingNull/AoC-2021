"""Test cases for day 9."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day9 import find_low_points
from day9 import load_dataset
from day9 import size_basins


@pytest.mark.parametrize(
    "dataset_path,num_lows,low_point_result,basin_result",
    [
        [Path("day9/data/data-small.txt"), 4, 15, 1134],
        [Path("day9/data/data-large.txt"), 224, 514, 1103130],
    ],
)
def test_day(
    dataset_path: Path, num_lows: int, low_point_result: int, basin_result: int
):
    """Test case for verifying the results of day 9."""
    data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded dataset for day 9 %s with %s array shape",
        dataset_path.name,
        data.shape,
    )
    low_points, risk_sum = find_low_points(data)
    basin_product = size_basins(data, low_points)
    log.info(
        "Found %s low points with risk sum %s and basin product %s.",
        len(low_points),
        risk_sum,
        basin_product,
    )
    assert len(low_points) == num_lows
    assert risk_sum == low_point_result
    assert basin_product == basin_result
