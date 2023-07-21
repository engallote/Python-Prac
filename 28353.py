import sys


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

res = 0
l, r = 0, len(arr) - 1
while l < r:
    if arr[l] + arr[r] <= K:
        l += 1
        r -= 1
        res += 1
    else:
        r -= 1

print(res)