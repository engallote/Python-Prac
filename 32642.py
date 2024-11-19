import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [0]

for i in arr:
    if i == 0:
        res.append(res[-1] - 1)
    else:
        res.append(res[-1] + 1)

print(sum(res))