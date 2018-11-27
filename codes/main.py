import numpy as np
import networkx as nx
from retr import retr_subgraph
from tree import print_tree
from tree import Node
from create_attacking_graph import create_attacking_graph


p1 = "dummyGraph.txt"


def readGraph(path):
    g = nx.read_edgelist(path, comments="#", create_using=nx.Graph(), nodetype=int)
    return g


g = readGraph(p1)


def get_all_nodes_of_a_degree(g,d):

    node_list_with_same_degree = []
    for node in g.nodes(data=False):
        if (g.degree[node] == d):
            node_list_with_same_degree.append(node)
    return node_list_with_same_degree

print(g.number_of_nodes())

sub_graph_info = create_attacking_graph(g.number_of_nodes())

print(sub_graph_info["extra_edges"])

#def create_attacking_graph(size_of_original_graph):
 #   k = 2.1 * np.log(size_of_original_graph)
