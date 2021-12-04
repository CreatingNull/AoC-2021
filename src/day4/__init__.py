"""--- Day 4: Giant Squid ---"""
from dataclasses import dataclass
from pathlib import Path

from aoc import log
from numpy import array
from numpy import short
from numpy import sum as sum_


@dataclass
class Bingo:

    bingo_input: array  # A list of the bingo numbers to be called in sequential order
    bingo_boards: array  # 3D array tracking the current state of the bingo boards
    win_order: []  # Set to the index of the winning board when complete
    result_products: []  # Captures the first and last result product values

    def __init__(self, dataset_path: Path):
        """Constructor loads the data and executes the game to populate the
        object."""
        self.win_order = []
        self.result_products = []
        with open(dataset_path) as file:
            self.bingo_input = array(
                [short(entry) for entry in file.readline().split(",")]
            )
            bingo_boards = []  # Easier to build bingo boards in a list.
            for line in file:
                if len(line.strip()) == 0:  # New bingo board
                    bingo_boards.append([])
                else:  # add row to current board
                    bingo_boards[-1].append(
                        [
                            int(entry.strip())
                            for entry in line.strip().split(" ")
                            if len(entry.strip()) > 0  # single digits have extra space
                        ]
                    )
            self.bingo_boards = array(bingo_boards, dtype=short)
            log.info(
                "Loaded day 4 %s dataset of bingo input %d with %d bingo boards",
                dataset_path.name,
                len(self.bingo_input),
                len(self.bingo_boards),
            )
        for called_number in self.bingo_input:  # run the game.
            self.__check_number(called_number)
            if len(self.win_order) == len(self.bingo_boards):  # All boards finished
                break

    def __check_number(self, called_value):
        """Checks if number exists on boards, if so will set number to -1 to
        show it's called.

        :param called_value: The called integer value to mark in the game of bingo.
        :return:
        """
        for board_index in range(len(self.bingo_boards)):
            if (
                board_index not in self.win_order
                and called_value in self.bingo_boards[board_index]
            ):
                log.debug("Found %d in bingo board index %d", called_value, board_index)
                self.bingo_boards[board_index][
                    self.bingo_boards[board_index] == called_value
                ] = -1
                # check for bingo
                if self.__check_bingo(self.bingo_boards[board_index]):
                    if (
                        len(self.win_order) == 0
                        or len(self.win_order) == len(self.bingo_boards) - 1
                    ):
                        # Zero marked elements
                        self.bingo_boards[board_index][
                            self.bingo_boards[board_index] == -1
                        ] = 0
                        summed_value = sum_(self.bingo_boards[board_index])
                        self.result_products.append(summed_value * called_value)
                        log.info(
                            "%s board at index %d. The sum of unmarked elements %d and "
                            "last element %d (product=%d)",
                            "First" if len(self.win_order) == 0 else "Last",
                            board_index,
                            summed_value,
                            called_value,
                            self.result_products[-1],
                        )
                    self.win_order.append(board_index)

    @staticmethod
    def __check_bingo(board: array) -> bool:
        """Checks rows and columns for all -1's indicating all numbers have
        been called.

        :param board: The numpy array / bingo board to chec.
        :return: Boolean, true indicates board has bingo!
        """
        # Check the rows
        for row_index in range(board.shape[0]):
            if all(-1 == board[row_index]):
                return True
        # Check the columns
        for column_index in range(board.shape[1]):
            if all(-1 == board[:, column_index]):
                return True
        return False
