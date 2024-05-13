#3
surname = []
name = []
age = []
mx = -1
x = 0
mn = 100
n = 0
with open ( "deti.txt", "r") as f:
    n = int(f.readline())
    for i in range(n):
        str = f.readline().split()
        surname.append(str[0])
        name.append(str[1])
        age.append(str[2])
        print(int(age[i]))
        if int(age[i]) < mn:
            mn = int(age[i])
            n = i
        if int(age[i]) > mx:
            mx = int(age[i])
            x = i
print(surname[n], name[n], age[n])
with open ( "young.txt", "w") as y:
    y.write(surname[n] + " " + name[n] + " " + age[n])
with open("old.txt", "w") as o:
    o.write(surname[x] + " " + name[x] + " " + age[x])







