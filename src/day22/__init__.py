"""--- Day 22: Reactor Reboot ---"""
from dataclasses import dataclass
from pathlib import Path

from aoc import open_utf8


# Used to compute the polarity of correction cuboids on intersection
POLARITY_LUT = {  # [New value][existing value] -> polarity
    -1: {-1: 1, 1: -1},
    1: {-1: 1, 1: -1},
}


@dataclass(frozen=True)
class Cuboid:
    """Class to hold an instruction / correction applied to the reactor."""

    polarity: int  # describes if this enables '1' or disables '-1' cubes.
    x_lo: int
    x_hi: int
    y_lo: int
    y_hi: int
    z_lo: int
    z_hi: int

    def num_cubes(self) -> int:
        """Returns the number of cube nodes within the cuboid."""
        return (  # +1 because is the grid nodes not the volume
            (self.x_hi - self.x_lo + 1)
            * (self.y_hi - self.y_lo + 1)
            * (self.z_hi - self.z_lo + 1)
        )

    def init_sequence(self) -> bool:
        """Checks if the cuboid could be part of the initialisation
        sequence."""
        return (
            self.x_lo > -50
            and self.x_hi < 50
            and self.y_lo > -50
            and self.y_hi < 50
            and self.z_lo > -50
            and self.z_hi < 50
        )


def __intersection(cuboid_existing: Cuboid, new_cuboid: Cuboid):
    """Takes in two cuboid nodes, checks if they intersect and returns a
    correction cuboid to compensate for if they do.

    :param cuboid_existing: The existing cuboid in the reactor.
    :param new_cuboid: The new instruction to apply.
    :return: A subtractive or additive cuboid to correct for the instruction insertion.
    """
    # Checks if the nodes intersect

    if (
        new_cuboid.x_hi < cuboid_existing.x_lo
        or new_cuboid.x_lo > cuboid_existing.x_hi
        or new_cuboid.y_hi < cuboid_existing.y_lo
        or new_cuboid.y_lo > cuboid_existing.y_hi
        or new_cuboid.z_hi < cuboid_existing.z_lo
        or new_cuboid.z_lo > cuboid_existing.z_hi
    ):
        return None  # No intersection
    # Returns the subtractive intersection cuboid if they intersect.
    # This is to reverse any incorrect influence adding the new cuboid would have.
    return Cuboid(
        # Intersections only add if we are compensating for a negative overlap.
        polarity=POLARITY_LUT[new_cuboid.polarity][cuboid_existing.polarity],
        x_lo=max(cuboid_existing.x_lo, new_cuboid.x_lo),
        x_hi=min(cuboid_existing.x_hi, new_cuboid.x_hi),
        y_lo=max(cuboid_existing.y_lo, new_cuboid.y_lo),
        y_hi=min(cuboid_existing.y_hi, new_cuboid.y_hi),
        z_lo=max(cuboid_existing.z_lo, new_cuboid.z_lo),
        z_hi=min(cuboid_existing.z_hi, new_cuboid.z_hi),
    )


def compute_reactor_state(instructions: [Cuboid], initialise_only: bool):
    """Steps through the reboot instructions and applys them to the reactor.

    :param instructions: List of cuboid instructions loaded from file.
    :param initialise_only: If we are just running the part 1 instructions.
    :return: number of active cubes in the reactor after the instructions execute.
    """
    reactor = []  # to store additive and subtractive cuboids for summation.
    for instruction in instructions:
        if not initialise_only or instruction.init_sequence():
            # Check for instruction intersection with existing cuboids
            subtractive_intersections = (
                []
            )  # negative cuboids required to compensate for additions.
            for cuboid in reactor:
                # If there is an intersection append a negative cuboid to compensate for it.
                if subtractive := __intersection(cuboid, instruction):
                    subtractive_intersections.append(subtractive)
            # subtractive instructions rely on negative intersections
            if instruction.polarity > 0:  # Add additive instructions
                reactor.append(instruction)
            reactor += subtractive_intersections
    active_cubes = 0
    for cuboid in reactor:
        # print(cuboid)
        active_cubes += cuboid.polarity * cuboid.num_cubes()
        # print(cuboid.polarity * cuboid.num_cubes())
    return active_cubes


def load_dataset(dataset_path: Path) -> [Cuboid]:
    """Returns a list of instructions as cuboid objects."""
    with open_utf8(dataset_path) as file:
        cuboids = []
        for instruction in file:
            instruction = instruction.strip()
            if len(instruction) > 0:
                instruction = instruction.split(" ")
                polarity = 1 if instruction[0] == "on" else -1
                instruction = instruction[1].split(",")
                x_range = [int(x) for x in instruction[0].split("x=")[1].split("..")]
                y_range = [int(y) for y in instruction[1].split("y=")[1].split("..")]
                z_range = [int(z) for z in instruction[2].split("z=")[1].split("..")]
                cuboids.append(
                    Cuboid(
                        polarity=polarity,
                        x_lo=x_range[0],
                        x_hi=x_range[1],
                        y_lo=y_range[0],
                        y_hi=y_range[1],
                        z_lo=z_range[0],
                        z_hi=z_range[1],
                    )
                )
    return cuboids
