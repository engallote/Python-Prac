import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [['.' for _ in range(N)] for _ in range(N)]

    for i in range(N):
        arr[i][0] = '#'
        arr[i][N - 1] = '#'

    l, r = 1, N - 2
    for i in range(1, N // 2 + 1):
        arr[i][l] = '#'
        arr[i][r] = '#'
        l += 1
        r -= 1

    for i in range(N):
        print(*arr[i], sep='')