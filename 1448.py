import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

res = 0
for i in range(N - 2):
    if arr[i] + arr[i + 1] > arr[i + 2]:
        res = max(res, arr[i] + arr[i + 1] + arr[i + 2])

if res == 0:
    res = -1

print(res)