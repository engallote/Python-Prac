import sys


h1, b1 = map(int, sys.stdin.readline().split())
h2, b2 = map(int, sys.stdin.readline().split())

h1 *= 3
h2 *= 3

res = abs(abs(h1 - h2) - abs(b1 - b2))

if h1 + b1 > h2 + b2:
    print(1, res)
elif res == 0:
    print("NO SCORE")
else:
    print(2, res)