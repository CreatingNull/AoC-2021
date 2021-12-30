"""Test cases for day 25."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day25 import find_idle
from day25 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,steps_limit",
    [
        [Path("day25/data/data-small.txt"), 58],
        [Path("day25/data/data-large.txt"), 571],
    ],
)
def test_day(dataset_path: Path, steps_limit):
    """Test case for verifying the results of day 26."""
    cucumber_map = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 24 dataset %s with seacucumber map shape %s.",
        dataset_path.name,
        cucumber_map.shape,
    )
    num_steps = find_idle(cucumber_map)
    log.info(
        "At step %d the sea-cucumbers stop moving.",
        num_steps,
    )
    assert num_steps == steps_limit
