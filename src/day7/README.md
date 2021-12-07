# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 7: The Treachery of Whales ---

This package contains the source and data for [day 7](https://adventofcode.com/2021/day/7) of the challenge.

* Status: Complete
* Difficulty Rating: 1.5 / 5

## Post-Task Thoughts

It could be really easy on this task to waste time trying to optimise a solution for part 1 only for it to be completely useless on part 2.
The key to these tasks is to follow the `make it barely work` principle for part 1, then once you have the full scope of part 2, start optimising from there.

The trick to part 2 was figuring out the fuel consumption for each movement is the triangular number of the flat consumption.
To be completely honest I couldn't remember what these numbers were called, so yes, I actually did google search `additional-factorial` to try and 'reverse-mathematics' my way to the wiki article.

I tried throwing an LRU cache at function that computes the triangular numbers, mostly just to see how much it'd help, I achieved around a 25% speedup at best.
However, due to the wide range of input numbers, and the relatively low time-cost of the function anyway, I ended up just committing the solution without any caching.
