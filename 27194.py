import math
import sys


N, M = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())

res = math.ceil(m / (x * 60) + (N - m) / (y * 60))

if res < M:
    print(0)
else:
    print(res - M)