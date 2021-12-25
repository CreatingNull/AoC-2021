# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 20: Trench Map ---

This package contains the source and data for [day 20](https://adventofcode.com/2021/day/20) of the challenge.

* Status: Complete
* Difficulty Rating: 4.5 / 5

## Post-Task Thoughts

It was pretty mean of AoC to specifically design the example not to trigger the infinite-plane, and then to include this in the actual input.
My opinion is the example data shouldn't be used specifically to mislead the programmer, that is just in bad taste, design your problems to be more subtle rather than using trick data.
They also don't clarify that either 0 or 512 MUST be 0 otherwise the answer is infinite, so really it's an unsolvable task for all inputs.
I dealt with the infinite plane conundrum by pretty much ignoring it on the time-step where the sum would go infinite.
Instead I just correct on the next timestamp by reversing the inverting the change to the border elements.

Again bitarray and numpy coming in handy, however I don't believe this was the most efficient solution at all.
I think if I was to do this again I would rethink the data structuring as you have to waste a lot of horsepower on array operations with this implementation.
