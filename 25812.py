import sys


N, r = map(int, sys.stdin.readline().split())
a, b = 0, 0

for _ in range(N):
    n = int(sys.stdin.readline())

    if n == r:
        continue

    if n * 2 > n + r:
        b += 1
    else:
        a += 1

if a == b:
    print(0)
elif a > b:
    print(1)
else:
    print(2)