import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

s, res = sum(arr), 0
for i in range(N - 1, 0, -1):
    s -= arr[i]
    res += arr[i] * s

print(res)