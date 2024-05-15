import numpy as np
#7

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

i = iris[:, 4]
i = i[np.append(np.where(i[1:] != i[:-1]), len(i) - 1)]

print(i)
print(len(i))

