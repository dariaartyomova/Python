#2
with open ('1.txt') as f:
    d = f.read()
mas = d.split('\n')
for i in range(len(mas)):
    mas[i] = int(mas[i])
mas = sorted(mas)

print(d)
f = open('2.txt', 'w')
for i in range(len(mas)):
    f.write(str(mas[i])+'\n')
f.close()