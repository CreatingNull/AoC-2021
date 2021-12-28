"""Test cases for day 23."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day23 import load_dataset
from day23 import solve_puzzle


@pytest.mark.parametrize(
    "dataset_path,limit,folded_paper",
    [
        # [Path("day23/data/data-small.txt"), 12521, False],
        [Path("day23/data/data-large.txt"), 14371, False],
        # [Path("day23/data/data-small.txt"), 44169, True],
        [Path("day23/data/data-large.txt"), 40941, True],
    ],
)
def test_day(dataset_path: Path, limit: int, folded_paper: bool):
    """Test case for verifying the results of day 23."""
    starting_map = load_dataset(ROOT_PATH.joinpath(dataset_path), folded_paper)
    log.info(
        "Loaded day 23 dataset %s with %s room states.",
        dataset_path.name,
        starting_map.rooms,
    )
    cost, iterations = solve_puzzle(starting_map)
    log.info(
        "Took %d search iterations to find solution of cost %d.",
        iterations,
        cost,
    )
    assert cost == limit
