def neigh_with_d(g, node, d):
    found = []
    neighs = list(g.neighbors(node))
    for x in range(0, len(neighs)):
        if (g.degree[neighs[x]] == d):
            found.append(neighs[x])
    return found


def find_subgraph2(g, candidates, length, degree_list, nodes_found, list_to_return):

    if len(nodes_found) == length:
        nodes_found.pop(len(nodes_found) - 1)
        return list_to_return

    nodes_found.append(candidates)

    if len(nodes_found) == length:
        list_to_return.extend(nodes_found)
        nodes_found.pop(len(nodes_found) - 1)
        return list_to_return
    valid_neighs = neigh_with_d(g, candidates, degree_list[len(nodes_found)])
    for y in range (0, len(valid_neighs)):

        if valid_neighs[y] not in nodes_found:
            find_subgraph2(g, valid_neighs[y], length, degree_list, nodes_found, list_to_return)
        else:
            print("Neighbor not good ", valid_neighs[y])
    nodes_found.pop(len(nodes_found)-1)
    return list_to_return