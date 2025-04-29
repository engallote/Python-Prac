import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if N < M:
    print(-1)
elif N == M:
    print(0)
else:
    print(1)