import sys


N, A, B, C = map(int, sys.stdin.readline().split())

n, a, b, c = 1, 1, 1, 1

for i in range(2, N + 1):
    n *= i

for i in range(2, A + 1):
    a *= i

for i in range(2, B + 1):
    b *= i

for i in range(2, C + 1):
    c *= i

print(int(n // (a * b * c)))