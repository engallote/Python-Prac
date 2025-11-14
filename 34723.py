import sys


P, M, C = map(int, sys.stdin.readline().split())
X = int(sys.stdin.readline())
res = 1000000000000

for p in range(1, P + 1):
    for m in range(1, M + 1):
        for c in range(1, C + 1):
            res = min(res, abs((p + m) * (m + c) - X))

print(res)