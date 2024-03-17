a = "YYYAAIFFSSS"
a += "*"

s = ""
for i in range(0, len(set(a))-1):
    c = 1

    while a[i]==a[i+1]:
        a = a.replace(a[i+1], "", 1)
        c += 1
    if c != 1:
        s += a[i] + str(c)
    else:
        s += a[i]

print(s)