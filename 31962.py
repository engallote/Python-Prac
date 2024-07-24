import sys


N, X = map(int, sys.stdin.readline().split())
res = -1
for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())

    if s + t <= X:
        res = max(res, s)

print(res)