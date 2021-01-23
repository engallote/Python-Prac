import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N, D = map(int, sys.stdin.readline().split())
    res = 0
    for _ in range(N):
        v, f, c = map(int, sys.stdin.readline().split())
        if v * (f/c) >= D:
            res += 1

    print(res)