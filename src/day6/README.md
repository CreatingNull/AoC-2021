# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 6: Lanternfish ---

This package contains the source and data for [day 5](https://adventofcode.com/2021/day/5) of the challenge.

* Status: Complete
* Difficulty Rating: 1 / 5

## Post-Task Thoughts

This was the easiest task to date, and also my highest leaderboard position so far this year.
As soon as the task mentioned exponential growth, I knew I was going to haves to be careful with how I stored and computed data.
Fortunately storing this in a python dictionary was a very simple solution to this issue mapping a `day countdown timer` integer key to a `sum of fish` value for that countdown.
This means the 'exponential' part of the data is simply captured in 9 integer values, which isn't particularly computationally intensive to operate on.

I think the 'gotcha' in this task would be with languages that have static length integers, fortunately in python 3 you don't have to worry about this.
CPython uses a 'bignum' arithmetic variant, where it's broken up into chunks and can essentially grow indefinitely (provided you don't overflow system memory).
This scaling property barely ever comes in handy for me, but in this case it's lovely to not be using a language like java that use staic-length integers.
My final sum was `1,572,358,335,990` which needs about 41 bits (6 bytes in practical reality) which is several orders of magnitude above the 32-bit signed integer types many languages have by default.
