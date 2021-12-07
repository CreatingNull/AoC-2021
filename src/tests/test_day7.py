"""Test cases for day 7."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day7 import find_minima
from day7 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,fuel,position,flat_fuel_cost",
    [
        [Path("day7/data/data-small.txt"), 37, 2, True],
        [Path("day7/data/data-large.txt"), 329389, 330, True],
        [Path("day7/data/data-small.txt"), 168, 5, False],
        [Path("day7/data/data-large.txt"), 86397080, 459, False],
    ],
)
def test_day(dataset_path: Path, fuel: int, position: int, flat_fuel_cost: bool):
    """Test case for verifying the results of day 7."""
    data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 7 dataset %s with %d crabs spread between %d and %d using %s",
        dataset_path.name,
        len(data),
        min(data),
        max(data),
        "flat fuel cost" if flat_fuel_cost else "increasing fuel cost",
    )
    min_index, min_value = find_minima(data, flat_fuel_cost)
    log.info(
        "Global minima found at location %d with fuel consumption %d",
        min_index,
        min_value,
    )
    assert min_index == position
    assert min_value == fuel
