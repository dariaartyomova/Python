import numpy as np
#3
norm = np.random.normal(size=10^4)
mn = norm.min()
mx = norm.max()
sr = sum(norm)/len(norm)
summ = 0
for i in range(len(norm)):
    summ += (sr-norm[i])**2
stand_deviation = (summ/(len(norm)-1)**(1/2))

print(stand_deviation)

str5 = ""
for i in range(5):
    str5 += str(norm[i]) + " "
print(str5)
