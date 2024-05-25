import csv
import random
def Show(a,b,c):
    top = ''
    for i in range(len(a[0])):
        top += a[0][i] + "  |   "

    print(top)

    if c=="top":

        for i in range(1, b+6):
            for y in range(len(a[i])):
                print(a[i][y], end='')
                print('   |   ', end='')

            print('')
    elif c=="bottom":
        for i in range(len(a), len(a)-5, -1):
            for y in range(len(a[i])):
                print(a[i][y], end='')
                print('   |   ', end='')
            print('')
    elif c=="random":

        for i in range(b+5):
            g=random.randrange(len(a))
            for y in range(len(a[g])):
                print(a[g][y], end='')
                print('   |   ', end='')
            print('')



def Tipe(b):
    try:
        int(b)
    except ValueError:
        try:
            float(b)
        except ValueError:
             return "string"
        return "float"
    return "int"


def Info(a):
    print(len(a)-1,"x",len(a[0]))
    for i in range(len(a[0])):
        c=0
        print(a[0][i], end='')
        for y in range(1,len(a)):
            if a[y][i]!='':
                c+=1
                g=Tipe(a[y][i])
        if a[0][i] =="Survived":
            print("   ",c,"    ","Bool")
        else:
            print("   ", c, "    ", g)


def DelNaN(b):
    i = 0
    while i < len(b):
        p = 0
        for y in range(len(b[i])):
            if b[i][y] == '':
                p = 1
        if p == 1:
            del b[i]
        else:
            i += 1

    with open("Titanic.csv", "w",newline='') as f:
        writer = csv.writer(f)
        for i in range(len(b)):
            writer.writerow(b[i])

def MakeDS(b):
    c=0
    b7=[]
    b3=[]
    for i in range(len(b)):

        c+=1
        if c<7:
            b7.append(b[i])
        elif c>7 and c<10:
            b3.append(b[i])
            if c==9:
                c=0
    with open("C:\\Users\\redfo\\Desktop\\Питон лабы\\Laba_итог\\workdata\\Learning\\train.csv", "w",newline='') as f:
        writer = csv.writer(f)
        for i in range(len(b7)):
            writer.writerow(b7[i])
    with open("C:\\Users\\redfo\\Desktop\\Питон лабы\\Laba_итог\\workdata\\Testing\\test.csv", "w",newline='') as f2:
        writer = csv.writer(f2)
        writer.writerows(b3)



colonki=12
a=[]

with open("Titanic.csv", newline='')as csvfile:
    reader= csv.reader(csvfile)
    for row in reader:
        a.append(row)

e="top"

Show(a,0,e)
Info(a)
DelNaN(a)
MakeDS(a)