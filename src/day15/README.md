# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 15: Chiton ---

This package contains the source and data for [day 15](https://adventofcode.com/2021/day/15) of the challenge.

* Status: Complete
* Difficulty Rating: 4 / 5

## Post-Task Thoughts

Not a particularly hard task, however, getting the implementation efficient is an absolute mission.
I haven't written an Astar algorithm search since university (5+ years) so I was a little hazy on the intricacies.
I got it implemented and efficient for the demo of part 1, but then it was ~20 seconds on the real data.
So with the help of the profiler I got that down to 0.3s, then they hit you with the 5x tiling in part 2, and we were back up to 20s!!!

The best heuristic is just the x delta plus the y delta as you can only move horizontally or vertically.
Unfortunately with my final dataset, I couldn't get cheeky and throw greedy gain on the heuristic, because it misses the global minima.
I only managed to get it down to ~8seconds on the part 2, but I need to come back and try to fix things up later.
