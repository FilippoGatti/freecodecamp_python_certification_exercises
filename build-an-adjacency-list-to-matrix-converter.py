def adjacency_list_to_matrix(list_matrix: dict):
    matrix = []
    
    for i in list_matrix.keys():
        inner_list = [0] * len(list_matrix.keys())
        for j in list_matrix[i]:
            inner_list[j] = 1
        matrix.append(inner_list)
    
    print(matrix)

    return matrix
