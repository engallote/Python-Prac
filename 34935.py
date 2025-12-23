import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
pre = -1000000000000000009
res = 1

for i in arr:
    if i > pre:
        pre = i
    else:
        res = 0
        break

print(res)