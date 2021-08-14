import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if a + b + c < 180 or a + b + c > 180:
        print("%d %d %d Check" % (a, b, c))
    else:
        print("%d %d %d Seems OK" % (a, b, c))
