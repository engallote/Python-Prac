import sys


N, h, v = map(int, sys.stdin.readline().split())

mx = max(h * v * 4, (N - h) * v * 4, h * (N - v) * 4, (N - h) * (N - v) * 4)
print(mx)