# Hill Climbing Algorithm

Hill Climbing is a local search algorithm used for optimization problems. It starts with an arbitrary solution to a problem and iteratively moves to the neighboring solutions with higher values, eventually reaching a local optimum.

## Overview

This repository contains an implementation of the Hill Climbing algorithm in Python. Hill Climbing is useful for finding local optima in optimization problems.

## Implementation

The Hill Climbing algorithm is implemented in Python as a function named `hill_climbing`. It takes an optimization problem as input and returns a local optimum solution.

### Pseudo-Code

```plaintext
function hill_climbing(problem):
    current_solution = problem.initial_solution()
    loop:
        neighbors = problem.get_neighbors(current_solution)
        best_neighbor = max(neighbors, key=problem.value)
        if problem.value(best_neighbor) <= problem.value(current_solution):
            return current_solution  // Local optimum found
        current_solution = best_neighbor
```
## Algorithm for Simple Hill Climbing:
**Step 1**: Evaluate the initial state, if it is goal state then return success and Stop.

**Step 2**: Loop Until a solution is found or there is no new operator left to apply.

**Step 3**: Select and apply an operator to the current state.

**Step 4**: Check new state:
If it is goal state, then return success and quit.
Else if it is better than the current state then assign new state as a current state.
Else if not better than the current state, then return to step2.

**Step 5**: Exit.
## Usage
To use the Hill Climbing algorithm, provide it with an optimization problem that defines methods for generating initial solutions, getting neighbors, and evaluating the value of a solution. Then, call the hill_climbing function with the problem as input to find a local optimum.

## Problems in Hill Climbing Algorithm
 **Local Maximum**: A local maximum is a peak state in the landscape which is better than each of its neighboring states, but there is another state also present which is higher than the local maximum.
 ![Local Maximum](https://static.javatpoint.com/tutorial/ai/images/hill-climbing-algorithm-in-ai2.png)

 **Plateau**: A plateau is the flat area of the search space in which all the neighbor states of the current state contains the same value, because of this algorithm does not find any best direction to move. A hill-climbing search might be lost in the plateau area.
 ![Plateau](https://static.javatpoint.com/tutorial/ai/images/hill-climbing-algorithm-in-ai3.png)

 **A hill-climbing algorithm which never makes a move towards a lower value guaranteed to be incomplete because it can get stuck on a local maximum. And if algorithm applies a random walk, by moving a successor, then it may complete but not efficient. Simulated Annealing is an algorithm which yields both efficiency and completeness.**