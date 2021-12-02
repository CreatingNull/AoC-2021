"""Root package for the challenge.

Contains generic functionality not specific to days.
"""
import logging
import sys
from enum import Enum
from pathlib import Path


ROOT_PATH = Path(__file__).parents[1]

# Configuring the global logger
log = logging.getLogger()
log.setLevel(logging.INFO)
__handler = logging.StreamHandler(sys.stdout)
__handler.setLevel(logging.DEBUG)
__handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
log.addHandler(__handler)


class DatasetType(Enum):
    ROW_LIST_NUMERIC = 0
    SPACE_DELIM = 1


def load_dataset(data_type: DatasetType, data_path: Path):
    """Processes a text dataset and returns the relevant data-structure."""
    if not data_path.is_file():
        raise FileNotFoundError("Data file must exist to be loaded.")
    if data_type == DatasetType.ROW_LIST_NUMERIC:
        # Return a list of numeric data
        with open(data_path) as file:
            return [int(line.rstrip()) for line in file]
    if data_type == DatasetType.SPACE_DELIM:
        # Return a 2D list containing string data, delimited via space.
        with open(data_path) as file:
            return [[cell.strip() for cell in line.split(" ")] for line in file]
    raise NotImplementedError("I don't know how to handle this data yet.")
