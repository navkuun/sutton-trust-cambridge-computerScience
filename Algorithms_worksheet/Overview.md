# Overview

### How does a divide and conquer algorithm proceed to solve a problem? When can it be used and when should it be avoided?

A divide and conquer algorithm divides the problem into it's individiual sub-problems, then proceeds to solve these sub-problems and then join them all together to therefore 'conquer' and solve the original problem

---

### Describe what a backtracking algorithm is and how it works, illustrating your answer using the maze example.

A backtracking algorithm is an technique where it builds up a solution bit-by-bit depending on the constraints given. If at any point it fails to meet the constraints the algorithms 'backtracks' to a previous points and removes the option to go to this point again as it has already been shown to not provide a solution.

---

### Describe what a greedy algorithm is and contrast it with other kinds of algorithm.

A greedy algorithm is a technique where the 'locally optimal' choice is chosen. Meaning that the option that is the best at the current moment is chosen, so it does not look to previous or latter occurences. This is different to other types of algorithms such as backtracking as it does not take any other data into account from other points in time, as in backtracking it looks to previous points if one points does not work.

---

### Contrast dynamic programming with a brute force approach. When is it appropriate to use a dynamic programming solution?

A dynamic programming algorithms is one where it uses past data to create a solution from bottom up(top-down also exists), it is an optimization technique that creates a solution from smaller solutions that were computed earlier. Dyanimc programming can only be used in problems that have the properties:

- Optimal substructure
- Overlapping sub-problems

It is different to a brute force approach as it does not check every possibility as these were computed previously and stored in a memoized array (usual case) to be used for later computations. So it is much more efficient than brute force.
