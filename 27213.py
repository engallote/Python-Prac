import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if N == 1 or M == 1:
    print(max(N, M))
else:
    res = M * 2 + (N - 2) * 2
    print(res)