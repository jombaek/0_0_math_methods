import numpy as np

with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    a = np.array([int(x) for x in fin.read().split()])

x, m = np.unique(a, return_counts=True)
w = np.divide(m, n)

with open('output.txt', 'w') as fout:
    fout.write(' '.join(str(i) for i in x))
    fout.writelines('\n')
    fout.write(' '.join(str(i) for i in m))
    fout.writelines('\n')
    fout.write(' '.join(str(i) for i in w))