import sys


N, M = map(int, sys.stdin.readline().split())
arr1, arr2 = [], []
res = 0

for _ in range(N):
    arr1.append(list(sys.stdin.readline().rstrip()))

sys.stdin.readline()

for _ in range(N):
    arr2.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            res += 1

print(res)