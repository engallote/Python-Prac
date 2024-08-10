import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline()) * 7

if N + M <= 30:
    print(1)
else:
    print(0)