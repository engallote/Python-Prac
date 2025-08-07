import sys


N = int(sys.stdin.readline())
res, pre, h = 1, 1, 1

for i in range(1000):
    pre += 2

    res = res + pre ** 2

    if res > N:
        break
    h += 1

print(h)