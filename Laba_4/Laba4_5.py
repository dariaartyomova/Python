#5
n= int(input())
a=[]
for i in range(n):
    b=input()
    a.append(b.split())

for i in range(len(a)):
    b = ''
    q=a[i][0]


    if q != ' ':
        print(q)
        for y in range (len(a)):
            for x in range(len(a[i])-2):
                if q in a[y][x]:
                    b=b+a[y][x+1] + " "+ a[y][x+2]+ '     '
                    a[y][x]=' '
                    a[y][x+1] = ' '
                    a[y][x+2] = ' '

    print(b)
