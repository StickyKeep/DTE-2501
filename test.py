# Just a test of things

import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[7,8,9], [10, 11, 12], [13, 14, 15]])
C = np.array([1, 2])
D = np.array([3, 4])

result = np.dot(A, B)
result2 = np.dot(C, D)
print(result)

result = A @ B
result = C @ D

print(result)
print(result2)

