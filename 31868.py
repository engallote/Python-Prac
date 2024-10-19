import sys


N, K = map(int, sys.stdin.readline().split())
cnt, res = 1, 0

while True:
    t = K // 2
    K = t
    cnt += 1

    if cnt == N:
        res = K
        break

    if K == 0:
        break

print(res)