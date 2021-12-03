import numpy as np

def WAM(a):
    return np.average(a.T[0], weights = a.T[1])

def WHM(a):
    return np.sum(a.T[1] / np.sum(a.T[1] / a.T[0]))

def WGM(a):
    return np.exp((1 / np.sum(a.T[1])) * np.sum(a.T[1] * np.log(a.T[0])))

with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    a = np.array([float(x) for x in fin.read().split()])

b = a.reshape(n, 2)

result = str(WAM(b)) + ' ' + str(WHM(b)) + ' ' + str(WGM(b))

with open('output.txt', 'w') as fout:
    fout.write(result)