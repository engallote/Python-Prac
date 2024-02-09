import sys


N, K = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(N + 1)]

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    arr[a] += 1
    arr[b] += 1

res = 0
for i in range(1, N + 1):
    if arr[i] >= 3:
        res += arr[i] * (arr[i] - 1) * (arr[i] - 2) // 6;
        res %= 1000000007

print(res)