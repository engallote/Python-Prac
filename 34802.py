import sys

h1, m1, s1 = map(int, sys.stdin.readline().split(":"))
h2, m2, s2 = map(int, sys.stdin.readline().split(":"))
a, b = map(int, sys.stdin.readline().split())

if b != 0:
    a -= a * (b / 100)
s = (h1 * 60 + m1) * 60 + s1
e = (h2 * 60 + m2) * 60 + s2

if s + a <= e:
    print(1)
else:
    print(0)
