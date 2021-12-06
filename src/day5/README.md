# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 5: Hydrothermal Venture ---

This package contains the source and data for [day 5](https://adventofcode.com/2021/day/5) of the challenge.

* Status: Complete
* Difficulty Rating: 2 / 5

## Post-Task Thoughts

Fun task, basically computation of Cartesian points.
Because we are iterating through multiple vents trying to look for matching points, storing points in a dictionary makes a lot of sense as you can utilise the efficiency of hashed lookups.
It was easy to design for this task as it was clear in part 1 what the scope of the second part was going to be (diagonal lines), so I think everyone was able to prepare themselves for handling this case.

One library I found particularly helpful for this task that I have previously not used extensively, was the [operator](https://docs.python.org/3/library/operator.html) lib.
Having quick and easy access to variable operator functions can be a very helpful in reducing duplication of large calculations.
Definitely adding this to the tool-belt for the future.
