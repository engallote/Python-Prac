import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    cur, res, x, w, pre = 0, 0, 0, 0, 0

    for i in range(M - 1):
        x, w = map(int, sys.stdin.readline().split())
        res += x - pre

        if cur + w < N:
            cur += w
        elif cur + w == N:
            cur = 0
            res += x * 2
        else:
            res += x * 2
            cur = w

        pre = x

    x, w = map(int, sys.stdin.readline().split())
    res += x - pre

    if cur + w <= N:
        cur = 0
        res += x
    else:
        res += x * 3
        cur = w

    print(res)

