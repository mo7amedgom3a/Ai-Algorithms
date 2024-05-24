# Uniform Cost Search (UCS)

## Graph Example
Consider the following weighted graph:

     A
    / \
   B   C
  /|   |\
  D E  F  G


## UCS Algorithm

Uniform Cost Search (UCS) explores the graph by expanding the node with the lowest path cost. It uses a priority queue to keep track of the nodes that need to be explored next, ordered by their cumulative path cost.

### Step-by-Step Explanation

1. **Initialization**
   - Start at the root node (A).
   - Initialize the priority queue frontier with the starting node and its path cost: `Frontier: [(A, 0)]`
   - Initialize the explored list to keep track of visited nodes: `Explored: []`
   - Initialize the expand list to keep track of expanded nodes: `Expand: []`

2. **Iteration 1**
   - Dequeue the first element from the frontier: `Node, PathCost = A, 0`
   - Add A to the explored list: `Explored: [A]`
   - Expand node A and add its neighbors to the frontier with updated path costs:
     - B (path cost 1): `Frontier: [(B, 1)]`
     - C (path cost 2): `Frontier: [(B, 1), (C, 2)]`
   - Add A to the expand list: `Expand: [A]`

3. **Iteration 2**
   - Dequeue the first element from the frontier: `Node, PathCost = B, 1`
   - Add B to the explored list: `Explored: [A, B]`
   - Expand node B and add its neighbors to the frontier with updated path costs:
     - D (path cost 3): `Frontier: [(C, 2), (D, 3)]`
     - E (path cost 4): `Frontier: [(C, 2), (D, 3), (E, 4)]`
   - Add B to the expand list: `Expand: [A, B]`

4. **Iteration 3**
   - Dequeue the first element from the frontier: `Node, PathCost = C, 2`
   - Add C to the explored list: `Explored: [A, B, C]`
   - Expand node C and add its neighbors to the frontier with updated path costs:
     - F (path cost 5): `Frontier: [(D, 3), (E, 4), (F, 5)]`
     - G (path cost 7): `Frontier: [(D, 3), (E, 4), (F, 5), (G, 7)]`
   - Add C to the expand list: `Expand: [A, B, C]`

5. **Completion**
   - All nodes have been expanded, and the goal node may have been found.

### Advantages of UCS

- **Optimality**: UCS guarantees finding the optimal solution with the lowest path cost.
- **Completeness**: If the path costs are non-negative, UCS is complete and will find a solution if one exists.
- **Adaptability**: UCS can adapt to various cost functions and edge weights.

### Disadvantages of UCS

- **Memory Usage**: UCS can consume a lot of memory, especially for graphs with high branching factors and path costs.
- **Time Complexity**: UCS can be slow for graphs with high path costs or deep solutions.
- **Implementation Complexity**: Managing the priority queue and updating path costs can be complex.

## Conclusion

Uniform Cost Search is a systematic algorithm that explores the graph by expanding the node with the lowest path cost. It is guaranteed to find the optimal solution but can be memory-intensive and slow for large or deep graphs.

For a more detailed implementation and examples, refer to the code in the UCS directory of this repository.

