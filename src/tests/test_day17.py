"""Test cases for day 17."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day17 import load_dataset
from day17 import search_launch_speeds


@pytest.mark.parametrize(
    "dataset_path,height_limit,launch_limit",
    [
        [Path("day17/data/data-small.txt"), 45, 112],
        [Path("day17/data/data-large.txt"), 4186, 2709],
    ],
)
def test_day(dataset_path: Path, height_limit, launch_limit):
    """Test case for verifying the results of day 17."""
    probe = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 17 dataset %s with goal location x=%s, y=%s",
        dataset_path.name,
        probe.goal_x,
        probe.goal_y,
    )
    probe.x = 6
    probe.y = 9
    height, launch_parameters = search_launch_speeds(probe)
    log.info(
        "Found the max height %d at out of %d successful launch parameters.",
        height,
        launch_parameters,
    )
    assert height == height_limit
    assert launch_parameters == launch_limit
