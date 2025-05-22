import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

d = min(N, M)

print(d * 2 + (N - d) % 2 + (M - d) % 2)