import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

res, pre = arr[0], arr[0]
for i in range(1, N):
    if arr[i] - pre != 1:
        res += arr[i]

    pre = arr[i]

print(res)