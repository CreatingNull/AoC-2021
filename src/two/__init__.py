"""--- Day 2: Dive! ---"""
from aoc import log


def compute_xy_product(instructions: [], aimed: bool) -> int:
    """Compute the final position from a list of [action, value] lists.

    :param instructions: The 2d list of instructions.
    :param aimed: Boolean to enable or disable aimed style navigation.
    :return: Integer product of the final x and y position.
    """
    x = 0  # Horizontal position of the submarine
    y = 0  # Vertical position of the submarine
    aim = 0  # Y movement multiplier when aimed
    for action, value in instructions:
        value = int(value)
        if action == "forward":
            x += value  # positive x movement
            if aimed:  # also change the depth
                y += value * aim
        else:
            delta = value if action == "down" else -value
            if aimed:  # modify aim
                aim += delta
            else:  # change depth
                y += delta
    product = x * y
    log.info(
        "Final position is x=%d and y=%d (product=%d)",
        x,
        y,
        product,
    )
    return product
