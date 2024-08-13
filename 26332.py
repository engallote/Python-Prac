import sys


N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(a, b)

    if a == 1:
        print(b)
    else:
        print(b + (b - 2) * (a - 1))