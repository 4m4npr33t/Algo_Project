def get_all_nodes_of_a_degree(g,d):

    node_list_with_same_degree = []
    for node in g.nodes(data=False):
        if (g.degree[node] == d):
            node_list_with_same_degree.append(node)
    return node_list_with_same_degree


def neigh_with_d(g, node, d):
    found = []
    neighs = list(g.neighbors(node))
    for x in range(0, len(neighs)):
        if (g.degree[neighs[x]] == d):
            found.append(neighs[x])
    return found


def find_subgraph(g, candidates, length, degree_list, nodes_found, list_to_return):
    print("degree list is ", degree_list)
    print("status of nodes found ", nodes_found)
    if len(nodes_found) == length:
        nodes_found.pop(len(nodes_found) - 1)
        return list_to_return
    print("status of nodes found ", nodes_found)
    print("Node added", candidates)
    nodes_found.append(candidates)
    if len(nodes_found) == length:
        list_to_return.extend(nodes_found)
        print("Length matched list added is",list_to_return)
        nodes_found.pop(len(nodes_found) - 1)
        return list_to_return
    print("status of nodes found ", nodes_found)
    print("Currently checking for degree ", degree_list[len(nodes_found)]);
    valid_neighs = neigh_with_d(g, candidates, degree_list[len(nodes_found)])
    print("Neighbours found with correct degree", valid_neighs)
    for y in range (0, len(valid_neighs)):
        if valid_neighs[y] not in nodes_found:
            print("exploring on neigh ", valid_neighs[y])
            find_subgraph(g, valid_neighs[y], length, degree_list, nodes_found, list_to_return)
        else:
            print("Neighbor not good ", valid_neighs[y])
    nodes_found.pop(len(nodes_found)-1)
    print("status of nodes found ", nodes_found)
    return list_to_return


def create_graph_list(graphs_list, length):
    lst = []
    for x in range(0, len(graphs_list), length):
        lst.append(graphs_list[x:x+length])
    return lst

def check_int_structure(g, graph_list, adj_matrix):
    for x in range (0, len(graph_list)):
        flag = True
        print("New graph to check for ", graph_list[x])
        for j in range(0, len(adj_matrix[0])):
            node = graph_list[x][j]
            print("Node checking for", node)
            neighs = list(g.neighbors(node))
            print("Neighs", neighs)
            for k in range(j, len(adj_matrix[0])):
                if adj_matrix[j][k] == 1:
                    print("Looking for neigh ", graph_list[x][k])
                    flag = graph_list[x][k] in neighs
                    print("Flag is", flag)
                    if not flag:
                        break
            if not flag:
                break
        if flag:
            return graph_list[x]
