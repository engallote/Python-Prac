import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(1, N + 1):
    idx1 = arr.index(i)
    idx2 = arr.index(i, idx1 + 1)
    res = max(res, idx2 - idx1 - 1)

print(res)