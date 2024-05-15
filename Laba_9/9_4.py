import numpy as np
#4
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
mx = 10**(-10)
for i in range(1, len(x)):
    if x[i-1] == 0:
        if x[i] > mx:
            mx = x[i]
print(mx)


