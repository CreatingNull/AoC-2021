"""--- Day 3: Binary Diagnostic ---"""
from dataclasses import dataclass


@dataclass
class DiagnosticRates:
    """Object to hold the computed rates for a dataset."""

    diagnostic_data: list  # The integer data to include in the rates calculations.
    num_bits: int  # The number of bits used in the input diagnostic data
    gamma: int = None
    epsilon: int = None
    o2: int = None
    co2: int = None

    def __init__(self, diagnostic_data, num_bits):
        self.diagnostic_data = diagnostic_data
        self.num_bits = num_bits
        self.__process_diagnostics()
        self.__compute_epsilon_rate()

    def __process_diagnostics(self):
        """Iterates the diagnostic data to compute summary rates."""
        gamma_bits = ""  # tracking the final bit result for gamma rate
        o2_inclusions = [data_index for data_index in range(len(self.diagnostic_data))]
        co2_inclusions = [data_index for data_index in range(len(self.diagnostic_data))]
        for bit_index in range(
            self.num_bits
        ):  # Iterate bits, note bitmasks are from MSB
            gamma_frequency = 0  # track the number of high bits for gamma calculation
            o2_frequency = 0
            co2_frequency = 0
            for data_index, line in enumerate(self.diagnostic_data):
                bit_value = line >> (self.num_bits - bit_index - 1) & 0b1
                if len(o2_inclusions) > 1 and data_index in o2_inclusions:
                    o2_frequency += bit_value
                if len(co2_inclusions) > 1 and data_index in co2_inclusions:
                    co2_frequency += bit_value
                gamma_frequency += bit_value
            gamma_bits += (
                "1" if gamma_frequency >= len(self.diagnostic_data) / 2 else "0"
            )
            o2_inclusions = self.__evaluate_bit_criteria(
                o2_inclusions, o2_frequency, bit_index, True
            )
            co2_inclusions = self.__evaluate_bit_criteria(
                co2_inclusions, co2_frequency, bit_index, False
            )
        if 1 < len(o2_inclusions) < 1 or 1 < len(co2_inclusions) < 1:
            raise RuntimeError("Couldn't resolve o2 or co2 rate to a valid value.")
        self.o2 = self.diagnostic_data[o2_inclusions[0]]
        self.co2 = self.diagnostic_data[co2_inclusions[0]]
        self.gamma = int(gamma_bits, 2)  # convert the gamma bits to int

    def __evaluate_bit_criteria(
        self, inclusion_indices, frequency, bit_index, most
    ) -> []:
        """Helper function to identify drop indexes that no longer meet bit
        criteria.

        :param inclusion_indices: The prior inclusion indices.
        :param frequency: The high bit frequency for the bit position.
        :param bit_index: The column of bits being evaluated.
        :param most: True if we are evaluating for most popularity.
        :return: The posterior inclusion indices.
        """
        if len(inclusion_indices) > 1:  # Then we need to keep evaluating
            high_comm = frequency >= len(inclusion_indices) / 2  # Is 1 more common
            bitmask = 2 ** (self.num_bits - bit_index - 1)
            inclusion_indices = [  # Reduce inclusion indices
                data_index
                for data_index in inclusion_indices
                if (  # Include on if match on current bit popularity
                    (
                        most  # o2 rate
                        and (
                            high_comm  # should be hi
                            and self.diagnostic_data[data_index] & bitmask > 0
                            or not high_comm  # should be lo
                            and self.diagnostic_data[data_index] & bitmask == 0
                        )
                    )
                    or (
                        not most  # co2 rate
                        and (
                            high_comm  # should be lo
                            and self.diagnostic_data[data_index] & bitmask == 0
                            or not high_comm  # should be hi
                            and self.diagnostic_data[data_index] & bitmask > 0
                        )
                    )
                )
            ]
        return inclusion_indices

    def __compute_epsilon_rate(self):
        """Computes the epsilon rate as the complement of the gamma rate."""
        self.epsilon = (~self.gamma) & (2 ** self.num_bits - 1)
