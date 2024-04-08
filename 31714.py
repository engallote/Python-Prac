import sys


N, M, D = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.sort()
    arr.append(tmp)

for i in range(N):
    for j in range(M):
        arr[i][j] += D * (i + 1)

flag = True
for i in range(1, N):
    for j in range(M):
        if arr[i - 1][j] >= arr[i][j]:
            flag = False
            break

    if not flag:
        break

if flag:
    print("YES")
else:
    print("NO")