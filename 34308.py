import sys


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    if N - i >= i - 1:
        print(1, end=' ')
    else:
        print(N, end=' ')