import sys


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
p = int(sys.stdin.readline())

mn = min(a, b, c, d)

if a == b == c == d:
    print(1)
elif a == mn and a + p == b == c == d:
    print(1)
elif b == mn and a == b + p == c == d:
    print(1)
elif c == mn and a == b == c + p == d:
    print(1)
elif d == mn and a == b == c == d + p:
    print(1)
else:
    print(0)