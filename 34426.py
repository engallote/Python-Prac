import sys


N = int(sys.stdin.readline())

for _ in range(N):
    w = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    m, idx, cnt = 1000000000000, 0, 1

    for i in range(0, w * 2, 2):
        if arr[i + 1] / arr[i] < m:
            m = arr[i + 1] / arr[i]
            idx = cnt
        cnt += 1

    print(idx)