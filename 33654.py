import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
pre = -10000000000

for i in arr:
    if pre <= i:
        print(i, end=' ')
        pre = i