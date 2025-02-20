import sys


N = int(sys.stdin.readline())

for _ in range(N):
    x, k, h = map(int, sys.stdin.readline().split())

    if k <= 140:
        if h == 0:
            res = x * k
        else:
            if k > h:
                res = x * (k - h) + 2 * x * h
            else:
                res = 2 * x * h
    else:
        if h == 0:
            k -= 140
            res = x * 140
            res += x * 1.5 * k
        else:
            k -= h
            res = x * 2 * h

            if k <= 140:
                res += x * k
            else:
                k -= 140
                res += x * 140
                res += x * 1.5 * k
    print(format(int(res), ","))