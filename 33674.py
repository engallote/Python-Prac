import sys


N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
star = [0 for _ in range(N)]
res, c = 0, 0

for i in range(M):
    for j in range(N):
        star[j] += arr[j]
        if star[j] > K:
            c = 1

    if c == 1:
        res += 1
        c = 0
        for j in range(N):
            star[j] = arr[j]

print(res)