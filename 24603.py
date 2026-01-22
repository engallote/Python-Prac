import sys

a, b, c = map(int, sys.stdin.readline().split())
arr = []
for i in range(a):
    d = int(sys.stdin.readline())
    print(int(d / b * c))