# Depth-First Search (DFS)

## Graph Example
Consider the following graph:

         A
        / \
        B   C
       /|   |\
       D E  F  G


## DFS Algorithm

Depth-First Search (DFS) explores as far down a branch as possible before backtracking. It uses a stack to keep track of the nodes that need to be explored next.

### Step-by-Step Explanation

1. **Initialization**
   - Start at the root node (A).
   - Initialize the stack frontier with the starting node: `Stack: [A]`
   - Initialize the visited list to keep track of visited nodes: `Visited: []`

2. **Iteration 1**
   - Pop the top element from the stack: `Node = A`
   - Add A to the visited list: `Visited: [A]`
   - Push all unvisited neighbors of A (B and C) to the stack: `Stack: [C, B]`

3. **Iteration 2**
   - Pop the top element from the stack: `Node = B`
   - Add B to the visited list: `Visited: [A, B]`
   - Push all unvisited neighbors of B (D and E) to the stack: `Stack: [C, E, D]`

4. **Iteration 3**
   - Pop the top element from the stack: `Node = D`
   - Add D to the visited list: `Visited: [A, B, D]`
   - D has no unvisited neighbors: `Stack: [C, E]`

5. **Iteration 4**
   - Pop the top element from the stack: `Node = E`
   - Add E to the visited list: `Visited: [A, B, D, E]`
   - E has no unvisited neighbors: `Stack: [C]`

6. **Iteration 5**
   - Pop the top element from the stack: `Node = C`
   - Add C to the visited list: `Visited: [A, B, D, E, C]`
   - Push all unvisited neighbors of C (F and G) to the stack: `Stack: [G, F]`

7. **Iteration 6**
   - Pop the top element from the stack: `Node = F`
   - Add F to the visited list: `Visited: [A, B, D, E, C, F]`
   - F has no unvisited neighbors: `Stack: [G]`

8. **Iteration 7**
   - Pop the top element from the stack: `Node = G`
   - Add G to the visited list: `Visited: [A, B, D, E, C, F, G]`
   - G has no unvisited neighbors: `Stack: []`

9. **Completion**
   - The stack is empty, and all nodes have been visited.

### Advantages of DFS

- **Memory Usage**: DFS has a lower memory requirement than BFS, as it only needs to store the nodes on the current path in the stack.
- **Simple to Implement**: DFS uses a straightforward stack-based approach.
- **Suitable for Deep Graphs**: DFS is more suitable for problems with solutions far from the root node or deeper graphs.

### Disadvantages of DFS

- **Completeness**: DFS is not guaranteed to find a solution in infinite-depth spaces or if a solution does not exist within the depth limit.
- **Optimality**: DFS is not optimal, as it does not guarantee the shortest path to the goal.
- **Can Get Stuck in Loops**: Without proper handling of visited nodes, DFS can get stuck in cycles.

## Conclusion

Depth-First Search is a fundamental search algorithm that explores as far down a branch as possible before backtracking. It is simple to implement and has lower memory requirements compared to BFS, making it suitable for deep graphs. However, it is not guaranteed to be complete or optimal and can get stuck in loops if cycles are not handled properly.

For a more detailed implementation and examples, refer to the code in the `DFS` directory of this repository.
