import sys

N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    res += len(sys.stdin.readline().rstrip())

print(res)