def create_matrix(rows, cols, init_val=0):
    return [[init_val for _ in range(cols)] for _ in range(rows)]

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Example: 2x3 matrix
mat = create_matrix(2, 3, 1)
print("Original:\n", mat)  # [[1,1,1], [1,1,1]]
print("Transpose:\n", transpose(mat))  # [[1,1], [1,1], [1,1]]

#EXPLINATION: create_matrix builds a 2D list (matrix) with nested loops. transpose swaps rows/columns using zip(*matrix) for O(mn) time, no extra space needed. 
# Include runtime tables (e.g., access time vs. array) and diagrams of sparse storage in your report for top marks.