# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 19: Beacon Scanner ---

This package contains the source and data for [day 19](https://adventofcode.com/2021/day/19) of the challenge.

* Status: Complete
* Difficulty Rating: 5 / 5

## Post-Task Thoughts

You know when more people have completed the later days than this one you're in for a real treat.
I had to pull out my old linear alegbra notes on this one, I don't think I've done spacial transformations using matrices in about 8 years.
The complexity in this one, provided you know how to reorient the scanners (which at worst is only 24 loops), is in finding an efficient method for testing alignment of the beacons.
I think the easiest solution is to normalise about random beacons (ie: shift them to be your origin) and then check against the set of aligned beacons on the other scanner.
This however is a terrible solution as it requires n1 * n2 * 24 loops, where n1 and n2 are the number of beacons in scanner 1 and 2 respectively.
There are other ways to implement this more efficiently, I just don't have the time to do this anymore, haha.

I enjoyed this one more than the last few days, wish I had more time to refactor into a more optimal solution.
