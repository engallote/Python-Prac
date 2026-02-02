import sys

N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    a, b = map(float, sys.stdin.readline().split())
    res += a * b

print(res)
