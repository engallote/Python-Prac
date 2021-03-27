import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
for i in range(N):
    sum, cnt = 0, 0
    for j in range(i, N):
        if sum + arr[j] <= C:
            sum += arr[j]
            cnt += 1
        else:
            continue
    if res < cnt:
        res = cnt

print(res)