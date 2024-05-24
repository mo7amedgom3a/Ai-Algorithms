# Depth-Limited Search (DLS)

## Graph Example
Consider the following graph:

     A
    / \
   B   C
  /|   |\
  D E  F  G


## DLS Algorithm

Depth-Limited Search (DLS) is a variant of Depth-First Search (DFS) that limits the depth to which the search can go. It is useful for preventing infinite descent in graphs with cycles or infinite depth.

### Step-by-Step Explanation

1. **Initialization**
   - Start at the root node (A) with a specified depth limit (L).
   - Initialize the stack frontier with the starting node and its depth: `Stack: [(A, 0)]`
   - Initialize the visited list to keep track of visited nodes: `Visited: []`

2. **Iteration 1**
   - Pop the top element from the stack: `Node, Depth = A, 0`
   - Add A to the visited list: `Visited: [A]`
   - Since Depth < L, push all unvisited neighbors of A (B and C) to the stack with incremented depth: `Stack: [(C, 1), (B, 1)]`

3. **Iteration 2**
   - Pop the top element from the stack: `Node, Depth = B, 1`
   - Add B to the visited list: `Visited: [A, B]`
   - Since Depth < L, push all unvisited neighbors of B (D and E) to the stack with incremented depth: `Stack: [(C, 1), (E, 2), (D, 2)]`

4. **Iteration 3**
   - Pop the top element from the stack: `Node, Depth = D, 2`
   - Add D to the visited list: `Visited: [A, B, D]`
   - D has no unvisited neighbors or Depth = L: `Stack: [(C, 1), (E, 2)]`

5. **Iteration 4**
   - Pop the top element from the stack: `Node, Depth = E, 2`
   - Add E to the visited list: `Visited: [A, B, D, E]`
   - E has no unvisited neighbors or Depth = L: `Stack: [(C, 1)]`

6. **Iteration 5**
   - Pop the top element from the stack: `Node, Depth = C, 1`
   - Add C to the visited list: `Visited: [A, B, D, E, C]`
   - Since Depth < L, push all unvisited neighbors of C (F and G) to the stack with incremented depth: `Stack: [(G, 2), (F, 2)]`

7. **Iteration 6**
   - Pop the top element from the stack: `Node, Depth = F, 2`
   - Add F to the visited list: `Visited: [A, B, D, E, C, F]`
   - F has no unvisited neighbors or Depth = L: `Stack: [(G, 2)]`

8. **Iteration 7
   - Pop the top element from the stack: Node, Depth = G, 2
   - Add G to the visited list: Visited: [A, B, D, E, C, F, G]
   - G has no unvisited neighbors or Depth = L: Stack: []

Completion
   - The stack is empty, and all nodes up to the specified depth limit have been visited.

Advantages of DLS

- Prevents Infinite Descent: By limiting the depth, DLS avoids getting stuck in infinite loops, making it suitable for graphs with cycles or infinite depth.
- Memory Usage: DLS has lower memory requirements than BFS, as it only needs to store the nodes on the current path up to the depth limit.
- Simple to Implement: DLS uses a straightforward stack-based approach with a depth limit check.

Disadvantages of DLS

- Completeness: DLS is not complete if the solution lies beyond the depth limit.
- Optimality: DLS is not optimal, as it does not guarantee the shortest path to the goal.
- Depth Limit Sensitivity: Choosing an inappropriate depth limit can result in missing the solution or inefficient search.

Conclusion

Depth-Limited Search is a useful variant of DFS that prevents infinite descent by limiting the depth of the search. It is simple to implement and has lower memory requirements, but it is not complete or optimal and is sensitive to the chosen depth limit.

For a more detailed implementation and examples, refer to the code in the DLS directory of this repository.
