import numpy as np

precision = 0.000001

with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        A[i] = np.array([float(x) for x in fin.readline().split()])
    b = np.array([float(x) for x in fin.readline().split()])

arr = np.column_stack((A, b))

def Metod_Gaussa(arr):
    x = [0] * n
    for i in range(n - 1):
        if abs(arr[i][i]) < precision:
            return [-1]
        for j in range(i + 1, n):
            ratio = arr[j][i] / arr[i][i]
            for k in range(n + 1):
                arr[j][k] = arr[j][k] - ratio * arr[i][k]
    if abs(arr[n - 1][n - 1]) < precision:
        return [-1]
    x[n - 1] = arr[n - 1][n] / arr[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = arr[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - arr[i][j] * x[j]
        x[i] = x[i] / arr[i][i]
    return x

result = Metod_Gaussa(arr)

with open('output.txt', 'w') as fout:
    fout.write(' '.join(str(i) for i in result))