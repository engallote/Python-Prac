import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    res = [0 for _ in range(N)]
    mx, idx = 0, 0
    for i in range(M):
        arr = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            res[j] += arr[j]

            if res[j] > mx:
                mx = res[j]
                idx = j

    print(idx + 1)