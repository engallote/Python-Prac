import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = []
for i in range(N):
    if arr[i] == 1:
        arr2.append(i)

l, r, res = 0, K - 1, 10000000000

while r < len(arr2):
    res = min(res, arr2[r] - arr2[l] + 1)
    r += 1
    l += 1

if res == 10000000000:
    res = -1

print(res)
