import numpy as np
import networkx as nx
from retr import retr_subgraph
from tree import print_tree
from tree import Node
from create_attacking_graph import create_attacking_graph
from join_graphs import join_graphs
from find_subgraph import find_subgraph
from find_subgraph import get_all_nodes_of_a_degree
from find_subgraph import create_graph_list
from find_subgraph import check_int_structure

p1 = "dummyGraph.txt"


def readGraph(path):
    g = nx.read_edgelist(path, comments="#", create_using=nx.Graph(), nodetype=int)
    return g


g = readGraph(p1)


print(g.number_of_nodes())

sub_graph_info = create_attacking_graph(g.number_of_nodes())

join_graphs(g, sub_graph_info)

print(g.number_of_nodes())

deg_lst = [0] * len(sub_graph_info["ext_degree"])

print(sub_graph_info["ext_degree"])
print(sub_graph_info["int_degree"])

for x in range(0, len(sub_graph_info["ext_degree"])):
    deg_lst[x] += sub_graph_info["ext_degree"][x]
    deg_lst[x] += sub_graph_info["int_degree"][x]

candidates =get_all_nodes_of_a_degree(g, deg_lst[0])

graphs_found = find_subgraph(g, candidates, len(sub_graph_info["mal_nodes"]), deg_lst, [], [])

graph_list = create_graph_list(graphs_found, len(sub_graph_info["mal_nodes"]))

print(graph_list)

recovered_sub_graph = check_int_structure(g, graph_list, sub_graph_info["int_adj_matrix"])

print(recovered_sub_graph)

#def create_attacking_graph(size_of_original_graph):
 #   k = 2.1 * np.log(size_of_original_graph)
