import numpy as np
import random


def create_attacking_graph(size):
    k = int(np.floor(2.1 * np.log(size)))
    # print(k)
    np.random.seed(5)
    d_0 = np.random.randint(1, 1.2 * k, 1)[0]
    # print(d_0)
    d_1 = np.random.randint(d_0, 1.2 * k, 1)[0]
    # print(d_1)
    mal_nodes = [0]*k
    ext_degrees = [0]*k
    count = 0
    for x in range(size, size + k):
        mal_nodes[count] = x
        ext_degrees[count] = np.random.randint(d_0, d_1+1, 1)[0]
        count += 1
    print(mal_nodes)
    # print(ext_degrees)
    b = int(np.floor(np.log(size) ** 2))
    # print(b)
    random.seed(10)
    nodes_to_attack = random.sample(range(0,size), b)
    # print(nodes_to_attack)
    ext_nodes_connected = [0]*k
    c = 3
    N = []
    for x in range(0, b):
        N.append([])
        while len(N[x]) < c:
            idx = np.random.randint(0, k, 1)[0]
            if ext_nodes_connected[idx] != ext_degrees[idx] and mal_nodes[idx] not in N[x]:
                N[x].append(mal_nodes[idx])
                ext_nodes_connected[idx] += 1
        # for y in range(0, k):
        #     if ext_nodes_connected[y] != ext_degrees[y] and len(N[x]) < c:
        #         N[x].append(mal_nodes[y])
        #         ext_nodes_connected[y] += 1
    # print(N)
    print(ext_degrees)
    # print(ext_nodes_connected)
    extra_edges_to_original_graph = []
    for x in range (0, k):
        extra_edges_to_original_graph.append([])
        while ext_degrees[x] != ext_nodes_connected[x]:
            rn_node = np.random.randint(0, size, 1)[0]
            if rn_node not in nodes_to_attack and rn_node not in extra_edges_to_original_graph[x]:
                extra_edges_to_original_graph[x].append(rn_node)
                ext_nodes_connected[x] += 1
    # print(extra_edges_to_original_graph)
    int_adj_matrix = np.zeros([k, k])
    for x in range (0,k):
        for y in range (x,k):
            if abs(x - y) == 1:
                int_adj_matrix[x][y] = 1
                int_adj_matrix[y][x] = 1
            elif x != y:
                dice = np.random.randint(0, 2, 1)[0]
                int_adj_matrix[x][y] = dice
                int_adj_matrix[y][x] = dice
    # print(int_adj_matrix)
    int_degree = np.sum(int_adj_matrix, axis=0)
    print(int_degree)



    to_return = {}
    to_return["mal_nodes"] = mal_nodes
    to_return["ext_degree"] = ext_degrees
    to_return["nodes_to_attack"] = nodes_to_attack
    to_return["N"] = N
    to_return["extra_edges"] = extra_edges_to_original_graph
    to_return["int_adj_matrix"] = int_adj_matrix
    to_return["int_degree"] = int_degree

    return to_return
