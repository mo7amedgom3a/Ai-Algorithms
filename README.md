# introduction 

Welcome to the Ai-Algorithms repository! This collection is dedicated to various AI search algorithms, ranging from fundamental uninformed and informed search techniques to advanced algorithms like hill-climbing and genetic algorithms. Whether you are a student, researcher, or practitioner, this repository aims to provide comprehensive implementations and resources to aid in your exploration and application of AI search strategies.

## Why Do We Need Search Algorithms?

Search algorithms are essential for solving a wide range of problems in artificial intelligence. They help in finding solutions to problems by systematically exploring possible states. Whether it's pathfinding in a maze, optimizing a function, or solving puzzles, search algorithms provide the tools needed to navigate through the problem space efficiently.

## Steps to Build a Search Algorithm

1. **Goal Formulation**: Define what constitutes a successful solution. What is the end state or goal we want to achieve?
2. **Problem Formulation**: Describe the problem in a formal way, including the components necessary for the search process:
   - **Initial State**: The starting point of the search.
   - **Actions**: The set of possible actions or moves that can be taken from each state.
   - **Transition Model**: Describes the result of each action; it defines the state that will be reached after a particular action.
   - **Goal Test**: A function that checks if a given state is the goal state.
   - **Path Cost**: A function that assigns a numeric cost to each path or sequence of actions.

3. **Search for a Solution**: Use an appropriate search algorithm to explore the state space and find a solution path from the initial state to the goal state.

## Properties of Search Algorithms

When evaluating search algorithms, consider the following properties:

- **Completeness**: Does the algorithm always find a solution if one exists?
- **Optimality**: Does the algorithm always find the best (lowest cost) solution?
- **Time Complexity**: How long does it take to find a solution?
- **Space Complexity**: How much memory does the algorithm use during the search process?

## General Search Algorithm Pseudocode

Here is a general pseudocode for a search algorithm that takes a problem and a search strategy, then returns a solution:

```pseudo
function GENERAL-SEARCH(problem, strategy):
    initialize the frontier using the initial state of the problem
    initialize the explored set to be empty

    loop do:
        if the frontier is empty then
            return failure
        
        choose a leaf node from the frontier based on the strategy
        if the chosen node is a goal state then
            return the solution
        
        add the chosen node to the explored set
        expand the chosen node, adding the resulting nodes to the frontier
        only if they are not in the frontier or explored set

```
## Repository Contents

The repository is structured into three main folders:

- **Uninformed Search**
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Depth-Limited Search
  - Uniform Cost Search

- **Informed Search**
  - Best-First Search
  - Greedy Best-First Search
  - A* Search

- **Beyond Classical Search**
  - Local Search
  - Hill-Climbing
  - Simulated Annealing
  - Local Beam Search
  - Stochastic Beam Search
  - Genetic Algorithm

## Installation

```bash
git clone https://github.com/mo7amedgom3a/Ai-Algorithms.git
```

## Usage

```python
python3 main.py
```
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the LICENSE file for details.
## Contact
For any questions or suggestions, feel free to open an issue or contact us at [mo7amed_gomaa.contact](mailto:mo7amed.gom3a.7moda@gmail.com).