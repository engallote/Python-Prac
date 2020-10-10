import sys
from collections import deque

N = int(sys.stdin.readline())
dp = [0] * N
par = [-1] * N
index = [0] * N
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp[0] = arr[0]
idx = 0

for i in range(1, N):
    if dp[idx] < arr[i]:
        idx += 1
        dp[idx] = arr[i]
        par[i] = index[idx - 1]
        index[idx] = i
    else:
        l, r = 0, idx
        while l < r:
            mid = (l + r) // 2
            if dp[mid] >= arr[i]:
                r = mid
            else:
                l = mid + 1
        dp[r] = arr[i]
        if r:
            par[i] = index[r - 1]
        index[r] = i

print(idx + 1)
res = []
idx = index[idx]
while idx != -1:
    res.append(arr[idx])
    idx = par[idx]

res.sort()
for i in res:
    print(i, end=' ')