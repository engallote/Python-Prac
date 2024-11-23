import sys


N = int(sys.stdin.readline())
mx, mn = 0, 10000000

for _ in range(N):
    cost = int(sys.stdin.readline())
    mx = max(mx, cost)
    mn = min(mn, cost)

mx //= 2

if mx > mn:
    print(0)
else:
    print(mn - mx)