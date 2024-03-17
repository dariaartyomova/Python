a = "Y3A22IF2S3"
a1 = ""
n = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
i = len(a)
a = "*" + a
s = ""
while i > 0:
    if a[i] in n:
        s = a[i] + s
        i = i-1

    else:
        if s != "":
            a1 = a[i] * (int(s)-1) + a1
        a1 = a[i] + a1
        s = ""
        i = i-1
print(a1)