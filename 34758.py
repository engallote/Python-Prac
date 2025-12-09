import sys


X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    if (x != X and y == Y) or (x == X and y != Y):
        print(0)
    else:
        print(1)