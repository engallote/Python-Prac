import sys


arr = list(map(int, sys.stdin.readline().split()))
if arr[-1] % 10 == 0:
    print(10)
else:
    print(arr[-1] % 10)