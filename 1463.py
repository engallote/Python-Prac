def solve(num):
    if num in dp:
        return dp[num]

    ret = min(solve(num // 2) + num % 2, solve(num // 3) + num % 3) + 1
    dp[num] = ret
    return ret


N = int(input())
dp = {1:0, 2:1}

print(solve(N))