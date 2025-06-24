import sys


N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if a < b:
        res += (b - a) * c

print(res)