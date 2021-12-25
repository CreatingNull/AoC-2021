"""--- Day 20: Trench Map ---"""
from pathlib import Path


from numpy import array
from numpy import byte
from numpy import zeros
from numpy import sum as sum_
from bitarray import bitarray
from bitarray.util import ba2int


from aoc import open_utf8
from aoc import log


def __find_array_binary(input_array: array) -> int:
    """
    Converts the rows of data to an integer representation.

    :param input_array: Pre-sliced array to convert.
    :return: Integer conversion of the binary data in the input_array.
    """
    return ba2int(
        bitarray(value for row in input_array for value in row)
    )


def __enhance_image(image: array, image_enhancement: bitarray):
    """
    Iterates through each pixel in the image resolves it via the enhancement algorithm.

    :param image: Numpy byte array with containing the pixel values.
    :param image_enhancement: Bit array for resolving output pixels based on numeric value.
    :return: The enhanced imaage.
    """
    m = 3  # num rows to consider in the algorithm
    n = 3  # num columns to consider in the algorithm
    m_range = m // 2  # Algorithm search window around index.
    n_range = n // 2
    m_pad = (m - 1)  # Amount to pad the image
    n_pad = (n - 1)
    initial_rows, initial_cols = image.shape
    # Adding expand range and padding range
    padded_image = zeros((initial_rows+m_pad*4, initial_cols+n_pad*4), dtype=byte)
    padded_image[2*m_pad:-2*m_pad, 2*n_pad:-2*n_pad] = image
    # Expand the output
    image = zeros((initial_rows+m_pad*2, initial_cols+n_pad*2), dtype=byte)
    # Go through the pixels in the actual image and compute the output.
    for row_index in range(initial_rows+2*m_pad):  # expands by m-1
        row_index += m_pad  # Adjust for padding
        for col_index in range(initial_cols+2*n_pad):  # expands by n-1
            col_index += n_pad  # Adjust for padding♦
            cell_value = __find_array_binary(
                padded_image[
                    row_index-m_range:row_index+m_range+1,
                    col_index-n_range:col_index+n_range+1,
                ]
            )
            image[row_index-m_pad, col_index-n_pad] = image_enhancement[cell_value]
    return image


def __render_image(image: array):  # todo remove this
    for row in image:
        for value in row:
            print("." if value == 0 else "#", end="")
        print()


def run_enhancement(image: array, image_enhancement: bitarray, passes: int):
    #__render_image(image)
    for _ in range(passes):
        image = __enhance_image(image, image_enhancement)
        #__render_image(image)
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
                for line in file if len(line.strip()) > 0
            ],
            dtype=byte,
        )
    return image_enhancement, input_image
