# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 11: Dumbo Octopus ---

This package contains the source and data for [day 11](https://adventofcode.com/2021/day/11) of the challenge.

* Status: Complete
* Difficulty Rating: 2 / 5

## Post-Task Thoughts

I think this has been my favourite task so far, and also introduced me to the cuteness of the [dumbo octopus](https://www.youtube.com/watch?v=eih-VSaS2g0).
It would've been a drag to implement using lists, but again numpy saves the day.
There's no point constraining yourself to the base language or re-inventing the wheel when such great open-source tools are already available.

Using recursion again made this task a lot easier, it was just a matter of executing again on a sub-array for each triggering point
The key was to ensure that you didn't flash a node twice, due to recusing on it in a lower frame and then continuing to iterate over it on a higher frame.
It was also important to ensure you could distinguish between pending flashes (10), already flashed this time-step (I used -1) and just flashed (0) from a previous step.
I was a little disappoint the custom dataset didn't increase in size from the example one, as I feel like my implementation could stretch it's legs on a larger array.
Also, part 2 was just a trivial extension on part 1.
