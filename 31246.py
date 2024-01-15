import sys


N, K = map(int, sys.stdin.readline().split())

cnt, mx = 0, 0
arr = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr[i][0] = a
    arr[i][1] = b
    mx = max(mx, abs(b - a))

    if a >= b:
        cnt += 1

if cnt >= K:
    print(0)
else:
    l, r, res = 0, mx + 1, 1000000000000
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for i in range(N):
            if arr[i][0] + mid >= arr[i][1]:
                cnt += 1

        if cnt >= K:
            res = min(res, mid)
            r = mid - 1
        else:
            l = mid + 1
    print(res)