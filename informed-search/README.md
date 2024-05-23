# Informed Search

Informed search algorithms, also known as **heuristic search algorithms**, use problem-specific knowledge to find solutions more efficiently. These algorithms employ heuristics to estimate the cost of reaching the goal from a given state, guiding the search process towards the most promising paths.

## Terminology

- **Heuristic Function (h(n))**: A heuristic function estimates the cost of the cheapest path from node n to the goal. It provides guidance on which paths to follow, based on domain-specific knowledge.
- **Path Cost (g(n))**: The path cost function g(n) represents the cost from the initial state to node n. It accumulates the costs of the actions taken to reach the current state.

## Factors for Measuring Complexity

To evaluate the performance of each search algorithm, we consider the following factors:

- **Maximum Branching Factor (b)**: The maximum number of successors of any node.
- **Depth of Least-Cost Solution (d)**: The depth at which the least-cost solution is found.
- **Maximum Depth of State Space (m)**: The maximum depth of the search tree.

## Algorithm Complexities

### Best-First Search

- **Time Complexity**: O(b^m)
- **Space Complexity**: O(b^m)

**Overview**: Best-First Search uses a heuristic to prioritize which node to expand next. It selects the node that appears to be closest to the goal based on the heuristic value.

- **Frontier**: A priority queue is used to keep track of the frontier nodes, ordered by their heuristic values.
- **Traversal**: Expands the most promising node based on the heuristic evaluation.

**Properties**:
- **Completeness**: No
- **Optimality**: No
## example
![GBFS](https://i.redd.it/ak7iexdgnhs51.gif)
### Greedy Best-First Search

- **Time Complexity**: O(b^m)
- **Space Complexity**: O(b^m)

**Overview**: Greedy Best-First Search specifically uses a heuristic function to select the node that appears closest to the goal, ignoring the path cost.

- **Frontier**: A priority queue is used to keep track of the frontier nodes, ordered by their heuristic values.
- **Traversal**: Expands the node with the lowest heuristic value.

**Properties**:
- **Completeness**: No
- **Optimality**: No
## example
![GBFS](https://upload.wikimedia.org/wikipedia/commons/f/f9/Greedy-search-path.gif)

### A* Search

- **Time Complexity**: O(b^d) (in the worst case)
- **Space Complexity**: O(b^d)

**Overview**: A* Search combines the path cost and the heuristic to select the next node to expand. It uses the formula f(n) = g(n) + h(n), where g(n) is the cost to reach the node, and h(n) is the heuristic estimate of the cost to reach the goal from the node.

- **Frontier**: A priority queue is used to keep track of the frontier nodes, ordered by their f(n) values.
- **Traversal**: Expands the node with the lowest f(n) value.

**Properties**:
- **Completeness**: Yes (if the heuristic is admissible)
- **Optimality**: Yes (if the heuristic is admissible and consistent)
## example
![GBFS](https://d2f0ora2gkri0g.cloudfront.net/40/f4/40f41f40-abb9-4d45-a476-62a7070f290e.gif)

## Conclusion

Informed search algorithms leverage heuristics to improve search efficiency, guiding the search process towards the most promising paths. While they vary in their completeness and optimality, each algorithm has specific use cases and advantages. Understanding their complexities and traversal methods is crucial for selecting the appropriate algorithm for a given problem.

For detailed implementations and examples, refer to the respective folders for each algorithm in this directory.
