import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    res = 0
    while N > 1:
        d, m = N // 2, N % 2
        if m != 0:
            res += 1
        N = d + m
    print(res)