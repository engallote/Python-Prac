import sys


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    if max(arr) == arr[b - 1]:
        continue
    else:
        if arr[a - 1] > 0:
            arr[a - 1] -= 1

print(*arr)