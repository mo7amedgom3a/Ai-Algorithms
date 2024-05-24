# Advanced Search Algorithms

In this folder, you'll find implementations of advanced search algorithms that go beyond classical approaches. These algorithms are designed to tackle complex optimization problems and explore solution spaces more efficiently.

## Local Search

Local search algorithms focus on exploring the neighborhood of the current solution iteratively in search of a better solution. Unlike global search algorithms, which explore the entire search space, local search algorithms make decisions based solely on the quality of neighboring solutions.

### Global Search vs. Local Search

Global search algorithms explore the entire search space systematically to find the optimal solution. In contrast, local search algorithms focus on improving the current solution iteratively by exploring its neighborhood.
## Cost Function vs. Objective Function

In optimization problems, the terms "cost function" and "objective function" are often used interchangeably, but they can have slightly different interpretations depending on the context.

### Objective Function

The objective function, also known as the fitness function or evaluation function, quantifies the quality of a solution based on predefined criteria. It assigns a numerical value to each solution, indicating how well it satisfies the problem requirements or objectives. The goal of optimization algorithms is to find the solution(s) that maximize or minimize the objective function, depending on the problem type (maximization or minimization).

### Cost Function

The cost function represents the actual cost associated with a solution. It measures the resources, time, or other constraints required to implement or execute the solution in a real-world scenario. The cost function is often used in practical optimization problems where minimizing resource usage or maximizing efficiency is the primary concern.

### Relationship to Global and Local Extrema

The concepts of global maximum, local maximum, global minimum, and local minimum are related to both the objective function and the cost function.

- **Global Maximum**: The highest value of the objective function in the entire search space. It represents the best possible solution(s) to the optimization problem.
- **Local Maximum**: The highest value of the objective function in the neighborhood of a particular solution. Local maxima are points where the objective function is higher than its neighboring points but not necessarily the highest in the entire search space.
- **Global Minimum**: The lowest value of the objective function in the entire search space. It represents the optimal solution(s) that satisfy the problem requirements.
- **Local Minimum**: The lowest value of the objective function in the neighborhood of a particular solution. Local minima are points where the objective function is lower than its neighboring points but not necessarily the lowest in the entire search space.

### Relationship to Optimization Algorithms

- **Global Search Algorithms**: Global search algorithms aim to find the global maximum or minimum of the objective function by exploring the entire search space systematically. They are typically used when the problem space is small, and finding the optimal solution is crucial.
- **Local Search Algorithms**: Local search algorithms focus on finding local maxima or minima by iteratively exploring the neighborhood of a particular solution. They are suitable for large, complex optimization problems where finding the global optimum is difficult or impractical.
![objective-Vs-cost](https://qph.cf2.quoracdn.net/main-qimg-f4be1e3cd5dcab8d84fb3ccdee113049-lq)
### Local Beam Search

Local beam search is a parallel variant of local search that maintains multiple candidate solutions, known as beams, in parallel. It starts with multiple initial solutions and iteratively explores their neighborhoods. It selects the best solutions from each iteration to form the next set of candidate solutions.

### Stochastic Beam Search

Stochastic beam search is a variant of local beam search that introduces randomness into the selection process. Instead of selecting the best solutions deterministically, stochastic beam search randomly selects solutions from the set of candidate solutions, allowing it to explore a broader solution space.

### Hill-Climbing

Hill-climbing is a simple local search algorithm that iteratively moves towards the best neighboring solution. At each iteration, it selects the neighboring solution with the highest objective function value and moves to it, assuming it is better than the current solution.

#### Terminology

- Objective Function: Evaluates the quality of a solution.
- Cost Function: Another term for the objective function.
- Global Maximum: The highest value of the objective function in the entire search space.
- Local Maximum: The highest value of the objective function in the neighborhood of the current solution.
- Local Minimum: The lowest value of the objective function in the neighborhood of the current solution.
- Global Minimum: The lowest value of the objective function in the entire search space.
- Flat: Refers to a region of the search space where the objective function values do not change significantly.
- Shoulder: Refers to a region of the search space where the objective function values change abruptly.
![Hill-Climbing](https://static.javatpoint.com/tutorial/ai/images/hill-climbing-algorithm-in-ai.png)
### Simulated Annealing

Simulated annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy. It starts with an initial solution and iteratively explores neighboring solutions. Unlike hill-climbing, simulated annealing accepts Bad solutions with a certain probability, allowing it to escape local optima and explore a broader solution space and then he accept only Good Solutions after period time.

### Genetic Algorithm

Genetic algorithms are population-based optimization algorithms inspired by the process of natural selection and genetics. They maintain a population of candidate solutions, known as chromosomes, and iteratively evolve them through selection, crossover, and mutation operations. Genetic algorithms can efficiently explore large solution spaces and find near-optimal solutions in complex optimization problems.

#### Terminology

- Population: The set of candidate solutions (chromosomes) in each generation.
![population](https://static.javatpoint.com/tutorial/machine-learning/images/genetic-algorithm-in-machine-learning2.png)
- Chromosomes: Candidate solutions represented as strings of genes.
- Fitness Function: Evaluates the quality of a chromosome.
- Selection: The process of selecting chromosomes for reproduction based on their fitness.
- Crossover: The process of combining genetic material from two parent chromosomes to produce offspring.
![crossover](https://static.javatpoint.com/tutorial/machine-learning/images/genetic-algorithm-in-machine-learning3.png)
- Mutation: The process of introducing random changes into a chromosome to maintain diversity.
![mutation](https://static.javatpoint.com/tutorial/machine-learning/images/genetic-algorithm-in-machine-learning4.png)

## Complexity Analysis and Properties

- **Time Complexity**: The time complexity of each algorithm depends on various factors such as the problem size, search space structure, and algorithm parameters. In general, local search algorithms have lower time complexity compared to global search algorithms, but they may get stuck in local optima.
- **Space Complexity**: The space complexity depends on the representation of solutions and the size of the search space. Population-based algorithms like genetic algorithms may require more memory due to the storage of multiple solutions in the population.
- **Properties**: Each algorithm has its own set of properties, such as completeness, optimality, and scalability. Local search algorithms are generally incomplete and may find suboptimal solutions. Genetic algorithms are scalable and can handle large solution spaces but do not guarantee finding the optimal solution.

For detailed implementation examples and further exploration, refer to the code in each algorithm's directory.

