"""Test cases for day 12."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day12 import enumerate_paths
from day12 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,visit_exception,path_limit",
    [
        [Path("day12/data/data-smallest.txt"), False, 10],
        [Path("day12/data/data-smaller.txt"), False, 19],
        [Path("day12/data/data-small.txt"), False, 226],
        [Path("day12/data/data-large.txt"), False, 4104],
        [Path("day12/data/data-smallest.txt"), True, 36],
        [Path("day12/data/data-smaller.txt"), True, 103],
        [Path("day12/data/data-small.txt"), True, 3509],
        [Path("day12/data/data-large.txt"), True, 119760],
    ],
)
def test_day(dataset_path: Path, visit_exception, path_limit):
    """Test case for verifying the results of day 12."""
    data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 12 dataset %s with %d caves.",
        dataset_path.name,
        len(data),
    )
    complete_paths = enumerate_paths(data, visit_exception)
    log.info(
        "After walking the cave there are %d paths with %s.",
        len(complete_paths),
        "a small cave visit exception" if visit_exception else "no small cave re-entry",
    )
    assert len(complete_paths) == path_limit
