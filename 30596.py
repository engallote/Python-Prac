import sys


arr = []

for _ in range(4):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(arr[0] * arr[2])