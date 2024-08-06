import sys


N, M, K = map(int, sys.stdin.readline().split())
res, dog, rab = 0, 0, N

for i in range(100000):
    if dog >= rab:
        res = i
        break

    dog += K
    rab += M

print(res)