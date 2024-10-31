import sys


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    arr = list(map(int, sys.stdin.readline().split()))
    res = 0
    for i in range(N):
        if res + arr[i] <= 300:
            res += arr[i]

    print(res)