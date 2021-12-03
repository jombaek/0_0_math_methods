import numpy as np

with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    a = np.array([float(x) for x in fin.read().split()])

k = int(1 + np.floor(np.log(n) / np.log(2)))
hist, bin_edges = np.histogram(a, k)

with open('output.txt', 'w') as fout:
    fout.write(' '.join(str(x) for x in hist))