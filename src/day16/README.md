# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 16: Packet Decoder ---

This package contains the source and data for [day 16](https://adventofcode.com/2021/day/16) of the challenge.

* Status: Complete
* Difficulty Rating: 3 / 5

## Post-Task Thoughts

This task was much more in my wheel-house, as I've dealt with my fair share of binary serial protocols.
As I complained about on day 3, pythons support for operating on binary numbers is rather poor.
Sometimes, particularity with problems like these you need to be working with things on a bit by bit level.
Storing these bits in massive python types and them having to excessively mask everything is so untidy and to be honest seems quite 'un-pythonic'.

I figured there must be other people who agree with this so there has to be a library someone has written to handle this use case.
I found [bitarray](https://github.com/ilanschnell/bitarray), a python c extension that handles all this exactly how I would expect it to work in python.
There's a few quirks here and there, but it makes operating with bits such an enjoyable process, which has never been the case for binary in python.
This actually resolves one of my biggest usability issues with python, and I am definitely going to be using this elsewhere.

Anyway the task was straight forward enough, build an equation via the packets into a tree and recursively solve the equation...
