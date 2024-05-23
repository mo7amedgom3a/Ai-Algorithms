# A* Search Algorithm

A* is an informed search algorithm that combines the advantages of Dijkstra's algorithm and greedy search. It evaluates nodes by combining the cost of the path from the start node (g(n)) and the heuristic function (h(n)) to estimate the cost to reach the goal.

## Heuristic Function Evaluation

Before diving into the step-by-step process, let's evaluate the heuristic function used in A*. In this example, we'll use a simple heuristic function that estimates the distance from each node to the goal node. The heuristic values for each node are as follows:

- A: h(A) = 3
- B: h(B) = 2
- C: h(C) = 1
- D: h(D) = 2
- E: h(E) = 1
- F: h(F) = 0
- G: h(G) = 2

These heuristic values represent the estimated distances from each node to the goal node. The goal node, F, has a heuristic value of 0, indicating that it is the goal state.

## Graph Representation as Tree

         A(3, 0)
          / \
      B(2, 1) C(1, 2)
       / \          \
    D(2, 3) E(1, 1)  F(0, 0) 
                       /
                    G(2, 2)



In the parentheses, the first value represents the actual cost (g(n)) from the start node to the current node, and the second value represents the heuristic value (h(n)).

## Step-by-Step Explanation

1. **Initialization**
   - Start at the root node (A).
   - Initialize the priority queue frontier with the starting node, its actual cost, and the heuristic value: `Frontier: [(A, 3, 0)]`
   - Initialize the explored list to keep track of visited nodes: `Explored: []`

2. **Iteration 1**
   - Dequeue the first element from the frontier: `Node, ActualCost, HeuristicValue = A, 3, 0`
   - Add A to the explored list: `Explored: [A]`
   - Expand node A and add its neighbors to the frontier with their actual costs, heuristic values, and combined costs (f(n) = g(n) + h(n)):
     - B (actual cost 2, heuristic value 1, combined cost 3): `Frontier: [(B, 2, 1, 3)]`
     - C (actual cost 1, heuristic value 2, combined cost 3): `Frontier: [(B, 2, 1, 3), (C, 1, 2, 3)]`

3. **Iteration 2**
   - Dequeue the first element from the frontier: `Node, ActualCost, HeuristicValue = C, 1, 2`
   - Add C to the explored list: `Explored: [A, C]`
   - Expand node C and add its neighbors to the frontier with their actual costs, heuristic values, and combined costs:
     - F (actual cost 0, heuristic value 0, combined cost 0): `Frontier: [(B, 2, 1, 3), (F, 0, 0, 0)]`

4. **Completion**
   - The goal node, F, is reached with a combined cost of 0, indicating that it is the optimal solution.

## Advantages of A*

- **Optimality**: A* guarantees finding the optimal solution if the heuristic function is admissible (h(n) never overestimates the true cost).
- **Efficiency**: A* efficiently explores the search space by considering both the actual cost and the estimated distance to the goal.
- **Completeness**: A* is complete if the search space is finite and the branching factor is finite.

## Disadvantages of A*

- **Memory Usage**: A* can consume a large amount of memory, especially for graphs with a high branching factor and path costs.
- **Time Complexity**: A* can be slow for graphs with high path costs or deep solutions, especially if the heuristic function is not admissible.
- **Heuristic Function**: A* relies heavily on the heuristic function, and choosing an inappropriate heuristic can lead to suboptimal solutions or inefficient search.

## Complexity Analysis

- **Time Complexity**: In the worst case, A* has exponential time complexity O(b^d), where b is the branching factor and d is the depth of the solution.
- **Space Complexity**: A* has space complexity O(b^d), as it needs to store all the nodes in the frontier.

## Properties of A*

- **Completeness**: A* is complete if the search space is finite and the branching factor is finite.
- **Optimality**: A* is optimal if the heuristic function is admissible (h(n) never overestimates the true cost) and consistent (h(n) is monotonically non-decreasing along the path).

## Conclusion

A* is an efficient and effective informed search algorithm that combines the advantages of Dijkstra's algorithm and greedy search. By considering both the actual cost and the estimated distance to the goal, A* guarantees finding the optimal solution while also being efficient in exploring the search space. However, its performance heavily relies on the admissibility and consistency of the heuristic function.

For a more detailed implementation and examples, refer to the code in the A* directory of this repository.
