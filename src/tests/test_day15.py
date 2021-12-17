"""Test cases for day 15."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day15 import a_starify
from day15 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,tiling,risk_limit",
    [
        [Path("day15/data/data-small.txt"), 1, 40],
        [Path("day15/data/data-large.txt"), 1, 447],
        [Path("day15/data/data-small.txt"), 5, 315],
        [Path("day15/data/data-large.txt"), 5, 2825],
    ],
)
def test_day(dataset_path: Path, tiling, risk_limit):
    """Test case for verifying the results of day 14."""
    search_map = load_dataset(ROOT_PATH.joinpath(dataset_path), tiling=tiling)
    log.info(
        "Loaded day 15 dataset %s tiling %d produces a %s grid",
        dataset_path.name,
        tiling,
        search_map.shape,
    )
    loops, cost = a_starify(search_map)
    log.info(
        "Located path of %d cost after %d A* iterations.",
        cost,
        loops,
    )
    assert cost == risk_limit
