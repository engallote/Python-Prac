import sys


N, M = map(int, sys.stdin.readline().split())

d = M // N
m = M % N

if (d % 2 == 0 and N // 2 > m) or (d % 2 == 1 and N // 2 < m):
    print("up")
else:
    print("down")