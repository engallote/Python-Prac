import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

tmp = list(map(int, sys.stdin.readline().split()))
for i in range(1, N + 1):
    arr[i][0] = tmp[i - 1]

tmp = list(map(int, sys.stdin.readline().split()))
for i in range(1, M + 1):
    arr[0][i] = tmp[i - 1]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if arr[i - 1][j] == arr[i][j - 1]:
            arr[i][j] = 0
        else:
            arr[i][j] = 1

print(arr[N][M])