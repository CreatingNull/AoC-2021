"""--- Day 17: Trick Shot ---"""
from dataclasses import dataclass
from pathlib import Path

from aoc import open_utf8


@dataclass
class Probe:
    """Our submarine launchable probe object."""

    goal_x: []  # min and max goal values
    goal_y: []
    x: int = 0  # x launch velocity
    y: int = 0  # y launch velocity

    def y_steps(self) -> set:
        """Find where a launch velocity in the y dimension intersects."""
        y_cur = self.y
        y_n_minus_1 = 0
        y_location = self.y  # launch step
        step = 1
        output = set()  # empty set means never touches
        # Loop while going up or higher than goal location.
        while (y_location - y_n_minus_1) > 0 or y_location >= self.goal_y[0]:
            if self.goal_y[0] <= y_location <= self.goal_y[1]:
                output.add(step)
            y_cur -= 1  # gravity
            y_n_minus_1 = y_location
            y_location += y_cur
            step += 1
        return output

    def x_steps(self, bound: int) -> set:
        """Find where a launch velocity in the x dimension intersects."""
        x_cur = self.x
        x_location = self.x
        step = 1
        output = set()
        while (x_location <= self.goal_x[1] and self.x > 0) or (
            self.goal_x[0] <= x_location and self.x < 0
        ):
            if self.goal_x[0] <= x_location <= self.goal_x[1]:
                output.add(step)
            if x_cur > 0:
                x_cur -= 1
            elif x_cur < 0:
                x_cur += 1
            x_location += x_cur
            step += 1
            if step > bound:  # if we stop moving in the x goal
                break
        return output

    def find_goal_steps(self):
        """Finds the step where we land in the objective, empty set if
        never."""
        steps = self.y_steps()
        if len(steps) > 0:  # find the intersection
            steps &= self.x_steps(bound=max(steps))
        return steps


def search_launch_speeds(probe: Probe):
    """Find all the launch parameters that'll get us to the goal.

    :param probe: Our probe object populated with the goal region.
    :return: Max height we can reach, total number of good launch parameters.
    """
    # Find numbers where the return path ends up in the goal region
    y_speeds = []
    y_steps = set()
    max_launch_y = 0
    for i in range(probe.goal_y[0], abs(probe.goal_y[0])):
        probe.y = i
        steps = probe.y_steps()
        y_speeds.append(i)
        y_steps |= steps
        max_launch_y = max(max_launch_y, i)
    x_speeds = []
    bound = max(y_steps)  # No point searching beyond what we can hit with y
    for i in range(probe.goal_x[1] + 1):
        if nth_triangular_number(i) >= probe.goal_x[0]:
            probe.x = i
            steps = probe.x_steps(bound)
            if len(steps) > 0 and len(steps & y_steps) > 0:
                x_speeds.append(i)
    launch_options = set()
    for y_speed in y_speeds:
        probe.y = y_speed
        for x_speed in x_speeds:
            probe.x = x_speed
            steps = probe.find_goal_steps()
            if len(steps) > 0:
                launch_options.add((x_speed, y_speed))
    return nth_triangular_number(max_launch_y), len(launch_options)


def nth_triangular_number(number: int) -> int:
    """Function to compute the triangular number for a positive integer.

    :param number: The integer n to compute the triangular number.
    :return: The resulting integer triangular number.
    """
    return number * (number + 1) // 2  # I like to call this the 'addition-factorial'


def load_dataset(dataset_path: Path) -> Probe:
    """Loads binary data from file into a bitarray."""
    with open_utf8(dataset_path) as file:
        data = file.readline().strip().split("x=")
        return Probe(
            goal_x=[int(n) for n in data[1].split(",")[0].split("..")],
            goal_y=[int(n) for n in data[1].split("y=")[1].split("..")],
        )
