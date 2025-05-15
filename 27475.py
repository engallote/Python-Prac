import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    du = list(map(int, sys.stdin.readline().split()))
    lr = list(map(int, sys.stdin.readline().split()))
    res = 0

    for i in du:
        if i in lr:
            res += 1

    print(res)