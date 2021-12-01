"""--- Day 1: Sonar Sweep ---"""
from dataclasses import dataclass


@dataclass
class Scan:
    """Describing the number of increases and decreases in a scan."""

    scan: list
    window: int  # window for rolling gradient comparison
    increases: int  # count of the number of increases in the scan

    def __init__(self, scan: list, window: int):
        """Creates the object and runs computations on data."""
        self.scan = scan
        self.window = window
        self.increases = 0
        for index in range(len(self.scan) - self.window):
            # Iterate through the window transitions and compute the sums
            if (
                sum(self.scan[index + 1 : index + self.window + 1])
                - sum(self.scan[index : index + self.window])
                > 0
            ):
                self.increases += 1
