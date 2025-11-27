import sys


arr = list(map(int, sys.stdin.readline().split()))
tmp = []
res = 0

for i in arr:
    if i in tmp:
        continue
    tmp.append(i)
    res += 1

print(4 - res)