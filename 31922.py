import sys


A, P, C = map(int, sys.stdin.readline().split())
print(max(A + C, P))