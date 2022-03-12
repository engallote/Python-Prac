import sys

N = int(sys.stdin.readline())
res = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    mul = 1
    for j in range(1, 4):
        mul *= arr[j]

    res[i][0] = arr[0]
    res[i][1] = sum(arr[1:])
    res[i][2] = mul

res.sort(key=lambda x : (x[2], x[1], x[0]))

for i in range(3):
    print(res[i][0], end=' ')

