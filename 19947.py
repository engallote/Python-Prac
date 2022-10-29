import sys


def getMoney(m, x):
    if x == 0:
        return m

    ret = 0
    if x >= 5:
        ret = max(ret, getMoney(int(m * 1.35), x - 5))
    if x >= 3:
        ret = max(ret, getMoney(int(m * 1.2), x - 3))
    if x >= 1:
        ret = max(ret, getMoney(int(m * 1.05), x - 1))

    return ret


H, Y = map(int, sys.stdin.readline().rstrip().split())
res = getMoney(H, Y)
print(res)