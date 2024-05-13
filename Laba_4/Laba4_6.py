#6
text = 'лиса лак алиса динозавр лиса, настенька.. лиса алиса! динозавр алиса'
point = ['.', ',', ';', ':', '!', '?']
a = ''
for i in range(len(text)):
    if text[i] not in point:
        a = a + text[i]
a = a.split(' ')
n = len(a)
sl = {}

for i in range(len(set(a))):
    k = 1
    f = ''
    for j in range(1, len(a)):
        if a[0]==a[j]:
            f = a[j]
            k += 1
    for j in range(k):

        if f in a:
            a.remove(f)
        else:
            f = a[0]
            a.pop(0)
    sl[f] = k
print(sl)
s_w = sorted(sl, key=lambda x: (-sl[x], x))

for i in s_w:
    print(i)












