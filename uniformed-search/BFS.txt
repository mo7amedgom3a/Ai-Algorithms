# Breadth-First Search (BFS)

## Graph Example
Consider the following graph:

      A
     / \
     B   C
    /|   |\
    D E  F G


## BFS Algorithm

Breadth-First Search (BFS) explores the graph level by level. It uses a queue to keep track of the nodes that need to be explored next.

### Step-by-Step Explanation

1. **Initialization**
   - Start at the root node (A).
   - Initialize the queue frontier with the starting node: `Queue: [A]`
   - Initialize the visited list to keep track of visited nodes: `Visited: []`

2. **Iteration 1**
   - Dequeue the first element from the queue: `Node = A`
   - Add A to the visited list: `Visited: [A]`
   - Enqueue all unvisited neighbors of A (B and C) to the queue: `Queue: [B, C]`

3. **Iteration 2**
   - Dequeue the first element from the queue: `Node = B`
   - Add B to the visited list: `Visited: [A, B]`
   - Enqueue all unvisited neighbors of B (D and E) to the queue: `Queue: [C, D, E]`

4. **Iteration 3**
   - Dequeue the first element from the queue: `Node = C`
   - Add C to the visited list: `Visited: [A, B, C]`
   - Enqueue all unvisited neighbors of C (F and G) to the queue: `Queue: [D, E, F, G]`

5. **Iteration 4**
   - Dequeue the first element from the queue: `Node = D`
   - Add D to the visited list: `Visited: [A, B, C, D]`
   - D has no unvisited neighbors: `Queue: [E, F, G]`

6. **Iteration 5**
   - Dequeue the first element from the queue: `Node = E`
   - Add E to the visited list: `Visited: [A, B, C, D, E]`
   - E has no unvisited neighbors: `Queue: [F, G]`

7. **Iteration 6**
   - Dequeue the first element from the queue: `Node = F`
   - Add F to the visited list: `Visited: [A, B, C, D, E, F]`
   - F has no unvisited neighbors: `Queue: [G]`

8. **Iteration 7**
   - Dequeue the first element from the queue: `Node = G`
   - Add G to the visited list: `Visited: [A, B, C, D, E, F, G]`
   - G has no unvisited neighbors: `Queue: []`

9. **Completion**
   - The queue is empty, and all nodes have been visited.

### Advantages of BFS

- **Completeness**: BFS is complete, meaning it will find a solution if one exists, given that the branching factor is finite.
- **Optimality**: BFS is optimal if all step costs are equal. It guarantees the shortest path to the goal.
- **Simple to Implement**: BFS uses a straightforward queue-based approach.

### Disadvantages of BFS

- **Memory Usage**: BFS can consume a lot of memory, especially for large graphs, since it stores all nodes at the current depth level.
- **Time Complexity**: BFS can be slow for deep graphs, as it explores all nodes level by level. The time complexity is O(b^d), where b is the branching factor and d is the depth of the least-cost solution.
- **Not Suitable for Infinite Graphs**: BFS is not suitable for graphs with infinite depth or a very high branching factor, as it can run out of memory.

## Conclusion

Breadth-First Search is a fundamental search algorithm that explores all nodes at the present depth before moving on to nodes at the next depth level. It is complete and optimal for unweighted graphs, but it can be memory-intensive and slow for large or deep graphs.

For a more detailed implementation and examples, refer to the code in the `BFS` directory of this repository.
