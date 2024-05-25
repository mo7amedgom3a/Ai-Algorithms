import random
import numpy as np
from graph.WeightedGraph import create_weighted_graph

graph = create_weighted_graph()


nodes = list(graph.keys())

# Create a complete graph with high cost for missing connections
def create_complete_graph(original_graph, nodes, high_cost=999):
    complete_graph = {node: {n: high_cost for n in nodes} for node in nodes}
    for node in original_graph:
        for neighbor in original_graph[node]:
            complete_graph[node][neighbor] = original_graph[node][neighbor]
    """
    the graph looks like this:
    {
        'A': {'A': 999, 'B': 1, 'C': 4, 'D': 999, 'E': 999, 'F': 999, 'G': 999},
        'B': {'A': 999, 'B': 999, 'C': 999, 'D': 2, 'E': 5, 'F': 999, 'G': 999},
        'C': {'A': 999, 'B': 999, 'C': 999, 'D': 999, 'E': 999, 'F': 3, 'G': 6},
        'D': {'A': 999, 'B': 999, 'C': 999, 'D': 999, 'E': 999, 'F': 999, 'G': 999},
        'E': {'A': 999, 'B': 999, 'C': 999, 'D': 999, 'E': 999, 'F': 999, 'G': 999},
        'F': {'A': 999, 'B': 999, 'C': 999, 'D': 999, 'E': 999, 'F': 999, 'G': 999},
        'G': {'A': 999, 'B': 999, 'C': 999, 'D': 999, 'E': 999, 'F': 999, 'G': 999}
    }
    no connection between nodes has a cost of 999
    """
    return complete_graph

# Create the complete graph
graph = create_complete_graph(graph, nodes)

# Parameters for the genetic algorithm
POPULATION_SIZE = 100
NUM_GENERATIONS = 200
MUTATION_RATE = 0.2
TOURNAMENT_SIZE = 5

# Generate a random path from start to goal
def generate_random_path(nodes, start, goal):
    path = [node for node in nodes if node not in [start, goal]]
    # shuffle the path to make it random
    random.shuffle(path)
    return [start] + path + [goal]

# Calculate the total distance of a path from start to goal
def calculate_fitness(path, graph):
    """
    Calculate the total distance of a path from start to goal
    :param path: list of nodes
    :param graph: graph with distances between nodes
    """
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance

# Tournament selection
def tournament_selection(population, fitnesses):
    """
    Select the best individual from a random tournament
    :param population: list of paths
    :param fitnesses: list of fitness values corresponding to the paths
    """
    # Select TOURNAMENT_SIZE random individuals from the population
    tournament = random.sample(list(zip(population, fitnesses)), TOURNAMENT_SIZE)
    tournament.sort(key=lambda x: x[1])
    # Return the individual with the best fitness
    return tournament[0][0]

# Crossover (ordered crossover)
def crossover(parent1, parent2, start, goal):
    """
    Create a child path by combining two parent paths
    :param parent1: list of nodes in the first parent
    :param parent2: list of nodes in the second parent
    :param start: start node
    :param goal: goal node
    """
    # Select a random subpath from parent1
    start_idx, end_idx = sorted(random.sample(range(1, len(parent1) - 1), 2))
    # Create a child path with the subpath from parent1
    child = [None] * len(parent1)
    # Copy the subpath from parent1 to the child
    child[start_idx:end_idx+1] = parent1[start_idx:end_idx+1]
    
    # Add the missing nodes from parent2 to the child
    pointer = 1
    for node in parent2[1:-1]:
        if node not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = node

    # Set the start and goal nodes
    child[0], child[-1] = start, goal
    # Return the child path [start, ..., goal]
    return child

# Mutation (swap mutation)
def mutate(path):
    """
    Swap two random nodes in the path with a given probability
    :param path: list of nodes
    """
    if random.random() < MUTATION_RATE:
        # Select two random nodes to swap (excluding the start and goal nodes)
        i, j = random.sample(range(1, len(path) - 1), 2)
        path[i], path[j] = path[j], path[i]

# Genetic Algorithm to find the shortest path from start to goal
def genetic_algorithm(graph, nodes, start, goal):
    """
    Find the shortest path from start to goal using a genetic algorithm
    :param graph: graph with distances between nodes
    :param nodes: list of nodes in the graph
    :param start: start node
    :param goal: goal node
    """
    graph = create_complete_graph(graph, nodes)
    population = [generate_random_path(nodes, start, goal) for _ in range(POPULATION_SIZE)]
    best_path = None
    best_fitness = float('inf')

    for generation in range(NUM_GENERATIONS):
        # Calculate the fitness of each individual in the population
        fitnesses = [calculate_fitness(path, graph) for path in population]

        # Create a new population by selecting parents, crossover, and mutation
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1 = crossover(parent1, parent2, start, goal)
            child2 = crossover(parent2, parent1, start, goal)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

        # Find the best path in the current generation
        current_best_fitness = min(fitnesses)
        if current_best_fitness < best_fitness:
            # Update the best path and fitness
            best_fitness = current_best_fitness
            best_path = population[fitnesses.index(current_best_fitness)]

        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    return best_path, best_fitness
