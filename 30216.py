import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt, cur = 1, 1

for i in range(1, N):
    if arr[i - 1] < arr[i]:
        cur += 1
    else:
        cnt = max(cnt, cur)
        cur = 1

cnt = max(cnt, cur)
print(cnt)