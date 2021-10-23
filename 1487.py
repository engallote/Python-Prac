import sys


N = int(sys.stdin.readline().rstrip())
arr = [[0] * 2 for _ in range(N)]

for i in range(N):
    arr[i][0], arr[i][1] = map(int, sys.stdin.readline().rstrip().split())

arr.sort(key=lambda x:x[0])
res, sm = 0, 0

for i in range(N):
    cost, s = arr[i][0], 0

    for j in range(N):
        if arr[j][0] >= cost and cost - arr[j][1] > 0:
            s += cost - arr[j][1]

    if s > sm:
        sm = s
        res = cost

print(res)