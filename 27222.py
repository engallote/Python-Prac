import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if arr[i] == 1 and a < b:
        res += b - a

print(res)