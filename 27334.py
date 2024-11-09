import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(arr)

arr2.sort()

for i in range(N):
    print(arr2.index(arr[i]) + 1)