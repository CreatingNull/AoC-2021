"""--- Day 5: Hydrothermal Venture ---"""
from dataclasses import dataclass
from operator import add
from operator import sub
from pathlib import Path


@dataclass
class Point:

    x: int
    y: int
    value_hv: int = 0
    value_d: int = 0


@dataclass
class Vent:

    p1: Point
    p2: Point

    def compute_cartesian_points(self) -> {str: Point}:
        """Compute the points crossed by the line in the vent.

        :return: Dictionary of 'x,y' keys to populated Point values.
        """
        run = self.p2.x - self.p1.x  # how far we move in the x dimension
        rise = self.p2.y - self.p1.y  # how far we move in the y dimension
        run_op = add if run > 0 else sub  # polarity of x movement
        rise_op = add if rise > 0 else sub  # polarity of y movement
        steps = range((abs(run) if abs(run) > 0 else abs(rise)) + 1)
        return {
            f"{run_op(self.p1.x, step if abs(run) else 0)},"
            f"{rise_op(self.p1.y, step if abs(rise) else 0)}": Point(
                run_op(self.p1.x, step if abs(run) else 0),
                rise_op(self.p1.y, step if abs(rise) else 0),
                value_hv=1 if rise == 0 or run == 0 else 0,
                value_d=1 if rise != 0 and run != 0 else 0,
            )
            for step in steps
        }


def load_dataset(dataset_path: Path) -> {str: Point}:
    """Loads the vents from file, returns a list of cartesian points.

    :param dataset_path: Path object to load the data from.
    :return: Dictionary of 'x,y' keys with populated Point values.
    """
    data = {}
    with open(dataset_path) as file:
        for line in file:
            if len(line.strip()) > 1:
                vent = Vent(
                    Point(
                        int(line.split(" -> ")[0].split(",")[0].strip()),
                        int(line.split(" -> ")[0].split(",")[1].strip()),
                    ),
                    Point(
                        int(line.split(" -> ")[1].split(",")[0].strip()),
                        int(line.split(" -> ")[1].split(",")[1].strip()),
                    ),
                )
                points = vent.compute_cartesian_points()
                for point in points:
                    if point in data:  # Multiple
                        data[point].value_hv += points[point].value_hv
                        data[point].value_d += points[point].value_d
                    else:  # Add the point to the global dataset
                        data[point] = points[point]
    return data
