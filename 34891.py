import sys


N, M = map(int, sys.stdin.readline().split())
print(N // M + (1 if N % M > 0 else 0))