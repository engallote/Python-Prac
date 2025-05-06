import sys


N, M = map(int, sys.stdin.readline().split())
print((N * N + M * M) ** 0.5)