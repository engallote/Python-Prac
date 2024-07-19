import sys


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    res, mx = 0, 0
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        if i >= 3:
            res -= arr[i - 3]

        res += arr[i]

        if mx < res:
            mx = res

    print(mx)