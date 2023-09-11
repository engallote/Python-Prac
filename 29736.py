import sys

A, B = map(int, sys.stdin.readline().split())
K, X = map(int, sys.stdin.readline().split())

res = 0
for i in range(max(A, K - X), min(B + 1, K + X + 1)):
    res += 1

if res == 0:
    print("IMPOSSIBLE")
else:
    print(res)