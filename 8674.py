import sys

N, M = map(int, sys.stdin.readline().split())

res = 100000000

if N % 2 == 0 or M % 2 == 0:
    res = 0
else:
    res = min(N, M)

print(res)