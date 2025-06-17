import sys


N, M = map(int, sys.stdin.readline().split())
res = 0

if N > 9:
    res += 60 * (N - 9)

res += M

print(res)
