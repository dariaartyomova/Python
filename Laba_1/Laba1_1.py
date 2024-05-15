"""#1
a = 3
b = 3
c = 3
if a == b == c:
    print(a, b)
    break
if a >= b:
    if a >= c:
        mx = a
    else:
        mx = c
if b >= a:
    if b >= c:
        mx = b
    else:
        mx = c

if a <= b:
    if a <= c:
        mn = a
    else:
        mn = c
if b <= a:
    if b <= c:
        mn = b
    else:
        mn = c

print(mx, mn)
#2.1
n = int(input())
while n>0:
    k = 1
    st = ""
    while k<=n:
        st += str(k)
        k = k+1
    print(st)
    n = n-1
#2.2
n = int(input())
x = 0
while n>0:
    k = 2
    st = "1"
    x += 1
    while k<=n:
        st = str(k) + st + str(k)
        k = k+1
    print(" "*x + st)
    n = n - 1
"""
#2.3
n = 13
x = 0
n.bit_length()

while n>0:
    st = "1"
    k = 2
    while k<=n:
        st = str(k) + st + str(k)
        k = k+1
    t = len(str(n))
    print(" " * x * t + st)
    x += 1
    n = n - 1

