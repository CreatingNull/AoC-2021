# ![NullTek Documentation](resources/NullTekDocumentationLogo.png) Advent of Code 2021


[![Language](https://img.shields.io/badge/python-3.10-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3100/)
[![Repo Tests](https://img.shields.io/github/workflow/status/CreatingNull/AoC-2021/Tests?logo=GitHub&style=flat-square&label=tests)](https://github.com/CreatingNull/AoC-2021/actions/workflows/run-tests.yml)
[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square&color=orange)](LICENSE.md)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Stars](https://img.shields.io/badge/progress-50%20stars-000000.svg?logo=star&style=flat-square&color=yellow)](https://adventofcode.com/2021)

Had a stab at the [2021 advent of code](https://adventofcode.com/2021/) challenge.

These are **not** ideal or reference solutions by any stretch of the imagination.

## Progress

| Day | Name                                    | Status                              |
|-----|-----------------------------------------|-------------------------------------|
| 1   | --- Day 1: Sonar Sweep ---              | :star: :star: [Complete](src/day1)  |
| 2   | --- Day 2: Dive! ---                    | :star: :star: [Complete](src/day2)  |
| 3   | --- Day 3: Binary Diagnostic ---        | :star: :star: [Complete](src/day3)  |
| 4   | --- Day 4: Giant Squid ---              | :star: :star: [Complete](src/day4)  |
| 5   | --- Day 5: Hydrothermal Venture ---     | :star: :star: [Complete](src/day5)  |
| 6   | --- Day 6: Lanternfish ---              | :star: :star: [Complete](src/day6)  |
| 7   | --- Day 7: The Treachery of Whales ---  | :star: :star: [Complete](src/day7)  |
| 8   | --- Day 8: Seven Segment Search ---     | :star: :star: [Complete](src/day8)  |
| 9   | --- Day 9: Smoke Basin ---              | :star: :star: [Complete](src/day9)  |
| 10  | --- Day 10: Syntax Scoring ---          | :star: :star: [Complete](src/day10) |
| 11  | --- Day 11: Dumbo Octopus ---           | :star: :star: [Complete](src/day11) |
| 12  | --- Day 12: Passage Pathing ---         | :star: :star: [Complete](src/day12) |
| 13  | --- Day 13: Transparent Origami ---     | :star: :star: [Complete](src/day13) |
| 14  | --- Day 14: Extended Polymerization --- | :star: :star: [Complete](src/day14) |
| 15  | --- Day 15: Chiton ---                  | :star: :star: [Complete](src/day15) |
| 16  | --- Day 16: Packet Decoder ---          | :star: :star: [Complete](src/day16) |
| 17  | --- Day 17: Trick Shot ---              | :star: :star: [Complete](src/day17) |
| 18  | --- Day 18: Snailfish ---               | :star: :star: [Complete](src/day18) |
| 19  | --- Day 19: Beacon Scanner ---          | :star: :star: [Complete](src/day19) |
| 20  | --- Day 20: Trench Map ---              | :star: :star: [Complete](src/day20) |
| 21  | --- Day 21: Dirac Dice ---              | :star: :star: [Complete](src/day21) |
| 22  | --- Day 22: Reactor Reboot ---          | :star: :star: [Complete](src/day22) |
| 23  | --- Day 23: Amphipod ---                | :star: :star: [Complete](src/day23) |
| 24  | --- Day 24: Arithmetic Logic Unit ---   | :star: :star: [Complete](src/day24) |
| 25  | --- Day 25: Sea Cucumber ---            | :star: :star: [Complete](src/day25) |

## Personal Rules

It's easy to get carried away on this challenge, but I have a full time job and a mountain of other hobbies, so...

1. This is about having fun, challenging myself and learning new things.
2. I may skip days, particularly if I am getting bogged down on the problem or life gets in the way (See Rule #1).
3. This year I am open to using 3rd party non-core python libraries where they would reduce dev time on a problem.
4. I will not look at any reference solutions until after the event is complete.
5. I can research ways of efficiently solving general problems required by the task provided it doesn't conflict with Rule #4.

## Structure

Every day has its own package in the [src](src), this is used to define any unique code or functions for solving the daily problems.
My personal data is included as a text file in each challenge's package under the `data` subdir, this is so anyone could verify my results without needing my AoC auth token.

The days code is executed using a module in the [tests](src/tests) package that executes via a Pytest runner.
This pytest modules verify the answers against those I computed in the challenge, you can see the result of all the automated tests in [Github Actions](https://github.com/CreatingNull/AoC-2021/actions/workflows/run-tests.yml).

Repository dependencies for execution are located in [requirements.txt](resources/requirements.txt).

Used the following third party libs:

* **[Numpy](https://github.com/numpy/numpy)** - Python lists are cool, but they're kinda terrible when it comes to higher dimensional numeric matrix mathmatics.
  Why waste your time when there is a well maintained library that is built for doing this efficiently?
* **[Bitarray](https://github.com/ilanschnell/bitarray)** - Python does a lot of things well, but lacking a native way to work with bits via the list paradigm is a huge downside for serial-communications use-cases.
  Why mess around with huge python types and having to bitmask everything when you can use this beautiful c extension?
* **[Frozen Dict](https://github.com/Marco-Sulla/python-frozendict)** - Python dicts are awesome collection types for hashed performance lookup of pretty much anything, however not being able to be hashed can be annoying.
  The frozendict package implements the rejected PEP for adding a frozen dictionary type, these work like normal dicts but are static such that you can hash them or pickle them ect.

Code formatting is handled via [pre-commit](https://github.com/pre-commit/pre-commit) see the [hooks](.pre-commit-config.yaml) used on this repo.

## License

The source of this repo uses the MIT open-source license, for details on the current licensing see LICENSE.md or click the badge above.
*   Copyright 2021 ?? <a href="https://nulltek.xyz" target="_blank">NullTek</a>.
