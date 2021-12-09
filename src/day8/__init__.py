"""--- Day 8: Seven Segment Search ---"""
from dataclasses import dataclass
from pathlib import Path

from aoc import log
from aoc import open_utf8

# digit | segments
# ----- | --------
#   0   |    6
#   1   |    2
#   2   |    5
#   3   |    5
#   4   |    4
#   5   |    5
#   6   |    6
#   7   |    3
#   8   |    7
#   9   |    6

LEN_LUT = {2: 1, 4: 4, 3: 7, 7: 8}

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

LOC_LUT = {
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
    235: {"a", "d", "g"},  # common between 2,3,5
    690: {"b", "f"},  # common between 6,9,0
}


@dataclass
class SevenSegSignal:

    pattern: str
    in_situ: str
    decoded_val: int = None

    def __init__(self, data: str, displayed: bool):
        self.pattern = "".join(sorted(data))


@dataclass
class SubDisplay:

    panels: [SevenSegSignal]
    definitions: {SevenSegSignal}
    seven_segment: {} = None

    def get_panel_reading(self):
        return "".join(str(val.decoded_val) for val in self.panels)

    def set_panels_from_wiring(self):
        for panel in self.panels:
            if not panel.decoded_val:
                for value in LOC_LUT:
                    if value < 10:
                        equivalent_pattern = "".join(
                            sorted(
                                final
                                for signal in LOC_LUT[value]
                                for final in self.seven_segment[signal]
                            )
                        )
                        if equivalent_pattern == panel.pattern:
                            panel.decoded_val = value


def __check_unique_lengths(signal: SevenSegSignal) -> int:
    return LEN_LUT[len(signal.pattern)] if len(signal.pattern) in LEN_LUT else None


def __decode_sequence(signals: SubDisplay):
    # Solve as much as possible using length
    count_simple = 0
    for key, signal in signals.definitions.items():
        if decoded_val := __check_unique_lengths(signal):
            signal.decoded_val = decoded_val
    for panel in signals.panels:
        if signals.definitions[panel.pattern].decoded_val:
            panel.decoded_val = signals.definitions[panel.pattern].decoded_val
            count_simple += 1
    if count_simple != 4:  # We actually have to do some hard work
        # start decoding create our reference display
        signals.seven_segment = {
            positional_char: {char for char in "abcdefg"}
            for positional_char in "abcdefg"
        }
        # Reduce our options for each signal location
        for pattern, signal in signals.definitions.items():
            if signal.decoded_val:  # we know where this signal should be
                for location in LOC_LUT[signal.decoded_val]:
                    # get rid of anything that isn't common
                    signals.seven_segment[location] = signals.seven_segment[
                        location
                    ].intersection({char for char in pattern})
            else:  # we partially where these signals should be
                common_length = 690 if len(pattern) == 6 else 235
                for location in LOC_LUT[common_length]:
                    signals.seven_segment[location] = signals.seven_segment[
                        location
                    ].intersection({char for char in pattern})
        # Tree traversal to solve impossibilities within the remaining options
        pass_at_0 = []
        for i in range(10):
            for signal_reference, set_len in sorted(
                {k: len(v) for k, v in signals.seven_segment.items()}.items(),
                key=lambda item: item[1],
            ):
                if signal_reference not in pass_at_0:
                    if set_len == 1:  # can't juice this lemon further
                        pass_at_0.append(signal_reference)
                    for signal in signals.seven_segment:
                        if signal_reference != signal and set_len == 1:
                            signals.seven_segment[signal] -= signals.seven_segment[
                                signal_reference
                            ]
            if len(pass_at_0) == 7:
                break
        if len(pass_at_0) != 7:
            raise RuntimeError("Algorithm dun broke!")

        log.debug("Resolved wiring to %s", signals.seven_segment)
    signals.set_panels_from_wiring()
    return count_simple, signals.get_panel_reading()


def decode_sequences(data: [SubDisplay]) -> []:
    simple_sum = 0
    rolling_output = 0
    for sequence in data:
        result = __decode_sequence(sequence)
        simple_sum += result[0]
        log.debug("Output sum resolves to %s", result[1])
        rolling_output += int(result[1])
    log.info(
        "We computed %d output codes from the length alone, total decode sum was %s.",
        simple_sum,
        rolling_output,
    )
    return [simple_sum, rolling_output]


def load_dataset(dataset_path: Path) -> [SubDisplay]:
    """Loads the dataset from file as a list of integer crab positions.

    :param dataset_path: Path object to load the data from.
    :return: List of integers representing positions of individual crabs.
    """
    with open_utf8(dataset_path) as file:
        signal_sets = []
        for line in file:
            if len(line.strip()) > 0:
                signal_sets.append(
                    SubDisplay(
                        [
                            SevenSegSignal(signal, True)
                            for signal in line.split("|")[1].strip().split(" ")
                        ],
                        {
                            SevenSegSignal(signal, False).pattern: SevenSegSignal(
                                signal, False
                            )
                            for signal in line.split("|")[0].strip().split(" ")
                        },
                    )
                )
    return signal_sets
