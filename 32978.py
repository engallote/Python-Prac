import sys


N = int(sys.stdin.readline())
arr1 = list(sys.stdin.readline().rstrip().split())
arr2 = list(sys.stdin.readline().rstrip().split())

for i in arr1:
    if i in arr2:
        continue
    else:
        print(i)
        break