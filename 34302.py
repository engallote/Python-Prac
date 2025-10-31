import sys


N = int(sys.stdin.readline())
res, p = 0, 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        p += 1
    else:
        p = 0

    res = max(res, p)

print(res)