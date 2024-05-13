#3
n = int(input())
a = set()
for i in range(n):
    t = input()
    if t in a:
        print("REPEAT")
    else:
        print("OK")
        a.add(t)




