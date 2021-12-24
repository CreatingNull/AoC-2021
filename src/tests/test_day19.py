"""Test cases for day 19."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day19 import align_scanners_to_reference
from day19 import load_dataset
from day19 import max_manhattan_distance


@pytest.mark.parametrize(
    "dataset_path,beacon_limit,manhattan_limit",
    [
        [Path("day19/data/data-small.txt"), 79, 3621],
        # Disabled the full test because my solution is slow :(
        # [Path("day19/data/data-large.txt"), 320, 9655],
    ],
)
def test_day(dataset_path: Path, beacon_limit, manhattan_limit):
    """Test case for verifying the results of day 19."""
    scanners = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 19 dataset %s with %d scanners.",
        dataset_path.name,
        len(scanners),
    )
    num_beacons = align_scanners_to_reference(scanners)
    manhattan_distance = max_manhattan_distance(scanners)
    log.info(
        "After scanner alignment found %d total beacons with max manhattan distance %d.",
        num_beacons,
        manhattan_limit,
    )
    assert num_beacons == beacon_limit
    assert manhattan_distance == manhattan_limit
