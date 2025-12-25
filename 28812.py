import sys


N, M = map(int, sys.stdin.readline().split())
res = 1000000000000

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    res = min(res, a + b + c * M)

print(res)