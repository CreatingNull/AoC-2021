"""Module contains the submarines replacement ALU."""
from dataclasses import dataclass


@dataclass
class Instruction:
    """Class captures the ALU instruction functionality and arguments."""

    func: callable  # operation to perform.
    a: str  # reference to the ALU register
    b: int | str = None  # constant, or reference / Nothing.


@dataclass
class ALU:
    """Class used to capture the state of the ALU."""

    w: int = 0
    x: int = 0
    y: int = 0
    z: int = 0

    def execute_program(self, program: [Instruction], input_values: [int]):
        """Run a set of operations on the ALU providing a list of input values
        where required."""
        input_index = 0
        for instruction in program:
            if instruction.b is None:  # use input as b
                instruction.func(self, instruction.a, input_values[input_index])
                input_index += 1
            else:
                instruction.func(self, instruction.a, instruction.b)

    def clear_registers(self):
        """Reinit the default state of the ALU."""
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0


def inp(alu: ALU, a: str, input_value: int):
    """Read an input value and write it to variable `a`"""
    setattr(alu, a, input_value)


def add(alu: ALU, a: str, b: int | str):
    """Add the value of `a` to the value of `b`, then store the result in
    variable `a`"""
    setattr(alu, a, getattr(alu, a) + (getattr(alu, b) if isinstance(b, str) else b))


def mul(alu: ALU, a: str, b: int | str):
    """Multiply the value of `a` by the value of `b`, then store the result in
    variable `a`"""
    setattr(alu, a, getattr(alu, a) * (getattr(alu, b) if isinstance(b, str) else b))


def div(alu: ALU, a: str, b: int | str):
    """Divide the value of `a` by the value of `b`, truncate the result to an
    integer, then store the result in variable `a`.

    (Here, "truncate" means to round the value toward zero.)
    """
    setattr(alu, a, getattr(alu, a) // (getattr(alu, b) if isinstance(b, str) else b))


def mod(alu: ALU, a: str, b: int | str):
    """Divide the value of `a` by the value of `b`, then store the remainder in
    variable `a`.

    (This is also called the modulo operation.)
    """
    setattr(alu, a, getattr(alu, a) % (getattr(alu, b) if isinstance(b, str) else b))


def eql(alu: ALU, a: str, b: int | str):
    """If the value of `a` and `b` are equal, then store the value 1 in
    variable `a`.

    Otherwise, store the value 0 in variable a.
    """
    setattr(
        alu, a, int(getattr(alu, a) == (getattr(alu, b) if isinstance(b, str) else b))
    )
