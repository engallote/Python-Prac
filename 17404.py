import sys


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

res = sys.maxsize
for color in range(3):
    dp = [[1000000000] * 3 for _ in range(N)]
    dp[0][color] = arr[0][color]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

    for i in range(3):
        if color != i:
            res = min(res, dp[N - 1][i])

print(res)