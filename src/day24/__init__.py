"""--- Day 24: Arithmetic Logic Unit ---"""
from pathlib import Path

from aoc import open_utf8
from day24 import alu
from day24.alu import ALU
from day24.alu import Instruction


def find_model_limit(monad: [Instruction], highest: bool) -> int:
    """Takes in a list of ALU instructions loaded from the MONAD dataset.

    :param monad: List of ALU instructions.
    :param highest: Boolean describing if we are looking for the highest or lowest solution.
    :return: Integer of the matching part-number if found else -1.
    """
    test_alu = ALU()
    test_range = __optimise_monad_input(monad, highest)
    for test_list in test_range:  # 11111111111111, -1):
        test_alu.execute_program(monad, test_list)
        if test_alu.z == 0:  # tested list has monad digits
            return int("".join(str(d) for d in test_list))
        test_alu.clear_registers()
    return -1  # Didn't locate a z=0 match


def __optimise_monad_input(monad: [Instruction], highest: bool):
    """Takes in the monad dataset and computes optimal solution based on digit
    dependencies.

    :param monad: List of ALU instructions in the MONAD program.
    :param highest: Boolean describing if we are searching for the highest or lowest solution.
    :return: A list of input values to check.
    """
    sub_instructions = []  # Capture the routine for each input digit.
    for instruction in monad:
        # Break the instruction into sub-instructions
        if instruction.b is None:  # Start next sub instruction on input.
            sub_instructions.append([instruction])
        else:
            sub_instructions[-1].append(instruction)
    # Start at max value for part 1.
    goal = [9 if highest else 1 for _ in range(len(sub_instructions))]
    z_base_26 = []
    for digit_index, sub_instruction in enumerate(sub_instructions):
        # The following are the unique values in each of the sub-instructions.
        z_div = sub_instruction[4].b  # z divisor (1 or 26)
        x_add = sub_instruction[
            5
        ].b  # x addition (<= 0 if z_div 1 or >= 10 if z_div 26)
        y_add = sub_instruction[15].b  # y addition
        if z_div == 1:  # accumulates z offset restriction on future input.
            z_base_26.append([digit_index, y_add])
        else:  # z = 26 which is the last element added to base_26 list.
            independent_index, y_add = z_base_26.pop()
            goal[digit_index] = goal[independent_index] + y_add + x_add
            # Offset on independent index to correct on current dependant index.
            # Unsure if this would work for all cases
            if goal[digit_index] >= 10:
                goal[independent_index] = goal[independent_index] - (
                    goal[digit_index] - 9
                )
                goal[digit_index] = 9
            elif goal[digit_index] <= 0:
                goal[independent_index] = goal[independent_index] + (
                    1 - goal[digit_index]
                )
                goal[digit_index] = 1
    return [goal]


def load_dataset(dataset_path: Path) -> [Instruction]:
    """Returns the program as a list of alu instructions."""
    with open_utf8(dataset_path) as file:
        program = []
        for line in file:
            if len(line.strip()) > 0:
                instruction = line.strip().split(" ")
                if len(instruction) == 2:
                    instruction.append(None)  # No b value
                else:
                    try:  # B instruction is constant.
                        instruction[2] = int(instruction[2])
                    except ValueError:
                        pass  # B instruction is string reference.
                program.append(
                    Instruction(
                        func=getattr(alu, instruction[0]),
                        a=instruction[1],
                        b=instruction[2],
                    )
                )
    return program
