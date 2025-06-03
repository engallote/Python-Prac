import sys


N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    res += int(sys.stdin.readline())

print(res)