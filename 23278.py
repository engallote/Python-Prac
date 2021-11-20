import sys


N, L, H = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

print(sum(arr[L:N - H])/(N-H-L))