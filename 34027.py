import sys


N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    d = num ** 0.5

    if round(d) == d:
        print(1)
    else:
        print(0)
