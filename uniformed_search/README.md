# Uninformed Search

Uninformed search algorithms, also known as blind search algorithms, explore the search space without any domain-specific knowledge. These algorithms rely solely on the problem definition, such as the set of possible actions and the goal state, to guide their search.

## Factors for Measuring Complexity

To evaluate the performance of each search algorithm, we consider the following factors:

- **Maximum Branching Factor (b)**: The maximum number of successors of any node.
- **Depth of Least-Cost Solution (d)**: The depth at which the least-cost solution is found.
- **Maximum Depth of State Space (m)**: The maximum depth of the search tree.
## example
![factors](https://github.com/mo7amedgom3a/Ai-Algorithms/blob/main/factors.png?raw=true)

## Algorithm Complexities

### Breadth-First Search (BFS)

- **Time Complexity**: O(b^d)
- **Space Complexity**: O(b^d)

**Overview**: BFS explores the search tree level by level, starting from the root node and expanding all nodes at the present depth before moving on to nodes at the next depth level.

- **Frontier**: A queue (FIFO) is used to keep track of the frontier nodes.
- **Traversal**: Explores all nodes at the current depth before proceeding to the next depth level.

**Properties**:
- **Completeness**: Yes (if the branching factor is finite)
- **Optimality**: Yes (if all step costs are equal)
## example 
![BFS](https://miro.medium.com/v2/resize:fit:1400/0*WAkA73-8Jqyz11hC.gif)

### Depth-First Search (DFS)

- **Time Complexity**: O(b^m)
- **Space Complexity**: O(b*m)

**Overview**: DFS explores as far down a branch as possible before backtracking. It uses a stack to keep track of the path being explored.

- **Frontier**: A stack (LIFO) is used to keep track of the frontier nodes.
- **Traversal**: Goes deep into each branch before backtracking to explore other branches.

**Properties**:
- **Completeness**: No (fails in infinite-depth spaces)
- **Optimality**: No
## example 
![DFS](https://miro.medium.com/v2/resize:fit:828/1*WR4AtjT_nhwSOtAW99Yd5g.gif)

### Depth-Limited Search (DLS)

- **Time Complexity**: O(b^l) (l is the depth limit)
- **Space Complexity**: O(b*l)

**Overview**: DLS is a variation of DFS with a predetermined depth limit to prevent infinite descent.

- **Frontier**: A stack with a depth limit is used.
- **Traversal**: Similar to DFS but stops at the depth limit.

**Properties**:
- **Completeness**: Yes (if the depth limit is greater than or equal to d)
- **Optimality**: No
## example 
![DLS](https://files.codingninjas.in/article_images/custom-upload-1689800279-6896183b.png)

### Uniform Cost Search (UCS)

- **Time Complexity**: O(b^(1 + ⌊C*/ε⌋)) (C* is the cost of the optimal solution, ε is the smallest step cost)
- **Space Complexity**: O(b^(1 + ⌊C*/ε⌋))

**Overview**: UCS expands the least-cost node first, ensuring that the cheapest path is always explored next.

- **Frontier**: A priority queue is used to keep track of the nodes, ordered by path cost.
- **Traversal**: Expands nodes in the order of their cumulative path cost.

**Properties**:
- **Completeness**: Yes (if step costs are positive)
- **Optimality**: Yes
## example 
if we need to move from (A) to (G)
![UCS](https://d2f0ora2gkri0g.cloudfront.net/78/3b/783beb1c-b852-4e2d-96c9-eb1a00b28c6d.gif)

## Conclusion

Uninformed search algorithms provide a foundational approach to problem-solving in AI, exploring the search space without heuristics. While they vary in their completeness and optimality, each algorithm has specific use cases and advantages. Understanding their complexities and traversal methods is crucial for selecting the appropriate algorithm for a given problem.

For detailed implementations and examples, refer to the respective folders for each algorithm in this directory.
