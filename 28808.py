import sys


N, M = map(int, sys.stdin.readline().split())
res = 0

for i in range(N):
    s = sys.stdin.readline()
    if "+" in s:
        res += 1

print(res)