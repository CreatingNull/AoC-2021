"""--- Day 15: Chiton ---"""
from heapq import heappop
from heapq import heappush
from pathlib import Path

from aoc import open_utf8
from numpy import add
from numpy import array
from numpy import byte
from numpy import zeros


class Node:
    """A star path node."""

    x: int
    y: int
    path: set
    cost: int
    heuristic: int = None

    # Reducing the number of arguments here doesn't help us
    # pylint: disable=R0913
    def __init__(self, x, y, parent, cost, end_x, end_y):
        self.x = x
        self.y = y
        if parent:
            self.path = parent.path
            self.path.add((parent.x, parent.y))
        else:
            self.path = set()
        self.cost = cost
        # In our data end is always the last node so this holds without abs
        self.heuristic = end_x - self.x + end_y - self.y + self.cost

    def add_children_to_heap(self, heap: [], search_map: array, end_x, end_y):
        """Adds adjacent nodes as new path ends into the heap.

        :param heap: Current heap object.
        :param search_map: Numpy array of search costs.
        :param end_x: Integer goal index x.
        :param end_y: Integer goal index y.
        :return:
        """
        for x, y in (
            (self.x, self.y + 1),
            (self.x + 1, self.y),
            (self.x, self.y - 1),
            (self.x - 1, self.y),
        ):

            if (x, y) not in self.path:
                if 0 <= x < search_map.shape[1] and 0 <= y < search_map.shape[0]:
                    heappush(
                        heap,
                        Node(x, y, self, self.cost + search_map[y][x], end_x, end_y),
                    )

    def __lt__(self, other):
        return self.heuristic < other.heuristic


def a_starify(search_map: array):
    """Beings an a-star search through the input numpy array.

    :param search_map: Input numpy array.
    :return:
    """
    end_point = (search_map.shape[1] - 1, search_map.shape[0] - 1)
    start_node = Node(0, 0, None, 0, end_point[0], end_point[1])
    heap = []
    start_node.add_children_to_heap(heap, search_map, end_point[0], end_point[1])
    current_node = heap[0]
    loop_count = 0
    while current_node.x != end_point[0] or current_node.y != end_point[1]:
        heappop(heap)  # never need to look at an explored node again
        current_node.add_children_to_heap(heap, search_map, end_point[0], end_point[1])
        current_node = heap[0]
        loop_count += 1
    return loop_count, current_node.cost


def load_dataset(dataset_path: Path, tiling) -> array:
    """Loads map from file."""
    with open_utf8(dataset_path) as file:
        reference = array(
            [
                [byte(char) for char in line.strip()]
                for line in file
                if len(line.strip()) > 0
            ],
            dtype=byte,
        )
    output = array(
        zeros((reference.shape[0] * tiling, reference.shape[1] * tiling)), dtype=byte
    )
    for add_val in range(tiling):  # span horizontally
        new_segment = add(add_val, reference)
        for i in range(add_val):
            new_segment[new_segment == 10 + i] = 1 + i  # wraps on overflow from 9
        output[
            0 : reference.shape[0],
            add_val * reference.shape[1] : (add_val + 1) * reference.shape[1],
        ] = new_segment
    new_reference = output[0 : reference.shape[0]]
    for add_val in range(tiling - 1):  # tile vertically n - 1 times
        new_segment = add(
            add_val + 1,
            new_reference,
        )
        for i in range(add_val + 1):
            new_segment[new_segment == 10 + i] = 1 + i  # wraps on overflow from 9
        output[
            (add_val + 1) * reference.shape[0] : (add_val + 2) * reference.shape[0]
        ] = new_segment
    return output
