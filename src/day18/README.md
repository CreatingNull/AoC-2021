# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 18: Snailfish ---

This package contains the source and data for [day 18](https://adventofcode.com/2021/day/18) of the challenge.

* Status: Complete
* Difficulty Rating: 4.5 / 5

## Post-Task Thoughts

Definitely not the hardest task, but I spend the most time on this so far.
I think the easiest way to tackle this problem is a [binary tree](https://en.wikipedia.org/wiki/Binary_tree), another structure I haven't really used since university.
I must've refactored this problem 3 or 4 times, I could visualise it, but I was going in circles, particularly with the explosion operation.
I'd get 95% of the cases working and then realise why the last case wasn't working and have to rebuild chunks of the traversal, breaking other cases in the process.

A real nightmare task for me, although I don't think it should've been this difficult.
I got bogged down in misunderstanding their technicalities where things were worded ambitiously:

```
you must repeatedly do the first action in this list that applies to the snailfish number:

    If any pair is nested inside four pairs, the leftmost such pair explodes.
    If any regular number is 10 or greater, the leftmost such regular number splits.

```

One would think that means do the first action that applies to the left most pair, but no it means do the explosion action first.
So if you have a split pending to the left of a pending explosion that is supposed to occur first.
I don't think they adequately explained this or provided broken down test-cases that triggered this.
Again I had to refactor multiple times just due to misunderstanding the edge cases grr!!!

Oh well, we got there in the end. I lost enthusiasm for cleaning this up to efficiently run part 2.
