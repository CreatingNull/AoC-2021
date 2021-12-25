# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 20: Trench Map ---

This package contains the source and data for [day 20](https://adventofcode.com/2021/day/20) of the challenge.

* Status: Complete
* Difficulty Rating: 4.5 / 5

## Post-Task Thoughts

It was pretty mean of AoC to specifically design the example not to trigger the infinite-plane, and then to include this in the actual input.
My opinion is the example data shouldn't be used specifically to mislead the programmer, that is just in bad taste, design your problems to be more subtle rather than using trick data.
They also don't clarify that either 0 or 512 MUST be 0 otherwise the answer is infinite, so really it's an unsolvable task for all inputs. 
I dealt with the infinite plane conundrum by bounding to the un-padded region and ignoring relying on the fact that all 0's and 512s will perpetually invert each other and so as long as we are on an even step we have a finite answer. 

Still easier than day 19 though... 
Again bitarray and numpy coming in handy, probably my most efficient solution in the last few days.
