#!/usr/bin/env python3
import heapq
from graph.WeightedGraph import create_weighted_graph
from graph.UnWeightedGraph import create_unweighted_graph
from  graph.visualize_weighted_graph import visualize_graph
from  graph.visualize_unweighted_graph import visualize_graph
from  graph.Draw_path import draw_path_on_graph
from uniformed_search.Breadth_first_Search import bfs
from uniformed_search.Depth_first_search import dfs
from uniformed_search.Depth_limited_Search import dls
from uniformed_search.Uniform_cost_search import ucs
from informed_search.Best_first_search import best_first_search
from informed_search.heuristic import *
from informed_search.A_Star import a_star_search
from Beyond_Classical_Search.Genetic import genetic_algorithm
if __name__ == "__main__":
    graph = {}
    print("*"*50)
    print("Welcome to Ai Algorithms")
    print("*"*50)
    print("choose the type of graph you want to work with")
    print("1. Weighted Graph")
    print("2. Unweighted Graph")
    print("*"*50)
    type_graph = int(input("enter the number of the graph you want to work with:"))
    print("*"*50)
    if type_graph == 1:
        graph = create_weighted_graph()
        visualize_graph(graph)
        print("you can see the graph in the weighted_graph.png file")
    else:
        graph = create_unweighted_graph()
        visualize_graph(graph)
        print("you can see the graph in the unweighted_graph.png file")
    print("*"*50)
    print("choose the type of algorithms you want to use")
    print("1. uniformed search")
    print("2. informed search")
    print("3. beyond classical search")
    print("*"*50)
    algo_type = int(input("Enter here ... "))
    print("*"*50)
    if algo_type == 1:
        print("choose the type of uniformed search algorithm you want to use")
        print(50*"*")
        print("1. Breadth First Search")
        print("2. Depth First Search")
        print("3. Depth Limited Search")
        print("4. Uniform Cost Search")
        print(50*"*")
        algo = int(input("enter here ... "))
        print("*"*50)
        print(graph)
        start = input("Enter the start node: ")
        print("*"*50)
        goal = input("Enter the goal node: ")
        print("*"*50)
        if algo == 1:
            path = bfs(graph, start, goal)
            algo_type = "BFS"
        elif algo == 2:
            path = dfs(graph, start, goal)
            algo_type = "DFS"
        elif algo == 3:
            depth = int(input("Enter the depth limit: "))
            path = dls(graph, start, goal, depth)
            algo_type = "DLS"
        else:
            if type_graph == 1:
                path = ucs(graph, start, goal)
            else:
                print("the graph is unwighted, we will replace from unwighted to weighted graph")
                graph = create_weighted_graph()
                path = ucs(graph, start, goal)
            algo_type = "UCS"
        print("The path is: ", path)
        draw_path_on_graph(graph, path, algo_type)
    elif algo_type == 2:
        print("choose the type of informed search algorithm you want to use")
        print(50*"*")
        print("1. Best First Search")
        print("2. A* Search")
        print(50*"*")
        algo = int(input("enter here ... "))
        print("*"*50)
        print(graph)
        print("*"*50)
        start = input("Enter the start node: ")
        goal = input("Enter the goal node: ")
        if algo == 1:
            path = best_first_search(graph, start, goal, heuristic_values)
            algo_type = "best_first_search"
        else:
            path = a_star_search(graph, start, goal, heuristic_values)
            algo_type = "A_star"
        print("The path is: ", path)
        draw_path_on_graph(graph, path, algo_type)
    else:
        print("choose the type of beyond classical search algorithm you want to use")
        print(50*"*")
        print("1. Genetic Algorithm")
        print("2. Simulated Annealing")
        print("3. Hill Climbing")
        print(50*"*")
        algo = int(input("enter here ... "))
        print("*"*50)
        print(graph)
        print("*"*50)
        if algo == 1:
            start = input("Enter the start node: ")
            goal = input("Enter the goal node: ")
            nodes = list(graph.keys())
            best_path, best_fitness = genetic_algorithm(graph, nodes, start, goal)
            draw_path_on_graph(graph, best_path, "GA")
            algo_type = "GA"
            print("The path is: ", best_path)
            print("The fitness is: ", best_fitness)
        elif algo == 2:
            print("see the Redme file from Ai-Algorithms/Beyond_Classical_Search/Simulated_Annealing.md")
        else:
            print("see the Redme file from Ai-Algorithms/Beyond_Classical_Search/Hill_Climbing.md")


    

