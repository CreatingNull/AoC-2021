"""Test cases for day 3."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day3 import DiagnosticRates


@pytest.mark.parametrize(
    "dataset_path,result_first,result_second",
    [
        [Path("day3/data/data-small.txt"), 198, 230],
        [Path("day3/data/data-large.txt"), 852500, 1007985],
    ],
)
def test_day(dataset_path: Path, result_first: int, result_second: int):
    """Test case for verifying the results of day 3."""
    rates = DiagnosticRates(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 3 dataset %s of %d rows of %s bit numbers",
        dataset_path.name,
        len(rates.diagnostic_data),
        rates.num_bits,
    )
    product_first = rates.gamma * rates.epsilon
    log.info(
        "Computed gamma rate %d and epsilon rate %d (product=%d)",
        rates.gamma,
        rates.epsilon,
        product_first,
    )
    product_second = rates.o2 * rates.co2
    log.info(
        "Computed o2 rate %d and co2 rate %d (product=%d)",
        rates.o2,
        rates.co2,
        product_second,
    )
    assert product_first == result_first
    assert product_second == result_second
