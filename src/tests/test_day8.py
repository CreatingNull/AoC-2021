"""Test cases for day 8."""
from pathlib import Path

import pytest
from aoc import log
from aoc import ROOT_PATH
from day8 import decode_sequences
from day8 import load_dataset


@pytest.mark.parametrize(
    "dataset_path,simple_decode,full_decode",
    [
        [Path("day8/data/data-smaller.txt"), 0, 5353],
        [Path("day8/data/data-small.txt"), 26, 61229],
        [Path("day8/data/data-large.txt"), 349, 1070957],
    ],
)
def test_day(dataset_path: Path, simple_decode: int, full_decode: int):
    """Test case for verifying the results of day 8."""
    data = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded dataset for day 8 %s with %d signal sets",
        dataset_path.name,
        len(data),
    )
    sums = decode_sequences(data)
    assert sums[0] == simple_decode
    assert sums[1] == full_decode
