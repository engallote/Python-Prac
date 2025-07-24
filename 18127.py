import sys


N, M = map(int, sys.stdin.readline().split())

res, cnt, jump = 1, N - 1, N - 1 - 1
for _ in range(M):
    res += cnt

    cnt += jump

print(res)