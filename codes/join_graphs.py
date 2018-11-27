def join_graphs(g,graph_info):
    print(len(graph_info["mal_nodes"]))
    for x in range (0, len(graph_info["mal_nodes"])):
        g.add_node(graph_info["mal_nodes"][x])
        for y in range(0, len(graph_info["extra_edges"][x])):
            g.add_edge(graph_info["mal_nodes"][x],graph_info["extra_edges"][x][y])
    print(g.number_of_edges())
    print(len(graph_info["nodes_to_attack"]))
    for x in range (0, len(graph_info["nodes_to_attack"])):
        for y in range (0, len(graph_info["N"][x])):
            g.add_edge(graph_info["nodes_to_attack"][x],graph_info["N"][x][y])
    print(g.number_of_edges())
    print(graph_info["int_adj_matrix"])
    print(len(graph_info["int_adj_matrix"][0]))
    for x in range(0, len(graph_info["int_adj_matrix"][0])):
        for y in range(x, len(graph_info["int_adj_matrix"][0])):
            if graph_info["int_adj_matrix"][x][y] == 1:
                g.add_edge(graph_info["mal_nodes"][x], graph_info["mal_nodes"][y])
    print(g.number_of_edges())