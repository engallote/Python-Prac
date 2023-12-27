import sys

N, M = map(int, sys.stdin.readline().split())
res = 0

for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    s = 0
    for i in range(M):
        if tmp[i] == 'O':
            s += 1

    if s > M // 2:
        res += 1

print(res)