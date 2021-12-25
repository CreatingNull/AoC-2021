"""--- Day 20: Trench Map ---"""
from pathlib import Path

from bitarray import bitarray
from bitarray.util import ba2int
from numpy import array
from numpy import byte
from numpy import ones
from numpy import sum as sum_
from numpy import zeros

from aoc import open_utf8

M_RANGE = 3 // 2  # Algorithm horizontal search window around index.
N_RANGE = 3 // 2  # Algorithm vertical search window around index.


def __enhance_image(image: array, image_enhancement: bitarray, invert):
    """Iterates through each pixel in the image resolves it via the enhancement
    algorithm.

    :param image: Numpy byte array with containing the pixel values.
    :param image_enhancement: Bit array for resolving output pixels based on numeric value.
    :param invert: If padding should be done using 1s to correct for the infinite plane.
    :return: The enhanced image.
    """
    initial_rows, initial_cols = image.shape
    # Adding expand range and padding range for padded image
    if invert:  # Corrects the bordering mistakes
        padded_image = ones(
            (initial_rows + 4 * M_RANGE, initial_cols + 4 * N_RANGE), dtype=byte
        )
    else:
        padded_image = zeros(
            (initial_rows + 4 * M_RANGE, initial_cols + 4 * N_RANGE), dtype=byte
        )
    padded_image[2 * M_RANGE : -2 * M_RANGE, 2 * N_RANGE : -2 * N_RANGE] = image

    # Output image only expands by m and n range.
    image = zeros((initial_rows + 2 * M_RANGE, initial_cols + 2 * N_RANGE), dtype=byte)
    # Go through the pixels in the actual image and compute the output.
    for row_index in range(M_RANGE, padded_image.shape[0] - M_RANGE):
        for col_index in range(N_RANGE, padded_image.shape[1] - N_RANGE):
            cell_value = ba2int(
                bitarray(
                    [
                        value
                        for row in padded_image[
                            row_index - M_RANGE : row_index + M_RANGE + 1,
                            col_index - N_RANGE : col_index + N_RANGE + 1,
                        ]
                        for value in row
                    ]
                )
            )
            image[row_index - M_RANGE, col_index - N_RANGE] = image_enhancement[
                cell_value
            ]
    return image


def run_enhancement(image: array, image_enhancement: bitarray, passes: int):
    """Steps through a number of enhancement passes on the input image.

    :param image: Numpy byte array with containing the pixel values.
    :param image_enhancement: Bit array for resolving output pixels based on numeric value.
    :param passes: The number of passes to execute on the image.
    :return: The sum of the bright pixels in the resulting image.
    """
    for step in range(passes):
        image = __enhance_image(
            image, image_enhancement, step % 2 and image_enhancement[0] == 1
        )
    return sum_(image)


def load_dataset(dataset_path: Path) -> (bitarray, array):
    """Loads binary data from file into a bitarray."""
    with open_utf8(dataset_path) as file:
        image_enhancement = bitarray(
            0 if char == "." else 1 for char in file.readline().strip()
        )
        input_image = array(
            [
                [0 if char == "." else 1 for char in line.strip()]
                for line in file
                if len(line.strip()) > 0
            ],
            dtype=byte,
        )
    return image_enhancement, input_image
