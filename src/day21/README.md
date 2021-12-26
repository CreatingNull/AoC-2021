# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 21: Dirac Dice ---

This package contains the source and data for [day 21](https://adventofcode.com/2021/day/21) of the challenge.

* Status: Complete
* Difficulty Rating: 4 / 5

## Post-Task Thoughts

This was a walk in the park compared to some of the previous days.
The first part of the task almost was pretty unrelated, as the quantum dice requires some special consideration in the design.
I ended up just solving it iteratively, using an optimised 'brute force' approach.

Fortunately there are a few simplifications we can make:

 * 3 rolls of the dirac dice can only yield 7 values, even though there are 27 permutations.
    Using this you can just multiply your number of universes by the number of combinations that can produce the dirac value, this massively reduces the number of iterations to compute.
 * The second major optimisation is by combining duplicate positions before progressing to the next turn.
   Many movements will put the players into the same state with the same score in different universes, again you can just treat these as one game and sum the number of universes it is applying to.
   This reduced me from around 30s execution time to about 1s, as it also heavily reduces the game states you need to iterate over.

The end is in sight now!
