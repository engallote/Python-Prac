import sys


X = int(sys.stdin.readline())
arr = [3, -2]
res = 0

for i in range(X):
    res += arr[i % 2]

print(res)