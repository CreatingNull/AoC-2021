# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 14: Transparent Origami ---

This package contains the source and data for [day 14](https://adventofcode.com/2021/day/14) of the challenge.

* Status: Complete
* Difficulty Rating: 4 / 5

## Post-Task Thoughts

Absolute mission to figure this one out.
First I tried the naive iterate over a string, which easily solves the first part.
Then they hit you with the 40 iterations, and based on my calculations that'd produce a string of length `20,890,720,927,745`.
So I figured that implementation was a no-go, and instead decided to recurse down the pair branches.
That way you are only recusing 40 layers deep, and can just track the char counts as you go, seemed like a good idea... wrong...
The computation cost of this doubles for every additional time-steps, at 20 iterations I was already seeing over 1s execution time.
I didn't have a couple of hundred hours to run this on one thread, and assumed there had to be a better way than running this solution in parallel on a gpu.

Finally I realised the pairs were just translating on each step.
The addition of the new char then creates 2 sets of pairs from each char in the old pair (the exponential characteristic).
Using this method means you don't have to keep track of positions of the pairs because they become independent of any other elements in the polymer.
The trick then at the end is to unpack all these pairs into a char count, which is half the number of times the chars appear in pairs.
Half (rounded up) works only because most of the pairs are internally conjoined, the ones that aren't are terminating the polymer (and never change).

Haven't looked at day 15 yet, I am a little scared of what is to come now.
