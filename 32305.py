import sys


N, K = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())

m = (N * K) % 12

t = (N * K) // 12
if m > 0:
    t += 1

print(t * d)