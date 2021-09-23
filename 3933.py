import sys


max = (2**15) + 1
dp = [[0 for _ in range(5)] for _ in range(max)]

for idx in range(1, max):
    if idx * idx > max:
        break
    dp[idx * idx][1] = 1

    for i in range(1, max - (idx * idx)):
        dp[i + idx * idx][2] += dp[i][1]
        dp[i + idx * idx][3] += dp[i][2]
        dp[i + idx * idx][4] += dp[i][3]


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    res = dp[N][1] + dp[N][2] + dp[N][3] + dp[N][4]
    print(res)
