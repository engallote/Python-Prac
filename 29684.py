import sys


while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    arr = list(map(int, sys.stdin.readline().split()))
    mn, idx = 100000000, -1

    for i in range(N):
        if abs(2023 - arr[i]) < mn:
            mn = abs(2023 - arr[i])
            idx = i

    print(idx + 1)