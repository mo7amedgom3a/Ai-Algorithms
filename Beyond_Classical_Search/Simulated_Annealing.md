# Simulated Annealing Algorithm
Simulated Annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy. It is used to find near-optimal solutions to optimization problems, especially those with a large search space and multiple local optima.
## Overview

Simulated Annealing simulates the physical process of annealing, where a material is heated and then slowly cooled to reach a low-energy state. Similarly, the algorithm starts with an initial solution and iteratively explores neighboring solutions, gradually reducing the exploration radius (temperature) to converge towards an optimal or near-optimal solution.
## The Physics Behind the Algorithm
The SA algorithm is based on the annealing process used in metallurgy, where a metal is heated to a high temperature quickly and then gradually cooled. At high temperatures, the atoms move fast, and when the temperature is reduced, their kinetic energy decreases as well. At the end of the annealing process, the atoms fall into a more ordered state, and the material is more ductile and easier to work with.

Similarly, in SA, a search process starts with a high-energy state (an initial solution) and gradually lowers the temperature (a control parameter) until it reaches a state of minimum energy (the optimal solution).

SA has been successfully applied to a wide range of optimization problems, such as TSP, protein folding, graph partitioning, and job-shop scheduling. The main advantage of SA is its ability to escape from local minima and converge to a global minimum. SA is also relatively easy to implement and does not require a priori knowledge of the search space.
## Algorithm
The simulated annealing process starts with an initial solution and then iteratively improves the current solution by randomly perturbing it and accepting the perturbation with a certain probability. The probability of accepting a worse solution is initially high and gradually decreases as the number of iterations increases.

The SA algorithm is quite simple, and it can be straightforwardly implemented as described below.

Simulated annealing is such an algorithm that escape local maxima by allowing some “bad” moves but gradually decrease their size and frequency.
## Acceptance Criterion
The acceptance criterion determines whether a new solution is accepted or rejected. The acceptance depends on the energy difference between the new solution and the current solution, as well as the current temperature. The classic acceptance criterion of SA comes from statistical mechanics, and it is based on the Boltzmann probability distribution. A system in thermal equilibrium at temperature T can be found in a state with energy E with a probability proportional to ![](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-e62ab736fd50c1090adf83d32ecb2da2_l3.svg)
![](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-87667f4faed520d201ab1a1326d4294e_l3.svg)
where k is the Boltzmann constant. Hence, at low temperatures, there is a small chance that the system is in a high-energy state. This plays a crucial role in SA because an increase in energy allows escape from local minima and find the global minimum.

Convergence to an optimal solution can theoretically be guaranteed only after an infinite number of iterations controlled by the procedure so-called cooling schedule.
The main control parameter is the temperature 𝑇.
The role of 𝑇 is to let the probability 𝑝 of accepting uphill moves be close to 1 in the earlier stage of the search and to let 𝑝→0 in the final stage.
A proper cooling schedule is needed in the finite-time implementation of SA to simulate the asymptotic convergence behavior of the SA
## pseudocode
![sm](https://github.com/mo7amedgom3a/Ai-Algorithms/blob/main/Beyond_Classical_Search/image.png?raw=true)

## Explanation
- **Initialization**: Start with an initial solution and set the initial temperature.
- **Loop**: Until the temperature reaches zero, iteratively perform the following steps:
- **Generate Neighbor**: Generate a neighboring solution randomly.
- **Calculate Energy Difference**: Calculate the difference in energy (objective function value) between the current and next solutions.
- **Acceptance Probability**: If the energy difference is negative (improvement) or with a certain probability based on the temperature and energy difference, accept the next solution as the current solution.
- **Cooling**: Reduce the temperature according to a cooling schedule.

## Example
![](https://www.baeldung.com/wp-content/uploads/sites/4/2023/03/animation.gif)
We can observe that worse solutions are frequently accepted when the temperature is high. Conversely, when the temperature is low (e.g., T<1), the algorithm is more selective, and better solutions are accepted with higher probability.

