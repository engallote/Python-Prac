import sys


N, M, C = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = [0 for _ in range(N)]
res[0] = 1
cur = 0

for i in arr:
    if i == 1:
        cur += 1
        cur %= N
    else:
        cur -= 1
        if cur < 0:
            cur = N - 1
    res[cur] += 1

print(res[C - 1])