import sys


N, M = map(int, sys.stdin.readline().split())

d = M // N
m = M % N
if m > 0:
    m = 1

print(d + m)