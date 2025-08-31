import sys


N, M = map(int, sys.stdin.readline().split())

d = 0
for i in range(1, 10000000):
    d += N
    N *= 2

    if d > M:
        print(i - 1)
        break