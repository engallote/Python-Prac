import sys

N, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

s = 0
for i in arr:
    s += i

if s % X == 0:
    print(1)
else:
    print(0)