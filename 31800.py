import sys


N = int(sys.stdin.readline())
pro = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

arr = []
for i in range(N):
    arr.append((i, pro[i]))

arr.sort(key= lambda x : -x[1])

for i in range(N):
    ki = 0
    if arr[0][0] != i:
        ki = arr[0][1] - cost[i]
    else:
        ki = arr[1][1] - cost[i]

    ki += cost[i]
    ki = pro[i] - ki

    print(ki, end=' ')