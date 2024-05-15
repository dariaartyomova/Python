import numpy as np
#2
value = []
count = []
arr = [2, 2, 2, 3, 3, 3, 5] #np.array(input())
temp = arr[0]
k = 1

for i in range(1, len(arr)):
    if arr[i] == temp:
        k += 1

    else:
        value.append(temp)
        count.append(k)
        temp = arr[i]
        k = 1
value.append(arr[i])
count.append(k)
print(np.array(value), np.array(count))







