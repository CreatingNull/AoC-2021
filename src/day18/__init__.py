"""--- Day 18: Snailfish ---"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

from aoc import open_utf8


@dataclass
class SnailfishNumber:
    """Captures a node in the binary tree."""

    left: int | SnailfishNumber = None
    right: int | SnailfishNumber = None
    # None is a tree root
    parent: SnailfishNumber | None = None
    # Tracks if this is the left or right child
    is_left: bool = True

    def set_data(self, data):
        """Populates the data in the node, with priority left."""
        if self.left is not None:
            self.right = data
            if isinstance(data, SnailfishNumber):
                data.is_left = False
        else:
            self.left = data

    def push_value(self, value: int, left: bool) -> bool:
        """Pushes a value all the way down a branch to sum with the leaf.

        :param value: Value to add to the leaf value.
        :param left: Boolean describing if you are pushing to the left or right.
        :return: True if successful push.
        """
        # Tree must be syntactically correct for this to work
        attribute = "left" if left else "right"
        current_node = self
        while isinstance(getattr(current_node, attribute), SnailfishNumber):
            current_node = getattr(current_node, attribute)
        if getattr(current_node, attribute) is None:
            return False  # nothing valid in this branch
        setattr(current_node, attribute, getattr(current_node, attribute) + value)
        return True

    def sub_tree(self) -> str:
        """Returns a string that represents the tree below this node."""
        tree = "["
        if isinstance(self.left, int):
            tree += str(self.left)
        else:
            tree += self.left.sub_tree()
        tree += ","
        if isinstance(self.right, int):
            tree += str(self.right)
        elif self.right:  # None is a valid right from vestigial []
            tree += self.right.sub_tree()
        return tree + "]"


def __split_pair(number: SnailfishNumber, left: bool) -> int | None:
    """Splits a number into a pair if the number is >= 10.

    :param number: Number node from the binary tree.
    :param left: Boolean if we are inspecting the right or left leaf.
    :return: 1 if we split else None.
    """
    # Search for the leftmost number greater or equal to 10.
    if left and isinstance(number.left, int) and number.left >= 10:
        # Split left number into pair
        number.left = SnailfishNumber(
            parent=number,
            left=number.left // 2,  # floor
            right=-(number.left // -2),  # ceil
            is_left=True,
        )
        return 1
    if not left and isinstance(number.right, int) and number.right >= 10:
        number.right = SnailfishNumber(
            parent=number,
            left=number.right // 2,
            right=-(number.right // -2),
            is_left=False,
        )
        return 1
    return None


def __explode_pair(number: SnailfishNumber, level: int = 0) -> []:
    """Explodes a tree node if nested more than 3 layers.

    :param number: Tree node to inspect for explosion.
    :param level: Current layer of the tree.
    :return: list containing the left number, right number, tree level.
    """
    if level > 3:
        if isinstance(number.left, int) and isinstance(number.right, int):
            # removes self, makes parent node 0 and bubbles values back up tree.
            if number.is_left:
                number.parent.left = 0
            else:
                number.parent.right = 0
            return [number.left, number.right, level]
    return None


def __bubble_result(number: SnailfishNumber, result: []):
    """Adds carries to the correct location after explosion.

    :param number: Number to inspect for bubble addition.
    :param result: Left num, right num, explosion level, left/right
    :return:
    """
    if result is not None and isinstance(result, list):
        push_left = False
        push_right = False
        # Parent conditions
        if result[3] == 0 and result[1] != -1:
            push_right = True  # Can push to parent's right branch if valid
        elif result[3] == 1 and result[0] != -1:
            push_left = True  # Can push to parent's left branch
        if push_right and result[1] != -1:
            if isinstance(number.right, SnailfishNumber):
                if number.right.push_value(result[1], True):
                    result[1] = -1
            elif isinstance(number.right, int):
                number.right += result[1]
                result[1] = -1
        if push_left and result[0] != -1:
            if isinstance(number.left, SnailfishNumber):
                if number.left.push_value(result[0], False):
                    result[0] = -1
            elif isinstance(number.left, int):
                number.left += result[0]
                result[0] = -1


# burnt out on this problem so suppressing, may come back and fix.
# pylint: disable=R0912
def perform_operation(number: SnailfishNumber, split, layer: int = 0):
    """traverses the tree and executes explosion / split pair."""
    if split:
        result_split = __split_pair(number, True)
        if result_split is not None:
            return result_split
    else:
        result_explode = __explode_pair(number, layer)
        if result_explode is not None:  # exploded a pair
            return result_explode
    result = None
    # recurse left first
    if isinstance(number.left, SnailfishNumber):
        result = perform_operation(number.left, split, layer + 1)
        if result is not None:
            if isinstance(result, int) and result == 1:
                return result  # we had a successful split
            if layer + 1 == result[2]:
                result.append(0)  # We were in the left branch
            else:
                result[3] = 0  # we are coming from the left branch.
    if result is None and isinstance(number.right, SnailfishNumber):
        result = perform_operation(number.right, split, layer + 1)
        if result is not None:
            if isinstance(result, int) and result == 1:
                return result
            if layer + 1 == result[2]:
                result.append(1)  # We were in the right branch
            else:
                result[3] = 1  # We are coming from the right branch.
    __bubble_result(number, result)
    if split:  # splitting right is lower priority than left branch
        return __split_pair(number, False)
    return result


def reduce_number(number: SnailfishNumber) -> []:
    """Loops the number until no explosions or splits occur."""
    while perform_operation(number, False) or perform_operation(number, True):
        continue
    return number


def get_magnitude(number: SnailfishNumber) -> int:
    """Traverses the tree and sums the magnitudes."""
    if isinstance(number, int):
        return number  # values are their literal magnitude.
    return get_magnitude(number.left) * 3 + get_magnitude(number.right) * 2


def add_all_numbers(numbers: [SnailfishNumber]):
    """Part 1 summing all the numbers."""
    # Adding two numbers adds a higher level parent node.
    number_left = numbers[0]
    for number_right in numbers[1:]:
        new_root = SnailfishNumber(
            parent=None,
            left=number_left,
            right=number_right,
        )
        new_root.left.parent = new_root
        new_root.right.parent = new_root
        # As all roots are set left by default
        new_root.right.is_left = False
        reduce_number(new_root)
        number_left = new_root
    return get_magnitude(number_left)


def find_greatest_magnitude(numbers: [SnailfishNumber]):
    """Part 2 finding the max magnitude of two numbers."""
    mod_max = 0
    for index_left, number_left in enumerate(numbers):
        for index_right, number_right in enumerate(numbers):
            if index_left != index_right:  # numbers must be different
                new_root = SnailfishNumber(
                    parent=None,
                    left=deepcopy(number_left),
                    right=deepcopy(number_right),
                )
                new_root.left.parent = (new_root,)
                new_root.right.parent = (new_root,)
                new_root.right.is_left = (False,)
                reduce_number(new_root)
                mod_max = max(mod_max, get_magnitude(new_root))
    return mod_max


def load_dataset(dataset_path: Path):
    """Loads binary data from file into an array of binary tree nodes."""
    nodes = []
    with open_utf8(dataset_path) as file:
        # Not a good idea in general unless you trust the source.
        current_node = None
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            accumulator = ""
            for char in line:
                if char == "[":  # creating a new node.
                    new_node = SnailfishNumber(
                        parent=current_node,
                    )
                    if current_node is not None:
                        current_node.set_data(new_node)
                    current_node = new_node
                elif char == "]":  # returning to parent node.
                    if len(accumulator) > 0:
                        current_node.set_data(int(accumulator))
                    if not current_node.parent:  # we reached the root.
                        nodes.append(current_node)
                    accumulator = ""
                    current_node = current_node.parent
                elif char == ",":  # clear the accumulator
                    if len(accumulator) > 0:
                        current_node.set_data(int(accumulator))
                    accumulator = ""
                else:  # build a literal value
                    accumulator += char
    return nodes
