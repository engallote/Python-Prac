import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
dp, index = [], []
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp.append(arr[0])
index.append(0)
for i in range(1, N):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        index.append(len(dp) - 1)
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        index.append(idx)

l = len(dp)
print(l)
res = []

for i in range(len(index) - 1, -1, -1):
    if index[i] == l - 1:
        res.append(arr[i])
        l -= 1

print(*res[::-1])