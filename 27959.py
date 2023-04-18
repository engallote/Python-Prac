import sys


N, M = map(int, sys.stdin.readline().split())
N *= 100

if N >= M:
    print("Yes")
else:
    print("No")