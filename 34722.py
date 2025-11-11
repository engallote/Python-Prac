import sys


N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())

    if a >= 1000 or b >= 1600 or c >= 1500 or 1 <= d <= 30:
        res += 1

print(res)