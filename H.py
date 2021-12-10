import numpy as np
import pandas as pd

with open('input.txt', 'r') as fin:
    n, m = map(int, fin.readline().split())
    a = np.array([int(x) for x in fin.read().split()])

b = a.reshape(n, m)

xy = pd.DataFrame(data = b.T)

r = xy.corr(method='kendall')
result = r.values.tolist()

with open('output.txt', 'w') as fout:
    fout.write('\n'.join(' '.join(str(x) for x in row) for row in result))