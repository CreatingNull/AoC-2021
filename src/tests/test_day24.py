"""Test cases for day 24."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day24 import find_model_limit
from day24 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,limit_high,limit_low",
    [
        [Path("day24/data/data-large.txt"), 36969794979199, 11419161313147],
    ],
)
def test_day(dataset_path: Path, limit_high: int, limit_low: int):
    """Test case for verifying the results of day 24."""
    program = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 24 dataset %s with %d alu instructions in program.",
        dataset_path.name,
        len(program),
    )
    highest = find_model_limit(program, True)
    lowest = find_model_limit(program, False)
    log.info(
        "Resolved highest model number to %d and lowest model number to %d",
        highest,
        lowest,
    )
    assert highest == limit_high
    assert lowest == limit_low
