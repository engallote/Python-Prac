import sys

N = int(sys.stdin.readline())
bus, res = 0, 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    bus -= a
    bus += b

    res = max(res, bus)

print(res)