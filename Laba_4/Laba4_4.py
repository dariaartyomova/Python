#4
st = 'one two one two three'
st = st.split(' ')
n = len(st)
a = {}
for i in range(n):
    a[i] = st[i]

s = ""
print(a)
for i in range(n-1, -1, -1):
    k = 0
    for j in range(i-1, -1, -1):
        if a[i] == a[j]:
            k += 1
    s = str(k) + s
print(s)


