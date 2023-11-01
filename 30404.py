import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

cur, cnt = 0, 0
for i in arr:
    if i <= cur <= i + K:
        continue
    else:
        cur = i + K
        cnt += 1

print(cnt)