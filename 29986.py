import sys


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = 0

for i in arr:
    if i <= M:
        res += 1

print(res)