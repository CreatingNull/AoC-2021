# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 23: Amphipod ---

This package contains the source and data for [day 23](https://adventofcode.com/2021/day/23) of the challenge.

* Status: Complete
* Difficulty Rating: 4.5 / 5

## Post-Task Thoughts

I liked this task, but building it out was so time-consuming.
My approach was to treat the game-state like a 'node' and then use dijkstra's algorithm to isolate one of the global minima.
You could possibly speed this solution up further by going astar and finding a heuristic.
Due to the sheer number of nodes it's possible this would actually increase the computation cost of each iteration.

One of the keys was once a nodes has been searched I added it to a set to avoid doing any work on duplicates in the future.
There are millions of duplicate game-states that are encountered while obtaining a solution and so this hugely impacts the execution time.
Unfortunately this meant making my datastructure hashable to do which I made use of 3rd party package frozendict.

There are a lot of intricacies to implementing the function of this game correctly, and it was easy to get caught on edge cases.
I actually really enjoyed this implementation, even though I am not that happy with the efficiency or solution, the task was a lot of fun.
