"""Root package for the challenge.

Contains generic functionality not specific to days.
"""
import logging
import sys
from functools import partial
from pathlib import Path


ROOT_PATH = Path(Path(__file__).parents[1])
open_utf8 = partial(open, encoding="UTF-8")  # Open with explict encoding

# Configuring the global logger
log = logging.getLogger()
log.setLevel(logging.INFO)
__handler = logging.StreamHandler(sys.stdout)
__handler.setLevel(logging.DEBUG)
__handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
log.addHandler(__handler)
