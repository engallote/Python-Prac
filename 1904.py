N = int(input())
mod = 15746
dp = [0] * 1000001
dp[1], dp[2] = 1, 2

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= mod

print(dp[N])