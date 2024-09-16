import numpy as np

# generate random 2x2 matrix

matrix = np.random.rand(2, 2)

# pad the matrix in different ways

print(np.pad(matrix, 1, 'constant'))
print(np.pad(matrix, ((1, 2), (2, 1)), 'constant'))