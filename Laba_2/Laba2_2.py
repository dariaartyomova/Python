import functools
n = int(input())

def sierpinski(n):

    def triangle(t, i):
       space = " " * (2**i)
       return [space+x+space for x in t] + [x + " " + x for x in t]

    return functools.reduce(triangle, range(n), ["*"])

print("\n".join(sierpinski(n)))


