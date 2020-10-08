import sys


def dfs(idx, chk):
    if chk == (1 << N) - 1:
        if arr[idx][0] > 0:
            return arr[idx][0]
        else:
            return INF
    if dp[idx][chk] != -1:
        return dp[idx][chk]

    ret = INF

    for i in range(N):
        if (chk & (1 << i)) == 0 and arr[idx][i] > 0:
            ret = min(ret, dfs(i, chk + (1 << i)) + arr[idx][i])
    dp[idx][chk] = ret
    return ret


N = int(sys.stdin.readline())
arr = []
dp = [[-1 for _ in range((1 << N))] for _ in range(N)]
INF = 100000000000
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

print(dfs(0, 1))