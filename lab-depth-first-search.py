def dfs(matrix: list, index: int):
    visited_node = []
    visited_node.append(index)
    stack = []
    stack.append(matrix[index])
    
    while stack:
        for line in stack:
            for i, el in enumerate(line):
                if i > index and el == 1 and i not in visited_node:
                    visited_node.append(i)
                    stack.append(matrix[i])

        if stack and stack[-1] == matrix[index]:
            for line in stack:
                for i, el in enumerate(line):
                    if i < index and el == 1 and i not in visited_node:
                        visited_node.append(i)
                        stack.append(matrix[i])
                        
        stack.pop()

    return visited_node
