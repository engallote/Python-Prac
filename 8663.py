import sys

X, S = map(int, sys.stdin.readline().split())
res = 0

while X > 0:
    if S == 1:
        res += X
        break

    X -= S
    S //= 2
    res += 1

print(res)