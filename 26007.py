import sys


N, M, K, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cur = [0 for _ in range(N + 1)]
cnt = [0 for _ in range(N + 1)]
cur[0] = X

for i in range(1, N + 1):
    cur[i] = cur[i - 1] + arr[i - 1]
    cnt[i] = cnt[i - 1]
    if cur[i] < K:
        cnt[i] += 1

for i in range(M):
    l, r = map(int, sys.stdin.readline().split())
    print(cnt[r - 1] - cnt[l - 1])
