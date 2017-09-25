# AISearch

[Project Description](http://people.cs.pitt.edu/~litman/courses/cs1571/1571f17_HW1.pdf)

Python version 2.7.6

Consulted: Google, StackOverflow, [AIMA-python](https://github.com/aimacode/aima-python/blob/master/search.py)

**Issues**
- In the aggregation problem a state will connect to itself (for example: N_3 thinks it's connected to N_1 *and* N_3 with a weighted edge of 4), causing the searches to do unnecessary creation of nodes.
- Monitor Path isn't correctly calculated in BFS, Unicost, or IDDFS