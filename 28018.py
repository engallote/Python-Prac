import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(1000003)]
dp = [0 for _ in range(1000003)]

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    arr[s] += 1
    arr[e + 1] -= 1

for i in range(1, 1000003):
    dp[i] = dp[i - 1] + arr[i]

Q = int(sys.stdin.readline())
qList = list(map(int, sys.stdin.readline().split()))

for q in qList:
    print(dp[q])