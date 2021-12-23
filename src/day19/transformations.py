"""Module to store the possible spacial transformation definitions."""
from numpy import array
from numpy import byte


TRANSFORMATIONS = {
    0: array(  # Reference orientation (Identity Matrix)
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ],
        dtype=byte,
    ),
    # --- Y ---
    1: array(  # Rotate 90' on Y axis
        [
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0],
        ],
        dtype=byte,
    ),
    2: array(  # Rotate 180' on Y axis
        [
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, -1],
        ],
        dtype=byte,
    ),
    3: array(  # Rotate 270' on Y axis
        [
            [0, 0, -1],
            [0, 1, 0],
            [1, 0, 0],
        ],
        dtype=byte,
    ),
    # --- Attitude 90' ---
    4: array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=byte),  # attitude 90'
    5: array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=byte),  # attitude 90' w/ Y 90'
    6: array(  # attitude 90' w/ Y 180'
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1],
        ],
        dtype=byte,
    ),
    7: array(  # attitude 90' w/ Y 270'
        [
            [0, 0, -1],
            [1, 0, 0],
            [0, -1, 0],
        ],
        dtype=byte,
    ),
    # --- Attitude 270' ---
    8: array(  # attitude 270'
        [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1],
        ],
        dtype=byte,
    ),
    9: array(  # attitude 270' w/ Y 90'
        [
            [0, 0, 1],
            [-1, 0, 0],
            [0, -1, 0],
        ],
        dtype=byte,
    ),
    10: array(  # attitude 270' w/ Y 180'
        [
            [0, -1, 0],
            [-1, 0, 0],
            [0, 0, -1],
        ],
        dtype=byte,
    ),
    11: array(  # attitude 270' w/ Y 260'
        [[0, 0, -1], [-1, 0, 0], [0, 1, 0]], dtype=byte
    ),
    # -- bank 90' --
    12: array(  # bank 90'
        [
            [1, 0, 0],
            [0, 0, -1],
            [0, 1, 0],
        ],
        dtype=byte,
    ),
    13: array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]], dtype=byte),  # bank 90' w/ Y 90'
    14: array(  # bank 90' w/ Y 180'
        [
            [-1, 0, 0],
            [0, 0, -1],
            [0, -1, 0],
        ],
        dtype=byte,
    ),
    15: array(  # bank 90' w/ Y 270'
        [
            [0, -1, 0],
            [0, 0, -1],
            [1, 0, 0],
        ],
        dtype=byte,
    ),
    # -- Bank 180' --
    16: array(  # 180' bank
        [
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, -1],
        ],
        dtype=byte,
    ),
    17: array(  # 180' Bank with Y 90'
        [
            [0, 0, -1],
            [0, -1, 0],
            [-1, 0, 0],
        ],
        dtype=byte,
    ),
    18: array(  # 180' bank with Y 180'
        [
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1],
        ],
        dtype=byte,
    ),
    19: array(  # 180' bank with Y 270'
        [
            [0, 0, 1],
            [0, -1, 0],
            [1, 0, 0],
        ],
        dtype=byte,
    ),
    # bank 270'
    20: array(  # bank 270'
        [
            [1, 0, 0],
            [0, 0, 1],
            [0, -1, 0],
        ],
        dtype=byte,
    ),
    21: array(  # bank 270' w/ Y 90'
        [
            [0, -1, 0],
            [0, 0, 1],
            [-1, 0, 0],
        ],
        dtype=byte,
    ),
    22: array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]]),  # bank 270' w/ Y 180'
    23: array(  # bank 270' w/ Y 270'
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ],
        dtype=byte,
    ),
}
