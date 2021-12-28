"""--- Day 23: Amphipod ---"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from heapq import heappop
from heapq import heappush
from pathlib import Path

from frozendict import frozendict

from aoc import open_utf8


# LUT for checking the cost of making a movement with the amphipod type
MOVE_COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
# LUT for finding the goal amphipod for a room index.
ROOM_OCCUPANTS = {0: "A", 1: "B", 2: "C", 3: "D"}
# LUT for room hallway index the duplication is for hash lookup in either direction.
ROOM_INDICIES = {"A": 0, "B": 1, "C": 2, "D": 3}
# LUT for finding hallway index of room entrance from room index.
ROOM_ENTRANCES = {0: 2, 1: 4, 2: 6, 3: 8}


@dataclass(frozen=True)
class Map:
    """Object stores a current game-state."""

    rooms: frozendict  # Frozendict containing the state of the rooms.
    hallway: tuple  # Tuple containing the state of the hallway.
    cost: int = 0  # Accrued cost of reaching this state.

    def add_next_states(self, heap: [], room_size: int):
        """Find the next possible game states and add to heap.

        :param heap: The dijkstra heap.
        :param room_size: The size of the rooms in our dataset.
        :return:
        """
        # First check what we could move from a room
        for room_key, room_occupants in self.rooms.items():
            # Each top node could move to any of the unlocked all way spaces
            if len(room_occupants) > 0:
                if self.__correctly_tenanted(room_key):
                    continue  # don't remove from rooms where they have the correct type
                for position, steps in Map.out_moves(self.hallway, room_key):
                    new_rooms = dict(self.rooms)
                    occupant = new_rooms[room_key][-1]  # remove the top node
                    new_rooms[room_key] = tuple(
                        (room for room in new_rooms[room_key][0:-1])
                    )
                    new_hallway = (
                        self.hallway[:position]
                        + tuple(occupant)
                        + self.hallway[position + 1 :]
                    )
                    heappush(
                        heap,
                        Map(
                            rooms=frozendict(new_rooms),
                            hallway=tuple(new_hallway),
                            cost=(
                                self.cost
                                + MOVE_COST[occupant]
                                * (  # Plus 1 when moving out only.
                                    room_size - len(room_occupants) + 1 + steps
                                )
                            ),
                        ),
                    )
        # Now find the states that can come from hallway movement into rooms
        for position, occupant in enumerate(self.hallway):
            if occupant is not None:  # There is an amphipod here
                # The only valid movement is into the applicable room.
                room_key = ROOM_INDICIES[occupant]
                if (
                    num_steps := Map.in_move(
                        self.hallway, self.rooms, room_key, position
                    )
                ) is not None:
                    # It is valid to move into the room.
                    new_rooms = dict(self.rooms)
                    new_rooms[room_key] = tuple(new_rooms[room_key] + tuple(occupant))
                    new_hallway = (
                        self.hallway[:position]
                        + tuple([None])
                        + self.hallway[position + 1 :]
                    )
                    heappush(
                        heap,
                        Map(
                            rooms=frozendict(new_rooms),
                            hallway=tuple(new_hallway),
                            cost=(
                                self.cost
                                + MOVE_COST[occupant]
                                * (room_size - len(self.rooms[room_key]) + num_steps)
                            ),
                        ),
                    )

    @staticmethod
    @lru_cache(maxsize=None)
    def out_moves(hallway: [], room: int) -> [tuple]:
        """Computes a list of the possible moves out from a room.

        :param hallway: List of the current hallway state in the Map.
        :param room: Index of the room we are coming out from.
        :return: List of possible hallway index, and steps to get there.
        """
        # Determine the possible positions for moving from the room.
        positions = []
        for index in range(len(hallway)):
            if index in ROOM_ENTRANCES.values():
                continue  # We can't stop on a room entrance
            if index < ROOM_ENTRANCES[room] and all(  # max range +1 not req.
                value is None for value in hallway[index : ROOM_ENTRANCES[room]]
            ):  # If we are unblocked to this index it is a possible move.
                positions.append((index, ROOM_ENTRANCES[room] - index))
            elif index > ROOM_ENTRANCES[room] and all(
                value is None for value in hallway[ROOM_ENTRANCES[room] : index + 1]
            ):
                positions.append((index, index - ROOM_ENTRANCES[room]))
        return positions

    @staticmethod
    def in_move(hallway: [], rooms: {}, room: int, from_index: int) -> int | None:
        """Finds if the nodes can move in from the hallway.

        :param hallway: List of hallway from the Map.
        :param rooms: Dictionary of rooms from the Map.
        :param room: The index of the goal room in the room's dict.
        :param from_index: The index of the hallway node.
        :return: Steps taken if the node can move home.
        """
        # Check other tenants of the room are correct
        if all(tenant == ROOM_OCCUPANTS[room] for tenant in rooms[room]):
            # Then a move is valid if we can make it.
            if from_index < ROOM_ENTRANCES[room] and all(
                value is None
                for value in hallway[from_index + 1 : ROOM_ENTRANCES[room]]
            ):
                return ROOM_ENTRANCES[room] - from_index
            if from_index > ROOM_ENTRANCES[room] and all(  # min range +1 not req.
                value is None for value in hallway[ROOM_ENTRANCES[room] : from_index]
            ):
                return from_index - ROOM_ENTRANCES[room]
        return None

    @staticmethod
    def check_solved(hallway: [], rooms: {}) -> bool:
        """Checks if the game state is complete."""
        return all(
            occupant == ROOM_OCCUPANTS[room]
            for room in rooms
            for occupant in rooms[room]
        ) and all(hall is None for hall in hallway)

    def __correctly_tenanted(self, room) -> bool:
        """Checks if only correct type amphipod are in the room."""
        return all(occupant == ROOM_OCCUPANTS[room] for occupant in self.rooms[room])

    def __lt__(self, other):
        return self.cost < other.cost


def solve_puzzle(starting_map: Map) -> (int | None, int):
    """Runs a dijkstra algorithm to iteratively search through game states.

    :param starting_map: Map object containing the starting state.
    :return: Tuple containing minimum cost, iterations taken to find result.
    """
    heap = [starting_map]  # For storing the dijkstra heap
    duplicates = set()  # For storing states we have visited via other paths
    room_size = len(starting_map.rooms[0])
    count = 0
    while heap:
        current_map = heappop(heap)
        if current_map in duplicates:
            continue  # No point exploring this again.
        if current_map.check_solved(current_map.hallway, current_map.rooms):
            return current_map.cost, count
        current_map.add_next_states(heap, room_size)
        duplicates.add(current_map)
        count += 1
    return None, count


def load_dataset(dataset_path: Path, paper_folded: bool):
    """Returns a list of instructions as cuboid objects."""
    with open_utf8(dataset_path) as file:
        lines = file.readlines()
        hallway_length = lines[1].count(".")
        room_occupants = [
            line.strip().replace("#", "")
            for line in lines[2:]
            if len(line.strip().replace("#", "")) > 0
        ]
        if paper_folded:  # Part 2 adds some hidden size to the rooms
            room_occupants = [room_occupants[0], "DCBA", "DBAC", room_occupants[-1]]
        rooms = {i: [] for i in range(len(room_occupants[0]))}
        room_occupants.reverse()  # makes it easier to pop the top.
        for level in room_occupants:
            for index, char in enumerate(level):
                rooms[index].append(char)
        for index in rooms:
            rooms[index] = tuple(rooms[index])  # make hashable
        map_state = Map(
            rooms=frozendict(rooms),
            hallway=tuple(None for _ in range(hallway_length)),
        )
    return map_state
