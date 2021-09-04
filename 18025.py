import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

d, res = 0, 100000000000
for i in range(N - 2):
    maxNum = max(arr[i], arr[i + 2])
    if res > maxNum:
        d = i + 1
        res = maxNum

print(d, res)