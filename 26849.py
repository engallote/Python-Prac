import sys


N = int(sys.stdin.readline())
res, mn, mx = 0.0, 10000000000, -10000000000

for _ in range(N):
    a, b = map(float, sys.stdin.readline().split())
    mx = max(a / b, mx)
    mn = min(a / b, mn)
    res += a / b

print("%.11f %.11f %.11f" %(mn, mx, res))