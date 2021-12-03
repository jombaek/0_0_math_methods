import numpy as np

with open('input.txt', 'r') as fin:
    N, M = map(int, fin.readline().split())
    a = np.array(list(map(float, fin.read().split())))

b = np.reshape(a, (N, M))

result = np.corrcoef(b)

with open('output.txt', 'w') as fout:
    np.savetxt(fout, result, fmt = '%.3f')