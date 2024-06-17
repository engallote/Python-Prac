import sys


N = int(sys.stdin.readline())
arr = ["G...", ".I.T", "..S."]

for i in range(3):
    res = []
    for j in range(4):
        for l in range(N):
            res.append(arr[i][j])

    for k in range(N):
        print(*res, sep='')