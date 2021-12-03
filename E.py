import numpy as np

def Moment(a, k):
    if k == 1:
        return 0
    elif k == 2:
        return np.var(a)
    else:
        return np.mean(np.power((a - np.mean(a)), k))

with open('input.txt', 'r') as fin:
    n, k = [int(x) for x in fin.readline().split()]
    a = np.array([float(x) for x in fin.read().split()])

with open('output.txt', 'w') as fout:
    fout.write(str(Moment(a, k)))