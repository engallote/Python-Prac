import sys


arr = list(map(int, sys.stdin.readline().split()))
last = arr[-1]
arr.sort()

if arr[14] == arr[13] or last != arr[14]:
    print(arr[14] + 1)
else:
    print(arr[14])