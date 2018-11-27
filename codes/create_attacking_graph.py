import numpy as np
import networkx as nx
from retr import retr_subgraph
from tree import print_tree
from tree import Node


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


deg_4 = get_all_nodes_of_a_degree(g,4)

print(deg_4)


nodes = retr_subgraph("root_node",g,deg_4,4,4,[])

print_tree(nodes,0)


#def create_attacking_graph(size_of_original_graph):
 #   k = 2.1 * np.log(size_of_original_graph)
