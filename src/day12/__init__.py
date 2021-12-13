"""--- Day 12: Passage Pathing ---"""
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path

from aoc import open_utf8


@dataclass
class Cave:
    """Object representing a cave and references to connecting caves."""

    name: str  # Identifier of the name
    thicc: bool  # If the cave can be visited infinite times
    links: {} = field(default_factory=dict)  # adjoining caves objects


def __walk_cave(cave: Cave, path: str, complete_paths: [], exception: bool):
    """Recursive function to explore each link of a cave.

    :param cave: The Cave object to explore from.
    :param path: The current path string up unto this point.
    :param complete_paths: List of all complete paths updated in-place.
    :param exception: If we have an active exception for a small cave on this path.
    :return:
    """
    path = f"{path}{cave.name}"
    for path_name in cave.links:
        if (  # Check if large cave or we have an exception to spend
            cave.links[path_name].thicc
            or path_name not in path
            or (exception and path_name not in ("start", "end"))
        ):
            __walk_cave(
                cave.links[path_name],
                path,
                complete_paths,
                exception
                if (cave.links[path_name].thicc or path_name not in path)
                else False,
            )
    if cave.name == "end":
        complete_paths.append(path)


def enumerate_paths(caves: {}, visit_exception: bool) -> []:
    """Function to start exploring the caves for valid paths.

    :param caves: A dictionary of cave names to Cave objects in the dataset.
    :param visit_exception: If we have the ability to explore a single small cave.
    :return: A list of the valid paths through the caves.
    """
    complete_paths = []
    __walk_cave(caves["start"], "", complete_paths, visit_exception)
    return complete_paths


def load_dataset(dataset_path: Path) -> {Cave}:
    """Loads the cave connectivity graph into a dict of Cave objects."""
    caves = {}
    with open_utf8(dataset_path) as file:
        for line in file:
            cave0, cave1 = line.strip().split("-")
            if cave0 not in caves:
                caves[cave0] = Cave(cave0, cave0.isupper())
            if cave1 not in caves:
                caves[cave1] = Cave(cave1, cave1.isupper())
            if cave1 not in caves[cave0].links and cave0 != "end":
                caves[cave0].links[cave1] = caves[cave1]
            if cave0 not in caves[cave1].links and cave1 != "end":
                caves[cave1].links[cave0] = caves[cave0]
    return caves
