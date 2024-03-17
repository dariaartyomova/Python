"""n= int(input())
a = [0]*n
for i in range(n):
    a[i] = str(input())"""
a = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
for i in range(len(set(a))):
    n = 0
    s = a[0]
    for j in range(0, len(a)):
        if a[0] == a[j]:
            n += 1
    print(n)

    while s in a:
        a.remove(s)