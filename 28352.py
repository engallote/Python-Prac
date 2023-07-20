import sys


N = int(sys.stdin.readline())
res = 1
week = 3628800 // 6

for i in range(2, N + 1):
    res *= i

res //= week

print(res)