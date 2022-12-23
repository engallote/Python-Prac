import sys


s = sys.stdin.readline()
pre, res, cnt = '.', 1000000000, 0

for i in s:
    if pre == i:
        cnt += 1
    else:
        if cnt > 0:
            res = min(res, cnt)
        cnt = 1
    pre = i

print(res)