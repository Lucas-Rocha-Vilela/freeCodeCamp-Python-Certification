def dfs_n_queens(n):
    if n < 1:
        return []
    solutions = []
    visited = []
    dive_in(n, 0, solutions, visited)
    return solutions
        
def dive_in(matrix_size, row, solutions, visited):
    if row >= matrix_size:
        solutions.append(visited.copy())
        return
    for col in range(matrix_size):
        if col not in visited and all(abs(col - v) != abs(row - i) for i, v in enumerate(visited)):
            visited.append(col)
            dive_in(matrix_size, row + 1, solutions, visited)
            visited.pop()

#print(dfs_n_queens(5))

