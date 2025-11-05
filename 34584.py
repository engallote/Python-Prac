import sys


x, d = map(int, sys.stdin.readline().split())

if x * 2 > d:
    print("take it")
else:
    print("double it")