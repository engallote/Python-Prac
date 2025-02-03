import sys


N, M = map(int, sys.stdin.readline().split())
if N == M:
    print(N + M)
else:
    print(min(N, M) + (min(N, M) + 1))