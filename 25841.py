import sys


N, M, K = map(int, sys.stdin.readline().split())
res = 0

for i in range(N, M + 1):
    s = str(i)
    res += s.count(str(K))

print(res)