import sys


N, M = map(int, sys.stdin.readline().split())
res = [0 for _ in range(M)]
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if res[j] < arr[j]:
            res[j] = arr[j]

print(sum(res))