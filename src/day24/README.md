# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 24: Arithmetic Logic Unit ---

This package contains the source and data for [day 24](https://adventofcode.com/2021/day/24) of the challenge.

* Status: Complete
* Difficulty Rating: 5 / 5

## Post-Task Thoughts

A bit of a bait and switch on this one, really doesn't have anything to do with the ALU they tell you to build.
I wouldn't be surprised if most people (myself included) tried to brute force this on an ALU first, then realising it was going to take thousands of years to complete 9^14 iterations.
The key is actually figuring out optimization / pattern detection in the MONAD instructions.
Very, very time-consuming and not particularly enjoyable.

You've got to remember you are looking for input that will drive z to 0 on the final step.
Then monad program can be broken down into 14 sets of 'independent-ish' instructions following each input command.
The only data that persists between each of these instructions is captured in the z accumulator on the ALU.
Only instructions on line 4, 5 & 15 have unique values between input digits, the other 15 instructions are pretty much boilerplate.
I don't know if there was any way to solve this other than working through the solution with a pad and pen and finding the dependency rules between digits.

I have no possible way of knowing if my solution is generalised across all inputs as they only provided one custom dataset and no example MONAD dataset.
Not fun at all, hoping the final day is a better problem than this.
