import sys


N = int(sys.stdin.readline())

for _ in range(N):
    n, a, d = map(int, sys.stdin.readline().split())
    res = a

    for i in range(1, n):
        a += d
        res += a

    print(res)