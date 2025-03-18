import sys


N, M = map(int, sys.stdin.readline().split())

if N >= M / 2:
    print("E")
else:
    print("H")