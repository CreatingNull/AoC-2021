"""--- Day 16: Packet Decoder ---"""
from dataclasses import dataclass
from functools import reduce
from operator import add
from operator import eq
from operator import gt
from operator import lt
from operator import mul
from pathlib import Path

from bitarray import bitarray
from bitarray.util import ba2int
from bitarray.util import hex2ba

from aoc import open_utf8


# Lookup table for resolving packet types to built in operators
OPERATORS = {0: add, 1: mul, 2: min, 3: max, 5: gt, 6: lt, 7: eq}


@dataclass
class Packet:
    """Object for storing a single packet of eq info."""

    version: int  # Stores the version info for the packet
    type: int  # Stores the operator type key / value key
    value_int: int = -1  # stores the literal value, -1 if not literal
    sub_packets: [object] = None  # stores a list of related packets
    bit_length: int = 0  # For keeping track of the binary cursor

    def __init__(self, binary_data: bitarray):
        self.version = ba2int(binary_data[0:3])
        self.type = ba2int(binary_data[3:6])
        cursor = 6
        if self.type == 4:  # stores a value
            # Value is n*5 bit sections with leading 1s until last
            value_bin = bitarray()
            for n in range(0, len(binary_data), 5):
                value_bin.extend(binary_data[7 + n : 11 + n])
                if binary_data[6 + n] == 0:  # found the last value nibble
                    cursor = 11 + n
                    break
            self.value_int = ba2int(value_bin)
        else:  # operator packet
            length_type_id = binary_data[6]
            if length_type_id == 0:  # sub-packets on length
                packet_length = ba2int(binary_data[7:22])
                cursor = 22 + self.add_sub_packets(binary_data[22 : 22 + packet_length])
            else:  # sub-packets on number of packets
                num_packets = ba2int(binary_data[7:18])
                cursor = 18 + self.add_sub_packets(binary_data[18:], num_packets)
        self.bit_length = cursor

    def add_sub_packets(self, binary_data, num: int = -1) -> int:
        """Adds packets from binary data via one of the two supported schemes.

        :param binary_data: The truncated binary data to obtain sub-packets from.
        :param num: The number of packets to obtain, -1 if using binary_data length.
        :return: Integer of the current cursor movement while adding binary data.
        """
        if not self.sub_packets:
            self.sub_packets = []
        cursor = 0
        while (len(self.sub_packets) != num and num != -1) or (
            num == -1 and cursor != len(binary_data)
        ):
            sub_packet = Packet(binary_data[cursor:])
            self.sub_packets.append(sub_packet)
            cursor += sub_packet.bit_length
        return cursor

    def compute_equation(self) -> (int, int):
        """Recursive function to compute the sum from the loaded packet tree.

        :return: The version sum of all packets in the tree, the equation result.
        """
        if self.value_int > -1:  # Is a value so no calculation required
            return self.version, self.value_int
        operator = OPERATORS[self.type]
        versions = []
        values = []
        for sub_packet in self.sub_packets:
            version, value = sub_packet.compute_equation()
            versions.append(version)
            values.append(value)
        return sum(versions) + self.version, int(reduce(operator, values))


def load_dataset(dataset_path: Path) -> bitarray:
    """Loads binary data from file into a bitarray."""
    with open_utf8(dataset_path) as file:
        return hex2ba(file.readline().strip())
