import sys


N, M = map(int, sys.stdin.readline().split())

res, r, c = 10000000000000, 0, 0
for i in range(1, N + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(1, M + 1):
        if arr[j - 1] == 0:
            if res > i + abs((M + 1) / 2 - j):
                res = i + abs((M + 1) / 2 - j)
                r = i
                c = j

if res == 10000000000000:
    print(-1)
else:
    print(r, c)