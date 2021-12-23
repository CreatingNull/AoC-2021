"""--- Day 19: Beacon Scanner ---"""
from dataclasses import dataclass
from pathlib import Path

from numpy import array
from numpy import dot
from numpy import short
from numpy import sum as sum_

from aoc import log
from aoc import open_utf8
from day19.transformations import TRANSFORMATIONS


@dataclass
class Scanner:
    """Class to store the scanners and the beacons they can see."""

    name: str
    beacons: [array]  # Contains a list of homogeneous coordinates
    offset: array
    aligned_beacons: [array] = None
    orientation: int = -1

    def transformify(self):
        """Translates the aligned beacons using the LUT."""
        if self.orientation >= 23:
            self.orientation = 0
        else:
            self.orientation += 1
        self.aligned_beacons = [
            dot(TRANSFORMATIONS[self.orientation], beacon) for beacon in self.beacons
        ]


def generate_beacon_map(beacons: [array], beacon_index: int) -> (set, array):
    """Normalises the beacons around a single beacon.

    :param beacons: A list of the beacon arrays.
    :param beacon_index: The index of the beacon to normalise about.
    :return: A set of the normalised beacons, and the origin beacon.
    """
    origin = beacons[beacon_index]
    return {tuple(beacon - origin) for beacon in beacons}, origin


def __align_scanner(reference: Scanner, unknown: Scanner, total_beacons: set):
    """Attempts to match the beacon fields between an aligned and unaligned
    scanner.

    :param reference: The aligned scanner to compare against.
    :param unknown: The unaligned scanner to attempt to align.
    :param total_beacons: Rolling set of all beacons aligned to the origin.
    :return: True if aligns else False.
    """
    for _ in TRANSFORMATIONS:
        for ref_index in range(len(reference.aligned_beacons)):
            ref_map, ref_origin = generate_beacon_map(
                reference.aligned_beacons, ref_index
            )
            for unknown_index in range(len(unknown.aligned_beacons)):
                unknown_map, unknown_origin = generate_beacon_map(
                    unknown.aligned_beacons, unknown_index
                )
                matched_points = sum(1 for point in ref_map if point in unknown_map)
                if matched_points >= 12:
                    unknown.offset = ref_origin - unknown_origin
                    unknown.offset += reference.offset
                    total_beacons |= {
                        tuple(beacon + ref_origin + reference.offset)
                        for beacon in unknown_map
                    }  # reference the unknown nodes to the origin
                    log.debug(
                        "Aligned %s at %s with translation=%d based on shared beacons with %s",
                        unknown.name,
                        unknown.offset,
                        unknown.orientation,
                        reference.name,
                    )
                    return True
        unknown.transformify()  # Orientation tracked internally
    return False


def align_scanners_to_reference(scanners: [Scanner]) -> int:
    """For each unaligned beacon align it to a previously aligned beacon.

    :param scanners: Full list of Scanner data, with reference at 0.
    :return: Total number of beacons.
    """
    total_beacons = {tuple(beacon) for beacon in scanners[0].beacons}
    unaligned = scanners[1:]
    unaligned.reverse()  # their datasets solve faster backwards
    aligned = [scanners[0]]
    ref_indices = [0]  # tracks the reference nodes we need to still compare.
    while len(unaligned) > 0:
        log.debug(
            "Seaching %d unaligned scanners for shared beacons with aligned scanner %s",
            len(unaligned),
            aligned[ref_indices[-1]].name,
        )
        current_reference = ref_indices.pop()
        aligned_indices = [  # align each scanner against reference.
            unknown_index
            for unknown_index, unknown_scanner in enumerate(unaligned)
            if __align_scanner(
                aligned[current_reference], unknown_scanner, total_beacons
            )
        ]
        aligned_indices.reverse()
        for new_index in aligned_indices:
            aligned.append(unaligned[new_index])
            del unaligned[new_index]
            ref_indices.append(len(aligned) - 1)
    return len(total_beacons)


def max_manhattan_distance(scanners: [Scanner]) -> int:
    """Compute the maximum manhattan distance from aligned scanners.

    :param scanners: List of aligned scanner objects.
    :return: Max manhattan integer distance of any two scanners.
    """
    max_dist = 0
    for scanner1 in scanners:
        for scanner2 in scanners:
            if scanner1.name != scanner2.name:
                manhattan_distance = sum_(scanner1.offset - scanner2.offset)
                if manhattan_distance > max_dist:
                    max_dist = manhattan_distance
    return max_dist


def load_dataset(dataset_path: Path):
    """Loads binary data from file into a bitarray."""
    scanners = []
    with open_utf8(dataset_path) as file:
        scanners.append(
            Scanner(name="scanner0", beacons=[], offset=array([0, 0, 0], dtype=short))
        )
        for line in file:
            if len(line.strip()) == 0:  # Next scanner
                scanners[-1].aligned_beacons = scanners[-1].beacons
                scanners.append(
                    Scanner(
                        name=f"scanner{len(scanners)}",
                        beacons=[],
                        offset=array([0, 0, 0], dtype=short),
                    )
                )
            elif "---" not in line:  # Is a beacon
                x, y, z = (value.strip() for value in line.split(","))
                scanners[-1].beacons.append(array([x, y, z], dtype=short))
    scanners[-1].aligned_beacons = scanners[-1].beacons
    return scanners
