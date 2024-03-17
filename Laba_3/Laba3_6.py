a = "открытое акционерное общество"
a = a.title()
i = len(a) + 1
s = ""
a = "*" + " " + a
while i > 0:
    if a[i-1] == " ":
        s = a[i] + s
        i -= 1
    i -= 1
print(s)