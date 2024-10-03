import sys


w, h = map(int, sys.stdin.readline().split())
n, a, b = map(int, sys.stdin.readline().split())

res = 0

dw = w // a
dh = h // b
mn = dw * dh

if mn == 0:
    print(-1)
    exit(0)

while n > 0:
    n -= mn
    res += 1

print(res)