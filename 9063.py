import sys

N = int(sys.stdin.readline())

minA, minB = 100000000, 1000000000
maxA, maxB = -100000000, -100000000
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    minA = min(a, minA)
    maxA = max(a, maxA)

    minB = min(b, minB)
    maxB = max(b, maxB)

print((maxA - minA) * (maxB - minB))