"""Test cases for day 14."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day14 import load_dataset
from day14 import polymerisation


@pytest.mark.parametrize(
    "dataset_path,steps,delta_limit",
    [
        [Path("day14/data/data-small.txt"), 10, 1588],
        [Path("day14/data/data-large.txt"), 10, 3697],
        # [Path("day14/data/data-small.txt"), 40, 2188189693529],
        # [Path("day14/data/data-large.txt"), 40, 0],
    ],
)
def test_day(dataset_path: Path, steps, delta_limit):
    """Test case for verifying the results of day 14."""
    template, rules, frequency = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 14 dataset %s with %s polymer template and %d polymer rules",
        dataset_path.name,
        template,
        len(rules),
    )
    frequency = polymerisation(template, rules, steps, frequency)
    log.info(
        "Found most common element '%s' with %d occurrences, "
        "and least common '%s with %d occurrences (delta=%d).",
        frequency[0][0],
        frequency[0][1],
        frequency[-1][0],
        frequency[-1][1],
        frequency[0][1] - frequency[-1][1],
    )
    assert frequency[0][1] - frequency[-1][1] == delta_limit
