# ![NullTek Documentation](../../resources/NullTekDocumentationLogo.png) --- Day 10: Syntax Scoring ---

This package contains the source and data for [day 10](https://adventofcode.com/2021/day/10) of the challenge.

* Status: Complete
* Difficulty Rating: 1.5 / 5

## Post-Task Thoughts

Another good task, although I feel like I've had to do this same problem a bunch of times in the past.
So I was a little bored by having to build the usual syntax parsing tree.

My design just used `ChunkTreeNode` objects that contained a uni-directional reference to their parent node.
Then it's simply a matter of loading the symbols in by walking all the way down a tree branch and back up.
If you reach the top of the branch again the line is syntactically complete.
So to auto complete this you just have to populate any remaining symbols based on parents that exist between your current location and the root node of the tree.

Some may find this difficult if they have never had to do any sort of abstract syntax tree parsing before?
But it seemed relatively straight forward to me.
