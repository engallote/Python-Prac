import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

res = min(N, M) / 2 * 100
print(int(res))