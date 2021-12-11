import numpy as np
from numpy import linalg as LA

with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    a = np.array([float(x) for x in fin.read().split()])

b = a.reshape(n, n)
w, v = LA.eig(b)
p = np.argsort(w)
w = w[p]
v = v[:, p].T
  
with open('output.txt', 'w') as fout:
    fout.write(' '.join(str(i) for i in w))
    fout.write('\n')
    fout.write('\n'.join(' '.join(str(x) for x in row) for row in v))