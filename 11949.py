import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

for i in range(1, M + 1):
    for j in range(1, N):
        if arr[j] % i < arr[j - 1] % i:
            tmp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = tmp

for i in arr:
    print(i)