import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res, mn = 0, 10000000000000

for i in range(N):
    if arr[i] < mn:
        mn = arr[i]
        res = i

print(res)