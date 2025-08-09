import sys


N, M = map(int, sys.stdin.readline().split())
mx = 0

for _ in range(5):
    a, b = map(int, sys.stdin.readline().split())
    mx = max(mx, a + b * 10)

res = N + M * 10

if mx >= res:
    print(mx - res + 1)
else:
    print(0)