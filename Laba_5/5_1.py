#1
with open ('input.txt', 'r') as f:
    d = f.read()
mas = d.split(' ')
k = 1
for i in range(len(mas)):
    k *= int(mas[i])
print(k)
f = open('output.txt', 'w')
f.write(str(k))
f.close()