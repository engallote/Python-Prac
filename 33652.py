import sys


N = int(sys.stdin.readline())
res = 1000000000000000000

for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    if t == 0:
        res = min(s, res)

if res == 1000000000000000000:
    res = -1
print(res)