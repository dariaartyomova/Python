import numpy as np
#6

a = np.arange(16).reshape(4, 4)
b = np.array(a[0])
a[0], a[2] = a[2], b
print(a)