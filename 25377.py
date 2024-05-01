import sys


N = int(sys.stdin.readline())

res = 100000
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        continue
    else:
        res = min(res, max(a, b))

if res == 100000:
    res = -1

print(res)