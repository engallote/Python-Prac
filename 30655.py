import sys

while True:
    N, M = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0:
        break

    arr = [0 for _ in range(N + 1)]
    arr[M] = 1

    for _ in range(N - 2):
        n = int(sys.stdin.readline())
        arr[n] = 1

    for i in range(1, N + 1):
        if arr[i] == 0:
            print(i)
            break