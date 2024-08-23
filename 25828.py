import sys


g, p, t = map(int, sys.stdin.readline().split())

res1 = g * p
res2 = g + (p * t)

if res1 == res2:
    print(0)
elif res1 > res2:
    print(2)
else:
    print(1)