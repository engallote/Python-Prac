import sys


N = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))
arr = list(sys.stdin.readline().split())

tmp = ["" for _ in range(N)]
for _ in range(3):
    for i in range(N):
        tmp[i] = arr[order[i] - 1]
    for i in range(N):
        arr[i] = tmp[i]

for i in arr:
    print(i)
