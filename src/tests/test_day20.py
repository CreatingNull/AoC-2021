"""Test cases for day 20."""
from pathlib import Path

import pytest

from aoc import log
from aoc import ROOT_PATH
from day20 import load_dataset
from day20 import run_enhancement


@pytest.mark.parametrize(
    "dataset_path,pixels_limit,passes",
    [
        [Path("day20/data/data-small.txt"), 35, 2],
        [Path("day20/data/data-large.txt"), 5489, 2],
        [Path("day20/data/data-small.txt"), 3351, 50],
        [Path("day20/data/data-large.txt"), 19066, 50],
    ],
)
def test_day(dataset_path: Path, pixels_limit, passes):
    """Test case for verifying the results of day 20."""
    image_enhancement, input_image = load_dataset(ROOT_PATH.joinpath(dataset_path))
    log.info(
        "Loaded day 20 dataset %s with %d length enhancement "
        "algorithm and %s defined input image.",
        dataset_path.name,
        len(image_enhancement),
        input_image.shape,
    )
    high_pixels = run_enhancement(input_image, image_enhancement, passes)
    log.info(
        "Located %d bright pixels after %d enhancement passes on the image.",
        high_pixels,
        passes,
    )
    assert high_pixels == pixels_limit
