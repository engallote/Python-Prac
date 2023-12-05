import sys

arr = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(1, 5):
    if abs(arr[0] - arr[i]) <= 1000:
        res += 1

print(res)