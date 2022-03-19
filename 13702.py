import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]

l, r, mid, res = 0, 1000000000000000, 0, 0
while l <= r:
    mid = (l + r) // 2
    cnt = 0

    if mid == 0:
        l = mid + 1
        continue

    for i in range(N):
        if arr[i] == 0:
            continue
        cnt += arr[i] // mid

    if cnt < K:
        r = mid - 1
    else:
        res = max(res, mid)
        l = mid + 1

print(res)