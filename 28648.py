import sys


N = int(sys.stdin.readline())
mn = 1000000000

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    mn = min(mn, a + b)

print(mn)