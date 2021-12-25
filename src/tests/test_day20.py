"""Test cases for day 20."""
from logging import DEBUG
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day20 import load_dataset, run_enhancement


log.setLevel(DEBUG)


@pytest.mark.parametrize(
    "dataset_path,pixels_limit",
    [
        [Path("day20/data/data-small.txt"), 35],
        #[Path("day20/data/data-large.txt"), 35],
    ],
)
def test_day(dataset_path: Path, pixels_limit):
    """Test case for verifying the results of day 20."""
    image_enhancement, input_image = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 20 dataset %s with %d length enhancement "
        "algorithm and %s defined input image.",
        dataset_path.name,
        len(image_enhancement),
        input_image.shape
    )
    high_pixels = run_enhancement(input_image, image_enhancement, 2)

    assert high_pixels == pixels_limit
