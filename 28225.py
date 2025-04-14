import sys


N, M = map(int, sys.stdin.readline().split())
num, d = 0, 10000000000

for i in range(1, N + 1):
    a, b = map(int, sys.stdin.readline().split())
    if (M - a) / b < d:
        d = (M - a) / b
        num = i

print(num)