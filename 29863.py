import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if N >= 20:
    N = 24 - N
    print(N + M)
else:
    print(M - N)