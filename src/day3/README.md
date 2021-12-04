# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 3: Binary Diagnostic ---

This package contains the source and data for [day 3](https://adventofcode.com/2021/day/3) of the challenge.

* Status: Complete
* Difficulty Rating: 2.5 / 5

## Post-Task Thoughts

Using one of the highest level languages (python) for directly operating with the lowest level language (binary) always seems like a bit of a mismatch to me.
Fortunately this task was simple enough that there was no reason to delve outside the built-ins, but you do feel like you're fighting the `duck typing` and lack of defined length integer objects.

One nice by-product of using the cpython interpreter, is there is always the possibility to evaluate a chunk of low level code in `c`, or use the `ctypes` directly if it makes sense to do so.
I didn't bother in this case, as the performance benefit would be negligible for the challenge. Something like numpy could also have been useful, but again this is a massive library to solve a tiny problem in a tiny program.
We'll see what the upcoming tasks bring...

Also, what sort of diagnostic system returns binary data as ascii strings?? Come on AoC!
