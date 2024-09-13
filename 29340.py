import sys


arr1 = list(sys.stdin.readline().rstrip())
arr2 = list(sys.stdin.readline().rstrip())

for i in range(len(arr1)):
    if arr1[i] > arr2[i]:
        print(arr1[i], end='')
    else:
        print(arr2[i], end='')