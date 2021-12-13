# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 12: Passage Pathing ---

This package contains the source and data for [day 12](https://adventofcode.com/2021/day/12) of the challenge.

* Status: Complete
* Difficulty Rating: 3.5 / 5

## Post-Task Thoughts

This was a bit of a tough one.
The first part was very simple because of the limitation with the small caves killing off a large proportion of the branches.
However, in part 2 when they opened up the exception to explore a single small-cave, exploring a large graph got significantly more complicated.
This was exacerbated by me accidentally skimming over the problem and misreading the part 2, so I was wondering why they had so few solutions.

Not 100% happy with my solution here, I think converting this from a recursive solution to an iterative one would probably improve efficiency.
Also, just counting the solved paths rather than keeping track of each solution would significantly reduce the run-time complexity for the large dataset.
This solution runs both parts on all 4 datasets in under 1s, if I have time later I'll come back and improve it further.
