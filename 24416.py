import sys


def fib(N):
    if N == 1 or N == 2:
        return 1
    if dp[N] != -1:
        return dp[N]

    dp[N] = fib(N - 1) + fib(N - 2)
    return dp[N];


def fib2(N):
    arr = [0 for _ in range(N + 1)]
    arr[1] = arr[2] = 1
    cnt = 0
    for i in range(3, N + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
        cnt += 1
    return cnt


N = int(sys.stdin.readline())
dp = [-1 for _ in range(N + 1)]

print(fib(N), fib2(N))