import sys


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
s = sum(arr)

l, r, res = 0, 100000000, 0
while l < r:
    m = (l + r) // 2
    if (s + (100 * m)) / (N + m) >= M:
        res = m
        r -= 1
    else:
        l += 1

print(res)