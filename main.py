#!/usr/bin/env python3
from graph.WeightedGraph import create_weighted_graph
from graph.UnWeightedGraph import create_unweighted_graph
from  graph.visualize_weighted_graph import visualize_graph
from  graph.visualize_unweighted_graph import visualize_graph
from  graph.Draw_path import draw_path_on_graph
from uniformed_search.Breadth_first_Search import bfs
from uniformed_search.Depth_first_search import dfs
from uniformed_search.Depth_limited_Search import dls
from informed_search.Best_first_search import best_first_search
from informed_search.heuristic import heuristic_values
if __name__ == "__main__":
    weighted_graph = create_weighted_graph()
    visualize_graph(weighted_graph)
    unweighted_graph = create_unweighted_graph()
    visualize_graph(unweighted_graph)
    path = bfs(weighted_graph, 'A', 'F')
    print(path)
    algorithm = 'BFS'
    draw_path_on_graph(unweighted_graph, path, algorithm)
    path = dfs(unweighted_graph, 'A', 'D')
    print(path)
    algorithm = 'DFS'
    draw_path_on_graph(unweighted_graph, path, algorithm)
    depth_limit = 3
    path = dls(unweighted_graph, 'A', 'E', depth_limit)
    print(path)
    algorithm = 'DLS'
    draw_path_on_graph(unweighted_graph, path, algorithm)
    path = best_first_search(weighted_graph, 'A', 'G', heuristic_values)
    print(path)
    algorithm = 'Best_First_Search'
    draw_path_on_graph(weighted_graph, path, algorithm)
