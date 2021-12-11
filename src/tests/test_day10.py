"""Test cases for day 10."""
from pathlib import Path

import pytest
from aoc import ROOT_PATH
from day10 import parse_data


@pytest.mark.parametrize(
    "dataset_path,error_limit,autocomplete_limit",
    [
        [Path("day10/data/data-small.txt"), 26397, 288957],
        [Path("day10/data/data-large.txt"), 464991, 3662008566],
    ],
)
def test_day(dataset_path: Path, error_limit: int, autocomplete_limit: int):
    """Test case for verifying the results of day 10."""
    syntax_score, autocomplete_score = parse_data(ROOT_PATH.joinpath(dataset_path))
    assert syntax_score == error_limit
    assert autocomplete_score == autocomplete_limit
