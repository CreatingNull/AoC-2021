# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 22: Reactor Reboot ---

This package contains the source and data for [day 22](https://adventofcode.com/2021/day/22) of the challenge.

* Status: Complete
* Difficulty Rating: 3.5 / 5

## Post-Task Thoughts

I'm back to enjoying this again, really fun task with this one!
It was clear from the dataset what the part 2 was going to be, so I planned my design for the full instruction set from the start.
This saved me having to mess around refactoring or redesigning for part 2.

Basically for my solution I compute the reaction core from a list of instruction 'cuboid' objects.
Each time an instruction is added, if it intersects with any existing instructions on the stack, I add a compensation cuboid for the intersected area such that it'll negate any mistake I introduced.
There are more efficient ways of doing this, but I think the solution actually turned out pretty elegant, definitely the solution I have been most proud of in the last week.

I am finding the key to these 3 dimensional tasks is to consider the problems in lower dimensional space first (1d or 2d) and then extend to higher dimensions.
Most of this stuff is orthogonal between dimensions, eg: x doesn't influence y so they can be considered in isolation.
It's also easier to draw and visualise in lower dimensional space, which is always a bonus.
