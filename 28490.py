import sys


T = int(sys.stdin.readline())

res = 0
for i in range(T):
    w, h = map(int, sys.stdin.readline().split())
    res = max(res, w * h)

print(res)