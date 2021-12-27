"""Test cases for day 22."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day22 import compute_reactor_state
from day22 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,initialisation_limit,reboot_limit",
    [
        [Path("day22/data/data-small.txt"), 474140, 2758514936282235],
        [Path("day22/data/data-large.txt"), 620241, 1284561759639324],
    ],
)
def test_day(dataset_path: Path, initialisation_limit, reboot_limit):
    """Test case for verifying the results of day 22."""
    instructions = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 22 dataset %s with %d reactor core instructions.",
        dataset_path.name,
        len(instructions),
    )
    init_sequence = compute_reactor_state(instructions, True)
    total_active = compute_reactor_state(instructions, False)
    log.info(
        "After the reactor initialisation sequence %d cubes are active, "
        "after the full reboot %d are active.",
        init_sequence,
        total_active,
    )
    assert init_sequence == initialisation_limit
    assert total_active == reboot_limit
