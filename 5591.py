import sys

N, M = map(int, sys.stdin.readline().split())
sum = [0 for _ in range(N)]

for i in range(N):
    num = int(sys.stdin.readline())

    if i == 0:
        sum[i] = num
    else:
        sum[i] = sum[i - 1] + num

res = 0
for i in range(M - 1, N):
    if i == M - 1:
        res = max(res, sum[i])
    else:
        res = max(res, sum[i] - sum[i - M])

print(res)