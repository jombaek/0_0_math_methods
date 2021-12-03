import numpy as np

with open('input.txt', 'r') as fin:
    n = fin.readline()
    a = np.array([float(x) for x in fin.read().split()])

result = (len(a) / np.sum(1.0 / a))

with open('output.txt', 'w') as fout:
    fout.write(str(result))