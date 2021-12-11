# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 4: Giant Squid ---

This package contains the source and data for [day 4](https://adventofcode.com/2021/day/4) of the challenge.

* Status: Complete
* Difficulty Rating: 2 / 5

## Post-Task Thoughts

There were a number of ways this bingo problem could have been tackled.
Personally I work best when I can spatially visualise things, so 2D arrays for the bingo boards made a lot of sense.
I did decide to use numpy arrays in favour of python lists, this was mainly just to access the optimised functions numpy provides, but obviously the reduced memory and increased performance are always nice.
Only downside of using numpy is it breaks compatibility with a lot of non-cpython interpreters, obviously for this application (and probably most applications) this isn't really relevant.

With tracking the bingo boards as 2D arrays, it was simple just to swap out the called numbers with a special value (-1 as data type was a signed byte and this never appears in board data).
Then it's just a matter triggering when a row or column is completely populated with -1's. Once we have bingo on a board it's easy to then swap all the -1's to zeros and element-wise sum the matrix for calculating our answer.

The second part of the problem was really nice in this task, rather than just finding the winning board, having to solve all the boards.
This was nice as it allowed you to solve both the first part and the second parts cleanly with the one algorithm, which is always satisfying.
