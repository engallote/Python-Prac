import sys


N = int(sys.stdin.readline())

pa, pb = 0, 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    pa += a
    pb += b

    print(pa - pb)