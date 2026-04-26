import numpy as np

# A. Creating Arrays

A = np.array([1,2,3,4])
print(A)

# B. Array Operations
A2 = np.array([5,6,7,8])
A_sum = A + A2
print(A_sum)

# C. Working with Matrices
matrix = np.array([[1,2],[3,4]])
transpose = matrix.T
print(transpose)

# D. Generating Data
random_nums = np.random.rand(3)
print(random_nums)