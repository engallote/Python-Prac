import sys


N = int(sys.stdin.readline())
res = 1
for i in range(2, N + 1):
    res *= i

print(res)