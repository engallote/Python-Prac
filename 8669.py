import sys


N = int(sys.stdin.readline())
arr = [0 for _ in range(1000001)]
res = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if arr[b] == 0:
        res += 1
        arr[b] = a
    elif arr[b] < a:
        arr[b] = a

print(res)