import sys


N, A, B = map(int, sys.stdin.readline().split())
a, b = 1, 1

for _ in range(N):
    a += A
    b += B

    if a < b:
        t = a
        a = b
        b = t
    if a == b:
        b -= 1

print(a, b)