"""Test cases for day 6."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day6 import load_dataset
from day6 import simulate_population


@pytest.mark.parametrize(
    "dataset_path,days,result",
    [
        [Path("day6/data/data-small.txt"), 80, 5934],
        [Path("day6/data/data-large.txt"), 80, 346063],
        [Path("day6/data/data-small.txt"), 256, 26984457539],
        [Path("day6/data/data-large.txt"), 256, 1572358335990],
    ],
)
def test_day(dataset_path: Path, days: int, result: int):
    """Test case for verifying the results of day 6."""
    data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 6 dataset %s with %d fish.", dataset_path.name, sum(data.values())
    )
    data = simulate_population(data, days)
    total_fish = sum(data.values())
    log.info(
        "after %d days there are %d total fish.",
        days,
        total_fish,
    )
    assert result == total_fish
