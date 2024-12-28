import sys


N, K = map(int, sys.stdin.readline().split())
d, s = map(float, sys.stdin.readline().split())

m = d * N
m -= s * K

if m / (N - K) > 100 or 0 > m / (N - K):
    print("impossible")
else:
    print(m / (N - K))