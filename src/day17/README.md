# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 17: Trick Shot ---

This package contains the source and data for [day 17](https://adventofcode.com/2021/day/17) of the challenge.

* Status: Complete
* Difficulty Rating: 3.5 / 5

## Post-Task Thoughts

Didn't enjoy this one at all, maybe my brain just wasn't working, but I am not happy with my solution.
The time pressure is also a massive consideration now, I don't have the spare time to sink into developing optimal solutions.

There was a few optimisations I managed to include:

* The height reached is the triangular number of the y-axis launch velocity.
* THe x-axis launch velocities triangular number must be greater than the low limit for the x goal. Otherwise, you'll never reach it.
* If you compute one dimension in isolation you can use this data to reduce the search space for the other axis.

Feeling a little demoralised by this task, lets hope for a second wind with day 17.
