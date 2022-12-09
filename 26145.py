import sys


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    arr.append(0)

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(N + M):
        arr[i] -= tmp[j]
        arr[j] += tmp[j]

for i in range(N + M):
    print(arr[i], end=' ')