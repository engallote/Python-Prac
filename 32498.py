import sys


N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    if num % 2 != 0:
        res += 1

print(res)