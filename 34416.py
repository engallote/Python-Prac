import sys


N = int(sys.stdin.readline())
w = int(sys.stdin.readline())
Q = int(sys.stdin.readline())
arr = [0 for _ in range(N + 1)]
arr[w] = 1

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

for i in range(1, N + 1):
    if arr[i] == 1:
        print(i)
        break