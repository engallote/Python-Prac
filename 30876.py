import sys


N = int(sys.stdin.readline())
xx, yy, res = 0, 0, 1000000

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y < res:
        xx = x
        yy = y
        res = y

print(xx, yy)