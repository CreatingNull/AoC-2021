"""Test cases for day 21."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day21 import load_dataset
from day21 import simulate_game


@pytest.mark.parametrize(
    "dataset_path,universe_limit",
    [
        [Path("day21/data/data-small.txt"), 444356092776315],
        [Path("day21/data/data-large.txt"), 105619718613031],
    ],
)
def test_day(dataset_path: Path, universe_limit):
    """Test case for verifying the results of day 21."""
    game = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 21 dataset %s with player 1 at %d " "and player 2 at %d.",
        dataset_path.name,
        game.position1,
        game.position2,
    )
    universes = simulate_game(game, 21)
    log.info(
        "The winning player wins in %s universes.",
        universes,
    )
    assert universes == universe_limit
