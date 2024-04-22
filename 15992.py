import sys


T = int(sys.stdin.readline())
mod = 1000000009
arr = [[0 for _ in range(1001)] for _ in range(1001)]

arr[1][1] = 1
arr[2][1] = 1
arr[3][1] = 1
for k in range(2, 1001):
    for i in range(1, 1001):
        for j in range(1, 4):
            if i - j >= 0:
                arr[i][k] += arr[i - j][k - 1]
                arr[i][k] %= mod

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(arr[a][b])