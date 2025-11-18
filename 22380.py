import sys


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    arr = list(map(int, sys.stdin.readline().split()))
    res, d = 0, M // N

    for i in range(N):
        if arr[i] <= d:
            res += arr[i]
        else:
            res += d

    print(res)