import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(10001)]

arr[0] = 1
arr[1] = 1

for i in range(2, 10001):
    arr[i] = arr[i - 1] + arr[i - 2]

for i in range(1, N + 1):
    a, b = map(int, sys.stdin.readline().split())

    print("Case #%d: %d" %(i, arr[a - 1] % b))