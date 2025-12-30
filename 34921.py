import sys


N, M = map(int, sys.stdin.readline().split())
res = 10 + 2 * (25 - N + M)

if res < 0:
    print(0)
else:
    print(res)