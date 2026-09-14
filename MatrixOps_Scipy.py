"""
Create a matrix of 4x4 order and find out the transpose of the matrix and the rank of the matrix using sci-py.
"""
import numpy as np
import scipy.linalg as la

M3 = np.array([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
])

M3_transpose = M3.T

# Calculate rank using SciPy's SVD implementation 
# We count how many singular values are greater than zero (or a tiny threshold)
singular_values = la.svd(M3, compute_uv=False)
matrix_rank = np.sum(singular_values > 1e-12)

print("Transpose Matrix:\n", M3_transpose)
print(f"\nRank of the Matrix: {matrix_rank}")
