import numpy as np
#1
with open ('1.txt', 'r') as f:
    mas = [[int(num) for num in line.split(',')] for line in f]
a = np.matrix(mas)
a = np.array(a)

print(a.sum())
print(a.max())
print(a.min())

























