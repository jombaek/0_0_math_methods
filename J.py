import numpy as np

with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        A[i] = np.array([int(x) for x in fin.readline().split()])
    b = np.array([int(x) for x in fin.readline().split()])

x = np.linalg.solve(A, b)
if np.linalg.matrix_rank(x) == 1:
    result = x
else:
    result = [-1]

with open('output.txt', 'w') as fout:
    fout.write(' '.join(str(i) for i in result))