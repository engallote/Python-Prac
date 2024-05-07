import sys


arr = []
for _ in range(3):
    N = int(sys.stdin.readline())
    arr.append(N)

arr.sort()
print(arr[1])