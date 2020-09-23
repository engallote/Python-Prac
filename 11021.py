import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print("Case #%d: %d" % (i, a + b))