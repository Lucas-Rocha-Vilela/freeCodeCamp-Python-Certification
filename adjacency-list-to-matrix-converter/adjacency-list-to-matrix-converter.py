def adjacency_list_to_matrix(adjacency_list: dict) -> list:
    adjacency_matrix = []
    for n in range(len(adjacency_list)):
        node_edges = []
        for edge in range(len(adjacency_list)):
            node_edges.append(0)
            if edge in adjacency_list[n]:
                node_edges[edge] = 1

        adjacency_matrix.append(node_edges)
    
    for i in range(len(adjacency_matrix)):
        print(adjacency_matrix[i])
    return adjacency_matrix

a = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
#adjacency_list_to_matrix(a)
#adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})


