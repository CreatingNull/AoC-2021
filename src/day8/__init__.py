"""--- Day 8: Seven Segment Search ---"""
from dataclasses import dataclass
from pathlib import Path

from aoc import log
from aoc import open_utf8


LEN_LUT = {2: 1, 4: 4, 3: 7, 7: 8}  # unique length outputs
LOC_LUT = {  # output to expected segments
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}
COMMON_PATTERNS = {  # signal length to common segment
    5: {"a", "d", "g"},  # common between 2,3,5
    6: {"b", "f"},  # common between 6,9,0
}


@dataclass
class SevenSegSignal:
    """Class represents a single set of signals for a number."""

    pattern: str  # The signal pattern ordered alphabetically
    decoded_val: int = None  # The resolved integer, None if unresolved.

    def __init__(self, data: str):
        """Constructor sorts input data for loading into pattern."""
        self.pattern = "".join(sorted(data))


@dataclass
class SubDisplay:
    """Class containing data for a single input row."""

    panels: [SevenSegSignal]  # The 4 output panels for decoding the value on.
    definitions: {SevenSegSignal}  # The definitions of 1 to 10.
    # Mapping known segments to possible mixed signals in our data
    seven_segment: {} = None  # Used when manually decoding the `sudoku`

    def get_panel_reading(self):
        """Returns a string representation of the output once panels are
        decoded."""
        return "".join(str(val.decoded_val) for val in self.panels)

    def set_panels_from_wiring(self):
        """Populates panel decoded val using resolved seven seg wiring."""
        for panel in self.panels:
            if not panel.decoded_val:
                for value, signals in LOC_LUT.items():
                    # decoding the panel using the wiring reference
                    equivalent_pattern = "".join(
                        sorted(
                            decoded
                            for signal in signals
                            for decoded in self.seven_segment[signal]
                        )
                    )
                    if equivalent_pattern == panel.pattern:
                        panel.decoded_val = value


def __resolve_by_sudoku(signals: SubDisplay):
    """Decodes by iteratively finding impossibilities in reference display."""
    # start decoding create our reference display
    signals.seven_segment = {
        positional_char: set("abcdefg") for positional_char in "abcdefg"
    }
    # Reduce our options for each signal location
    for pattern, signal in signals.definitions.items():
        if signal.decoded_val:  # we know where this signal should be
            for location in LOC_LUT[signal.decoded_val]:
                # get rid of anything that isn't common
                signals.seven_segment[location] = signals.seven_segment[
                    location
                ].intersection(set(pattern))
        else:  # we partially where these signals should be
            for location in COMMON_PATTERNS[len(pattern)]:
                signals.seven_segment[location] = signals.seven_segment[
                    location
                ].intersection(set(pattern))
    # Tree traversal to solve impossibilities within the remaining options
    pass_at_0 = set()
    for _ in range(2):  # All the problems can be solved in 2 steps
        for signal_reference, set_len in sorted(
            {k: len(v) for k, v in signals.seven_segment.items()}.items(),
            key=lambda item: item[1],
        ):  # The lower length items contain more useful information
            if signal_reference not in pass_at_0:
                if set_len == 1:  # can't juice this orange further
                    pass_at_0.add(signal_reference)
                for signal in signals.seven_segment:
                    if signal_reference != signal and set_len == 1:
                        signals.seven_segment[signal] -= signals.seven_segment[
                            signal_reference
                        ]
        if len(pass_at_0) == 7:
            break
    log.debug("Resolved wiring to %s", signals.seven_segment)


def __decode_sequence(signals: SubDisplay) -> (int, str):
    """Takes in a single SubDisplay dataset and resolves the output signal.

    :param signals: Sub display input signal to decide.
    :return: (simple sum, string representation of output)
    """
    # Solve as much as possible using length
    count_simple = 0
    for _, signal in signals.definitions.items():
        if (
            decoded_val := LEN_LUT[len(signal.pattern)]
            if len(signal.pattern) in LEN_LUT
            else None
        ):
            signal.decoded_val = decoded_val
    for panel in signals.panels:
        if signals.definitions[panel.pattern].decoded_val:
            panel.decoded_val = signals.definitions[panel.pattern].decoded_val
            count_simple += 1
    if count_simple != 4:  # We actually have to do some hard work
        __resolve_by_sudoku(signals)
    signals.set_panels_from_wiring()
    return count_simple, signals.get_panel_reading()


def decode_sequences(data: [SubDisplay]) -> []:
    """Computes the rolling output and simple sums for the input data.

    :param data: List of sub display objects
    :return: (simple sum, rolling output)
    """
    simple_sum = 0  # Computed off only unique length
    rolling_output = 0  # Part 2 full solution.
    for sequence in data:  # Decode the output
        result = __decode_sequence(sequence)
        simple_sum += result[0]
        log.debug("Output sum resolves to %s", result[1])
        rolling_output += int(result[1])  # string to int
    log.info(
        "We computed %d output codes from the length alone, total decode sum was %s.",
        simple_sum,
        rolling_output,
    )
    return simple_sum, rolling_output


def load_dataset(dataset_path: Path) -> [SubDisplay]:
    """Loads the dataset from file as a list of integer crab positions.

    :param dataset_path: Path object to load the data from.
    :return: List of integers representing positions of individual crabs.
    """
    with open_utf8(dataset_path) as file:
        signals = []
        for line in file:
            if len(line.strip()) > 0:
                signals.append(
                    SubDisplay(
                        [
                            SevenSegSignal(signal)
                            for signal in line.split("|")[1].strip().split(" ")
                        ],
                        {
                            SevenSegSignal(signal).pattern: SevenSegSignal(signal)
                            for signal in line.split("|")[0].strip().split(" ")
                        },
                    )
                )
    return signals
