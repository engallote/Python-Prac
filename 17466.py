import sys


N, P = map(int, sys.stdin.readline().split())

res = 1
for i in range(2, N + 1):
    res *= i
    res %= P

print(res)