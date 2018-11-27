from tree import Node


def retr_subgraph(val, g, starting_cands, degree, size_of_sub_graph, list_of_elements_found):
    root_node = Node(val)

    for i in range (0,len(starting_cands)):
        # if len(sub_graph_found) == size_of_sub_graph:
        #     print("Returned")
        #     return sub_graph_found
        list_of_elements_found.append(starting_cands[i])
        root_node.add_child(Node(starting_cands[i]))
        # print(root_node.children)
        print("Exploring node : " + str(starting_cands[i]))
        child_of_cand = list(g.neighbors(starting_cands[i]))
        # print("Neighbors found are " + str(child_of_cand))
        for x in range(0, len(child_of_cand)):
            if (g.degree[child_of_cand[x]] == degree):
                if child_of_cand[x] not in list_of_elements_found:
                    print("Degree Matched at neighbour " + str(child_of_cand[x]) + " and recursing on it")
                    element = []
                    element.append(child_of_cand[x])
                    ret_node = retr_subgraph(child_of_cand[x],g, element, degree, size_of_sub_graph, list_of_elements_found)
                    root_node.add_child(ret_node)
                    list_of_elements_found.pop(len(list_of_elements_found)-1)
    return root_node