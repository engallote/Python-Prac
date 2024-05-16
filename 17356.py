import sys

N, M = map(int, sys.stdin.readline().split())

res = (M - N) / 400
print(1/(1 + 10**res))