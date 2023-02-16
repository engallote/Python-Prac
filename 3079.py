import math
import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

l, r, mid, res = 0, 10 ** 18, 0, 10**18
while l <= r:
    mid = (l + r) // 2

    tmp = 0
    for i in arr:
        tmp += mid // i

    if tmp >= M:
        res = min(res, mid)
        r = mid - 1
    else:
        l = mid + 1

print(res)