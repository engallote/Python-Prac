import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
p = arr[1] - arr[0]

print(arr[-1] + p)